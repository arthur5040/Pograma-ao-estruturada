#3048 
lista = []
for _ in range(int(input ())):
    number = input()
    if not lista:
        lista.append(number)
    elif number != lista[-1]:
        lista.append(number)
        
print(len(lista))


#2413 
t = int(input())

print(t * 4)


#2388
N = int(input())
dt = 0

for _ in range(N):
    V, T = map(int, input().split())
    d = V * T 
    dt += d

print(dt)


#2339
C, P, F = map(int, input().split())

QTFN = C * F

if QTFN <= P:
    print("S")
else:
    print("N")


#2006
T = int(input())
re = input().split()

rc = 0

for r in re:
    if int(r) == T:
        rc += 1

print(rc)


#1281
n = int(input())
while n:  
    n -= 1 
    feira = {}
    final = 0.0 
    
    m = int(input())
    while m:
        m -= 1 
        item, valor = input().split()
        feira[item] = float(valor)
        
    p = int(input())
    while p:
        p -= 1
        item, qt = input().split()
        final += feira[item]*int(qt)
        
    print("R$ %.2f" % final)


#1016 
x = int(input())

print(x * 2, "minutos")