# git 学习使用相关

记录下，git 常规操作，

## git filter-branch

误提交pods w文件夹或者node_modules文件的话，如果想要删除这个文件夹，大可不必删除然后重新提交commit

* 删除文件

```markdown
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch -r Pods" --prune-empty --tag-name-filter cat -- --all

```

这句的意思是从遍历所有的commit，删除那个文件，重写历史commit，注意只重写了当前分支。

* 推送

 然后强行远程推送
 
 ```markdown
git push origin --all --force
```
 
 
 

 
