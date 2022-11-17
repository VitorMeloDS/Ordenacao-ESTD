def merge(vetor) :
    if len(vetor) > 1:
      div = len(vetor) // 2
      esq = vetor[:div].copy()
      dir = vetor[div:].copy()

      merge(esq)
      merge(dir)

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
