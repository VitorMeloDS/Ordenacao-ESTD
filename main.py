import random
import timeit
from ordenacao_hibrida import ordenacao
from selection_sort import sort
from merge_sort import merge
from os import system, name, _exit
from time import sleep

if __name__ == '__main__':

  clear = lambda: system('cls' if name == 'nt' else 'clear')
  clear()

  lista = []

  def apresentacao() -> bool:
    inicializador = input('\nPara iniciar o processo digite "start", para ordenação hibrida digite "hibrido", para ordenação merge digite "merge sort",\npara a ordenação de sort digite "selection sort" e para sair digite "exit": ').lower().strip()
    if inicializador == 'start':
      return True
    elif inicializador == 'exit':
      return False
    elif inicializador == 'hibrido':
      print('\nNão há nada para fazer!'); sleep(2); clear(); apresentacao()
      return True
    elif inicializador == 'merge sort':
      print('\nNão há nada para fazer!'); sleep(2); clear(); apresentacao()
      return True
    elif inicializador == 'selection sort':
      print('\nNão há nada para fazer!'); sleep(2); clear(); apresentacao()
      return True
    else:
      print('\nComando não reconhecido, digite uns dos comando expecificados!'); sleep(2); clear(); apresentacao()
      return True

  def valores_aleatorios(min, max):
    return random.randint(min, max)

  def hibrida():
    return ordenacao(lista)

  def selection_sort():
    
    return sort(lista)

  def merge_sort():
    return merge(lista)

  def entradaDado():
    try:
      while True:
        min = 1
        max = int(input('\nDigite a quantidade de elementos: '))
        escolha_ordenacao = input('Digite o tipo de ordenação que deseja: ').lower().strip()
        qtd_vezes = 100

        for i in range(max):
          lista.append(valores_aleatorios(min, max))

        if escolha_ordenacao == None or max == None:
          print('\nComando não reconhecido, digite uns dos comando expecificados!')
          sleep(2); clear(); entradaDado()
        elif escolha_ordenacao == 'exit':
          _exit(0)
        elif escolha_ordenacao == 'selection sort':
          selection_sort()
          tempo_sort = timeit.timeit(stmt=selection_sort, number=qtd_vezes)
          print(
            f"\nTeste repetido {qtd_vezes} vezes\nTempo de duração do teste: {tempo_sort}\nTempo médio do teste {tempo_sort/qtd_vezes}"
          )
        elif (escolha_ordenacao == 'merge sort'):
          merge_sort()
          tempo_merge = timeit.timeit(stmt=merge_sort, number=qtd_vezes)
          print(
            f"\nTeste repetido {qtd_vezes} vezes\nTempo de duração do teste: {tempo_merge}\nTempo médio do teste {tempo_merge/qtd_vezes}"
          )
        elif (escolha_ordenacao == 'hibrido'):
          hibrida()
          tempo_hibrido = timeit.timeit(stmt=hibrida, number=qtd_vezes)
          print(
            f"\nTeste repetido {qtd_vezes} vezes\nTempo de duração do teste: {tempo_hibrido}\nTempo médio do teste {tempo_hibrido/qtd_vezes}"
          )

    except Exception as e:
      if e:
        print(e)
      print('\nComando não reconhecido, digite uns dos comando expecificados!')
      sleep(2); entradaDado()

  def main():
    try:
      if apresentacao():
        entradaDado()
    except Exception as e:
      print(e)

main()  
