class CircularQueue:
    def __init__(self):
        self.list = ['R1', 'R2', 'R3', 'R4']
        self.MAX_SIZE = len(self.list)
        self.head = 0
        self.tail = self.MAX_SIZE -1
        self.road = 'R1'
        self.mode = 'Auto'

    def forward(self):
        self.head += 1
        self.tail += 1
        if self.tail == self.MAX_SIZE:
            self.tail = 0
        if self.head == self.MAX_SIZE:
            self.head = 0
        self.road = self.list[self.head]

    def backward(self):
        self.head -= 1
        self.tail -= 1
        if self.tail == -1:
            self.tail = 3
        if self.head == -1:
            self.head = 3
        self.road = self.list[self.head]