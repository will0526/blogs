#同一个文件夹下两个python文件不能import

## import 与 from import

```markdown

# 直接导入模块
import math
print math.pi #导出圆周率的值

# 导入模块中具体的常量
from math import pi
print pi

# 导入模块中所有内容
from math import *
print pi


```

* from语句有破坏命名空间的潜质。如果使用from导入变量，变量碰巧和作用域中现有变量重名，变量就会被悄悄的覆盖掉。

* 另一方面，from module import *形式的确可能破坏命名空间，让变量名难以理解，尤其是在导入一个以上的文件时。
* 简单的模块一般倾向于使用import，而不是from。多数的from语句是用于明确列举想要的变量

## Python中的模块和包

每个.py文件都是可以认为是一个Python模块

.py文件中可以包含类、方法、变量和常量

按照Python的约定，需要在文件夹中创建名为__init__.py的空文本文件，以标识文件夹是一个包

该文件的主要作用使初始化Python包。如果目录下面包含了该文件，Python解释器就会将该目录当做一个包

```markdown
package/
    __init__.py
    file.py
    file2.py
    subpackage/
        __init__.py
        submodule1.py
        submodule2.py
```

## 同一文件夹下的两个python文件，不能import其中的类或者方法

当同一文件夹下的两个python文件，不能直接import其中的类或者方法，必须引用文件夹名称作为模块名，而文件夹下并没有__init__.py
```markdown

# file.py 中
from file2 import *  

# 以上会报错，找不到 file2，
# 需使用 from package.file2 import * 
```

解决方法：

右键文件夹subpackage， Mark Directory as Resource Root



