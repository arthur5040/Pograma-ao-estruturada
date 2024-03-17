"""
Arthur Agostinho do Espírito Santo 
Primeiro período 

AC2 
"""

#questão 1

def eq_seg_grau(a, b, c):
    d = b**2 - 4 * a * c
    pr = -b + d ** 0.5
    sr = -b - d ** 0.5
    print (pr , sr)

eq_seg_grau(1,3,-4)


#questão 2
def calcula_salario(valor_hora , num_horas , irpf=0.275):
   
    valorbruto = valor_hora * num_horas 
   
    impostoderenda = valorbruto * irpf
   
    print(valorbruto - impostoderenda) 

calcula_salario (valor_hora = 30.0, num_horas= 8.0)
    
