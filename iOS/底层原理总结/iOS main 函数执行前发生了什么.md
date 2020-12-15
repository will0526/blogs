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

