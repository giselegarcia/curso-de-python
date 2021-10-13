nome = input(' Qua é o seu nome? ')
idade = int(input('Qual é a sua idade? '))
sexo = str(input('Qual é seu sexo? '))
print(' Seu nome é: {:=^20}!'.format(nome))
print('Sua idade é: {:>20}!'.format(idade))
print('Seu sexo é: {:<20}!'.format(sexo))


