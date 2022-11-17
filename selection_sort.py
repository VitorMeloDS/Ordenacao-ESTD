def sort(vetor):
  n = len(vetor)

  for i in range(n):
    inicio = i
    for j in range(i + 1, n):
      if vetor[inicio] > vetor[j]:
        inicio = j

    temp = vetor[i]
    vetor[i] = vetor[inicio]
    vetor[inicio] = temp

  return vetor
