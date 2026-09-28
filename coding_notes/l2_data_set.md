# 本讲是py程序设计的第二部分，主要介绍在python里面常用的数据集合类型。

## 1.字符串
### def:用单引号或者双引号括起来的一个字符序列
1. 下标从0开始,可以访问其字符，如` s = "smile" print(s[0])>> s `
2. ` len() `函数求长度
3. 使用` + `拼接两个字符串，but "ab"+2错误
4. 比较（可以使用所有关系运算符）
   从第一个字符开始比较   
   结果为` True/False `

```python
def main():
    word = "ijklmnop"
    s = ""
    length = len(word)
    for i in range(length // 2)
    """range是前闭后开"""
        if i < 2:
            c1 = word[3]
            c2 = word[6-3*i]
        else :
            c1 = word[6*(i-2)]
            c2 = word[7]
        s = s + c1 + c2
    print(s)
main()
#lollipop
```

5. 好用的库函数
> 
6. 字符子串
    ` s[m:n] `表示由m到n形成的子串（左闭右开）
7. 转义字符
   ` ' \" ' ` = ' \" '
