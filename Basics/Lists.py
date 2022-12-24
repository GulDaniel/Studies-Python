#atribuindo valores
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#acessando os valores
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title()
print(message)

#modificando elementos
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#acrescentando elementos
#no final
motorcycles.append('honda')
print(motorcycles)

#posição específica
motorcycles.insert(0, 'kawasaki')
print(motorcycles)

#removendo elementos
#posição específica
del motorcycles[0]
print(motorcycles)

#no final
pop_cycle = motorcycles.pop()
print(motorcycles)
print(pop_cycle)

#específica com pop
first_cycle = motorcycles.pop(0)
print(first_cycle)
print(motorcycles)

#removendo por valor
motorcycles.remove('yamaha')
print(motorcycles)
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)

#ordenando elementos
#permanente
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#ordem alfa inversa
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
#temporário
print(cars)
print(sorted(cars))

#ordem elem inversa
print(cars)
cars.reverse()
print(cars)

#tamanho da lista
len(cars)
