谷歌，diff_match_patch，在 React Native 开发时增量更新使用




```

从文件里读出内容
NSString *aContent = [NSString stringWithContentsOfFile:afile encoding:NSUTF8StringEncoding error:nil];
NSString *bContent = [NSString stringWithContentsOfFile:bfile encoding:NSUTF8StringEncoding error:nil];

实例化对比对象
DiffMatchPatch *dmp = [[DiffMatchPatch alloc]init];

//比对差异
NSMutableArray *diffs = [NSMutableArray array];
diffs = [dmp diff_mainOfOldString:bContent andNewString:aContent];

//生成补丁
NSMutableArray *patches = [dmp patch_makeFromDiffs:diffs];
//应用补丁
NSArray *results = [dmp patch_apply:patches toString:bContent];
results 是个数组，数组第一个字段为应用补丁后的内容。（字符串）
然后将应用后的内容回写到原文件
NSString *string = results.firstObject;
[string writeToFile:bfile atomically:YES];
    ```