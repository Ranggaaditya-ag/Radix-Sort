#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Membaca DataFrame dari file CSV
df = pd.read_csv('Data Sort.csv', header=None)

# Pilih indeks kolom yang akan diurutkan, misalnya indeks 0
column_index = 0

# Mengambil data dari kolom yang akan diurutkan
arr = df.iloc[:, column_index].values

# Implementasi algoritma Counting Sort
def counting_sort(arr):
    max_num = max(arr)
    n = len(arr)
    output = [0] * n
    count = [0] * (max_num + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

# Memanggil fungsi counting_sort
counting_sort(arr)

# Mengganti kolom asli dengan hasil pengurutan
df.iloc[:, column_index] = arr

# Menampilkan DataFrame yang telah diurutkan
print(df)

