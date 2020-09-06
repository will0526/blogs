

## 推送流程原理介绍


![image](https://xg.qq.com/docs/assets/iOSPushMap.jpg)

简要说明iOS客户端实现推送流程的步骤：

第一步：要求客户端设备与APNs建立TSL连接，APNs需要验证设备的有效性；

第二步：客户端App在合适的时机，借助系统提供的接口向APNs请求推送消息用的Token；(SDK 内部实现)

第三步：客户端App在合适的时机，将从APNs获取的Token注册到信鸽服务器；（SDK内部实现）

第四步：通过管理台(xg.qq.com)或者是REST API创建送消息，然后信鸽服务器再去请求APNs下发消息；

第五步：APNs服务器接收到信鸽服务器的推送消息请求后，根据Token来将推送的消息下发到指定的设备；

以上流程可以看出，终端设备的联网状态是至关重要的。


iOS中提供了2中推送通知

1.本地推送通知(Local Notification)

2.远程推送通知(Remote Notification)

## 本地推送通知


* 创建本地推送通知对象

[[UILocalNotification alloc] init]创建一个本地通知

* 设置本地通知的相关属性
    
    必须设置的属性
    
    * 推送通知的触发时间(何时发出推送通知)
    
    @property(nonatomic,copy) NSDate *fireDate
    
    * 推送通知的具体内容
    
    @property(nonatomic,copy) NSString *alertBody
    
    * 在锁屏时显示的动作标题(完整测标题:"滑动来" + alertAction)
    
    @property(nonatomic,copy) NSString *alertAction
    
    * 设置锁屏界面alertAction是否有效
    
    localNote.hasAction = YES;
    
    * app图标数字
    
    @property(nonatomic,assign) NSInteger applicationIconBadgeNumber
    
    * 调度本地推送通知(调度完毕后,推动通知会在特定时间fireDate发出)
    
    [[UIApplication shareApplication] scheduleLocalNotification:ln]
    
    可以进行设置的设置
    
    * 设置通知中心通知的标题
    
    localNote.alertTitle = @"222222222222";
    
    * 设置音效(如果不设置就是系统默认的音效, 设置的话会在mainBundle中查找)

    localNote.soundName = @"buyao.wav";
    
    * 每隔多久重复发一次推送通知
    
    @property(nonatomic) NSCalendarUnit repeatInterval
    
    * 点击推送通知打开app时显示的启动图片(mainBundle 中提取图片)
    
    @property(nonatomic,copy) NSSring *alertLaunchImage
    
    * 附加的额外信息
    
    @property(nonatomic,copy) NSDictionary *userInfo
    
    * 时区
    
    @property(nonatomic,copy) NSTimeZone *timeZone
    
    (一般设置为[NSTimeZone defaultTimeZone],跟随手机的时区)

```markdown
  // 1.创建一个本地通知
    UILocalNotification *localNote = [[UILocalNotification alloc] init];
    
    // 2.设置本地通知的一些属性(通知发出的时间/通知的内容)
    // 2.1.设置通知发出的时间
    localNote.fireDate = [NSDate dateWithTimeIntervalSinceNow:5.0];
    // 2.2.设置通知的内容
    localNote.alertBody = @"吃饭了吗?";
    // 2.3.设置锁屏界面的文字
    localNote.alertAction = @"查看具体的消息";
    // 2.4.设置锁屏界面alertAction是否有效
    localNote.hasAction = YES;
    // 2.5.设置通过点击通知打开APP的时候的启动图片(无论字符串设置成什么内容,都是显示应用程序的启动图片)
    localNote.alertLaunchImage = @"111";
    // 2.6.设置通知中心通知的标题
    localNote.alertTitle = @"222222222222";
    // 2.7.设置音效
    localNote.soundName = @"buyao.wav";
    // 2.8.设置应用程序图标右上角的数字
    localNote.applicationIconBadgeNumber = 1;
    // 2.9.设置通知之后的属性
    localNote.userInfo = @{@"name" : @"张三", @"toName" : @"李四"};
    
    // 3.调度通知
    [[UIApplication sharedApplication] scheduleLocalNotification:localNote];
```
收到本地推送后的处理

APP在后台的情况下：

```markdown
- (void)application:(UIApplication *)application didReceiveLocalNotification:(UILocalNotification *)notification
{
    // 在这里写跳转代码
    // 如果是应用程序在前台,依然会收到通知,但是收到通知之后不应该跳转
    if (application.applicationState == UIApplicationStateActive) return;
    
    if (application.applicationState == UIApplicationStateInactive) {
        // 当应用在后台收到本地通知时执行的跳转代码
        [self jumpToSession];
    }
    
    NSLog(@"%@", notification);
}

```

APP进程被杀死的情况下

启动app,启动完毕会调用AppDelegate的下面的方法

-(BOOL)application:(UIApplication *)application didFinishLaunchWithOptions:(NSDictionary *)launchOptions;

launchOptions参数通过UIApplicationLaunchOptionsLocalNotificationKey取出本地推送通知对象

需要特别注意的是:在iOS8.0以后本地通知有了一些变化,如果要使用本地通知,需要得到用户的许可.

在didFinishLaunchWithOptions方法中添加如下代码


````markdown

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    
    /*
     UIUserNotificationTypeNone    = 0,      不发出通知
     UIUserNotificationTypeBadge   = 1 << 0, 改变应用程序图标右上角的数字
     UIUserNotificationTypeSound   = 1 << 1, 播放音效
     UIUserNotificationTypeAlert   = 1 << 2, 是否运行显示横幅
     */
    
    [application setApplicationIconBadgeNumber:0];
    
    if (IS_iOS8) {
        UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound categories:nil];
        [application registerUserNotificationSettings:settings];
    }
    
    // 如果是正常启动应用程序,那么launchOptions参数是null
    // 如果是通过其它方式启动应用程序,那么launchOptions就值
    if (launchOptions[UIApplicationLaunchOptionsLocalNotificationKey]) {
        // 当被杀死状态收到本地通知时执行的跳转代码
       
    }
    
    return YES;
}
````


## 远程推送

注册远程推送通知:

