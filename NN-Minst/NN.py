import numpy as np

# creating a 2 layer NN
# create NN class
class NeuralNet:
    def __init__(self, x, y):
        self.input = x
        self.weight1 = np.random.rand(self.input.shape[1], 4)
        self.weight2 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(y.shape)

