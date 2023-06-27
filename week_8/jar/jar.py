class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Invalid Capacity')
        self._size = 0
        self._capacity = capacity

        ...

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError('You have exceed capacity')
        if self.size + n > self.capacity:
            raise ValueError('You have exceed capacity')
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError('Not enough cookies in jar')
        self._size -= n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size


jar = Jar()
jar.deposit(12)
jar.withdraw(8)
print(jar)