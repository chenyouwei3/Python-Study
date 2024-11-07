#元组-不可变
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob',"test")

#长度
tuple_length=len(tuple)
tinytupl_length=len(tinytuple)
print(f"列表的长度分别是是: {tuple_length},{tinytupl_length}")

print('--------------添加----------------')
#只能连接元组

print('---------------删除---------------')
#只能切割元组

#内置函数https://www.runoob.com/python3/python3-tuple.html
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组


tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

