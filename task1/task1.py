from random import randint
n=30
A = [randint(-100,100) for i in range(n)]
print(A)
b=max(A)
print('max =',b)
c=A.index(b)
print('number =',c+1)
A2 = [i for i in A if i % 2 == 1]
if not A2:
    print("Немає чисел")
else:
    A2.sort(reverse=True)
    print(A2)