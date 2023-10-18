# 8. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês e depois, calcule e mostre o total do seu salário no referido mês.

#Solicita as informações ao usuário.
valor_hora = float(input("Informe o valor por hora trabalhada: "))
qtd_hora = float(input("Quantas horas voçê trabalhou no mês : "))

total_sal = valor_hora * qtd_hora #Calcula o valor a receber.

print(f'Total a resceber : {total_sal}')#Mostra o valor a resceber.
