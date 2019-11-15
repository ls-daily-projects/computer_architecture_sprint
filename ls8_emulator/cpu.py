from .ram import RAM


class CPU():
    def __init__(self):
        self.ram = RAM()

    def load_program(self, program=[]):
        address = 0

        for loc in program:
            self.ram.write(address, loc)
            address += 1

    def start(self):
        print("Started from the top!")
        print(self.ram)
