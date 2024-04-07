# 1000
print("Hello World!")

#1001
A = int((input()))
B = int((input()))

print('X =', A+B)

#1010
codigo_peca1, num_peca1, valor_unitario1 = map(float, input().split())
codigo_peca2, num_peca2, valor_unitario2 = map(float, input().split())

total_peca1 = num_peca1 * valor_unitario1
total_peca2 = num_peca2 * valor_unitario2

valor_total = total_peca1 + total_peca2

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")

#1013
a, b, c = map(int, input().split())

maior_ab = (a + b + abs(a - b)) / 2

maior_valor = int((maior_ab + c + abs(maior_ab - c)) / 2)

print(f"{maior_valor} eh o maior")

#1015
import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("{:.4f}".format(distancia))
