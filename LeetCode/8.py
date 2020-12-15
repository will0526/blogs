def myAtoi( s: str) -> int:
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
        # 使用正则表达式 ^：匹配字符串开头，[\+\-]：代表一个+字符或-字符，?：前面一个字符可有可无，\d：一个数字，+：前面一个字符的一个或多个，\D：一个非数字字符
        # max(min(数字, 2**31 - 1), -2**31) 用来防止结果越界

print(myAtoi('sdfasdf1000343sadf'))