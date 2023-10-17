'''
3. Faça um programa que peça um número para o usuário (string),
converta-o para float e depois imprima-o na tela. Você consegue
fazer a mesma coisa, porém convertendo para int?
'''
# Solicita ao usuário um número. No input, o que for digitado no teclado,
# por padrão, a saída é do tipo str (string "Cadeia de caracteres").

num = input('Digite um número: ')  # num é a variável que irá receber o que o usuário digitar.

print('Número =', num)  # Mostra na tela o valor digitado pelo usuário ainda como str.

print('Tipo antes da conversão:', type(num))  # Mostra na tela o tipo de dado que o usuário digitou.

num = float(num)  # Função float() convertendo para o tipo float.

print('Número =', num)  # Mostra na tela o valor digitado pelo usuário, agora convertido para o tipo float.
print('Tipo depois da conversão:', type(num))  # Mostra na tela o tipo de dado que o usuário digitou depois de convertido.

num = int(num)  # Função int() convertendo para o tipo int.

print('Número =', num)  # Mostra na tela o valor digitado pelo usuário, agora convertido para o tipo int.
print('Tipo depois da conversão:', type(num))  # Mostra na tela o tipo de dado que o usuário digitou depois de convertido.

'''
Outra forma de converter o input do usuário:

num = float(input('Digite um múmero:')) # A converção acontece no momento em que o dado é digitado.
'''