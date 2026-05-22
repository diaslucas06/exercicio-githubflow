def quadratica(a, b, c):
    delta = (b**2)-(4*a*c)
    raiz_delta = delta**(1/2)
    X1 = (-b + raiz_delta)/(2*a)
    X2 = (-b - raiz_delta)/(2*a)
    return X1, X2

print("Calculadora de Equação de 2° Grau")
print('*********************************')
print('**Insira o valor das variáveis:**')

a = int(input('Digite o valor de A:'))
b = int(input('Digite o valor de B:'))
c = int(input('Digite o valor de c:'))

print(quadratica(a, b, c))