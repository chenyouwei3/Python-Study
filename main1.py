#测试-语句
if False:
    print("First_True")
else:
    print("First_False")

if True:
    print("Second_True")
else:
    print("Second_False")
#测试-赋值
item_one=1
item_two=2
item_three=3
total1 = item_one + \
        item_two + \
        item_three
total2 = ['item_one', 'item_two', 'item_three',]
print(total1)
print(total2)
#测试-切割字符串
str="123456"
print(str[-4])
print(str[0:-1])# 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print('------------------------------')
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# 等待用户输入
input("\n\n按下 enter 键后退出。")


#导包
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path