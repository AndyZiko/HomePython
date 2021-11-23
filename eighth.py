from random import *
# random.(импортируемый объект, поэтому точку и далее функия из этого объекта\модуля randint задает диапазон
# можно также импортировать отдельно randint из random пример: from random import randint
# если хотим импортировать все функции обекта ставим * в конце
for i in range (10):
    print(randint(0, 9))