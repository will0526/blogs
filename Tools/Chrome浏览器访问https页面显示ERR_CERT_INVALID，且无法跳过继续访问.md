#Chrome浏览器访问https页面显示ERR_CERT_INVALID，且无法跳过继续访问

 Chrome访问https页面显示ERR_CERT_INVALID，以往版本可以选择跳过，继续访问，但是新版本Chrome不允许继续，且提示：

您的连接不是私密连接
攻击者可能会试图从 XX.XX.XX.XX 窃取您的信息（例如：密码、通讯内容或信用卡信息）。了解详情

NET::ERR_CERT_INVALID

将您访问的部分网页的网址、有限的系统信息以及部分网页内容发送给 Google，以帮助我们提升 Chrome 的安全性。隐私权政策

XX.XX.XX.XX 通常会使用加密技术来保护您的信息。Google Chrome 此次尝试连接到 XX.XX.XX.XX 时，此网站发回了异常的错误凭据。这可能是因为有攻击者在试图冒充 XX.XX.XX.XX，或 Wi-Fi 登录屏幕中断了此次连接。请放心，您的信息仍然是安全的，因为 Google Chrome 尚未进行任何数据交换便停止了连接。

您目前无法访问 XX.XX.XX.XX，因为此网站发送了 Google Chrome 无法处理的杂乱凭据。网络错误和攻击通常是暂时的，因此，此网页稍后可能会恢复正常。

Mac OS Chrome浏览器访问自签名证书网站点高级后没有继续访问而提示以上信息。
Safari中则有继续访问并且证书已添加到信任，Chrome 目前未找到解决方法，仅作记录。

解决方法： 在当前页，直接键盘敲入 thisisunsafe 来自评论区↓

