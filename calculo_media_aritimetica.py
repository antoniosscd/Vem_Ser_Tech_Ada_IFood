# 5. Faça um programa que peça as 4 notas bimestrais de um aluno e mostre a média aritmética delas.

#Informa o que fazer.
print('Digite as 4 notas do aluno: ')

#Inicia as variáveis soma e media.
soma = 0
media = 0

#Solicita as notas ao usuário.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a primeira nota: '))
nota3 = float(input('Digite a primeira nota: '))
nota4 = float(input('Digite a primeira nota: '))

soma += nota1 + nota2 +nota3 + nota4 # Soma as notas.

média = soma/4 # Cálculo da média aritimética.

print('Média do aluno é =',média) # Mostra a média.
