# 前言

本文将跟随程序执行顺序，刨根问底，从 dyld 到 runtime ，看看 main 函数之前都发生了什么。

# dyld 动态链接库

iOS 中用到的所有系统 framework 都是动态链接的，类比成插头和插排，静态链接的代码在编译后的静态链接过程就将插头和插排一个个插好，运行时直接执行二进制文件

除了链接基本的动态库，比如UIKit，Foundation，CoreFoundation。
还会添加默认的，有两个默认添加的 lib：libobjc 即 objc 和 runtime，libSystem 中包含了很多系统级别 lib，

列几个熟知的：

libdispatch ( GCD )

libsystem_c ( C语言库 )

libsystem_blocks ( Block )

libcommonCrypto ( 加密库，比如常用的 md5 函数 )

这些 lib 都是dylib格式，有几点好处

代码共用：很多程序都动态链接了这些 lib，但它们在内存和磁盘中中只有一份

易于维护：由于被依赖的 lib 是程序执行时才 link 的，所以这些 lib 很容易做更新，比如libSystem.dylib 是 libSystem.B.dylib 的替身，哪天想升级直接换成 libSystem.C.dylib 然后再替换替身就行了

减少可执行文件体积：相比静态链接，动态链接在编译时不需要打进去，所以可执行文件的体积要小很多

援引并翻译
[!《 Mike Ash 这篇 blog 》](https://www.mikeash.com/pyblog/friday-qa-2012-11-09-dyld-dynamic-linking-on-os-x.html)
对 dyld 作用顺序的概括：

* 从 kernel 留下的原始调用栈引导和启动自己
* 将程序依赖的动态链接库递归加载进内存，当然这里有缓存机制
* non-lazy 符号立即 link 到可执行文件，lazy 的存表里
* Runs static initializers for the executable
* 找到可执行文件的 main 函数，准备参数并调用
* 程序执行中负责绑定 lazy 符号、提供 runtime dynamic loading services、提供调试器接口
* 程序main函数 return 后执行 static terminator
* 某些场景下 main 函数结束后调 libSystem 的 _exit 函数

# ImageLoader

ImageLoader 作用是将这些文件加载进内存，且每一个文件对应一个ImageLoader实例来负责加载。

两步走：

* 在程序运行时它先将动态链接的 image 递归加载 （也就是上面测试栈中一串的递归调用的时刻）

* 再从可执行文件 image 递归加载所有符号

# runtime 与 +load



