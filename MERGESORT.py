# ==========================================
# 2. MERGESORT (Ordenamiento por Mezcla)
# ==========================================

def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  return _merge(left, right)


def _merge(left, right):
  result = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  result.extend(left[i:])
  result.extend(right[j:])
  return result

if __name__ == "__main__":
  mi_lista = [38, 27, 43, 3, 9, 82, 10]
  print("Lista original:", mi_lista)
  print("Lista ordenada con Mergesort:", merge_sort(mi_lista))

if __name__ == "__main__":
  mi_lista = [38, 27, 43, 3, 9, 82, 10]
  print("Lista original:", mi_lista)
  print("Lista ordenada (Mergesort):", merge_sort(mi_lista))