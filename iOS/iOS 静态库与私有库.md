#iOS 静态库 与私有库

私有库
https://www.jianshu.com/p/0c640821b36f
http://www.cnblogs.com/brycezhang/p/4117180.html

静态库参考
Xcode 创建.a和framework静态库
https://www.jianshu.com/p/43d55ae49f59

.a包可以包含第三方.a 包
framework可以包含.a和资源文件

umbrella framework 可以包含framework，但是在引用的时候找不到subframe work ，失败。
参考 https://stackoverflow.com/questions/27484997/how-to-create-an-umbrella-framework-in-ios-sdk
https://stackoverflow.com/questions/41397746/umbrella-framework


动态库，默认是吧 pod 引用打入 framework 里的