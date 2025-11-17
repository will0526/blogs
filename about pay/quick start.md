# quick start

## Step1 接入准备

在开始开发前，您需要先完成以下步骤：

### 1.[注册](!https://dashboard.huifu.com/customers/login) 斗拱 账号并入网
开通生产商户或联调环境的商户，并获取商户管理员操作账号。（请销售经理协助）

### 2.参数配置(配置公私钥，配置支付渠道)
#### 2.1 配置RSA 公私钥
斗拱系统中有两套公私钥，分别对应为商户侧和斗拱侧。
在每次网络请求中，商户侧使用商户私钥加密发送请求签名，斗拱侧使用商户公钥（对配置在商户控台）进行验签。
斗拱使用斗拱私钥加密响应报文签名，商户侧使用斗拱公钥进行验签。（详情见[说明](!https://paas.huifu.com/partners/jiekouguifan#/api_v2jqyq) ）

建议直接使用斗拱提供的sdk，已为您封装好加签验签方法等网络请求方法。

商户 RSA 公私钥可以选择自己生成（**2048位， pkcs8格式**）也可以使用斗拱控台生成。[详情见](!https://paas.huifu.com/partners/guide/#/guide_gsycshq)

#### 2.2 获得产品号，系统号，商户号，对应公私钥。

产品号，系统号，商户号，汇付侧公钥可通过控台获取
![控台](https://cloudpnrcdn.oss-cn-shanghai.aliyuncs.com/opps/imgs/gongsiyao/gongsiyao5.png)

## Step2 对接服务端 SDK

**（写在最前面，请按以下步骤操作）**
### 接入步骤
* 1，安装好依赖库保证运行环境没问题，可直接运行SDK demo，建议从[聚合正扫](!https://paas.huifu.com/partners/api/#/smzf/api_jhzs?id=minizfb) 接口开始，如能正常下单，说明运行环境没问题。
* 2，只更改配置信息。使用上一步获取到的 产品号，系统号，商户号，对应公私钥替换demo 中的参数。如能成功，说明商户配置没问题，否则请检查商户控台配置。
* 3，选择对应的支付通道，修改代码，调用聚合正扫接口，如返回正确的支付信息。则说明接口对接成功
* 4，参照 demo 将 sdk 接入您自己的项目中
* 5，您可以使用我们为您提供的代码片段快速接入对应接口。可在[在线联调工具](!https://paas.huifutest.com/explorer/api-debug) 获取到对应接口代码片段
![联调工具](https://cloudpnrcdn.oss-cn-shanghai.aliyuncs.com/opps/imgs/guide/api_debug.jpg)
安装并部署服务端服务到您的服务器，将下单功能开放接口给前端应用调用

### 常见问题
* 接口请求报签名错误，说明商户私钥签名后的内容，斗拱侧使用商户公钥校验不通过。
建议检查商户公私钥是否匹配，以及公私钥格式（**2048位， pkcs8格式**）
* 接口返回验签出错，说明汇付公钥配置不正确，如只是某些接口报这个错，聚合正扫接口是好的。可使用 [在线联调工具](!https://paas.huifutest.com/explorer/api-debug) 对比检查请求与返回报文。


## Step3 前端应用对接

前端应用通过网络请求获取到应用服务端从斗拱获取的支付信息。在前端页面或者APP内处理后，发起支付。

以支付宝为例（通过拉起支付宝APP 然后调用支付宝内said为10000007的扫码功能来发起支付）

* 1，调用 聚合正扫 接口时trade_type: A_NATIVE(支付宝正扫)
* 2，前端拿到服务端返回的payinfo信息中的qr_code，在 APP 内 通过打开第三方APP的方式打开此URL
示例代码：
    ```text
    # iOS app
    [[UIApplication sharedApplication]openURL:[NSURL URLWithString: "alipays://platformapi/startapp?saId=10000007&qrcode=https://qr.alipay.com/bax02911brluc2xieoph6001"]];
    # android app
    // 固定前缀
    String topic = "alipays://platformapi/startapp?saId=10000007&qrcode=";
    // 从汇付正扫接口获取的参数（以下值仅为示例）
    String qrcodeUrl = "https://qr.alipay.com/bax02911brluc2xieoph6001"
    // 字符串拼接
    String jumpUrl = topic + qrcodeUrl;
    // 按以上示例拼接得出结果
    // jumpUrl 为 alipays://platformapi/startapp?saId=10000007&qrcode=https://qr.alipay.com/bax02911brluc2xieoph6001
    Intent intent = new Intent();
    intent.setAction("android.intent.action.VIEW");
    // jumpUrl 为先前示例中拼装的 url
    Uri contentUrl = Uri.parse(jumpUrl);
    intent.setData(contentUrl);
    activity.startActivity(intent);

* 3，取出接口返回的qr_code，在 APP 内 通过打开第三方APP的方式打开如下URL
* 4，获取终态，客户支付完成后汇付会将支付结果推送到客户异步地址，如果长时间未收到异步结果可以调用扫码交易查询接口查询交易状态

详情参见：[支付宝接入指引](!https://paas.huifu.com/partners/guide#/zffssm/guide_zffssm_zfbzf?id=_331-native%e6%94%af%e4%bb%98%e6%96%b9%e5%bc%8f%e6%8e%a5%e5%85%a5%e6%b5%81%e7%a8%8b)

* 对应微信接入可参见[微信接入指引](!https://paas.huifu.com/partners/guide#/zffssm/guide_zffssm_wxapp?id=_331-%e4%ba%a4%e6%98%93%e6%b5%81%e7%a8%8b)

更多请参见[指引文档](!https://paas.huifu.com/partners/guide#/)

至此您已经完成服务端与前端的对接工作，您可参考接口文档与在线联调工具进行下一步开发。




