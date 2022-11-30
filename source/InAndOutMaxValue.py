# coding=utf-8
from asyncore import read
from hashlib import new
from inspect import _void
from random import randrange

FILE_NAME = "file.data"


def WriteFile(n: int, ary: list):
    with open(FILE_NAME, "w") as file:
        file.write(str(n) + "\n")
        for val in ary:
            file.write(str(val) + " ")
        pass
    return


def ReadFile():
    ary = []
    with open(FILE_NAME, "r") as file:
        n = int(file.readline())
        ary = [int(i) for i in file.readline().split()]
    pass
    return ary


def Main() -> _void:
    print("请输入数字个数：")
    n = int(input())
    print("请输入%d个数！" % (n))

    ary = input()
    if len(ary.split()) == n:
        ary = [int(i) for i in ary.split()]
    else:
        print("数据不合法！")
        return

    WriteFile(n, ary)

    newAry = ReadFile()

    print("所有的最大值与位置：")
    maxValue = max(newAry)
    for i in range(0, len(newAry)):
        if maxValue == newAry[i]:
            print("最大值为%d，位置在%d" % (maxValue, i + 1))
    return


if __name__ == "__main__":
    Main()