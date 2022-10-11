import numpy as np


class Perceptron:
    def __init__(self, feature_dim, num_classes): # 3 points
        """
        in this constructor you have to initialize the weights of the model with zeros. Do not forget to put
        the bias term!
        """
        self.numC = num_classes
        self.weight = [list] * num_classes
        for i in range(num_classes):
            self.weight[i] = []
            for j in range(feature_dim + 1):
                self.weight[i].append(0)
        

    def train(self, feature_vector, y): # 10 points
        """
        this function gets a single training feature vector (feature_vector) with its label (y) and adjusts
        the weights of the model with perceptron algorithm.
        Hint: use self.predict() in your implementation.
        """
        y_hat = self.predict(feature_vector)
        if y_hat != y:
            for i in range(self.numC):
                if i != y:
                    self.weight[i] = np.subtract(self.weight[i], np.dot(0.0001, feature_vector))
                else:
                    self.weight[i] = np.add(self.weight[i], np.dot(0.0001, feature_vector))
        #print(self.weight)
        


    def predict(self, feature_vector): # 10 points
        """
        returns the predicted class (y-hat) for a single instance (feature vector).
        Hint: use np.argmax().
        """
        #print('hey')
        y = [0] * self.numC
        for i in range(self.numC):
            y[i] = np.dot(feature_vector, self.weight[i])
        y_hat = np.argmax(y)
        return y_hat

