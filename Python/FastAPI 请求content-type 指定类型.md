


### FastAPI 请求content-type 指定类型

* form表单

不一定非要处理所有参数
```markdown
@router.post('/v1/apply/audit/callback', tags=['申请单审核回调'])
def apply_audit_callback(*, jsonData: str = Form(...), respDesc: str = Form(...), respCode: str = Form(...),
                         checkValue: str = Form(...),):
```

* text

```markdown
 req: str=Body(..., media_type="text/html")
```                         

* json

可以定义req类型，结构

```markdown
@router.post('/v1/login', response_model=RespLogin, tags=['商户登录接口'])
@logit
@validate_sign
def login(req: ReqLogin):
```



