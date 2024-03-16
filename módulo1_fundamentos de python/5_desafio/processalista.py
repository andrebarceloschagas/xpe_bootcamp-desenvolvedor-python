# Encontra e retorna o maior número impar presente na lista
def maior_impar(lista):
    return max([n for n in lista if n % 2 != 0])

# Encontra e retorna o menor número impar presente na lista
def menor_impar(lista):
    return min([n for n in lista if n % 2 != 0])

# Encontra e retorna o maior e o menor número ímpar presentes na lista
def maior_menor_impar(lista):
    return (max([n for n in lista if n % 2 != 0]), min([n for n in lista if n % 2 != 0]))
