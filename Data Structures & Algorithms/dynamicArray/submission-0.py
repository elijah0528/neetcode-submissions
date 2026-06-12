class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = []
    def get(self, i: int) -> int:
        return self.store[i]

    def set(self, i: int, n: int) -> None:
        self.store[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() >= self.getCapacity():
            self.resize()
        self.store.append(n)

    def popback(self) -> int:
        return self.store.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.store)
    
    def getCapacity(self) -> int:
        return self.capacity