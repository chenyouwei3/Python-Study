#推导式是一次性全部生成,生成器表达式是一个一个的生成
#推导式[] {}     生成式是()


#list推导式
squares=[x**2 for x in range(1,10)]
print("list推导",squares)
even_squares=[x**2 for x in range(10) if x%2==0]
print("list推导",even_squares)
#dict推导式
dictTest_listDemo = ['Google','Runoob', 'Taobao']
newDict={key:len(key) for key in dictTest_listDemo}
square_dict={x:x**2 for x in range(5) if x%2==0}
print("dict推导",square_dict)
#set推导式
set={x for x in 'abcdefg' if x not in 'abc'}
print("set推导",set)
#tuple推导式
a = (x for x in range(1,10))


