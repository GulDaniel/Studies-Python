import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#nome_do_modulo.nome_da_função()
#todas as funções de pizza foram importadas

#importar função específica
from pizza import make_pizza
#from nome_do_modulo import função_0, função 1, função_2...
#não necessita mais do ponto
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#alias
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
#from nome_do_modulo import nome_da_função as alias
#também serve para módulos
#import pizza as p
#p.make_pizza(16. 'pepperoni')


#importar todas as funções
#from pizza import *
#make_pizza(16, 'pepperoni')
