##思路概述：

商户APP跳转到商户小程序，跳转时附带支付参数，小程序内下单做支付。支付完成后，回调商户APP带回支付结果，APP展示支付结果。

##功能要点：

* 1，APP跳转微信小程序(附带参数)
* 2，小程序获取用户open_id
* 3，小程序处理（支付参数）
* 4，小程序下单做支付
* 5，小程序返回APP

##APP跳转微信小程序
* [下载微信SDK](https://developers.weixin.qq.com/doc/oplatform/Downloads/iOS_Resource.html)
* 接入SDK，
[官方说明](https://developers.weixin.qq.com/doc/oplatform/Mobile_App/Launching_a_Mini_Program/iOS_Development_example.html)

配置准备：
* 在微信开放平台上有账号而且有通过的移动应用。
* 在微信公众平台有账号而且有小程序，最好发布为体验版本
![image.png](https://upload-images.jianshu.io/upload_images/2728934-0ffd1bb3a2f7a415.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
* 在微信开放平台把对应的移动应用和小程序建立关联

* 调用代码
示例代码：
```
//微信建议应用启动时调用
[WXApi registerApp:@"wx_app_id"];//wx_app_id 为移动应用的appid
...
...
...
//跳转小程序部分
WXLaunchMiniProgramReq *launchMiniProgramReq = [WXLaunchMiniProgramReq object];
launchMiniProgramReq.userName = @"gh_4fxxxxxx";  //待拉起的小程序原始Id 
launchMiniProgramReq.path = @"pages/index/index?query='test'";    ////拉起小程序页面的可带参路径，不填默认拉起小程序首页，对于小游戏，可以只传入 query 部分，来实现传参效果，如：传入 "?foo=bar"。
launchMiniProgramReq.miniProgramType = WXMiniProgramTypePreview; //拉起小程序的类型
[WXApi sendReq:launchMiniProgramReq];
...
...
...

```
小程序返回APP 回调需实现以下代码
```
-(void)onResp:(BaseResp*)resp{
    
    if ([resp isKindOfClass:[WXLaunchMiniProgramResp class]])
    {
//        NSString *string = resp.extMsg;
        // 对应JsApi navigateBackApplication中的extraData字段数据
    }
}
```

##小程序获取用户open_id

1,小程序调用接口 [获取登录凭证（code）]([https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html)
)
2,使用 code 换取 openid 和 session_key 等信息，后台调用接口 [获取openID](https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/login/auth.code2Session.html)




## 小程序处理
1，接收APP传来的参数
上面的App打开的path是'path/index',所以需要把App的onLaunch事件定义在page/index.js上
![image.png](https://upload-images.jianshu.io/upload_images/2728934-f799a281d90ed1b6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这里的options.scene是1069，这个场景id表示从app打开。
options.query.key1和options.query.key2就是app打开小程序传递的参数。
2，下单，
3，发起支付
调用wx.requestPayment(OBJECT)发起微信支付，见[官方说明](https://pay.weixin.qq.com/wiki/doc/api/wxa/wxa_api.php?chapter=7_7&index=5)

4，关闭小程序，回到APP

[官方说明](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/launchApp.html)

```
<button open-type="launchApp" app-parameter="wechat" binderror="launchAppError">打开APP</button>

```

```
Page({
  launchAppError (e) {
    console.log(e.detail.errMsg)
  }
})

```
**注意**
APP端需要设置正确URL scheme才能从微信正确回调。
![image.png](https://upload-images.jianshu.io/upload_images/2728934-7976ca9036c11f86.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




