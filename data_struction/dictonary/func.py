tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(len(tinydict))#tinydict长度
print(str(tinydict))#转化为str

print(type(tinydict))

#copy函数
newTinyDict=tinydict.copy()
print(newTinyDict)
newTinyDict["Name"]="TEST"
print(newTinyDict)
print(tinydict)

#fromkeys函数
keys=["0","2","3"]#新字典的keys
new_tinydict=tinydict.fromkeys(keys,"unTest")
print(new_tinydict)
print('---------------GET函数---------------')

#get函数
print(tinydict.get("Name","xixi"))
print(tinydict.get("dadada","xixi"))#没有对应的key
print('---------------setdefault函数---------------')

#setdefault函数
#和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
print(tinydict.setdefault("Name","xixi"))
print(tinydict.setdefault("dadada","xixi"))#没有对应的key
print(tinydict)
print('---------------updata函数---------------')

#updata函数
#没有的添加，有的覆盖，也可以用key-value的元组
newmap={'DA': 'Runoob', 'AgDAe': 7, 'Class': 'XIXIXI'}
tinydict.update(newmap)
print(tinydict)
print('---------------values函数---------------')

#values函数、
print(tinydict.values())
print(tinydict.keys())
#删除字典 key（键）所对应的值，返回被删除的值
print(tinydict.pop("Class"))#第二个参数是默认值
#删除最后一个popitem  看版本3.7为分界线
print(tinydict.popitem())

#clear函数
tinydict.clear()
print(tinydict)
