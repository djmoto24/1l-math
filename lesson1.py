import matplotlib
#matplotlib.use('TkAgg')  # задаём используемый backend
import numpy as np
import matplotlib.pyplot as plt

# Создадим простой массив
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("a:", a)
print("b:", b)

# Элементарные операции
print("a + b =", a + b)
print("a * b =", a * b)
print("b / 10 =", b / 10)

# Матрицы
M = np.array([
    [1, 2],
    [3, 4]
])

N = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix M:\n", M)
print("Matrix N:\n", N)
print("M dot N =\n", M @ N)  # матричное умножение

# Простая визуализация
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Function")
plt.show()
