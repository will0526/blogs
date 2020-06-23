##卡顿优化 -CPU

1，尽量用轻量级的对象，比如用不到事件处理的地方，可以考虑使用CALayer取代UIView
2，不要频繁地调用UIView的相关属性，比如frame、bounds、transform等属性，尽量减少不必要的修改
3，尽量提前计算好布局，在有需要时一次性调整对应的属性，不要多次修改属性
4，Autolayout会比直接设置frame消耗更多的CPU资源
5，图片的size最好刚好跟UIImageView的size保持一致
6，控制一下线程的最大并发数量
7，尽量把耗时的操作放到子线程

##卡顿优化 -GPU

1，尽量避免短时间内大量图片的显示，尽可能将多张图片合成一张进行显示
2，尽量减少视图数量和层次
3，减少透明的视图（alpha<1），不透明的就设置opaque为YES
4，尽量避免出现离屏渲染


##离屏渲染

在OpenGL中，GPU有2种渲染方式
1、On-Screen Rendering：当前屏幕渲染，在当前用于显示的屏幕缓冲区进行渲染操作
2、Off-Screen Rendering：离屏渲染，在当前屏幕缓冲区以外新开辟一个缓冲区进行渲染操作

###离屏渲染消耗性能的原因
1、需要创建新的缓冲区
2、离屏渲染的整个过程，需要多次切换上下文环境，先是从当前屏幕（On-Screen）切换到离屏（Off-Screen）；等到离屏渲染结束以后，将离屏缓冲区的渲染结果显示到屏幕上，又需要将上下文环境从离屏切换到当前屏幕

###哪些操作会触发离屏渲染？
1、光栅化，layer.shouldRasterize = YES
2、遮罩，layer.mask
3、圆角，同时设置layer.masksToBounds = YES、layer.cornerRadius大于0。考虑通过CoreGraphics绘制裁剪圆角，或者叫美工提供圆角图片
4、阴影，layer.shadowXXX。如果设置了layer.shadowPath就不会产生离屏渲染

##耗电优化

耗电的主要来源？


CPU处理，Processing
网络，Networking
定位，Location
图像，Graphics

定位优化

如果只是需要快速确定用户位置，最好用CLLocationManager的requestLocation方法。定位完成后，会自动让定位硬件断电
如果不是导航应用，尽量不要实时更新位置，定位完毕就关掉定位服务
尽量降低定位精度，比如尽量不要使用精度最高的kCLLocationAccuracyBest
需要后台定位时，尽量设置pausesLocationUpdatesAutomatically为YES，如果用户不太可能移动的时候系统会自动暂停位置更新
尽量不要使用startMonitoringSignificantLocationChanges，优先考虑startMonitoringForRegion:

##APP启动优化

先来看app启动流程

APP的启动可以分为2种
1、冷启动（Cold Launch）：从零开始启动APP
2、热启动（Warm Launch）：APP已经在内存中，在后台存活着，再次点击图标启动APP

APP启动时间的优化，主要是针对冷启动进行优化

通过添加环境变量可以打印出APP的启动时间分析（Edit scheme -> Run -> Arguments）
1、DYLD_PRINT_STATISTICS设置为1
2、如果需要更详细的信息，那就将DYLD_PRINT_STATISTICS_DETAILS设置为1

APP的冷启动概括为三大阶段
dyld，Apple的动态链接器，可以用来装载Mach-O文件（可执行文件、动态库等）
启动APP时，dyld所做的事情有
1、装载APP的可执行文件，同时会递归加载所有依赖的动态库
2、当dyld把可执行文件、动态库都装载完毕后，会通知Runtime进行下一步的处理

##runtime

启动APP时，runtime所做的事情有
1、调用map_images进行可执行文件内容的解析和处理
2、在load_images中调用call_load_methods，调用所有Class和Category的+load方法
3、进行各种objc结构的初始化（注册Objc类 、初始化类对象等等）
4、调用C++静态初始化器和__attribute__((constructor))修饰的函数
到此为止，可执行文件和动态库中所有的符号(Class，Protocol，Selector，IMP，…)都已经按格式成功加载到内存中，被runtime 所管理

##main

1、APP的启动由dyld主导，将可执行文件加载到内存，顺便加载所有依赖的动态库
2、并由runtime负责加载成objc定义的结构
3、所有初始化工作结束后，dyld就会调用main函数
4、接下来就是UIApplicationMain函数，AppDelegate的application:didFinishLaunchingWithOptions:方法

##优化方案

一、dyld

减少动态库、合并一些动态库（定期清理不必要的动态库）
减少Objc类、分类的数量、减少Selector数量（定期清理不必要的类、分类）
减少C++虚函数数量
Swift尽量使用struct

二、runtime
用+initialize方法和dispatch_once取代所有的__attribute__((constructor))、C++静态构造器、ObjC的+load

三、main

在不影响用户体验的前提下，尽可能将一些操作延迟，不要全部都放在finishLaunching方法中按需加载