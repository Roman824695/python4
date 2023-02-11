#В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
#Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
#Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
#Пример:
#4 -> 1 2 3 4
#9


n = int(input('Введите число кустов : '))
a = list()

def list_mas(a, b):
    i = 0 
    while i < a:
      b.append(int(input(f'Введите колличество ягод на кусте № {i+1}  : ')))
      i += 1
    return b 

list_mas(n, a)
print(*a)
maxsum = 0

for i in range(n):
	cursum = sum(a[i:i+3])
	if cursum > maxsum:
		maxsum = cursum
if a[0] + a[-1] + a[-2] > maxsum:
	maxsum = a[0] + a[-1] + a[-2]
if a[0] + a[1] + a[-1] > maxsum:
	maxsum = a[0] + a[1] + a[-1]

print(maxsum)
