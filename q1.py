'''

字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。

例如：

输入：19
输出：2

输入：258
输出：2

输入：0219
输出：3


'''

def  how_many_ways(digitarray):
    length = len(digitarray)
    if digitarray[0] == '0':
        return 0
    f = {}
    f[0], f[1] = 1, 1
    for l in range(2, length + 1):
        x = int(digitarray[l - 2:l])

        if digitarray[l - 1] == '0':
            if digitarray[l - 2] == '0' or x > 26:
                return 0
            else:
                f[l] = f[l - 2]
        elif digitarray[l - 2] == '0' or x > 26:
            f[l] = f[l - 1]
        else:
            f[l] = f[l - 1] + f[l - 2]

    return f[length]
while True:
    try:
        s = input()
        print(how_many_ways(s))
    except:
        break
