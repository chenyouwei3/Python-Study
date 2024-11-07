#列表-引用类型
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]  # 定义一个列表
tinylist = [123, 'runoob']
#长度
list_length=len(list)
tinylist_length=len(tinylist)
print(f"列表的长度分别是是: {list_length},{tinylist_length}")
print('---------------添加---------------')

#添加元素
#将一个元素添加到列表的末尾
list.append("test")
print(list)
#将一个可迭代对象中的元素添加到列表末尾
list.extend([5,"DDDD"])
print(list)
#在指定位置插入一个元素
list.insert(1,1.55)# 在索引1的位置插入1.5
print(list)
print('-------------删除-----------------')

#删除
#删除指定值的第一个匹配项。如果值不存在，将引发 ValueErro
list.remove(1.55)
print(list)  # 输出: [1, 2, 3, 4, 5, 6]
#删除并返回指定索引的元素（默认删除最后一个元素）
last_element = list.pop()
print(last_element)  # 输出: 6
print(list)  # 输出: [1, 2, 3, 4, 5]
#删除指定索引的元素
del list[0]  # 删除索引为0的元素
print(list)  # 输出: [2, 3, 4, 5]
print('---------------切割--------------')
#切割
print (list[0])         # 打印列表的第一个元素
print (list[1:3])       # 打印列表第二到第四个元素（不包含第四个元素）
print (list[2:])        # 打印列表从第三个元素开始到末尾
print (tinylist * 2)    # 打印tinylist列表两次
#拼接
print (list + tinylist)  # 打印两个列表拼接在一起的结果

#内置函数https://www.runoob.com/python3/python3-list.html

def reverseWords(input):
    # 通过空格将字符串分隔为列表
    inputWords = input.split(" ")
    # 翻转字符串
    inputWords = inputWords[-1::-1]  # 反转列表
    print(inputWords)
    # 重新组合字符串
    output = ' '.join(inputWords)  # 使用空格连接
    return "success", output

if __name__ == "__main__":
    print(__name__)
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)  # 输出: ('success', 'runoob like I')
