# Como converter graus Celsius para Fahrenheit em Python?
#
# Este programa solicita ao usuário uma temperatura em graus Celsius (°C)
# e realiza a conversão para Fahrenheit (°F), aplicando a fórmula:
# °F = (°C × 9/5) + 32.
# Ideal para praticar entrada de dados, operadores matemáticos e formatação de saída.

temp = float(input('Informe a temperatura em °C: '))
fah = ((9 * temp) / 5) + 32
print(f'A temperatura de {temp:.2f}°C corresponde a {fah:.2f}°F!')
