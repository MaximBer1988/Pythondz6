# 3.	Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

list1=[1, 1, 2, 3, 4, 5, 5]
# i=0
# uniq_list=[]
# while i <len(list1):
#   if list1.count(list1[i])<2:
#     uniq_list.append(list1[i])
#   i=i+1  
# print(uniq_list)
res = [] 
[res.append(item) for item in list1 if list1.count(item)<2] 
print(res)