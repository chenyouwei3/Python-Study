#!/usr/bin/python3

var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 1     #1为true    0为false
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")

test=1
match test:
    case 1|0:     #可以多个值匹配
        print("controller1")
    case 2:
        print("controller2")
    case 3:
        print("controller3")
    case _:  #default
        print("controller_default")