# ==========================================
# 4. HEAPSORT (Ordenamiento por Montículo)
# ==========================================

def _heapify(arr, n, i):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2
  if l < n and arr[l] > arr[largest]:
    largest = l
  if r < n and arr[r] > arr[largest]:
    largest = r
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    _heapify(arr, n, largest)


def heap_sort(arr):
  n = len(arr)
  for i in range(n // 2 - 1, -1, -1):
    _heapify(arr, n, i)
  for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    _heapify(arr, i, 0)
  return arr

if __name__ == "__main__":
  mi_lista = [12, 11, 13, 5, 6, 7]
  print("Lista original:", mi_lista)
  print("Lista ordenada (Heapsort):", heap_sort(mi_lista))
  