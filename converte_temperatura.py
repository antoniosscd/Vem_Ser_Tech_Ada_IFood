# 9. Faça um programa que peça a temperatura em graus Fahrenheit (F), transforme e mostre a temperatura em graus Celsius (°C).
# C = (5 * (F-32) / 9).

#Solicita a temperatura em Fahrenheit (F).
temp = float(input("Informe a temperatura na escala Fahrenheit: "))

temp_convert = (5 * (temp-32) / 9) # Conversão em Celsius(°C).

print(f'Temperatura informada em graus Celsius (°C) é igual a {temp_convert}°C ')#Imprime a temperatura na escala Celcius.