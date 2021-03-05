# 二维码下载iOS APP方案
## itms-services



一般采用的是使用itms-services 来实现下载(升级)。
itms-services 的地址是:

itms-services://?action=download-manifest&url=$(plistURL)

plistURL 必须为https的链接

即下载页面的按钮点击实现跳转
window.location.href = itms-services://?action=download-manifest&url=$(plistURL)

## plist 文件模板

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>items</key>
        <array>
            <dict>
                <key>assets</key>
                <array>
                    <dict>
                        <key>kind</key>
                        <string>software-package</string>
                        <key>url</key>
                        <string>${ipaDownloadUrl}</string>
                    </dict>
                </array>
                <key>metadata</key>
                <dict>
                    <key>bundle-identifier</key>
                    <string>${identifier}</string>
                    <key>bundle-version</key>
                    <string>${version}</string>
                    <key>kind</key>
                    <string>software</string>
                    <key>subtitle</key>
                    <string>${subtitle}</string>
                    <key>title</key>
                    <string>${title}</string>
                </dict>
            </dict>
        </array>
    </dict>
</plist>
```

