'''
# 7. Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
# Obs: Formula da área de um círculo, A = 3.14*r²
'''
#Inicializando as variáveis 'pi' e area.
pi = 3.14
area = 0

#Solicita o valor do raio do circulo.
raio_circulo = float(input('Digite a área do círculo: '))

area += pi*(raio_circulo**2)# Cálculo da area do cículo.

#Mostra o tamanho da área do cículo em metros quadrados.
print('A área do cículo é =', area)
