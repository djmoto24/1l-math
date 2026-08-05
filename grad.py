import numpy as np
def loss(y_true, x1, b1):
    pred = x1 - b1
    print(pred)
    loss = np.mean((pred - y_true)**2)
    print(loss)
    return loss

true = np.array([1.0, 0.0, 0.25])
#b1 = np.random.randint(0,10,3)
b1 = np.array([0, 9, 8])
x1 = np.array([2.0, -1.0, 3])

res = loss(true, x1, b1)

b1 = np.array([0, 8, 6])

res2 = loss(true, x1, b1)