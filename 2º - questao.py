num = []
numMulti2 = []
numMulti3 = []
numMulti2e3 = []

for n in range(0,7):
    num.append(int(input(f'Digite o {n + 1} número: ')))
    if num[n]% 2 == 0 :
        numMulti2.append(num[n])
    if num[n]% 3 == 0 :
        numMulti3.append(num[n])
    if num[n]% 3 ==0 and num[n]% 2 == 0 :
        numMulti2e3.append(num[n])
    
print(f'lista dos números digitados divisíveis por 2: {numMulti2}')
print(f'lista dos números digitados divisíveis por 3: {numMulti3}')
print(f'lista dos números digitados divisíveis por 2 e 3: {numMulti2e3}')