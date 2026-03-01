import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
X = np.linspace(0, 10, 20)
true_w, true_b = 2.0, 1.0
noise = np.random.normal(0, 1, X.shape)
y = true_w * X + true_b + noise

w, b = 0.5, 0.0
y_pred = w * X + b

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

loss_value = mse(y, y_pred)
print("MSE =", loss_value)

plt.scatter(X, y, label="данные (x, y)")
plt.plot(X, y_pred, color="red", label="модель y = w*x + b")
plt.title(f"Линейная модель, MSE = {loss_value:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
