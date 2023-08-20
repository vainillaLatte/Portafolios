def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


array = []
num = (int(input("Ingrese el largo del arreglo:\n")))
print("Ingrese los números que componen el arreglo:")
for i in range(0 ,num):
  num1= (int(input()))
  array.append(num1)

print("Arreglo original:", array)
insertion_sort(array)
print("Arreglo ordenado:", array)
