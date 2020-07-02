import numpy as np

# creating a 1 layer NN

# Sigmoid
def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)
# create NN class
class NeuralNet:
    def __init__(self, x, y):
        self.input = x
        self.weight1 = np.random.rand(self.input.shape[1], 4)
        self.weight2 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(self.y.shape)
    # Add feedforward function
    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weight1))
        self.output = sigmoid(np.dot(self.layer1, self.weight2))
    #Add backpropogation
    def backpropogation(self):
        # use chainrule to get derivative of the loss function
        d_weight2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weight1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weight2.T) * sigmoid_derivative(self.layer1)))
        # Update the weight with the derivative (slope) of loss function
        self.weight1 += d_weight1
        self.weight2 += d_weight2

# test code

X = np.array([[0, 0, 1],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1]])

y = np.array([[0], [1], [1], [0]])

NN = NeuralNet(X, y)

for i in range(1500):
    NN.feedforward()
    NN.backpropogation()

print(NN.output)