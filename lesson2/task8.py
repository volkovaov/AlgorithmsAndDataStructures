# Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо
# посчитать, задаются вводом с клавиатуры.

print("Введите цифру, которую будем искать:")
desired = input()

print("Введите количество элементов последовательности:")
n = int(input())

lst = []
for i in range(1,n+1):
    print("Введите элемент последовательности (число) №", i)
    a = input()
    lst.append(a)

#print(lst)

cnt = 0
for memb in lst:
    digits = list(memb)
#    print(digits)
    for a in digits:
        if a == desired:
            cnt += 1

print(cnt)