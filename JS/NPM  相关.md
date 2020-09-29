#学习公众号文章笔记

[文章地址](!https://mp.weixin.qq.com/s/bm7rtXoAYsluDpevPs69Fw)




## package.json 如何产生的

npm init

npm init 的时候,会有一个初始化 pacakge.json，按照提示输入对应内容

## package.json 中的常规属性


### npm 中的依赖包

* dependenices

通过命令npm install/i packageName -S/--save 把包装在此依赖项里

```markdown
例
npm i moment@2.24.0 -S
```

如果没有指定版本，直接写一个包的名字，则安装当前npm仓库中这个包的最新版本。如果要指定版本的，可以把版本号写在包名后面，比如npm i vue@3.0.1 -S。

```markdown
 "dependencies": {
      "lodash": "^4.17.13",
      "moment": "^2.24.0",
 }
```

* devDependenices

```markdown
npm i eslint -D
```
有一些包有可能你只是在开发环境中用到，例如你用于检测代码规范的 eslint ,用于进行测试的 jest ，用户使用你的包时即使不安装这些依赖也可以正常运行，反而安装他们会耗费更多的时间和资源，所以你可以把这些依赖添加到 devDependencies 中，这些依赖照样会在你本地进行 npm install 时被安装和管理，但是不会被安装到生产环境

```markdown
 "devDependencies": {
      "jest": "^24.3.1",
      "eslint": "^6.1.0",
 }
```

* bin

```markdown
"bin": {
    "vm2": "./bin/vm2"
  },
```

bin 字段指定了各个内部命令对应的可执行文件的位置。如果全局安装模块报，npm 会使用符号链接把可执行文件链接到 /usr/local/bin，如果项目中安装，会链接到 ./node_modules/.bin/。

上面的这种当你的包安装到全局时：npm 会在 /usr/local/bin 下创建一个以 vm2 为名字的软链接，指向全局安装下来的 vm2 包下面的 "./bin/index.js"。这时你在命令行执行 vm2 则会调用链接到的这个 js 文件。

* main

一个常用的npm包
```markdown
{
  "main": "lib/index.js",
}
```

main 属性指定程序的主入口文件，其他项目在引用这个 npm 包时，实际上引入的是 lib/index 中暴露出去的模块。


## npm script

### 什么是 npm script 脚本?

在生成的 package.json 文件中，有一个 scripts 对象，在这个对象中，npm 允许使用 scripts 字段定义脚本命令。

```markdown
"scripts": {
    "test": "test.js"
    "build": "tsc",
  },
```
scripts 对象中每一个属性，对应一段脚本。比如，test 命令对应的脚本是 node test.js。

命令行下使用 npm run 命令，就可以执行这段脚本。

查看当前项目的所有 npm 脚本命令，可以使用不带任何参数的npm run命令。

### 原理

每次在运行 scripts 中的一个属性时候(npm run), 实际系统都会自动新建一个shell(一般是Bash)，在这个shell里面执行指定的脚本命令。因此 凡是能在 shell 中允许的脚本，都可以写在npm scripts中。

```markdown
特别的点，npm run 新建的 shell，会在当前目录的 node_modules/.bin 子目录加入到 PATH 变量，
执行结束后，再将 PATH 变量恢复原样。
也就是说，当前项目目录 node——modules/.bin 子目录中所有的脚本，都可以直接用脚本名称调用，不需要增加路径.
（简单总结：通过 npm 启动的脚本，会默认把 node_modules/.bin 加到 PATH 环境变量中。）
```

当前项目的依赖里面有 Mocha，只要直接写 mocha test 就可以了。

```markdown
"test": "mocha test"
```
而不用写成下面这样。
```markdown
"test": "./node_modules/.bin/mocha test"
```
然后我们就可以直接执行 npm run test 了。npm 脚本的退出码，也遵守 Shell 脚本规则。如果退出码不是0，npm 就认为这个脚本执行失败。

npm install 安装的某个模块，如果模块在 package.json 中配置了 bin 属性，在安装时候会自动软链接到 node_modules/.bin 中，举个例子：如 mocha 源码 配置了：

````markdown
{
    "name":"mocha",
    "bin":{
        "mocha":"./bin/mocha"
    }
}
````

### 脚本默认值

npm 本身对两个脚本提供了默认值，这两个脚本不用在 script 属性中定义，可以直接使用
```markdown

"start": "node server.js"
"install": "node-gyp rebuild"
```
npm run start 的默认值是 node server.js ，前提是根目录下有 server.js 这个脚本

npm run install 的默认值是 node-gyp rebuild，前提是根目录下有 binding.gyp 文件

* node-gyp：node 下的 gyp。npm 为了方便直接源码分发，用户装的时候需要自己进下编译，我们在开发 node 程序中需要调用一些其他语言编写的工具甚至 dll，这时候需要先编译下其他语言，否则会出现跨平台的问题。node-gyp 是用来编译原生 C++ 模块的，也可以编写自己写的 C++文件，node-gyp 在较新的 Node 版本中都是自带的，而且是最先版本。

* gyp 文件：当 Node.js 项目中有需要和 C++ 交互的需求时，项目的根目需要创建 binging.gyp 文件，每个.gyp 文件都描述了如何去构建项目，每个.gyp文件都描述了如何去构建项目，gyp文件的语法是 Python数据格式(Json格式)，配置中数据是键-值对的形式。


### 钩子(生命周期)

package.json 中的 script 也是有生命周期的

npm 脚本有两个钩子，pre 和 post，当我们执行start脚本时候，start 的钩子就是 prestart 和 poststart。

当我们执行 npm run start 的时候，npm 会自动按照下面的顺序执行
```markdown
npm run prestart && npm run start && npm run poststart
```
在实际开发中，我们可以做一些准备或者清理工作，下面是个例子

```markdown
"clean": "rimraf ./dist && mkdir dist",
"prebuild": "npm run clean",
"build": "cross-env NODE_ENV=production webpack"
```

### env 环境变量

执行 npm run 脚本时候, npm 会设置一些特殊的env环境变量。其中package.json中的所有字段，都会被设置为以npm_package_开头的环境变量

看个简单的例子

```markdown
{
  "name": "npm-demo",
  "version": "1.0.0",
  "script": {
    "build": "webpack --mode=production"
  },
  "files": ["src"]
}
```

可以得到 npm_package_name、npm_package_version、npm_package_script_build、npm_package_files_0等变量。注意上面 package.json 中对象和数组中每个字段都会有对应的环境变量。


#### 环境变量常用小技巧

* env 命令可以列出所有环境变量

npm run env

* 在shell脚本中输出环境变量

echo PATH

* 在 shell 脚本设置环境变量

echo PATH = /usr/local/lib

### 脚本传入参数

node 处理 scripts 中的参数，除了属性后面的第一个命令，以空格分割的任何字符串(除特别shell语法)都是参数，并且都能通过 process.argv 属性访问

```markdown
process.argv 属性返回一个数组，数组包含了启动 node 进程时的命令行参数。
第一个元素为启动 node 进程的可执行文件的绝对路径名 process.execPath,
第二个元素为当前执行的 jacascript 文件路径。剩余的元素为其他命令行参数。
```
如下 script 例子

```markdown
"scripts":{
  "serve": "vue-cli-service serve --mode=dev --mobile -config build/example.js"
}
```
当我们执行 npm run server 命令的时候，process.argv 的具体内容为：

```markdown
[ '/usr/local/Cellar/node/12.14.1/bin/node',
  '/Users/mac/Vue-projects/hao-cli/node_modules/.bin/vue-cli-service',
  'serve',
  '--mode=dev',
  '--mobile',
  '-config',
  'build/example.js']
```

### 执行顺序

npm 脚本执行多任务分为两种情况

* 并行任务(同时的平行执行)，使用&符号
```markdown
$ npm run script1.js & npm run script2.js
```

* 串行任务(前一个任务成功，才执行下一个任务)，使用 && 符号
```markdown
$ npm run script1.js && npm run script2.js
```
### 任意脚本
我们配置的脚本命令，如 "start": "node test.js"，node test.js 会当做一行代码传递给系统的 shell 去解释执行。
实际使用的 shell 可能会根据系统平台而不同，类 UNIX 系统里，如 macOS 或 linux 中指代的是 /bin/sh， 
在 windows 中使用的是 cmd.exe。原理我们也看了，因为交给 shell 去解释执行的，说明配置的脚本可以是任意能够在 shell 中运行的命令，而不仅仅是 node 脚本或者 js 代码。如果你的系统里安装了 python（或者说系统变量 PATH里能找到 python 命令），你也可以将 scripts 配置为 "myscript": "python xxx.py"


## npm 配置 
### npm config

npm cli 提供了 npm config 命令进行 npm 相关配置，通过 npm config ls -l 可查看 npm 的所有配置，包括默认配置。npm 文档页为每个配置项提供了详细的说明 https://docs.npmjs.com/misc/config .修改配置的命令为 npm config set, 我们使用相关的常见重要配置:

* proxy, https-proxy: 指定 npm 使用的代理

* registry 指定 npm 下载安装包时的源，默认为 https://registry.npmjs.org/ 可以指定为私有 Registry 源

* package-lock 指定是否默认生成 package-lock 文件，建议保持默认 true

* save true/false 指定是否在 npm install 后保存包为 dependencies, npm 5 起默认为 true

删除指定的配置项命令为 npm config delete <key>.

设置淘宝镜像

```markdown
npm config set registry https://registry.npm.taobao.org
```
恢复使用之前的 npm

```markdown
npm config set registry https://registry.npmjs.org
```

### env 环境变量

如果env环境变量中存在以npm_config_为前缀的环境变量，则会被识别为npm的配置属性。比如在env环境变量中设置npm_config_package_lock变量：

```markdown
export npm_config_package_lock=false //修改的是内存中的变量，只对当前终端有效
```
这时候执行npm install，npm会从环境变量中读取到这个配置项，从而不会生成package-lock.json文件。

### npmrc 文件

除了使用 CLI 的 npm config 命令显示更改 npm 配置，还可以通过 npmrc 文件直接修改配置。

这样的 npmrc 文件优先级由高到低包括：

* 工程内配置文件: /path/to/my/project/.npmrc

* 用户级配置文件: ~/.npmrc

* 全局配置文件: $PREFIX/etc/npmrc (即npm config get globalconfig 输出的路径)

* npm内置配置文件:/path/to/npm/npmrc

## npm 包发布

### 规范的 npm 模块目录
一个 node.js 模块是基于 CommonJS 模块化规范实现的，严格按照 CommonJS 规范，模块目录下除了必须包含包描述文件 package.json 以外，还需要包含以下目录：

* bin：存放可执行二进制文件的目录

* lib：存放js代码的目录

* doc：存放文档的目录

* test：存放单元测试用例代码的目录

### 如何发布自己的 npm 包

1，先去 npm 注册个账号，然后在命令行使用
```markdown
npm adduser #根据提示输入用户名密码即可
```
2，使用命令发布你的包
```markdown
在推送之前，可以通过配置一个 .npmignore 文件来排除一些文件, 防止大量的垃圾文件推送到 npm,
 规则上和你用的 .gitignore 是一样的。
.gitignore 文件也可以充当 .npmignore 文件
```
```markdown
npm publish
```
3，发布成功之后，你就可以像下载安装其他包一样使用你自己的开发工具了

````markdown
npm install testDemo
````
### 关于 npm 包的更新

更新 npm 包也是使用 npm publish 命令发布，不过必须更改 npm 包的版本号，即 package.json 的 version 字段，否则会报错，同时我们应该遵 Semver(语义化版本号) 规范，npm 提供了 npm version 给我们升级版本

```markdown
# 升级补丁版本号
$ npm version patch

# 升级小版本号
$ npm version minor

# 升级大版本号
$ npm version major
```
### 本地开发的 npm 包如何调试

可以使用 npm link 调试，将模块链接到对应的运行项目中去，方便地对模块进行调试和测试。具体使用步骤如下

* 假如我的项目是 testNpmStudy，假如我的 npm 模块包名称是 npm-test

* 进入到 模块包 npm-test 目录中，执行 npm link

* 在自己的项目 testNpmStudy 中创建连接执行 npm link npm-test

* 在自己项目的 node_module 中会看到链接过来的模块包，然后就可以像使用其他的模块包一样使用它了。

* 调试结束后可以使用 npm unlink 取消关联

```markdown
npm link 主要做了两件事：
为目标 npm 模块创建软链接，将其链接到全局 node 模块安装路径 /usr/local/lib/node_modules/。
为目标 npm 模块的可执行 bin 文件创建软链接，将其链接到全局 node 命令安装路径 /usr/local/bin/。
```



