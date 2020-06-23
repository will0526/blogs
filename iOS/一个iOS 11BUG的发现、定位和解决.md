**前言**

在iOS 11发布之后，出现了一系列适配相关的问题，UIScrollView在pagingEnabled=YES时**滑动手势不灵敏**，UITableView的**滑动删除功能变动**，UIImagePickerViewController的**取消按钮点击区域变小**等，本文介绍其中一个UIAlertView问题，分享其**发现、定位和解决**。

**正文**

**1、问题产生**

问题的最初，是iOS 11正式版发布后不久，测试的同学提了一个iOS 11相关的BUG，表现是：**在直播间内发送聊天信息，如果被禁言，会弹出“被禁言”提示，键盘收回去，然后就弹不出来**。

开发在接到这个BUG的时候，先把问题抽象出来几个要素：直播间内、键盘弹出、弹出提示、键盘收回、键盘无法弹出。

弹出提示是用的UIAlertView的方式。在键盘出现时弹出UIAlertView的提示，键盘会收起，UIAlertView消失后，键盘会再次弹出，是一次正常的表现。

**2、问题复现**

按照复现路径做一次尝试，发现BUG可以复现，**确定问题存在**；

根据经验，**猜测问题可能出现在键盘和UIAlertView上**，与“禁言”的业务无关。

在直播间内尝试其他非“禁言”的场景，同样是在键盘出现的时候，弹出UIAlertView的提示，也会造成后续键盘无法弹出的情况。

在尝试完其他非直播间的主场景之后，发现问题可以描述为：

**iOS 11的机器只要弹出来一次UIAlertView，之后再通过becomeFirstResponder无法呼起键盘；必须手动点击输入区域，触发系统的键盘弹出行为，或者切入后台再切回来，才能正常弹出来键盘。**

部分页面在点击评论后，会添加一层透明maskView，并弹出键盘。点击透明的maskView会调用resignFirstResponder，在键盘消失的notification中消除maskView。因为键盘无法弹出（也无法收到键盘消失的notification，但maskView还是正常添加），导致这部分页面无法进行后续的交互。

**3、问题评估**

在复现问题后，需要对问题的严重性进行评估，确定BUG修复的优先级。

从已知的表现来看，iOS 11下的使用影响较大（UIAlertView的提示较多）。

用iOS 11的机器下载外网版本进行测试，发现BUG竟然无法复现！

虽然很诡异，但是问题的优先级可以降到更低，排入正常的BUG解决列表中。

**4、问题解析**

外网版本是Xcode8编译的本，本地版本使用的Xcode9 GM编译的，难道是Xcode 9编译导致？

1、新建一个demo，只有输入框和按钮，模拟UIAlertView弹出，发现demo是正常的；
2、把app的工程设置复制到demo，把对输入框的属性设置同样复制到demo，demo依旧正常；
3、把demo代码复制到app，并把app的rootViewController赋值为demo中的VC，依旧正常；

可以确定是app中某部分代码导致的键盘无法弹出的。

经过二分注释的方式，迅速（4、5次左右）定位到问题是app中的某个Service类导致。

仔细排插Service类的属性，发现里面有一个属性的是继承UIWindow并且level比UIWindowLevelStatusBar高。

自此，根据所学和苹果UIKit的文档，我们可以对问题进行一次回溯。

**5、问题回溯**

![](http://upload-images.jianshu.io/upload_images/2728934-8f1766c8a64994d7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

苹果官网上响应链和UIWindow的说明，里面关于becomeFirstResponder()的解释是：Asks UIKit to make this object the first responder in its window.

对于UIAlertView的iOS 11系统行为，猜测：

**1、在UIAlertView弹出的时候，会抢占系统的keyWindow，所以会出现键盘在UIAlertView的时候收回（因为keyWindow改变）**；
**2、在UIAlertView消失的时候，会遍历所有Window，找到其中z轴最高作为keyWindow，所以会出现键盘在UIAlertView消失后弹出（keyWindow变成原来的）**；

通过写代码调试app，确定了上面的猜测。

在iOS 11，如果UIAlertView弹出时，存在windowLevel 大于 UIWindowLevelNormal 的UIWindow，就会触发这个键盘无法弹出的BUG。

**6、问题修复**

1、保证app中，没有常驻的UIWindow；
2、修复键盘无法弹出时，maskView无法消除的BUG；
3、UIAlertView在后续的版本替换掉；

**总结**

这次问题从产生、复现、定位、评估再到修复的时间，和写这篇文章的时间差不多。

BUG的解决流程各不相同，借此提醒自己对于BUG的解决要有目的性和优先级。