print("TABELA DE DESCONTOS \n"
      "até 20 litros de álcool = 3% de desconto! \n"
      "acima de 20 litros = 5% de desconto! \n"
      "até 20 litros de gasolina = 4% de desconto! \n"
      "acima de 20 litros = 6% de desconto.")

litros = int(input("QUANTOS LITROS VOCÊ VAI QUERER?"))
tipo_combustivel = input("QUAL COMBUSTÍVEL VAI QUERER?")
alcool = litros * 1.90
gasolina = litros * 2.50

if tipo_combustivel == "A" and litros <= 20:
    valor = litros - litros * 3/100               
    print("O VALOR DO LITRO DO ÁLCOOL FICOU EM {} COM 3% DE DESCONTO".format(valor))
elif tipo_combustivel == "A" and litros > 20:
    valor = litros - litros * 5/100
    print("O VALOR DO LITRO DO ÁLCOOL FICOU EM {} COM 5% DE DESCONTO".format(valor))
elif tipo_combustivel == "G" and litros <= 20:
    valor = litros - litros * 4/100
    print("O VALOR DO LITRO DA GASOLINA FICOU EM {} COM 4% DE DESCONTO".format(valor))
elif tipo_combustivel == "G" and litros >20:
    valor = litros - litros * 6/100
    print("O VALOR DO LITRO DA GASOLINA FICOU EM {} COM 6% DE DESCONTO".format(valor))
else:
    print("INFORME O COMBUSTÍVEL!")

    
    
    #linha 13 => quantidade de litros - valor do desconto sobre a quantidade de litro 
