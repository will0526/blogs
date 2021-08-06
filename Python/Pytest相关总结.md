#python unit test

## pytest 配置相关

* pytest.ini

```markdown
[pytest]
#report 导出目录
addopts = -s --html=./test_report/report.html
;addopts = -v -s --html=./test_report/report.html --alluredir ./test_report/result

#运行相关文件，类，方法
python_files = test_oc*.py
python_classes = Test*
python_functions = test_*
```

* 运行命令

根目录运行
```markdown
pytest #直接跑测试
```


```markdown
coverage run -m pytest # 通过coverage跑测试用例
coverage html --omit=./venv/* # 生成覆盖率报告，--omit=./venv/，忽略venv下文件

```

## 单元测试

```markdown

class TestOCPayment(unittest.TestCase):

    def setUp(self):
        #每次运行case 前运行方法
        self.order_no = str(random.randint(100000, 9999999))
        self.runner = CliRunner()

        self.runner.invoke(main, ['login', 'prod', '-a', api_key, '-t', mock_api_key, '-p', private_key])

    def tearDown(self):
        #每次运行case 后运行方法
        self.order_no = ''
        self.runner.invoke(main, ['logout'], )

    def test_payment_create_011(self):
        """
        参数测试payment create 命令，参数完整，创建成功
        :return:
        """
        result = self.runner.invoke(main,
                                    ['payment', 'create', '--app_id', app_id, '--order_no', self.order_no,
                                     "--pay_channel", "alipay", "--pay_amt", "1.00"])

        assert "Payment create 支付发起交易成功!" in result.output

```

## fixture


```markdown

@pytest.fixture()     预置条件函数前加装饰器
def login():
    print "\n登录代码"
 
 
def test_login_1(login): #需要执行预置条件的测试用例参数传预置条件函数名
    print "1111111"
 
 
def test_login_2():  #不需要执行预置条件的测试用例参数不传预置条件函数名
    print "2222222"

```

* 多个py文件共用预置条件

1.定义conftest.py文件文件名称必须为conftest

2.需要执行预置条件的测试用例的参数填写预置条件函数名称

```markdown
fixture(scope="function", params=None, autouse=False, ids=None, name=None):
    """使用装饰器标记fixture的功能
     可以使用此装饰器（带或不带参数）来定义fixture功能。
    :arg scope: scope 有四个级别参数 "function" (默认), "class", "module" or "session".
 
    :arg params: 一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它
 
    :arg autouse:  如果为True，则为所有测试激活fixture func 可以看到它。 如果为False（默认值）则显式需要参考来激活fixture
 
    :arg ids: 每个字符串id的列表，每个字符串对应于params 这样他们就是测试ID的一部分。 如果没有提供ID它们将从params自动生成
 
    :arg name:   fixture的名称。 这默认为装饰函数的名称。 如果fixture在定义它的同一模块中使用，夹具的功能名称将被请求夹具的功能arg遮蔽; 解决这个问题的一种方法是将装饰函数命名
                       “fixture_ <fixturename>”然后使用”@ pytest.fixture（name ='<fixturename>'）“”。
```