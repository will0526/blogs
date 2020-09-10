# Adapay  SDK  设计说明


[TOC] 


# 修订记录

| 版本 | 作者 | 日期  | 说明 |
| ---- | ---- | ----| ---- |
| 1.0.0 | wyy | 20190909 | 初稿 |
| 1.1.0 | wyy | 20200901 | 优化 |

# 版本记录

| 版本 | 作者 | 日期  | 说明 |
| ---- | ---- | ----| ---- |
| 1.0.0 | wyy | 20190830 | 初稿 |
| 1.1.0 | wyy | 20200901 | 优化 |
# 简介
Adapay SDK 主要包含 server SDK 与 client SDK 。商户通过接入 server SDK 与 client SDK 可快速接入支付系统，实现支付功能。

# 功能说明
## server SDK
帮助商户服务端接入交易模块，目前 Adapay 的 SDK 支持的交易模块包括 支付（Payment）、退款（Refund）、查询、关单功能，具体可参考 API文档。
目前 server SDK 包含 Java，PHP，Python，Node，Go 语言。
### 功能列表
| 编号 | 功能 | 说明 |
| ---- | ---- | ----|
| 1 | SDK 初始化 | 初始化服务端 SDK |
| 2 | 异步消息 | 启动 MQTT 建立消息监听 |
| 3 | 聚合支付 | 支付对象（Payment）相关操作功能 |
| 3 | 钱包收银台 | 退款对象（Refund）相关操作功能 |
| 4 | 辅助接口 | 个人用户对象（Member）相关操作功能 |


### 1.SDK 初始化

####1.1功能说明

在交易开始前，SDK 先完成内部的初始化，包括加载商户配置文件，获取 MQTT 接入 token。建立 MQTT 连接。
    
####1.2多商户初始化
   
   说明：将多商户的配置信息通过字典的形式传入 SDK 内，后续调用接口时，可通过字典key值取对应商户配置信息
   
   方法设计：
    
   ```
    dict.add(merchantKey1, merchantConfig1)//merchantkey 商户配置key， merchantConfig1商户配置信息
    dict.add(merchantKey2, merchantConfig2)
    dict.add(merchantKey3, merchantConfig3)
    Adapay.init(dict, prod_mode);   //dict多商户配置字典，prod_mode生产模式还是测试模式，默认生产模式
   ```
    
####1.3单商户初始化
    
   说明：直接将商户的配置信息传入SDK中，调用接口时直接使用即可
   方法设计：
   ```
    Adapay.init(config, prod_mode);//config商户配置，prod_mode生产模式还是测试模式，默认生产模式
   ```
   
###2 异步消息
####2.1启动MQTT 监听
MQTT 建立连接授权方式为 token 模式，调用 Adapay 后端接口，获取 MQTT token，使用token 建立连接
   
MQTT连接说明：
     
     1，监听模式为广播
     2，授权方式为 token 模式
     3，clientID 为 (外部传入deviceID+商户live apikey) hash 值
     4，MQTT链接断开或重连失败时需发起连接
     
具体 MQTT 接入方法参见<a href="https://help.aliyun.com/product/100973.html?spm=a2c4g.11186623.6.540.f2be23f7hQ48od">微消息队列</a>

方法设计：
   ```
    Adapay.startMQTT(deviceID, config, callback)
   ```
  
####2.2 MQTT 消息处理 
处理 MQTT 消息，MQTT消息数据结构详见<a href="https://docs.adapay.tech/api/webhook.html#id7">MQTT 消息数据</a>

####2.3 MQTT 异常处理

token过期时，会接收到token过期消息，收到过期通知时，主动发起获取token，重新连接


###3. 聚合支付

设计说明

   * 支付对象
	    *  创建支付对象
		    * Payment.create(params)
	    * 查询支付对象
            * Payment.query(params)
        *   关闭支付对象
            * Payment.close(params)
	    * 查询支付对象列表
	        * Payment.list(params)
	    * 支付关单
	        * Payment.close(params)
   * 退款对象
        * 创建退款对象
            * Refund.create(params)
        * 查询退款对象
            * Refund.query(params)
   * 支付撤销对象
        *   创建支付撤销对象
            *   Payment.createReverse(params)
        *   查询支付撤销对象
            *   Payment.queryReverse(params)
        *   查询支付撤销对象列表
            *   Payment.queryReverseList(params)
   
   * 支付确认对象 PaymentConfirm
        *   创建支付确认对象
            *   PaymentConfirm.create(params)
        *   查询支付确认对象
            *   PaymentConfirm.query(params)
        *   查询支付确认对象列表
            *   PaymentConfirm.queryConfirmList(params)        
   
   * 个人用户 Member
        * 创建用户
		    * Member.create(params)
	    * 查询用户
		    * Member.query(params)
	    * 更新用户
		    * Member.update(params)
	    * 查询用户列表
		    * Member.list(params)
   * 企业用户 CorpMember
        * 创建用户
            * CorpMember.create(params, attach_file)
        * 查询用户
		    * CorpMember.query(params)
   * 结算账户 SettleAccount
        * 创建结算账户
            * SettleAccount.create(params)
        * 查询结算账户
            * SettleAccount.query(params)
        * 删除结算账户
            * SettleAccount.delete(params)
        * 修改结算账户配置
            * SettleAccount.update(params)
        * 查询结算账户明细列表
            * SettleAccount.detail(params)
           
### 钱包收银台
   * 取现对象 Drawcash
        * 创建取现对象
            * Drawcash.create(params)
        * 查询取现对象
            * Drawcash.query(params)
   * 账户对象 Account
        * 查询账户余额
            * Account.balance(params)
        * 创建钱包支付对象
            * Account.payment(params)
   * 收银台对象 Checkout
        * 创建收银台对象	
        	* Checkout.create(params)
        * 查询收银台对象列表
            * Checkout.list(params)
   * 钱包 Wallet
        * 钱包登录
            * Wallet.login(params)

### 辅助接口

   * 工具类 AdapayTools
        * 对账单下载
            * AdapayTools.downloadbill(bill_date)
        * 获取银联云闪付用户标识
            * AdapayTools.unionUserId(unionParam)

##Client SDK

###功能列表

| 编号 | 功能 | 说明 |
| ---- | ---- | ----|
| 1 | 发起支付 | 创建支付对象（payment） 

###1 发起支付
* 功能说明
商户侧应用通过商户服务端获取交易凭证 <a href="https://docs.adapay.tech/api/trade.html#payment">Payment对象</a>，将 Payment对象 对应的 JSON 格式字符串传入 SDK 发起支付。
* 流程说明
	![Alt text](./1567841299599.png)
	* test 模式，prod_mode 为 false的话，跳转到payment 内的payinfo字段返回的URL页面，开始轮询模拟支付结果
	* 如果不是APP支付（正扫，反扫，）的话，直接轮询支付结果
	* 结果回调为 <a href="https://docs.adapay.tech/api/trade.html#payment">Payment对象</a>
* 方法定义
	* Adapay.doPay(payment,callback);
	* 传入参数
		* payment 调用服务端下单接口返回的支付凭据，不可为空
		* callback 获得支付结果后回调方法
		* queryTimeout 轮询超时时间，默认 180 秒，可不传
	* 返回参数
		* resultCode 返回码，见附录 [返回码表](#result_code)
		* resultMessage 返回描述
		* payment 支付对象信息，具体以服务端返回内容为准
	
* 轮询接口说明
	* 根据支付凭证内的query_url 查询支付结果，
	* GET 请求
	* 无需加解签
	* 轮询间隔 5秒一次，默认轮询时间 120秒




#附录
<a id="api_introduce"></a>
##接口说明
* 请求参数
		
	公共参数 head 头参数
			
	| 参数 | 类型 | 必填 | 说明 |
	| ---- | ---- | ----|----|
	| authorization | string | Y | 商户进件返回的 api_key |
	| signature | string | Y | 加密签名 |
	| sdk_version | string | Y | sdk 版本号（例 Java_v1.0.2） |
	
* 返回参数

	公共返回参数

    | 参数 | 类型 | 必填 |说明 |
	| ---- | ---- | ----|----|
	| status | string | Y | 交易状态：成功succeeded,处理中 pending, 或者失败 failed |
	| type | string | Y | 错误类型，可以是 invalid_request_error、api_error、channel_error 或 card_error |
	| failure_code | string | Y | 错误码，由第三方支付渠道返回的错误代码 |
	| failure_msg | string | Y | 返回具体的错误描述 |
	| param | string | Y | 当发生参数错误时返回具体的参数名，如 id |
	| signature | string | Y | 返回参数的签名串  |

* 签名规则
	 详见 <a href="https://doc.rdc.aliyun.com/docs/87OpqR8x/vLPyVQiaekMF?spm=0.0.0.0.F4nz84">签名方式</a>
	* RSA1 算法（RSA+SHA1）
	    * POST 请求：待加密原文为请求URL地址与请求参数拼接的字符串SHA1签名
		    * RSA（SHA1（请求URL +  JSON.string（请求参数））
	    * GET 请求：待加密原文为请求URL地址与请求参数拼接的字符串（参数根据字母顺序拼接为JSON 字符串）SHA1签名
		    *  RSA（SHA1（请求URL +  JSON.string(请求参数字母顺序字符串））
		    




##服务端异常响应码
<a id="exception_code"></a>

| 参数 |说明 |
| ---- |----|
| request\_parameter\_error|请求参数错误|
|system_exception | 系统异常 |
|config_exception | 配置错误|
|security_exception |签名错误 |
|token\_revoke\_error | token 注销失败|
|token\_apply\_error | token 申请失败|
|token\_invalided | token 已失效|
|payment\_id\_not\_exists |对应支付记录不存在 |
|request\_order\_no\_repeate |请求订单号重复 |
|channel_error|通道异常|
|channel_response_code_fail|支付渠道响应码错误|
|mer_not_register|商户未入驻|


##客户端返回码
<a id="result_code"></a>
|参数|说明|
|----|----|
|ResultSuccess|支付成功|
|ResultFailed|支付失败|
|ResultPending|支付中|
|ResultParamError| 参数错误|
|ResultOutTime|订单超时|
|ResultCancel|用户取消|
|ResultError|其他错误|










