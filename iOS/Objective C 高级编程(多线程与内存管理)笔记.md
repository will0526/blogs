#第一章自动引用计数
##1.1自动引用计数
自动引用计数，即内存管理中对引用自动计数的技术

##1.2内存管理

###1.2.1内存管理的四个原则：

* 自己生成的对象，自己持有（初始化）
    
    alloc/new/copy/mutableCopy
* 非自己生成的对象，自己也能持有（）
   
    除以上方法以外生成的对象
    
    id obj = NSMutableArray array]//取得对象存在，但不持有对象
    
    [obj reatain] //通过retain 方法持有
    

* 不再需要自己持有的对象时释放
    
    不再使用时，release

* 非自己持有的对象无法释放
    
    程序如果释放非自己持有的对象，会导致程序奔溃
    
###1.2.2 MRC情况下

    使用alloc 或retain方法后，引用计数+1
    调用release后，-1
    归0时，调用dealloc 废弃对象
    
    
###1.2.3 autorelease
    
    超出变量作用域后，自动废弃
    
    在产生大量autorelease对象是，只要不废弃NSAutoreleasePool生成的对象就不会释放，需要咋适当的地方生成，持有或者废弃。
    （[pool drain]== [pool release]）


##1.3ARC规则

###1.3.1

    指定ARC 有效，编译器属性为 "-fobjc-arc"

    id 类型和对象默认所有权案修饰符是__strong
    
* 循环引用，容易发生内存泄露，所谓内存泄露就是应到废弃的对象在超出其生存周期后继续存在。

* __weak 弱引用不持有对象实例，可避免循环引用。在超出其变量作用域时，即被释放。
在持有某对象的弱引用时，若对象被废弃，则此弱引用将自动失效，且被赋值为nil

* 如果直接使用weak 修饰符修饰生成的变量，对象会被立即释放。因此将生成对象赋给strong修饰符的变量，然后再赋给weak修饰符的变量。
    
* 在ARC情况下，@autoreleasepool来代替 NSAutoreleasePool

* 对象类型的变量，不能作为C语言结构体的成员

* 不要显式调用dealloc

* 显式转换 id 和 void * 通过 __bridge 转换


##1.4ARC实现


属性声明中，copy retain strong 的修饰符为__strong
         unsafe_unretained、 assign 为 __unsafe_unretained
         weak 为__weak
         
弱引用不持有对象，所以引用计数器不改变

__autoreleasing 修饰符，注册到autoreleasepool中计数器+1


#二、blocks

##2.1blocks

blocks ：带有自动变量（局部变量）的匿名函数


##2.2blocks模式

* block 语法：
        
      ^ 返回值类型  参数列表  表达式
      ^           参数列表  表达式   
      ^                    表达式

   返回值类型与参数列表是可以省略的

* block 类型变量
    
      int (^blk)(int)
      返回类型（^变量名称）(参数列表类型)
   
   block类型变量可以作为函数参数使用
   
   block 可以作为函数返回值使用
   
* typedef 声明block

      typedef int (^blk_t)(int)


block 执行时自动变量的值，是其声明时的值。

block不能改变在语法外声明的变量的值，如需改变，在该变量钱附加__block 说明符，称为__block 变量



##2.3blocks实现

#三 Grand Central Dispatch(GCD)

##3.1 GCD

##3.2 API

##3.3 GCD 实现

#四、ARC、blocks、GCD使用范例

##ARC

##blocks

##GCD