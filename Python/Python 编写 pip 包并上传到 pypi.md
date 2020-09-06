# Python 编写 pip 包并上传到 pypi

* 创建项目
* 安装到本地测试
* 打包
* 上传 pypi

## 创建项目

创建项目，目录结构如下

```markdown
-- test
  |
  |-- test
  |  |
  |  |-- __init__.py
  |  |-- models.py
  |
  |-- setup.py
```

其中 test/test 是主代码目录，setup.py 是必备的打包文件

setup.py
```markdown
from setuptools import setup, find_packages

setup(
    name = 'test',
    version = '0.0.1',
    keywords='test',
    description = 'a library for wx Developer',
    license = 'MIT License',
    url = 'https://github.com/wxnacy/wwx',
    author = 'will',
    author_email = 'willwyy@163.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [
        'requests>=2.19.1',
        'pycrypto>=2.6.1',
        'xmltodict>=0.11.0'
        ],
)

```
项目代码根据你的需求编写，你可以写一个这样的例子来测试

models.py
```markdown
class Message():
    @classmethod
    def test():
        print('Hello World')
```
__init__.py

```markdown
from .models import Message
```

## 安装到本地测试
接下来在 setup.py 所在目录下执行安装命令，安装到本地

```markdown
$ pip install .
```

在项目中你就可以使用测试了

```markdown
from test import Message
Message.test()
```
## 打包

测试完成后，再上传到 pypi 之前需要先打包

```markdown
$ python setup.py <params>
```

params 有如下取值
```markdown
sdist             create a source distribution (tarball, zip file, etc.)
bdist             create a built (binary) distribution
bdist_dumb        create a "dumb" built distribution
bdist_rpm         create an RPM distribution
bdist_wininst     create an executable installer for MS Windows
bdist_egg         create an "egg" distribution
```

sdist 可以支持上传到 pypi

```markdown
$ python setup.py sdist
```

然后根目录中会出现 dist 目录存放打包好的文件

## 上传 pypi

首先去[官网](https://pypi.org/)注册用户。另外可以[测试环境](https://testpypi.org/)注册，在测试环境上传包

最后一步上传到 pypi，首先去搜索确认项目名没有被占用，并注册用户，然后使用 twine 进行上传

* 下载 twine

```markdown
$ pip install twine
```
* 上传
```markdown
$ twine upload dist/*
```

然后根据提示输入用户名密码即可。

可以设置全局账户信息

创建 ~/.pypirc 文件并添加如下信息
```markdown
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = <username>
password = <password>
```

然后再次上传就不会提示输入用户密码了

## 使用

安装
```markdown
pip install SomePackage              # 最新版本
pip install SomePackage==1.0.4       # 指定版本
pip install 'SomePackage>=1.0.4'     # 最小版本
```
卸载
```markdown
pip uninstall SomePackage
```
