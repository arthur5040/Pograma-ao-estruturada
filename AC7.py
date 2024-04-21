#AC 7


#1048:
salario = float(input())
if salario <= 400.00:
    perc = 15
elif salario <=800.00:
    perc = 12
elif salario <=1200.00:
    perc = 10
elif salario <= 2000.00:
    perc = 7
else:
    perc = 4

reajuste = salario * perc / 100 
novo_salario = salario + reajuste

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {perc} %") 

#1065
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

cont_par = 0
if num1 % 2 == 0:
    cont_par += 1 
if num2 % 2 == 0:
    cont_par += 1 
if num3 % 2 == 0:
    cont_par += 1 
if num4 % 2 == 0:
    cont_par += 1 
if num5 % 2 == 0:
    cont_par += 1 

print(cont_par, "valores pares")

#1132
x = int(input())
y = int(input())

if x > y:
    x, y = y, x

soma = 0 

for j in range (x, y+1):
    if not j % 13 == 0:
        soma += j
       
print(soma)

#1137
V = int(input())
N = [0] * 10
N[0] = V

for a in range(1, 10):
    N[a] = 2 * N[a-1]

for a in range(10):
    print(f"N[{a}] = {N[a]}")


#1180
def encontr_menor_val_e_pos(tam, vetor):
    menor = vetor[0]
    pos = 0
    for a in range(1, tam):
        if vetor[a] < menor:
            menor = vetor[a]
            pos = a
    return menor, pos

tam = int(input())
vetor = list(map(int, input().split()))
menor, pos = encontr_menor_val_e_pos(tam, vetor)
print("Menor valor:", menor)
print("Posicao:", pos)


#1182

l = int(input())
opera = input()
   

m=[]
for i in range(12):
    m.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        m[i].append(x)
        

if opera == 'S':
    soma = 0
    for k in range(12):
        soma = soma + m[k][l]
    print(soma)
if opera == 'M':
    med = 0
    soma = 0
    for k in range(12):
        soma = soma + m[k][l]
    med= soma/12
    print('{:.1f}'.format(med))