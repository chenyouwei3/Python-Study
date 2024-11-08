#import list
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2,70.2 ]  # 定义一个列表

#只有全部是同一类型才能比较
#print(f"列表最大值{max(list)}")
#print(f"列表最小值{min(list)}")
print("出现次数"+str(list.count(70.2)))

#反转过后
list.reverse()
print(list)

#排序函数
#值类型必须是同一类型
list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
list.sort(reverse=True)  # 降序排序
list.sort()
# 默认升序排序  字符串是abc 数字123
print(list)
list = ['banana', 'apple', 'cherry', 'date']
list.sort(key=len)  # 根据字符串长度进行排序
print(list)
#复制函数
newlist=list.copy()#浅拷贝
print("新数组",newlist)
list.clear()  #清空函数
print(list)


