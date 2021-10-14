n= float(input('Digite um número: '))
print(' O numero que você digitou é: {} '.format(n))

n= float(input('Digite um número: '))
dobro = n*2
triplo = n*3
r = n**(1/2)
print('O numero que você digitou é:{}, seu dobro é {}, seu triplo é {} e sua raíz quadrada é {}!' .format(n,(n*2),(n*3),pow(n,(1/2))))

n1 = float(input('Digite a nota de Português: '))
n2 = float(input('Digite a nota de Matemática: '))
n3 = float(input('Digite a nota de História: '))
n4 = float(input('Digite a nota de Química: '))
n5 = float(input('Digite a nota de Física: '))
media= (n1+n2+n3+n4)/4
print('Sua média semestral é: {}'.format(media))

altura= float(input('Digite quantos metros você tem: '))
centimetros = altura*100
milimetros = altura*1000
print(' Voce têm {} metros,  {} centímetros e {} milimetros '.format(altura,centimetros,milimetros))

real = float(input('Quantos reais você tem em sua carteira? '))
m = real/3.27
print(' Com {} reais você poderá comprar {:.2f} doláres'.format(real,m))