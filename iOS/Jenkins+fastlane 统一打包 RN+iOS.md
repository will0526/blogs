版权声明：本文为博主原创文章，转载请附上原文出处链接
#Jenkins+fastlane 统一打包 RN+iOS

##Fastlane配置
iOS根目录下，建一个fastlane文件夹，并保存
Fastfile
Appfile

Fastfile信息参考如下

```
fastlane_version "1.98.0"


WORKSPACE = ENV["WORKSPACE"]
IPA_SCHEME = ENV["IPA_SCHEME"]
IPA_NAME = ENV["IPA_NAME"]
IPA_BUILD = ENV["IPA_BUILD"]
IPA_CODESIGN = ENV["IPA_CODESIGN"]
IPA_PROVISION = ENV["IPA_PROVISION"]
IPA_PROVISION_SPECIFIER = ENV["IPA_PROVISION_SPECIFIER"]
IPA_BUNDLEID = ENV["IPA_BUNDLEID"]
TEST_SERVER_URL = ENV["TEST_SERVER_URL"]
TEST_SERVER_PATH = ENV["TEST_SERVER_PATH"]


IPA_ENV = ENV["IPA_ENV"]

IPA_TEAM = ENV["IPA_TEAM"]
if "#{IPA_TEAM}" != "" then
    IPA_TEAM_DEFINE = "DEVELOPMENT_TEAM=\'#{IPA_TEAM}\'"
else
    IPA_TEAM_DEFINE = ""
end




# 获取工程属性
def getBuildSetting(scheme, key)

    # 尝试从工程的plist文件中查找
    plistPath = `xcodebuild -showBuildSettings -workspace ../#{WORKSPACE}.xcworkspace -scheme #{scheme} | grep INFOPLIST_FILE | awk -F '=' '{print $2}' | awk '{$1=$1;print}' | tr -d '\n'`
    value = get_info_plist_value(path: "#{plistPath}", key: "#{key}")
    
    # 查看从plist中找到的结果是否指向工程属性
    if value
        key = /(?=\$\()[^\)]*\)/.match("#{value}")
        if ! key
            return value
        end
        
        # 重新定义工程属性的名称
        key = value[2,value.length-3]
    end
    
    # 如果plist中没有查找到或指向了工程中的属性，则从工程属性中查找
    value = `xcodebuild -showBuildSettings -workspace ../#{WORKSPACE}.xcworkspace -scheme #{scheme} | grep \" #{key}\" | awk -F '=' '{print $2}' | awk '{$1=$1;print}' | tr -d '\n'`
    return value
end

# 生成下载用的PLIST文件
def genPlist(url, ipaName, name, version, bundleID, plistFile)

    plistContent = "<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\"?>\n"+
    "<!DOCTYPE plist PUBLIC \\\"-//Apple//DTD PLIST 1.0//EN\\\" \\\"http://www.apple.com/DTDs/PropertyList-1.0.dtd\\\">\n"+
    "<plist version=\\\"1.0\\\">\n"+
    "  <dict>\n"+
    "      <key>items</key>\n"+
    "      <array>\n"+
    "          <dict>\n"+
    "              <key>assets</key>\n"+
    "              <array>\n"+
    "                  <dict>\n"+
    "                      <key>kind</key>\n"+
    "                      <string>software-package</string>\n"+
    "                      <key>url</key>\n"+
    "                      <string>#{url}/#{ipaName}</string>\n"+
    "                  </dict>\n"+
    # "                  <dict>\n"+
    # "                      <key>kind</key>\n"+
    # "                      <string>full-size-image</string>\n"+
    # "                      <key>needs-shine</key>\n"+
    # "                      <false/>\n"+
    # "                      <key>url</key>\n"+
    # "                      <string>#{url}/full-size-image.png</string>\n"+
    # "                  </dict>\n"+
    # "                  <dict>\n"+
    # "                      <key>kind</key>\n"+
    # "                      <string>display-image</string>\n"+
    # "                      <key>needs-shine</key>\n"+
    # "                      <false/>\n"+
    # "                      <key>url</key>\n"+
    # "                      <string>#{url}/display-image.png</string>\n"+
    # "                  </dict>\n"+
    "              </array>\n"+
    "              <key>metadata</key>\n"+
    "              <dict>\n"+
    "                  <key>title</key>\n"+
    "                  <string>#{name}</string>\n"+
    "                  <key>bundle-version</key>\n"+
    "                  <string>#{version}</string>\n"+
    "                  <key>bundle-identifier</key>\n"+
    "                  <string>#{bundleID}</string>\n"+
    "                  <key>kind</key>\n"+
    "                  <string>software</string>\n"+
    "              </dict>\n"+
    "          </dict>\n"+
    "      </array>\n"+
    "  </dict>\n"+
    "</plist>"

    `echo \"#{plistContent}\" > #{plistFile}`

end

# 制作ipa
def genIPA(isTestEnv)
    `rm -rf ../build`

# 钥匙串的路径为 ${HOME}/Library/Keychains/  ，我们需要操作的是 login.keychain-db  或者  login.keychain
#示例 security set-key-partition-list -S apple-tool:,apple: -s -k keychainPass keychainName
#具体 security set-key-partition-list -S apple-tool:,apple:,codesign: -s -k 123456 ~/Library/Keychains/login.keychain-db


#更新 bundleID
update_app_identifier(
  xcodeproj: "./#{WORKSPACE}.xcodeproj", # Optional path to xcodeproj, will use the first .xcodeproj if not set
  plist_path: "./#{WORKSPACE}/Info.plist", # Path to info plist file, relative to xcodeproj
  app_identifier: "#{IPA_BUNDLEID}" # The App Identifier
)

#更新配置文件设置，只对打包的 scheme 进行修改，其他不动
    update_project_provisioning(
     xcodeproj: "./#{WORKSPACE}.xcodeproj",
     profile: "./profile.mobileprovision", # optional if you use sigh
     target_filter: "#{IPA_SCHEME}", # matches name or type of a target
     build_configuration: "Release",
     code_signing_identity: "#{IPA_CODESIGN}" # optionally specify the codesigning identity
    )


    gym(
        workspace: "./#{WORKSPACE}.xcworkspace",
        scheme: "#{IPA_SCHEME}",
        clean: true,
        derived_data_path: './build/',
        output_directory: './build/',
        archive_path: './build/',
        output_name: "#{IPA_SCHEME}",
        configuration: 'Release',
        codesigning_identity: "#{IPA_CODESIGN}",
        include_symbols: 'true',
        include_bitcode: 'false',
        export_xcargs: "-allowProvisioningUpdates",
	toolchain: "cn.ijiami.obf",
        export_method: "#{IPA_ENV}",
        export_options: {
        provisioningProfiles: { 
          "#{IPA_BUNDLEID}":"#{IPA_PROVISION}"
        },
      },
        xcargs: "PROVISIONING_PROFILE_SPECIFIER='#{IPA_PROVISION}' PRODUCT_BUNDLE_IDENTIFIER='#{IPA_BUNDLEID}' ENVIRONMENT_TEST='#{isTestEnv}' CURRENT_PROJECT_VERSION='#{IPA_BUILD}' PROVISIONING_PROFILE_SPECIFIER='#{IPA_PROVISION_SPECIFIER}' PRODUCT_BUNDLE_NAME='#{IPA_NAME}' #{IPA_TEAM_DEFINE}"
    )

end

# 制作framework
def genFramework(isTestEnv)

    `rm -rf ../build`
    xcodebuild(
        workspace: "../#{WORKSPACE}.xcworkspace",
        scheme: "#{FRAMEWORK_SCHEME}",
        derivedDataPath: './build/',
        archive_path: './build/',
        configuration: 'Release',
        xcargs: "CODE_SIGN_IDENTITY='#{FRAMEWORK_CODESIGN}' PROVISIONING_PROFILE='#{FRAMEWORK_PROVISION}' PRODUCT_BUNDLE_IDENTIFIER='#{FRAMEWORK_BUNDLEID}' ENVIRONMENT_TEST='#{isTestEnv}'"
    )
    `cp -r ../build/Build/Products/Release-iphoneos/#{FRAMEWORK_SCHEME}.framework ../build/`
    
end

# ipa发布到测试服务器
def uploadTestServer(isTestEnv, isAppStore, isFramework)

    # 创建打包目录
    foldername = `date +%s | tr -d '\n'`
    if isFramework then
        foldername = "#{FRAMEWORK_SCHEME}_#{foldername}"
    else
        foldername = "#{IPA_SCHEME}_#{foldername}"
    end
    `mkdir ../build/#{foldername}`

    # 创建描述文件，一行代表一个信息：
    # 工程名称
    # 软件名称
    # 版本号
    # build号
    # 创建时间
    # 运行环境
    if isFramework then
        `echo '#{FRAMEWORK_SCHEME}' > ../build/#{foldername}/index.link`
        `echo '#{FRAMEWORK_SCHEME}' >> ../build/#{foldername}/index.link`
        `echo '#{FRAMEWORK_VERSION}' >> ../build/#{foldername}/index.link`
        `echo '#{FRAMEWORK_BUILD}' >> ../build/#{foldername}/index.link`
    else
        `echo '#{IPA_SCHEME}' > ../build/#{foldername}/index.link`
        `echo '#{IPA_NAME}' >> ../build/#{foldername}/index.link`
        `echo '#{IPA_VERSION}' >> ../build/#{foldername}/index.link`
        `echo '#{IPA_BUILD}' >> ../build/#{foldername}/index.link`
    end
    package_time = `date '+%Y-%m-%d %H:%M:%S' | tr -d '\n'`
    `echo '#{package_time}' >> ../build/#{foldername}/index.link`
    if isTestEnv && isAppStore then #这里是联调
        `echo 'joinDebug' >> ../build/#{foldername}/index.link`
    elsif isTestEnv then
        `echo 'test' >> ../build/#{foldername}/index.link`
    elsif isAppStore then
        `echo 'appstore' >> ../build/#{foldername}/index.link`
    else
        `echo 'product' >> ../build/#{foldername}/index.link`
    end
    if isFramework then
        `echo 'framework' >> ../build/#{foldername}/index.link`
    else
        `echo 'application' >> ../build/#{foldername}/index.link`
    end

    # 将ipa或者framework文件复制到该目录中
    if isFramework then
        `mv ../build/#{FRAMEWORK_SCHEME}.framework ../build/#{foldername}/`
        `cp -r ../#{FRAMEWORK_SCHEME}/#{FRAMEWORK_SCHEME}.bundle ../build/#{foldername}/`
    else
        `mv ../build/#{IPA_SCHEME}.ipa ../build/#{foldername}/d.ipa`
        genPlist("#{TEST_SERVER_URL}/#{foldername}", "d.ipa", "#{IPA_NAME}", "#{IPA_VERSION}", "#{IPA_BUNDLEID}", "../build/#{foldername}/d.plist")
    end
    
    
    `upload_app ../build/#{foldername} iPhone`

   


end

default_platform :ios

platform :ios do
    before_all do
        # 设置全局变量
        ENV['FASTLANE_XCODE_LIST_TIMEOUT'] = '600'
        if "#{IPA_NAME}" == "" then
            IPA_NAME = getBuildSetting("#{IPA_SCHEME}", 'CFBundleDisplayName')
        end
        
        IPA_VERSION = getBuildSetting("#{IPA_SCHEME}", 'CFBundleShortVersionString')

        if "#{IPA_BUILD}" == "" then
            IPA_BUILD = getBuildSetting("#{IPA_SCHEME}", 'CFBundleVersion')
        end

   
        cocoapods(
        repo_update: false
        )

    end
    
    desc "打测试包"
    lane :test do |options|
        genIPA(1)
        uploadTestServer(true, false, false)
    end

    desc "打生产包"
    lane :product do |options|
        genIPA(0)
        uploadTestServer(false, false, false)
    end

    desc "打appstore包"
    lane :appstore do |options|
        genIPA(0)
       
        uploadTestServer(false, true, false)
    end


  

  after_all do |lane|
    
  end

  error do |lane, exception|
    
  end
end





```

Appfile信息参考如下


```
app_identifier "" # The bundle identifier of your app
apple_id "david.yi@chinapnr.com" # Your Apple email address
team_id "Y3697NHB4K"  # Developer Portal Team ID

```





##创建Jenkins项目

![image](http://upload-images.jianshu.io/upload_images/2728934-6e24fa5970a49196.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


##配置全局参数如下
![image](http://upload-images.jianshu.io/upload_images/2728934-8d0194180b6ca5fb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

|参数名称|参数类型|默认值|描述|参数值|备注|
|--- |--- |--- |--- |--- |--- |
|RN_VERSION |字符参数|无|RN bundle 版本号|&nbsp;|选中下方的“Trim the string”选项|
|RN_BUILD_TYPE|选项参数|无|RN 打包类型（Baseline：基线包，Extra：增量包）|Baseline/Extra|&nbsp;|
|GIT_BRANCH_RN|Git Parameter|无|RN 项目的 git 地址|&nbsp;|1."Parameter Type" 选择"Branch or Tag", 2."Advanced"中 "Use repository" 填入RN 项目git 地址|
|BUILD_IOS_IPA|布尔值参数|无|是否构建iOS应用|&nbsp;|如不勾选，默认只构建RN项目|
|GIT_BRANCH_IOS|Git Parameter|无|iOS 项目的 git 地址|&nbsp;|1."Parameter Type" 选择"Branch or Tag", 2."Advanced"中 "Use repository" 填入 iOS 项目git 地址|
| IPA_EXPORT_ENV |Extend choice parameter|development|ios 打包类型|development,app-store,ad-hoc|三种,默认是 development ,如果打的是 appStore 包，无论选什么,都会强制改为 app-store|
|ENVIRONMENT_CHOICE|选项参数|test|环境标志位|test/product/preproduct/appstore|测试/生产/准生产/App Store（生产环境）|
|IPA_NAME|hidden parameter|无|应用名称|无|应用APP显示名称|
|WORKSPACE|hidden parameter|无|工程名称|无|工程名称|
|IPA_SCHEME|hidden parameter|无|工程中要打包的目标名称|无|工程中要打包的目标名称|
|IPA_BUNDLEID|hidden parameter|无|工程bundleID|无|bundleID|
|IPA_CODESIGN_TEST|hidden parameter|无|codesign|无|只要不是 AppStore ，codesign 都是这一个|
|IPA_CODESIGN_APPSTORE|hidden parameter|无|appstore codesign|无|appstore codesign|
|TEST_SERVER_URL|hidden parameter|http://oa2pro.chinapnr.com/mobile/CI/iPhone/|测试服务器的地址|无|打包成功后应用上传地址|
|podUpdate|布尔值参数|无|是否要清除缓存，更新pod|无|除非SDK有更新，此项不需要勾选|

如图

![image](http://upload-images.jianshu.io/upload_images/2728934-763c6ffc346ce845.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2728934-a95584588f4f05e6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2728934-fd298cd020f3a863.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2728934-73c085424321a3df.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2728934-8836c6314f409988.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2728934-5d8d9505ba1dc260.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2728934-43fa07d9ef3e24d5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2728934-8d89c5812efb2d4f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2728934-435b75b02858fcd1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2728934-2198015710590404.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2728934-6764dfa4c66ce372.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2728934-b2ab12c8ee7dce1b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


##源码管理
分别设置RN与iOS的git信息
![image](http://upload-images.jianshu.io/upload_images/2728934-0f258a08dc57f60a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


##设置App Store账号信息
直接选择app store账号


##添加RN打包脚本

```
#打包RN包

cd "rn"

export rnPath="./ios/RNBundle" 
if [ -d "${rnPath}" ]; then
	rm -r ${rnPath}
	mkdir ${rnPath}
else
    mkdir ${rnPath}
fi

npm install

react-native bundle --entry-file index.js --bundle-output  ${rnPath}/index.ios.bundle --platform ios --assets-dest  ${rnPath} --dev false 

if [! -f "${rnPath}/index.ios.bundle"]; then
	echo "index.ios.bundle 生成失败"
	exit 1001
else
	echo "生成成功"
fi

echo "{'rn_version':'${RN_VERSION}','rn_build':'${BUILD_NUMBER}'}" >>  ${rnPath}/rn_info.json

```

##添加iOS打包脚本

```
#清pod缓存
if [ "$podUpdate" = "true" ]; then
	#是否要清除缓存，更新pod
	pod cache clean --all
	pod repo update
    
fi

#打包IPA
if [ "$BUILD_IOS_IPA" = "true" ]; then
	
    if [ "$IPA_EXPORT_ENV" = "app-store" ]; then
        export IPA_CODESIGN=$IPA_CODESIGN_APPSTORE
    else
        export IPA_CODESIGN=$IPA_CODESIGN_TEST
    fi
    
    export IPA_BUNDLEID=$IPA_BUNDLEID
    export IPA_BUILD=$BUILD_NUMBER
    export IPA_ENV=$IPA_EXPORT_ENV
    
    cd "./rn/ios"
    
    export 
      
    if [ "$IPA_EXPORT_ENV" = "app-store" ]; then
    
        result=`fastlane sigh -u $FASTLANE_ID -a $IPA_BUNDLEID --app-store true -q profile.mobileprovision`
        export IPA_PROVISION=`security cms -D -i profile.mobileprovision | sed -n -e '/<key>Name/,/string>/p' | sed -n '/string>/p' | awk -F '>' '{print $2}' | awk -F '<' '{print $1}'`
    
        export IPA_PROVISION_SPECIFIER=`security cms -D -i profile.mobileprovision | sed -n -e '/<key>Name/,/string>/p' | sed -n '/string>/p' | awk -F '>' '{print $2}' | awk -F '<' '{print $1}'`
        
    elif [ "$IPA_EXPORT_ENV" = "ad-hoc" ]; then    
    
        result=`fastlane sigh -u $FASTLANE_ID -a $IPA_BUNDLEID --adhoc true -q profile.mobileprovision`
        export IPA_PROVISION=`security cms -D -i profile.mobileprovision | sed -n -e '/<key>Name/,/string>/p' | sed -n '/string>/p' | awk -F '>' '{print $2}' | awk -F '<' '{print $1}'`
    
        export IPA_PROVISION_SPECIFIER=`security cms -D -i profile.mobileprovision | sed -n -e '/<key>Name/,/string>/p' | sed -n '/string>/p' | awk -F '>' '{print $2}' | awk -F '<' '{print $1}'`
    
    elif [ "$IPA_EXPORT_ENV" = "development" ]; then    
    
        result=`fastlane sigh -u $FASTLANE_ID -a $IPA_BUNDLEID --development true -q profile.mobileprovision`
        export IPA_PROVISION=`security cms -D -i profile.mobileprovision | sed -n -e '/<key>Name/,/string>/p' | sed -n '/string>/p' | awk -F '>' '{print $2}' | awk -F '<' '{print $1}'`
    
        export IPA_PROVISION_SPECIFIER=`security cms -D -i profile.mobileprovision | sed -n -e '/<key>Name/,/string>/p' | sed -n '/string>/p' | awk -F '>' '{print $2}' | awk -F '<' '{print $1}'`
    fi
    
    
    if [ "$ENVIRONMENT_CHOICE" = "test" ]; then
        
        result=`fastlane test`
        echo 'test'
    elif [ "$ENVIRONMENT_CHOICE" = "product" ]; then
        echo 'product'
        result=`fastlane product`
    elif [ "$ENVIRONMENT_CHOICE" = "appstore" ]; then
        echo 'app_Store'
        result=`fastlane appstore`
    fi  
fi

```

##上传RN bundle

```
#压缩RN包并上传

cd ./rn/ios/RNBundle

echo "开始压缩"
export RN_ZIP_NAME="${IPA_SCHEME}_v${RN_VERSION}_b${BUILD_NUMBER}_ios_${RN_BUILD_TYPE}.zip"

export RN_BUILD_TYPE=${RN_BUILD_TYPE}

zip -r "${RN_ZIP_NAME}" . -x ".*" -x "__MACOSX" ".DS_Store"


cd ../..
 # 创建打包目录
 
export foldername="${IPA_SCHEME}_$(date +%s | tr -d '\n')"

mkdir ./${foldername}

    # 创建描述文件，一行代表一个信息：
    
echo "${IPA_SCHEME}" > ./${foldername}/index.link   # 工程名称
echo "${IPA_NAME}" >> ./${foldername}/index.link	# 软件包名称
echo "${RN_VERSION}" >> ./${foldername}/index.link	# 版本号
echo "${BUILD_NUMBER}" >> ./${foldername}/index.link	# build号
    
export package_time=$(date +'%Y-%m-%d %T')
echo "${package_time}" >> ./${foldername}/index.link	# 创建时间

if RN_BUILD_TYPE="BaseLine"; then
   echo "baseLine" >> ./${foldername}/index.link	# 基线包
else
   echo "extra" >> ./${foldername}/index.link		# 差量包
fi

echo "application" >> ./${foldername}/index.link

echo "${RN_ZIP_NAME}" >> ./${foldername}/index.link	#文件夹名称

# 上传RN包    
mv ./ios/RNBundle/${RN_ZIP_NAME} ./${foldername}/${RN_ZIP_NAME}

upload_app ./${foldername} ReactNative_I

 # 移除文件夹
rm -rf ./${foldername}
rm -f ./"${foldername}.zip"
cd ..
rm -rf ./rn

```

##构建项目

![image](http://upload-images.jianshu.io/upload_images/2728934-0869c4f6abe06d94.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

##构建成功
构建成功后根据构建的项目名称，build号下载

