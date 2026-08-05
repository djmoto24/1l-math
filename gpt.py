import numpy as np

def relu(z):
    #ss=np.array([0, 25, 4, 7, -6])
    return np.maximum(0, z)

def dense(x, w, b):
    z = np.dot(x, w) + b
    return relu(z)

def mse_loss(y_true, y_pred):
    return np.mean(pow(y_true - y_pred, 2))

def new_weight(N, W, loss):
    w_new = loss\
    return w_new

def forward(x, W1, b1, W2, b2):
    y1 = dense(x1, W1, b1)
    y2 = dense(y1, W2, b2)
    return y2

y_true = np.array([1.0, 0.0])
#b1 = np.random.randint(0,10,3)
b1 = np.array([0, 9, 8])
#b2 = np.random.randint(0,10,2)
b2 = np.array([4, 9])
# Пример параметров
x1 = np.array([2.0, -1.0, 3, 4, 5])   # вектор признаков

w1 = np.array([[0.47872114, 0.54784731, 0.58729743],
       [0.04777224, 0.79809179, 0.99973349],
       [0.00122712, 0.66449366, 0.54446426],
       [0.24323801, 0.46599917, 0.9026964 ],
       [0.87863254, 0.66430801, 0.80540156]])

#w2 = np.random.randn(3, 2)
w2 = np.array([[0.26088565, 0.50804946],
       [1.14439631, 0.46033224],
       [0.76459648, 1.03317258]])

y_pred = forward(x1, w1, b1, w2, b2)
print(y_pred)
loss = mse_loss(y_true, y_pred)
print("loss =", loss)