def ordenacao(vetor):
  if len(vetor) < 128:
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
    
  else:
    if len(vetor) > 1:
      div = len(vetor) // 2
      esq = vetor[:div].copy()
      dir = vetor[div:].copy()

    ordenacao(esq)
    ordenacao(dir)

    i = j = k = 0

    while i < len(esq) and j < len(dir):
      if esq[i] < dir[j]:
        vetor[k] = esq[i]
        i += 1
      else:
        vetor[k] = dir[j]
        j += 1
      k += 1

    while i < len(esq):
      vetor[k] = esq[i]
      i += 1
      k += 1
    while j < len(dir):
      vetor[k] = dir[j]
      j += 1
      k += 1
      
  return vetor