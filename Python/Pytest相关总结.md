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