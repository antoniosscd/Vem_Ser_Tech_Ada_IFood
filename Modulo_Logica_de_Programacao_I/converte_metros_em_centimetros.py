# 6. Faça um programa que converta um valor em metros para centímetros.


conversor = 100
centimetros = 0

#Solicita o tamnho que deseja converter.
tamanho = float(input("Digite o tamnho em metros que deseja converter para centímetros: "))


centimetros = tamanho * conversor #Calcula a conversão de metros em centímetros.

#Mostra a coverção do tamanho informado em metros para centímetros.
print('A tamanho em metros,',tamanho,',convertido para centímetros é = ',centimetros,'centímetros')