class Stack:
    def __init__(self):
        self.mas = []
        self.error = False

    def append(self, n):
        self.mas.append(n)

    def st(self):
        if not self.error and len(self.mas) > 0:
            return ' '.join([str(i) for i in self.mas])
        elif self.error:
            return "ERROR"
        else:
            return 'EMPTY'

    def drop(self):
        if len(self.mas) < 1:
            self.error = True
            return False
        self.mas.pop(-1)

    def swap(self):
        if len(self.mas) < 2:
            self.error = True
            return False
        a = self.mas[-2]
        b = self.mas[-1]
        self.mas[-1] = a
        self.mas[-2] = b

    def dup(self):
        if len(self.mas) < 1:
            self.error = True
            return False
        self.append(self.mas[-1])

    def over(self):
        if len(self.mas) <= 1:
            self.error = True
            return False
        self.append(self.mas[-2])

    def plus(self):
        if len(self.mas) < 2:
            self.error = True
            return False
        a = self.mas.pop(-1)
        b = self.mas.pop(-1)
        self.append(a + b)

    def minus(self):
        if len(self.mas) < 2:
            self.error = True
            return False
        b = self.mas.pop(-1)
        a = self.mas.pop(-1)
        self.append(a - b)

    def mul(self):
        if len(self.mas) < 2:
            self.error = True
            return False
        b = self.mas.pop(-1)
        a = self.mas.pop(-1)
        self.append(a * b)

    def div(self):
        if len(self.mas) < 2:
            self.error = True
            return False
        b = self.mas.pop(-1)
        a = self.mas.pop(-1)
        self.append(a // b)


s = Stack()

with open('input.txt') as f:
    commands = [el.strip() for el in f.readlines()]

for el in commands:
    if el == 'DROP':
        s.drop()
    elif el == "SWAP":
        s.swap()
    elif el == 'DUP':
        s.dup()
    elif el == 'OVER':
        s.over()
    elif el == '+':
        s.plus()
    elif el == '-':
        s.minus()
    elif el == '/':
        s.div()
    elif el == '*':
        s.mul()
    else:
        s.append(int(el))

with open('output.txt', 'w') as f:
    f.write(s.st())
