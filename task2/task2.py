import re

string = input('Введіть строку:')
# Отделяем числа от строки и вносим их в массив
l = len(string)
integ = []
i = 0
while i < l:
    s_int = ''
    a = string[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = string[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))

print('Масив чисел:',integ)
string = re.sub(r'\d+', '', string, flags=re.UNICODE)
print('Строка без чисел:', string)
# Функция меняющая в словах первую и последнюю букву на заглавные
def up(string):
    string, result = string.title(), ''
    for word in string.split():
        result += word[:-1] + word[-1].upper() + ' '
    return result[:-1]

print('Заміна першої і останньої літери в кожному слові на великі:', up(string))

max_num=max(integ)
max_num_in=integ.index(max_num)
print('Максимальне значення в масиві:', max_num)
# Создаём новый массив с числами в степени
newlist=[]
for i in range(len(integ)):
    if i != max_num_in:
        new = integ[i] ** i
        newlist.insert(i, new)
print('Новий масив чисел піднесених до степеня:', newlist)

