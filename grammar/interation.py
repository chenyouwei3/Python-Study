list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素
print (next(it))

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x)
# for key,value in enumerate(list):
#     print(key,value)

