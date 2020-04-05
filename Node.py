from random import randrange


class Node:
    def __init__(self, activation_function):
        self.base = randrange(-10, 10)
        self.val = 0
        self.act_func = activation_function

    def activate(self):
        self.val = self.act_func(self.val)
