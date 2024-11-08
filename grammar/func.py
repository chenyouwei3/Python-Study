def hello() :
    print("Hello World!")

def max(a, b):
    if a > b:
        return a
    else:
        return b



hello()
print(max(20030324, 20030109))


#id函数查看内存地址变化
def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象


a = 1
print(id(a))
change(a)



# 可写函数说明   引用传递
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)


#关键字参数   传入的时候强调参数名
def printme(str):
    print(str)
    return


# 调用printme函数
printme(str="菜鸟教程")


#默认参数
# !/usr/bin/python3

# 可写函数说明
# def printinfo(name, age=35):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
#
#
# # 调用printinfo函数
# printinfo(age=50, name="runoob")
# print("------------------------")
# printinfo(name="runoob")



# 可不定长参数     *是元组    **是字典
def printinfo(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)