from Node import Node


class NeuralNetworkController:
    def __init__(self):
        self.layers = []
        self.weights = []

    def add_layer(self, size, activation_function):
        new_layer = []
        if len(self.layers) >= 1:
            self.weights.append([])
        for i in range(0, size):
            new_layer.append(Node(activation_function))
        self.layers.append(new_layer)
