
class Stack(list):
    def peek(self):
        return self[len(self) - 1]

    def push(self, x):
        self.append(x)


