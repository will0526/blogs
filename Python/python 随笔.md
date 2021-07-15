#python 随笔

## 基本语法与API


* os.path.join(path1[, path2[, ...]])
把目录和文件名合成一个路径
  
  1.如果各组件名首字母不包含’/’，则函数会自动加上
  2.如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃
  3.如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾









## 常用用法

### 上传应用文件

```markdown
#FastAPI
@router.post('/v1/app_upload', tags=['上传应用应用文件'])
# @logit
async def upload_file(file: UploadFile=File(..., alias="file", title='form-data文件', description="file"),
                      appId: str = Form(...),db:Session =Depends(get_db)):

    with open(file_path, "wb") as f:
         f.write(await file.read())
         
```


## 疑难杂症

### 导入无效

问题：在Adapay.py 的文件中 import Adapay 导入不了Adapay SDK的内容

原因：命名问题，import 的是自己，没有导入 Adapay SDK

