# RN 开发相关命令

## 打包

```
react-native bundle --entry-file index.js --bundle-output  ${RN_LOCAL_ZIP_PATH}/index.ios.bundle --platform ios --assets-dest  ${RN_LOCAL_ZIP_PATH} --dev false 
```

其中主要参数的含义是：

* entry-file：js的根文件，在RN中一般是index.js或index.android.js/index.ios.js
* platform：平台，iOS或Android
* dev：开发者模式，若是false，警告会被禁止，bundle文件会被压缩
* bundle-output: 生成的bundle文件名
* assets-dest: 资源文件的文件夹




## 安装插件

```
npm install react-native-hf-crypt-tools@1.0.0 --save
```

指定源安装：

```
npm --registry http://nexus-emas.chinapnr.com:9991/repository/npm-public/ install react-native-hf-crypt-tools@1.0.0 --save
```

## 启动NPM 服务

```
/usr/local/bin/node /usr/local/lib/node_modules/react-native-cli start
```


## iOS 自动获取debug IP address

```
export NODE_BINARY=node
../node_modules/react-native/scripts/react-native-xcode.sh
```