dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

#遍历
for key, value in dict.items():
    print(key, value)

#长度
dict_length=len(dict)
print(f"列表的长度分别是是: {dict_length}")

#添加
dict["C"]=10
print(dict)
print('---------------添加---------------')

#删除
del dict['C']
print(dict)
print('-------------删除-----------------')


#内置函数https://www.runoob.com/python3/python3-dictionary.html