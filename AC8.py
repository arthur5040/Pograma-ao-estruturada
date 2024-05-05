#1028
def mdc(n1, n2):
    res = n1 % n2
    if res == 0:
        return abs(n2)
    return mdc(n2, res)

def main():
    nt = int(input())
    for _ in range(nt):
        a, b = map(int, input().split())
        print(mdc(a, b))

if __name__ == "__main__":
    main()


#1087
def min(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0
    elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return 1
    else:
        return 2

while True:
    X1, Y1, X2, Y2 = map(int, input().split())
    if X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0:
        break
    print(min(X1, Y1, X2, Y2))


#1161
def fatorial(n):
    if n == 0:
        return 1 
    else:
        return n * fatorial(n-1)
    
while True:
    try:
        entr = input().split()
        M = int(entr[0])
        N = int(entr[1])
        soma = fatorial(M) + fatorial(N)
        print(soma)
    except EOFError:
        break

#1170
def cdc(C):
    dias = 0 
    while C > 1:
        C /= 2
        dias += 1 
    return dias

N = int(input())

for _ in range(N):
    C = float(input())
    if C <= 1:
        print("1 dia")
    else:
        dias_pc = cdc(C)

        print(dias_pc, "dias")



#1171
N = int(input())
contagem = {}
for _ in range(N):
    num = int(input())
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1
for num in sorted(contagem.keys()):
    print(f"{num} aparece {contagem[num]} vez(es)")

#1221
N = int(input())
for _ in range(N):
    X = int(input())
    if X < 2:
        print("not prime")
    else:
        is_prime = True
        for i in range(2, int(X ** 0.5) + 1):
            if X % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Prime")
        else:
            print("Not Prime")

            


#1329
while True:
    num = int(input())
    if num == 0:
        break
    result = [int(x) for x in input().split()]
    m = 0
    for resultado in result:
        if resultado == 0:
            m += 1
            
    j = num - m
    print("Mary won " + str(m) + " times and John won " +  str(j)+ " times")



#1555
n = int(input())
for _ in range(n):
    x, y = [int(val) for val in input().split()] 
    
    r = (3 * x) ** 2 + y ** 2
    b = 2 * (x ** 2) + (5 * y) ** 2
    c = -100 * x + y ** 3
    
    if c > b and c > r:
        print ("Carlos ganhou")
        
    elif b > c and b > r:
        print ("Beto ganhou")
            
    else:
        print ("Rafael ganhou") 