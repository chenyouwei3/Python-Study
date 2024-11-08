#!/usr/bin/env python3

n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))


count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")
    print("爆了")


#for用于迭代对象

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    print(site)


word = 'runoob'

for letter in word:
    print(letter)

for number in range(1, 6):
    if number ==2:
        continue
    if number==5:
        print("结束")
        break
    print(number)
else:
  print("Finally finished!")