horas = int(input("Quantas horas vc trabalhou?"))
valor = float(input("Quanto vc ganha a hora?"))
salario = horas * valor

print("Voce trabalha {} horas por mes." .format(horas))
print("Voce recebe {} reais por hora no mes." .format(valor))
print("O seu salario é de {} reais" .format(salario))

desconto = 0.06
salario_desconto = salario - salario * 0.06 # salario - O QUANTO VAI SER DESCONTADO (valor)

print("O seu salario com desconto fica em {} reais" .format(salario_desconto))


#outro jeito de se fazer:
desconto = salario * 6/100 # fração da porcentagem, que nos resulta no valor a ser descontado (na parte da multipicação)
# 6/100 = 0.06
# salario * 0.06 = valor a ser descontado
salario_desconto = salario - desconto


#outros
# v - v * 0.05   tirar o valor a ser descontado
# v * 0.95       desconto
# v * 95/100     desconto em forma de fracao
# v - v * 5/100  tirar a porcentagem do valor com fracao
