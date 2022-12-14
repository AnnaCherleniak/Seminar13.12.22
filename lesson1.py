# LESSON 1. Знакомство с python.

# 1. Напишите программу, 
# которая принимает на ввод два числа и проверяет, является одно число квадратом другого. 
#a = int(input())
#b = int(input())
#if a == b**2 or b == a**2:
    #print('yes')
#else:
    #print('no')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них. 
#list = []
#for i in range(5):
    #x = int(input())
    #list.append(x)
## print(max(list))
#maxx = list[0]
#for el in list:
 #   if el > maxx:
  #      maxx = el
#print(maxx)
## OR
#maxx = int(input())
#for _ in range(4):
 #   x = int(input())
  #  if x > maxx:
   #     maxx = x
#print(maxx)


## Способы вывода данных
#print(7, end=', ')
#print(8)
#print(7, 8, 9, sep=', ')
#some_list = [1, 2, 3, 4]
#print(some_list, sep=', ')
#print(*some_list, sep=', ')
## Задача 3. 
# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N.
#n = int(input())
#for i in range(-n, n):
 #   print(i, end=', ')
#print(n)

## Задача 4. 
# Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.
#number = str(input())
#for i in number:
 #   if str[i] == ',':
  #      print(str[i+1])



## Задача 5. Напишите программу, которая принимает на вход число и проверяет, 
# кратно ли оно 5 и 10 или 15, но не 30

n = int(input())
if n % 5 == 0 and n % 10 == 0 or n % 15 == 0:
    print('да')
else:
    print('нет')