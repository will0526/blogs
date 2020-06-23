这里对有包大小有影响的配置项进行了描述，同时兼顾Crash收集所需要的dysm文件所配置。

Deployment列：

Deployment Postprocessing: NO 

Strip Debug Symbos During Copy: Debug: NO Release YES（Deployment Postprocessing设置为NO了，后面这个选项设置是无效的，保险起见还是统一一下）

Strip Link Product: YES

Strip Style: Debugging Symbols

Apple LLVM 6.0 – Code Generation列：

Generate Debug Symbols: YES（当设置为yes的时候，断点会失效，在测试的时候需要设置回no）

Optimization Level: Debug: None Release: Fastest, Smallest


同时把Debug Information Level设置成Line tables only也会减少包的大小