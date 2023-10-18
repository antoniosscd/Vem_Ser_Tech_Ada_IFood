# 5. Faça um programa que peça as 4 notas bimestrais de um aluno e mostre a média aritmética delas.

print('Digite as 4 notas do aluno: ')
soma = 0
média = 0

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a primeira nota: '))
nota3 = float(input('Digite a primeira nota: '))
nota4 = float(input('Digite a primeira nota: '))

soma += nota1 + nota2 +nota3 + nota4

média = soma/4

print('Média do aluno é =',média)
