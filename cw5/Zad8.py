class Ok:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        self.index = self.index + 1
        if(self.data[self.index] == 'a' or self.data[self.index] == 'e' or self.data[self.index] == 'o' or self.data[self.index] == 'u' or self.data[self.index] == 'i' or self.data[self.index] == 'y'):
            return self.data[self.index]
ob = Ok("Costam")
print(ob.__iter__())
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())


