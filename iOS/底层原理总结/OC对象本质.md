#OC对象的本质

* 面试题：一个NSObject对象占用多少内存？

Objective-C代码，底层实现其实都是C\C++代码。

OC的对象结构都是通过基础C\C++的结构体实现的。

```markdown

NSObject *objc = [[NSObject alloc] init];

struct NSObject_IMPL {
    Class isa;
};
// 查看Class本质
typedef struct objc_class *Class;
我们发现Class其实就是一个指针，对象底层实现其实就是这个样子。

```

系统为NSObject对象分配8个字节的内存空间，用来存放一个成员isa指针，那么isa指针这个变量的地址就是结构体的地址，也就是NSObjcet对象的地址。

```markdown

那么一个NSObject对象占用多少内存？
NSObjcet实际上是只有一个名为isa的指针的结构体，
因此占用一个指针变量所占用的内存空间大小，如果64bit占用8个字节，如果32bit占用4个字节。
```

我们发现只要是继承自NSObject的对象，那么底层结构体内一定有一个isa指针。

上述代码实际打印的内容是16 16，也就是说，person对象和student对象所占用的内存空间都为16个字节。
其实实际上person对象确实只使用了12个字节。但是因为内存对齐的原因。使person对象也占用16个字节。

我们可以总结内存对齐为两个原则：
```markdown
原则 1. 前面的地址必须是后面的地址正数倍,不是就补齐。
原则 2. 整个Struct的地址必须是最大字节的整数倍。
```


* 面试题：OC的类信息存放在哪里。

OC对象主要可以分为三种

instance对象（实例对象）
class对象（类对象）
meta-class对象（元类对象）


* 面试题：对象的isa指针指向哪里。
