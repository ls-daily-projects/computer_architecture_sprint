class RAM():
    """CPU's RAM"""

    def __init__(self, size=0xFF):
        self.size = size
        self.storage = [0b0] * self.size

    def __str__(self):
        gap = 32
        output = "-" * gap
        output += " The RAM "
        output += "-" * gap
        output += "\n["
        output += "----".join([str(val) for val in self.storage])
        output += "]"
        return output

    def __len__(self):
        return self.size

    def write(self, address, value):
        self.storage[address] = value
        return self

    def read(self, address):
        return self.storage[address]
