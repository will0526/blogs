
**引子：**

你有没有想过为你的用户减少一道操作？

**什么是通用链接？**

通用链接是iOS9出的一个特性，他能让用户通过链接直接打开你的APP。经常配合分享功能，让用户快速进入到我们的APP里面。

APP的两大引流功能 --> 分享+推送，个人认为应该在这上面多下功夫。分享功能至少要能将对你们APP感兴趣的用户引入到APP,但是我很失望的看到很多APP没有做到这一点，就更别提使用通用链接来跳过微信对URL Schemes的屏蔽。

**开工实现**

前提条件：通用链接其实很容易实现，坑全部在下面这两个条件上了。

q1:能够通过 SSL 访问域名。(即支持https://访问，用谷歌浏览器打开网页就能测试出来，下面就是支持https的。

![](http://upload-images.jianshu.io/upload_images/2728934-47430a5ed2470b05.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
WechatIMG13.jpeg

q2:支持上传一个无后缀文件到你的域名解析的服务器的.well-known文件下面，并且能通过链接直接访问并且下载。

如果你们的后台服务器是支持SSL的，直接将文件丢在根目录下面，然后配置一下iis的MIME的权限（因为iis默认不支持无后缀的文件，所以访问不到）。

如果你们后台服务器的域名还不支持SSL,那么先去腾讯云，阿里云去购买证书，然后到iis下面去安装这个证书。

上面两项我坑了好久，因为服务器经验不是很足，这里也只能给你们指出关键坑。如果上面两个准备好了，其他的就很轻松了。

*1.登录APPDevelop*

https://developer.apple.com/

*2.开启对应的AppIDs的Associated Domains服务*

![](http://upload-images.jianshu.io/upload_images/2728934-9f8e23c35d943d78.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
WechatIMG14.jpeg

![](http://upload-images.jianshu.io/upload_images/2728934-e103e51a5177208e.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
WechatIMG15.jpeg

*3.编辑对应的Provisioning Profiles，并且重新下载双击安装*

![](http://upload-images.jianshu.io/upload_images/2728934-4138fdeafffffda9.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
WechatIMG17.jpeg

*4.打开Xcode项目，开启项目的Associated Domains，这时候会看到左边目录下多出了一个文件，这是正常的。*

![](http://upload-images.jianshu.io/upload_images/2728934-bff27f9f5eb76a62.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
WechatIMG18.jpeg

*5. 编写一个无后缀的apple-app-site-association（我已经放在demo的文件下面，你们可以自行参考）*

{
    "applinks": {
        "apps": [],
        "details": [
            {
                "appID": "47P6T6SYNE.com.zzyg.travelnotes",
                "paths": [ "/botaochen/*"]
            }
        ]
    }
}

appID里面47P6T6SYNE是项目的TeamID,com.zzyg.travelnotes是项目的BundleID

![](http://upload-images.jianshu.io/upload_images/2728934-f8467fe15a1b84e2.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
WechatIMG19.jpeg

说明一下这里的details里面是不同的链接方式都能进入到APP里面，这样开发者可以通过控制details里面的paths来进行不同页面不同模块的跳转。

比如我可以通过：https://www.icarusli.com/botaochen/123访问APP，https://www.icarusli.com是域名 botaochen/*  “*”可以是任何字符串。

给一个其他成熟公司的通用链接文件是怎么写的，可以参考一下

*6.将apple-app-site-association文件上传到服务器的.well-known文件夹下面。*

*7.验证文件是否合格*

苹果验证网站
域名+“apple-app-site-association”进行验证（有时候这里校验也不是很准确）
https://www.icarusli.com/apple-app-site-association

*8.测试一下通用链接是否生效。*

![](http://upload-images.jianshu.io/upload_images/2728934-60bf4727a15b133d.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
WechatIMG21.jpeg

如果出现下面第二项就成功了。

*9.后续和APP的交互*

-(BOOL)application:(UIApplication *)application continueUserActivity:(NSUserActivity *)userActivity restorationHandler:(void (^)(NSArray * _Nullable))restorationHandler{
    if ([userActivity.activityType isEqualToString: NSUserActivityTypeBrowsingWeb]) {
        NSURL *url = userActivity.webpageURL;
    }
    return YES;
}

利用这个代理，能够捕捉通过通用链接进入APP的时机，以及通用链接上面附带的信息。

通用链接实际上还是比较好实现的，看步骤都不难，如果能注意到我最开始说的两个问题就没什么好说的了，其他的就是按部就班。