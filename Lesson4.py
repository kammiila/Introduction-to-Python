# name = input('What is your name?')
# print(f'Hello my name is {name}')

# num1: int = int(input('Ведите первое число'))
# num2 = int(input('Введите второе число'))
# summa = num1 + num2
# print(summa)

# price = 12
# print(type(price))
# price = price + 4.5
# print(type(price))

# name = 'Sam'
# print(type(name))

num1 = int(input('Сколько людей в cs-11 вобщем?'))
num4 = int(input('Сколько отсутсвуют в cs-11?'))
cs11 = num1 - num4
print(f'В классе присутсвуют {cs11}, отсутсвуют {num4}')

num2 = int(input('Сколько людей в cs-12 вобщем?'))
num5 = int(input('Сколько отсутсвуют в cs-12?'))
cs12 = num2 - num4
print(f'В классе присутсвуют {cs12}, отсутвуют {num5}')

num3 = int(input('Сколько лбдей в cs-13 вобщем?'))
num6 = int(input('Сколько отсутвуют в cs-13?'))
cs13 = num3 - num6
print(f'В классе {num1}, отсутсвуют {num4}')

summa = cs11 + cs12 + cs13
summa2 = num4 + num5 + num6
summa3 = summa + summa2
print(f'В группах присутсвуют {summa} людей, отсутсвуют {summa2} людей, вообщем {summa3} людей')


