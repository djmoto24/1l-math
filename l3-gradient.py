import numpy as np
import matplotlib.pyplot as plt

# 1. Генерируем данные (как в первом уроке)
np.random.seed(0)
X = np.linspace(0, 10, 20)
true_w, true_b = 2.0, 1.0
noise = np.random.normal(0, 1, X.shape)
y = true_w * X + true_b + noise

# 2. Начальные параметры модели
w, b = 0.5, 0.0

# 3. Функция потерь: MSE
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# 4. Градиенты MSE по w и b
def gradients(X, y_true, y_pred):
    N = len(X)
    error = y_true - y_pred  # вектор ошибок (y_i - y_hat_i)

    dw = -2 * np.mean(X * error)   # dMSE/dw
    db = -2 * np.mean(error)       # dMSE/db
    return dw, db

# 5. Параметры обучения
lr = 0.01          # скорость обучения
n_steps = 100      # число шагов

# 6. Обучение: градиентный спуск
for step in range(n_steps):
    # прямой проход: предсказания
    y_pred = w * X + b

    # считаем лосс
    loss_value = mse(y, y_pred)

    # считаем градиенты
    dw, db = gradients(X, y, y_pred)

    # обновляем параметры
    w = w - lr * dw
    b = b - lr * db

    # немного логов
    if step % 10 == 0:
        print(f"step={step}, w={w:.3f}, b={b:.3f}, loss={loss_value:.3f}, dw={dw:.3f}, db={db:.3f}")

# 7. Финальное предсказание после обучения
y_pred_final = w * X + b
final_loss = mse(y, y_pred_final)
print(f"\nПосле обучения: w={w:.3f}, b={b:.3f}, MSE={final_loss:.3f}")

# 8. Визуализация
plt.scatter(X, y, label="данные (x, y)")
plt.plot(X, y_pred_final, color="red", label=f"модель y = w*x + b")
plt.title(f"Линейная модель после обучения, MSE = {final_loss:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()