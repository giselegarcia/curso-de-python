n1 = float(input(' Digite em metros a largura da sua parede: '))
n2 = float(input(' Digite em metros a altura de sua parede: '))
m = (n1*n2)
print(' Sua parede tem {} m²,'.format(m), end = '')
t = (m/2)
print (' dessa forma, você precisará de {} litros de tinta para pintar a área calculada '.format(t))
