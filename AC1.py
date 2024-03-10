#Exercício 1 

a = float(input ("informe a variavel a: "))
b = float(input ("informe a variavel b: "))
c = float(input ("informe a variavel c: "))

d = b**2 - 4 * a * c

pr = (-b+ d**0.5) / (2*a)
sr = (-b- d**0.5) / (2*a)

print("a primeira raiz é", pr)
print("a segunda raiz é", sr)

#Exercício 2 

ano = int(input ("informe um ano: "))
print((ano %4 ==0) and ((ano %100 !=0) or (ano %400 ==0)))