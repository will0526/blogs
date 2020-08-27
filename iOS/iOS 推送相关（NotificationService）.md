

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






