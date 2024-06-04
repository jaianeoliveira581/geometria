#(com lambda simplifica calculo, se sua função tiver 2 ou mais linhas, usar o çambda para simplificar) calcular_retângulo = lambda base, altura: base + altura
#Crie um programa que o usuário possa escolher se deseja saber a área de um círculo, de um triângulo ou de um trapézio.

import os

# função do menu
def exibir_menu():
    print('1 - Área do círculo.')
    print('2 - Área do triângulo.')
    print('3 - Área do trapézio.')
    print('4 - Sair do programa.')

# função da área do círculo
def calcular_circulo(r):
    a = 3.14*r**2
    return a

# função da área do triângulo
def calcular_triangulo(b, h):
    a = (b*h)/2
    return a

# função da área do trapézio
def calcular_trapezio(base_menor, base_maior, h):
    a = ((base_menor + base_maior)*h)/2
    return a

# programa principal
while True:
    exibir_menu()
    opcao = input('Opção desejada: ')
    os.system('cls')

    match opcao:
        case '1':
            print('Área do círculo: a = π*r²')
            r = int(input('Informe o valor do raio: '))
            print(f'Área do círculo: {calcular_circulo(r)}.')
            continue
        case '2':
            print('Área do triângulo: a = (b*h)/2')
            b = int(input('Informe o valor da base: '))
            h = int(input('Informe o valor da altura: '))
            print(f'Área do triângulo: {calcular_triangulo(b, h)}.')
            continue
        case '3':
            print('Área do trapézio: a = ((b+B)*h)/2')
            base_menor = int(input('Informe o valor da base menor: '))
            base_maior = int(input('Informe o valor da base maior: '))
            h = int(input('Informe o valor da altura do trapézio: '))
            print(f'Área do trapézio: {calcular_trapezio(base_menor, base_maior, h)}')
            continue
        case '4':
            break
        case _:
            print('Opção inválida.')
            continue