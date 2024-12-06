print("Sistema desenvolvido por: Valdenilson Felipe Souza Silva.")

valorBase = float(input("Informe o valor base do plano: R$ "))
idade = int(input("Informe a sua idade:"))

porcetagem = 0

if idade >= 0 and idade < 19:
    porcetagem = 100/100  
elif idade >= 19 and idade < 29:  
    porcentagem = 150 / 100  
elif idade >= 29 and idade < 39:
    porcentagem = 225 / 100 
elif idade >= 39 and idade < 49:  
    porcentagem = 240 / 100  
elif idade >= 49 and idade < 59:  
    porcentagem = 350 / 100  
else:   #Aqui eu usei apenas um else porque é a ultima condição.
    porcentagem = 600 / 100  

valorMensal = valorBase * porcentagem
print ("O Valor mensal do plano é:R$ ",valorMensal)