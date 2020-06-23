**看啥都不如看官网**
[podspec 官方网站](https://guides.cocoapods.org/syntax/podspec.html)



基于pod自动创建
只需要输入pod的lib命令即可完成初始项目的搭建，下面详细说明具体步骤，以BZLib作为项目名演示。

1.执行命令pod lib create BZLib。在此期间需要确认下面4个问题。
Would you like to provide a demo application with your library? [ Yes / No ]
yes
Which testing frameworks will you use? [ Specta / Kiwi / None ]
Kiwi
Would you like to do view based testing? [ Yes / No ]
No
What is your class prefix?
BZ
第一个问题询问是否提供一个demo项目，通常选择Yes，其他的可以根据需要选择。命令执行完后，就会创建好一个通过cocoapods管理依赖关系的基本类库框架。



这里是demo spec 文件


  s.ios.deployment_target = '8.0'

  s.source_files = 'MPOS/**/*'
   s.resource_bundles = {
     'MPOS' => ['MPOS/Resource/Images/*.png']
   }
   
   s.public_header_files = 'MPOS/System/*.h'
   s.frameworks = 'UIKit'
   s.dependency 'CPSwiperFramework', '~> 1.0.1'
   s.dependency 'MBProgressHUD', '~> 0.9.1'
   s.dependency 'Reachability', '~> 3.2'
   s.dependency 'ViewUtils', '~> 1.1.2'
   s.dependency 'JMHoledView', '~> 0.1.1'
   s.dependency 'AFNetworking', '~> 2.6.0'
   s.dependency 'NSData+MD5Digest', '~> 1.0.0'
   s.dependency 'OpenUDID', '~> 1.0.0'
   s.dependency 'SFHFKeychainUtils', '~> 0.0.1'
   s.dependency 'MD5Digest', '~> 1.0.2'
   s.dependency 'OpenSSL-Universal', '~> 1.0.1.p'
   s.dependency 'SDWebImage', '~> 3.8.2'
   s.dependency 'UIColor+Additions', '~> 2.0.2'
   s.dependency 'MOBFoundation', '~> 2.0.11'
   

5.引用自己或第三方的framework或.a文件时
在podsepc中应该这样写:

s.ios.vendored_frameworks = "xxx/**/*.framework"
s.ios.vendored_libraries = "xxx/**/*.a”


按照默认配置，类库的源文件将位于`Pod/Classes`文件夹下，资源文件位于`Pod/Assets`文件夹下，可以修改`s.source_files`和`s.resource_bundles`来更换存放目录。`s.public_header_files`用来指定头文件的搜索位置。
`s.frameworks`和`s.libraries`指定依赖的SDK中的framework和类库，**需要注意，依赖项不仅要包含你自己类库的依赖，还要包括所有第三方类库的依赖**，只有这样当你的类库打包成`.a`或`.framework`时才能让其他项目正常使用。示例中`s.frameworks`和`s.libraries`都是ASIHTTPRequest的依赖项。
`podspec`文件的详细说明可以看[Podspec Syntax Reference](http://guides.cocoapods.org/syntax/podspec.html)。

#### 3.进入Example文件夹，执行`pod install`，让demo项目安装依赖项并更新配置。
4.添加代码。注意文件存放的位置在Pod/Classes目录下，跟podspec配置要一致。
运行Pod install，让demo程序加载新建的类。也许你已经发现了，只要新增加类/资源文件或依赖的三方库都需要重新运行Pod install来应用更新。