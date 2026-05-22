def calculo_salario(horas, valor_hora):
    salario = horas * valor_hora
    salario_novo = (1 + horas ** 1.5 / valor_hora ** 2.5) * salario
    return salario_novo

print('CÁLCULO DE NOVO SALÁRIO')

print('========================================')

horas = int(input("Digite a quantidade de horas: "))
valor_hora = float(input("Digite o valor da hora: "))

print('========================================')

resultado = calculo_salario(horas, valor_hora)
print(f'Novo salário: {resultado:.2f}')