import random
import timeit
from ordenacao_hibrida import ordenacao
from selection_sort import sort
from merge_sort import merge
from os import system, name, _exit
from time import sleep

clear = lambda: system('cls' if name == 'nt' else 'clear')
clear()

lista = []

def init():
  min = 1
  max = int(input('\nDigite a quantidade de elementos: '))
  escolha_ordenacao = input('Digite o tipo de ordenação que deseja: ').lower()
  qtd_vezes = 100

  for i in range(max):
    lista.append(valores_aleatorios(min, max))

  if (escolha_ordenacao == 'selection sort'):
    selection_sort()
    tempo_sort = timeit.timeit(stmt=selection_sort, number=qtd_vezes)
    print(
      f"Teste repetido {qtd_vezes} vezes\nTempo de duração do teste: {tempo_sort}\nTempo médio do teste {tempo_sort/qtd_vezes}"
    )
  elif (escolha_ordenacao == 'merge sort'):
    merge_sort()
    tempo_merge = timeit.timeit(stmt=merge_sort, number=qtd_vezes)
    print(
      f"Teste repetido {qtd_vezes} vezes\nTempo de duração do teste: {tempo_merge}\nTempo médio do teste {tempo_merge/qtd_vezes}"
    )
  elif (escolha_ordenacao == 'hibrido'):
    hibrida()
    tempo_hibrido = timeit.timeit(stmt=hibrida, number=qtd_vezes)
    print(
      f"Teste repetido {qtd_vezes} vezes\nTempo de duração do teste: {tempo_hibrido}\nTempo médio do teste {tempo_hibrido/qtd_vezes}"
    )
  elif (escolha_ordenacao == 'tempo'):
    comparar_tempo(tempo_sort, tempo_merge, tempo_hibrido, qtd_vezes)
  elif (escolha_ordenacao == 'exit'):
    _exit(0)
  else:
    print(
      '\nComando não reconhecido digite uma das alternativas opções "selection sort", "merge sort", "hibrido" "exit"'
    )
    sleep(2)
    init()


  return max

def valores_aleatorios(min, max):
  return random.randint(min, max)

def hibrida():
  return ordenacao(lista)

def selection_sort():
  return sort(lista)

def merge_sort():
  return merge(lista)

def comparar_tempo(sort, merge, hibrido, qtd_vezes):
  if (sort):
    print(f'\nTempo de duração do teste sort: {sort}\nTempo médio do teste {sort/qtd_vezes}')
  elif (merge):
    print(f'\nTempo de duração do teste merge: {merge}\nTempo médio do teste {merge/qtd_vezes}')
  elif (hibrido):
    print(f'\nTempo de duração do teste hibrido: {hibrido}\nTempo médio do teste {hibrido/qtd_vezes}')

init()

if init() < 128:
  print("-> Selection Sort <-")
else:
  print("-> Merge Sort <-")