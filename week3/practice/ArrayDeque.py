class ArrayDeque:
    def __init__(self):
        self.j = 0
        self.n = 0
        self.a = [None] * 5
        
    def add(self, i,x):
        # resize
        if i < self.n/2:
            print(self.j-1 % len(self.a))
            for k in range(0, i-1):
                #print(self.a[self.j+k % len(self.a)], self.a[self.j+k-1 % len(self.a)])
                self.a[self.j+k-1 % len(self.a)] = self.a[self.j+k % len(self.a)]
        else:
            for k in range(self.n, i+1):
                #print(self.a[self.j+k % len(self.a)], self.a[self.j+k+1 % len(self.a)])
                self.a[self.j+k+1 % len(self.a)] = self.a[self.j+k % len(self.a)]
        self.a[self.j+i % len(self.a)] = x
        self.n += 1

a = ArrayDeque()
a.add(1,5)
print(a.a)
a.add(1,5)
print(a.a)