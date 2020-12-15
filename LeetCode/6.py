def convert(self, s: str, numRows: int) -> str:
    if len(s) == 0 or numRows == 1:
        return s
    result = ''
    space = 2 * (numRows - 1)  # 第一行与最后一行，每个字母的间隔
    for row in range(numRows):  # 按行读取，找规律
        temp = ''
        i = row
        left = space - 2 * row  # 中间行数，两个字符之间的距离
        while i < len(s):
            if left == 0:
                left = space - left
            temp += s[i]
            i += left
            left = space - left
        result += temp
    return result