import random
import sys
import time
import tracemalloc

# Aumentar límite de recursión por si Tree Sort o Merge Sort superan el estándar
sys.setrecursionlimit(200000)

# ==========================================
# 1. IMPLEMENTACIONES DE ALGORITMOS
# ==========================================


# --- MERGESORT ---
def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  result = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  result.extend(left[i:])
  result.extend(right[j:])
  return result


# --- HEAPSORT ---
def heapify(arr, n, i):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2
  if l < n and arr[l] > arr[largest]:
    largest = l
  if r < n and arr[r] > arr[largest]:
    largest = r
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)


def heap_sort(arr):
  n = len(arr)
  # Se hace una copia para no modificar el original si se requiere reuso
  arr_copy = list(arr)
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr_copy, n, i)
  for i in range(n - 1, 0, -1):
    arr_copy[i], arr_copy[0] = arr_copy[0], arr_copy[i]
    heapify(arr_copy, i, 0)
  return arr_copy


# --- PYTHON BUILT-IN SORT (Timsort - Referencia de control) ---
def python_sort(arr):
  return sorted(arr)


# ==========================================
# 2. SISTEMA DE BENCHMARK (TIEMPO Y MEMORIA)
# ==========================================


def medidor(func, arr):
  """Mide el tiempo transcurrido (segundos) y memoria máxima (MB)"""
  tracemalloc.start()
  inicio_tiempo = time.perf_counter()

  try:
    _ = func(arr)
    fin_tiempo = time.perf_counter()
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tiempo_total = fin_tiempo - inicio_tiempo
    memoria_mb = peak_memory / (1024 * 1024)  # Convertir a MB
    return f"{tiempo_total:.4f} s", f"{memoria_mb:.2f} MB"
  except MemoryError:
    tracemalloc.stop()
    return "MemoryError", "N/A"
  except Exception as e:
    tracemalloc.stop()
    return f"Error ({type(e).__name__})", "N/A"

# ==========================================
# 3. EJECUCIÓN DE LAS PRUEBAS
# ==========================================
if __name__ == "__main__":
  # Tamaños solicitados (ajustados a 10M como límite seguro para Python puro sin MemoryError)
  tamanos = [100_000, 1_000_000, 10_000_000]

  print("=" * 70)
  print(f"{'N (Elementos)':<15} | {'Algoritmo':<15} | {'Tiempo':<12} | {'Memoria Peak':<12}")
  print("=" * 70)

  for n in tamanos:
    print(
        f"\n[INFO] Generando arreglo aleatorio de {n:,} números reales (esto"
        " puede tardar unos segundos)..."
    )
    try:
      # Generar arreglos de números reales (floats entre 0.0 y 10000.0)
      datos = [random.uniform(0.0, 10000.0) for _ in range(n)]
    except MemoryError:
      print(
          f"❌ No se pudo crear el arreglo de tamaño {n:,} por falta de RAM"
          " (MemoryError)."
      )
      break

    # Algoritmos a evaluar para el tamaño N
    algoritmos = [("Heap Sort", heap_sort), ("Merge Sort", merge_sort)]

    for nombre, func in algoritmos:
      # Omitir Merge Sort para N >= 10,000,000 por consumo masivo de listas intermedias
      if nombre == "Merge Sort" and n >= 10_000_000:
        print(f"{n:<15,} | {nombre:<15} | {'Omitido (>RAM)':<12} | {'N/A':<12}")
        continue

      print(f"[INFO] Ejecutando {nombre} para N = {n:,}...")
      tiempo, memoria = medidor(func, datos)
      print(f"{n:<15,} | {nombre:<15} | {tiempo:<12} | {memoria:<12}")

    # Liberar memoria del arreglo base antes del siguiente ciclo
    del datos

  print("\n" + "=" * 70)
  print("¡Pruebas de benchmark finalizadas con éxito!")