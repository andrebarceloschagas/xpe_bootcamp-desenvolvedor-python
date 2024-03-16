# Atividade 01. Execute e analise a saída do seguinte código:

# relação dos nomes
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']
# estrutura que irá armazenar o número de letras de cada nome
qtd_letras = {}
# calcula o tamanho de cada nome (em número de letras) e armazena o valor na estrutura
for nome in nomes:
    qtd_letras[nome] = len(nome)

print(qtd_letras)
print(type(nomes)) # <class 'list'>
print(type(qtd_letras)) # <class 'dict'>
print(len(nomes)) # 8
print(len(qtd_letras)) # 6


""" # Atividade 02. Reescreva o código da Atividade 01 utilizando o conceito de compreensão de dicionários (dict comprehension).

# relação dos nomes
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio', 'Antonio']

# estrutura que irá armazenar o número de letras de cada nome
qtd_letras = {nome: len(nome) for nome in nomes}
print(qtd_letras) """

""" Atividade 03. Crie uma função area(r, pi), que calcule a área de um círculo.

# a) A utilização de um valor padrão para pi (𝜋 = 3,14), sem a necessidade de declarar explicitamente o seu valor;

função que calcula a área de um círculo
def area_ciculo(r):
    return 3,14 * (r ** 2)

print('Área do círculo:', area_ciculo(8))

# b) A utilização com a declaração explicita do valor exato de pi desejado.

# função que calcula a área de um círculo

def area_ciculo(r, pi):
    return pi * (r ** 2)

print('Área do círculo:', area_ciculo(8, 3.14)) """

""" # Atividade 04. Reescreva a função area da atividade 3, utilizando o conceito de funções anônimas (funções lambdas):

# area_circulo = lambda r, pi: pi * (r ** 2)
# print('Área do círculo:', area_circulo(8, 3.14)) """

""" # Atividade 05. Crie um módulo em Python, chamado processalista (arquivo processalista.py), com as seguintes funções,
# que deverão receber como argumento uma lista (tipolist) de números inteiros.

import processalista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a) Encontra e retorna o maior número impar presente na lista
print(processalista.maior_impar(lista))

# b) Encontra e retorna o menor número impar presente na lista
print(processalista.menor_impar(lista))

# c) Encontra e retorna o maior e o menor número ímpar presentes na lista
print(processalista.maior_menor_impar(lista))
 """


""" # Atividade 06. Considere a seguinte agenda de disponibilidade de atendimento de uma clínica com vários médicos, cada um de uma especialidade distinta. Essa
# clínica possuí apenas três consultórios, e, por isso, no máximo três médicos podem atender por dia.

# A clínica percebeu que os pacientes que desejam se consultar com mais de um médico sempre solicitam que o atendimento seja realizado no mesmo dia. Por
# exemplo, um paciente gostaria de se consultar, no mesmo dia, com o ortopedista e com o neurologista, então os dias disponíveis serão: terça e quinta. Outro
# exemplo é um paciente que gostaria de se consultar com o dermatologista, o neurologista e o psiquiatra. O único dia disponível será a sexta.
# Entretanto, essas solicitações estão causando dor de cabeça, pois é necessário verificar manualmente a disponibilidade. Você, como um(a) aspirante a
# desenvolvedor Python, aceitou o desafio de ajudar a automatizar essa tarefa. Para tanto, irá desenvolver duas funções que receberão a relação de disponibilidade de
# cada médico e que retornarão os dias disponíveis:

# relação de dias da semana que cada médico atende
cardiologista = {'terca', 'quarta'}
ortopedista = {'terca', 'quinta'}
dermatologista = {'segunda', 'quarta', 'sexta'}
neurologista = {'terca', 'quinta', 'sexta'}
psiquiatra = {'segunda', 'quarta', 'sexta'}

# Calcula quais os dias possíveis para dois médicos
def disp_dois_especialistas(medico01, medico02):
    return medico01.intersection(medico02)


# Calcula quais os dias possíveis para três médicos
def disp_tres_especialistas(medico01, medico02, medico03):
    return medico01.intersection(medico02, medico03)


# Assim, para os exemplos anteriores, as funções deverão ter os seguintes retornos:
# Médicos solicitados: ortopedista e neurologista
print(disp_dois_especialistas(ortopedista, neurologista))
# RETORNA: terça e quinta
# Médicos solicitados: dermatologista, neurologista, psquiatra
print(disp_tres_especialistas(dermatologista, neurologista, psiquiatra))
# RETORNA: sexta """