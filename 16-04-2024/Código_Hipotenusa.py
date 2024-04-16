
print("Seja bem-vindo a calculadora de Arquimedes!")

# Timer para as perguntas

import time
start_time = time.time()

time.sleep(3)

end_time = time.time()

# Pergunta para o usuário:

letra_a = int(input("Digite a letra A: "))
letra_l = int(input("Digite a letra L: "))

# Calculando os resultados:

print("Calculando resultados: ")
import time
start_time = time.time()

# Timer respostas e cálculos:

time.sleep(3)

end_time = time.time()

# Calculo da área:

area_retangulo = (letra_l * letra_a)
print("A área do retângulo é: ", area_retangulo)

# Calculo do perímetro:

perimetro_retangulo = (2 * (letra_a * letra_a))
print("O perímetro do retângulo é: ", perimetro_retangulo)

# Calculo da hipotenusa:
hipotenusa = (letra_a ** 2 + letra_l ** 2) ** 0.5
print("A hipotenusa é: ", hipotenusa)
