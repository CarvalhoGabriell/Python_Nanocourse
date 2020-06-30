# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# soma = n1 + n2
#
# print('A soma entre {} e {} é igual a {}'.format(n1,n2,soma))

word = input('Digite alguma coisa aqui: ')
print('O tipo primitivo desse valor é: ', type(word))
print('Essa palavra é um numero?', word.isnumeric())
print('É somente espaços', word.isspace())
print('Está printada na tela?', word.isprintable())
print('É alphabetico?', word.isalpha())
print('É um alphanumérico', word.isalnum())
print('Está tudo em maiúsculas', word.isupper())
print('Está tudo em minúsculas', word.islower())
print('Está capitalizada?', word.istitle())

