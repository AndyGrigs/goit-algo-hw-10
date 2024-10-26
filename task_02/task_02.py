import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло
n_points = 100000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, n_points)
y_random = f(x_random)

# Створення графіка
fig, ax = plt.subplots()

# Лінійний діапазон для відображення функції
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([a - 0.5, b + 0.5])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Обчислення площі під кривою
area_mc = (b - a) * np.mean(y_random)

# Обчислення інтеграла за допомогою quad
area_quad, error = spi.quad(f, a, b)

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Виведення результатів
print(f"Інтеграл методом Монте-Карло: {area_mc}")
print(f"Інтеграл за допомогою quad: {area_quad} з похибкою {error}")
