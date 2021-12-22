# 主要步骤

1. 商户入网

1. 开发前配置

1. 服务端开发

1. 客户端开发

# 商户入网

商户按照以下流程操作，成为银联 Apple Pay 在线支付商户

# 开发前配置

本小节提供给具有一定苹果者账号维护经验的人员使用

## 关于商户 CSR

CSR文件为苹果开发者在配置苹果开发证书时所需要的文件 即 certSigningRequest文件。

接入银联 Apple Pay 在线支付的商户，须生成 Apple Pay 专用的 CSR 文件并提交至Apple 开发者网站进行签名，以签署证书，取得 Apple Pay 的访问权限。 在银联 SDK 模式中，银联代为商户生成 CSR 文件，商户可直接登录银联商户服务平台获取。		

## 申请 CSR										

在申请银联 Apple Pay 接入时，银联的联系人会分配商户服务平台的登录权限及 CSR的申请权限。登录银联[__商户服务平台__](https://merchant.unionpay.com/)，通过商户服务平台申请 CSR。进入安全管理-CSR 文件下载，点击“生成 CSR”按钮，并将获取的 CSR 保存。CSR 文件与商户代码一一对应，是交易安全保护的重要环节，请勿将CSR 透漏给无关人员。

![](https://tcs.teambition.net/storage/312c4f785b1858ec8c686ef397ed53b3e002?Signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9hcHBJZCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9vcmdhbml6YXRpb25JZCI6IiIsImV4cCI6MTY0MDc1NjQ5MCwiaWF0IjoxNjQwMTUxNjkwLCJyZXNvdXJjZSI6Ii9zdG9yYWdlLzMxMmM0Zjc4NWIxODU4ZWM4YzY4NmVmMzk3ZWQ1M2IzZTAwMiJ9.g0Q3Skyy4OT7Egq5TN-9PhZn-MWCWKGK3Qoe--sGG6E&download=FF5D643C-C98A-4897-BCFE-1DEA13E0952D.png "")

**重置 CSR 后，原 CSR 即刻失效，应重新向 Apple 公司的网站提交新的 CSR 文件**

## 注册并配置 merchant ID

登录[__苹果开发者中心__](https://developer.apple.com/)，创建Identifiers，选择 merchant ID

![](https://tcs.teambition.net/storage/312cda5624d08fc4b2b69fd675ad678a8254?Signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9hcHBJZCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9vcmdhbml6YXRpb25JZCI6IiIsImV4cCI6MTY0MDc1NjQ5MCwiaWF0IjoxNjQwMTUxNjkwLCJyZXNvdXJjZSI6Ii9zdG9yYWdlLzMxMmNkYTU2MjRkMDhmYzRiMmI2OWZkNjc1YWQ2NzhhODI1NCJ9.ar3Hopa3BogJBbimdZ5B0nEg_BNZImJxNQs-9l4sUjc&download=20211220112052.jpg "")

填入描述以及merchant ID，点击continue。最后点击register

![](https://tcs.teambition.net/storage/312c35f9f7e12d4bed37468d695fb2005461?Signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9hcHBJZCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9vcmdhbml6YXRpb25JZCI6IiIsImV4cCI6MTY0MDc1NjQ5MCwiaWF0IjoxNjQwMTUxNjkwLCJyZXNvdXJjZSI6Ii9zdG9yYWdlLzMxMmMzNWY5ZjdlMTJkNGJlZDM3NDY4ZDY5NWZiMjAwNTQ2MSJ9.VEkqalEBlkLJczGIDaVV5jzWCB1b-jdutVbSjcvaqCA&download=image.png "")

![](https://tcs.teambition.net/storage/312ce758abf18c671ceea45d1f7a65ab5749?Signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9hcHBJZCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9vcmdhbml6YXRpb25JZCI6IiIsImV4cCI6MTY0MDc1NjQ5MCwiaWF0IjoxNjQwMTUxNjkwLCJyZXNvdXJjZSI6Ii9zdG9yYWdlLzMxMmNlNzU4YWJmMThjNjcxY2VlYTQ1ZDFmN2E2NWFiNTc0OSJ9.ZDWitJ9GFc116R5OMO7Nau_-9ln9J5D8zA5IegX_p-4&download=20211220112327.jpg "")

注册成功后，选择生成的merchant ID ，编辑并配置证书

![](https://tcs.teambition.net/storage/312cf944a90caa787a338532a38b5f1918d3?Signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9hcHBJZCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9vcmdhbml6YXRpb25JZCI6IiIsImV4cCI6MTY0MDc1NjQ5MCwiaWF0IjoxNjQwMTUxNjkwLCJyZXNvdXJjZSI6Ii9zdG9yYWdlLzMxMmNmOTQ0YTkwY2FhNzg3YTMzODUzMmEzOGI1ZjE5MThkMyJ9.EW9pD7JB2AXQBKUGnJelqp-fD-t704Pxnr_D1NWykyk&download=B31F6CD5-0704-416A-9605-775A1BFEF1EC.png "")

选择 create certificate，选择开通中国大陆Apple Pay支付能力选项，选取上一步从银联下载的CSR文件

![](https://tcs.teambition.net/storage/312c90968cc8dcc9a9e8f5219ec92ac24e1c?Signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9hcHBJZCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9vcmdhbml6YXRpb25JZCI6IiIsImV4cCI6MTY0MDc1NjQ5MCwiaWF0IjoxNjQwMTUxNjkwLCJyZXNvdXJjZSI6Ii9zdG9yYWdlLzMxMmM5MDk2OGNjOGRjYzlhOWU4ZjUyMTllYzkyYWMyNGUxYyJ9.CLV1nnsF9ifjYWmgSwT0M3a8itBh3ebkO8ysBR1RKOA&download=20211220112803.jpg "")

![](https://tcs.teambition.net/storage/312c0c03c55076f4c2b8ef90ee7456f91000?Signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9hcHBJZCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9vcmdhbml6YXRpb25JZCI6IiIsImV4cCI6MTY0MDc1NjQ5MCwiaWF0IjoxNjQwMTUxNjkwLCJyZXNvdXJjZSI6Ii9zdG9yYWdlLzMxMmMwYzAzYzU1MDc2ZjRjMmI4ZWY5MGVlNzQ1NmY5MTAwMCJ9.W2Tdf2LJ9cbTcStZjNm5wneAhOEKsEOi0Rkl-Gb0NG0&download=20211220112817.jpg "")

## 配置App ID

选择应用对应的APP ID，勾选Apple Pay Payment processing，配置上一步生成好的 merchant ID 并保存，下载cer 文件，安装到开发设备中。

![](https://tcs.teambition.net/storage/312cca8691f0ce2f50e0b5231a98d8836c75?Signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9hcHBJZCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9vcmdhbml6YXRpb25JZCI6IiIsImV4cCI6MTY0MDc1NjQ5MCwiaWF0IjoxNjQwMTUxNjkwLCJyZXNvdXJjZSI6Ii9zdG9yYWdlLzMxMmNjYTg2OTFmMGNlMmY1MGUwYjUyMzFhOThkODgzNmM3NSJ9.KcaDp51FE6qVY0tzSRcy09dJ8QF3HdhTU1Eajrnw4NA&download=83B413E7-E840-4135-BC1B-1663FFD31B33.png "")

# 服务端开发

对接汇付服务端[__下单接口__](https://atsp.yuque.com/docs/share/bf4003e5-7cc9-4cb0-9acf-8e3a27a00af2?#)，传入对应参数，获取 TN 号

（此处无需对接银联Apple Pay 服务端SDK）



# 客户端开发				

本小节提供给那些具有一定 iOS 编程经验的开发人员使用						

## 接入SDK

可从[__银联官方网站__](https://open.unionpay.com/tjweb/doc/mchnt/list?productId=3)获取最新的SDK 包以及接入说明，在此根据 SDK 作简要说明，流程配置大体相同。以银联官方接入说明为准。

### SDK 说明

Apple Pay 版本静态库，以下简称 UPAPayPlugin，包含文件: 

UPAPayPlugin.h

UPAPayPluginDelegate.h

libUPAPayPlugin.a

### 添加SDK 包

将 sdk/inc 目录和 sdk/libs 目录下对应版本的三个文件添加到商户 App 工程中，添加 后如图:

![](https://tcs.teambition.net/storage/312c4fe8b300a02f6eb439d292e64467894e?Signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9hcHBJZCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9vcmdhbml6YXRpb25JZCI6IiIsImV4cCI6MTY0MDc1NjQ5MCwiaWF0IjoxNjQwMTUxNjkwLCJyZXNvdXJjZSI6Ii9zdG9yYWdlLzMxMmM0ZmU4YjMwMGEwMmY2ZWI0MzlkMjkyZTY0NDY3ODk0ZSJ9.JSMSX6Uq0-40_g4PZHwxHlGTgm-of7sSVVx3hMI7V70&download=4682F70E-F044-4B49-8E2E-FB6863C55B39.png "")

### 工程配置

1，添 加 CFNetwork.framework 、 libUPAPayPlugin.a 、 PassKit.framework 、 SystemConfiguration.framework 到商户 App 工程中，添加后如下图:

![](https://tcs.teambition.net/storage/312c50bb10e478d08f6c740681c3ff482d98?Signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9hcHBJZCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9vcmdhbml6YXRpb25JZCI6IiIsImV4cCI6MTY0MDc1NjQ5MCwiaWF0IjoxNjQwMTUxNjkwLCJyZXNvdXJjZSI6Ii9zdG9yYWdlLzMxMmM1MGJiMTBlNDc4ZDA4ZjZjNzQwNjgxYzNmZjQ4MmQ5OCJ9.lSFVedXVSixcr6rBURsruVzBz5YAk_jGKxISUXVrdCY&download=2670BAEA-046E-4B54-A845-C2B4BC57AB10.png "")

2，配置Apple Pay capability，添加第二步注册成功的merchant ID

![](https://tcs.teambition.net/storage/312c6dd268bfabf9774317b69739093bb312?Signature=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcHBJRCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9hcHBJZCI6IjU5Mzc3MGZmODM5NjMyMDAyZTAzNThmMSIsIl9vcmdhbml6YXRpb25JZCI6IiIsImV4cCI6MTY0MDc1NjQ5MCwiaWF0IjoxNjQwMTUxNjkwLCJyZXNvdXJjZSI6Ii9zdG9yYWdlLzMxMmM2ZGQyNjhiZmFiZjk3NzQzMTdiNjk3MzkwOTNiYjMxMiJ9.zXfXIck3fcryJRrJ3WdQdcwcpSHEUBwiIWdvYEHSHk0&download=80D69785-927C-4586-AA78-B24D27123BBD.png "")

### 支付接口						

```text
+(BOOL)startPay:(NSString*)tn 
		   mode:(NSString*)mode
 viewController:(UIViewController*)viewController
       delegate:(id<UPAPayPluginDelegate>)delegate 
 andAPMechantID:(NSString* )mID
```

| 参数名称           | 类型                       | 含义                                            |
| -------------- | ------------------------ | --------------------------------------------- |
| tn             | NSString*                | 交易流水号，服务端下单返回的pay_info                        |
| mode           | NSString*                | 接入模式，"00"代表接入生产环境，"01"代表接入开发测试环境（建议直接生产环境调试）  |
| viewController | UIViewController*        | 发起调用的视图控制器                                    |
| delegate       | id<UPAPayPluginDelegate> | 实现 UPAPayPluginDelegate 方法的 UIViewController; |
| mID            | NSString*                | 在苹果开发者网站注册申请的merchant ID （详情见第二步）             |
| 返回值            | BOOL                     | YES:调起支付控件成功; NO:调起支付控件失败;                    |

### 支付回调

```text
-(void) UPAPayPluginResult:(UPPayResult *) payResult;
```

银联手机支付控件结果回调函数有四个支付状态返回值，在 UPPayResult 类中有 关于 UPPaymentResultStatus 的详细说明，从而根据支付结果的不同进行相应的处理。

示例代码：

```text
#pragma mark -
#pragma mark 响应控件返回的支付结果
#pragma mark -
- (void)UPAPayPluginResult:(UPPayResult *)result
{
    if(result.paymentResultStatus == UPPaymentResultStatusSuccess) {
        NSString *otherInfo = result.otherInfo?result.otherInfo:@"";
        NSString *successInfo = [NSString stringWithFormat:@"支付成功\n%@",otherInfo];
        [self showAlertMessage:successInfo];
    }
    else if(result.paymentResultStatus == UPPaymentResultStatusCancel){

        [self showAlertMessage:@"支付取消"];
    }
    else if (result.paymentResultStatus == UPPaymentResultStatusFailure) {
        
        NSString *errorInfo = [NSString stringWithFormat:@"%@",result.errorDescription];
        [self showAlertMessage:errorInfo];
    }
    else if (result.paymentResultStatus == UPPaymentResultStatusUnknownCancel)  {
        
        //TODO UPPAymentResultStatusUnknowCancel表示发起支付以后用户取消，导致支付状态不确认，需要查询商户后台确认真实的支付结果
        NSString *errorInfo = [NSString stringWithFormat:@"支付过程中用户取消了，请查询后台确认订单"];
        [self showAlertMessage:errorInfo];
        
    }
}
```

