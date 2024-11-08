s1={1,2,3,4}
s2={1,2,5,6,7,8}
# #求交集
# inter=s1.intersection(s2)
# print(inter)
#
# #intersection_update()   返回交集过后，把当前集合也更新成交集
# inter=s1.intersection(s2)
# print(inter)
#求差集
# diff1=s1.difference(s2)#3 4
# print(diff1)
#
# #移除集合中的元素，该元素在指定的集合也存在。
# s1.difference_update(s2)
# print(s1)
#
# #判断是否有共同元素  判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
# print(s1.isdisjoint(s2))
#
# #判断是否为子集  		判断指定集合是否为该方法参数集合的子集
# print(s1.issubset(s2))
#
# #判断该方法的参数集合是否为指定集合的子集
# print(s1.issuperset(s2))

#	返回两个集合中不重复的元素集合
# print(s1.symmetric_difference(s2))
# print(s2.symmetric_difference(s1))

#移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
# s1.symmetric_difference_update(s2)
# print(s1)
# s2.symmetric_difference_update(s1)
# print(s2)

#求并集
print(s1.union(s2))