# 1.	Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import math
list = [1, 2, 3, 5, 1, 2 , 1, 11]
# sum=0
# i=1
# while i < len(list):
#   sum=sum+list[i]
#   print(list[i])
#   i=i+2
# print(sum)


res = [] 
[res.append(item) for item in list if list.index(item) % 2 != 0] 
print(res)

print(sum(res))