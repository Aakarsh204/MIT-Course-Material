import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return [1/(1+np.exp(-num)) for num in x]

def relu(x):
    return [max(num, 0) for num in x]

def leaky_relu(x, alpha = 0.1):
    return [num if num > 0 else num*alpha for num in x]

def plot(f):
    x = np.linspace(-50, 50, 50)
    p = f(x)
    plt.xlabel('x')
    plt.ylabel("f(x)")
    plt.plot(x, p)
    plt.show()

if __name__ == '__main__':
    print("Enter the activation function \n1. Sigmoid\n2. ReLU\n3. Leaky ReLU")
    choice = int(input())
    if choice == 1:
        f = sigmoid
    elif choice == 2:
        f = relu
    else:
        f = leaky_relu
    x = [1.0]
    print(f'Applying activation function on {x[0]} gives {f(x)[0]:.2f}')
    x = [-10.0]
    print(f'Applying activation function on {x[0]} gives {f(x)[0]:.2f}')
    x = [15.0]
    print(f'Applying activation function on {x[0]} gives {f(x)[0]:.2f}')
    plot(f)
