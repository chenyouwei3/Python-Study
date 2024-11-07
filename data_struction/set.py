#set
#集合中的元素是唯一的，即不能包含重复值
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
#长度
sites_length=len(sites)
print(f"列表的长度分别是是: {sites_length}")
print('--------------添加----------------')

#添加元素
sites.add(1)
print(sites)
#将一个可迭代对象中的元素添加到列表末尾
sites.update(["dada",1])
print(sites)
print('---------------删除---------------')

#删除元素
sites.remove("Taobao")#删除指定值的元素。如果元素不存在，将引发 KeyError。
print(sites)
sites.discard("1")#删除指定值的元素，如果元素不存在也不会引发错误
#随机删除
element = sites.pop()
print(element)  # 输出: 6
print(sites)  # 输出: [1, 2, 3, 4, 5]
#sites.clear() #清空
print('------------------------------')

#内置函数https://www.runoob.com/python3/python3-set.html
# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素