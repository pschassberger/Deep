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
    # Add feedforward function
    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weight1))
        self.output = sigmoid(np.dot(self.layer1, self.weight2))
    #Add backpropogation
    def backpropogation(self):
        # use chainrule to get derivative of the loss function
        d_weight2 = np.dot(self.layer1.T, (2 * (self.y - self.output) 
                            * sigmoid_derivative(self.output)))
        d_weight1 = np.dot(self.input.T, (np.dot(2 * (self.y - self.output) 
                    * sigmoid_derivative(self.output), self.weight2.T) * sigmoid_derivative(self.layer1)))
        # Update the weight with the derivative (slope) of loss function
        self.weight1 += d_weight1
        self.weight2 += d_weight2

# test code