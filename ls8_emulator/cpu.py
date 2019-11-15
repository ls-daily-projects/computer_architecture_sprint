from .ram import RAM


class CPU():
    def __init__(self):
        self.is_running = False

        # Registers
        self.program_counter = 0
        self.current_mem_address = 0
        self.current_mem_data = 0
        self.current_instruction = 0
        self.current_flags = 0

        self.ram = RAM()

    def load_program(self, program=[]):
        address = 0

        for loc in program:
            self.ram.write(address, loc)
            address += 1

    def start(self):
        self.is_running = True

        while self.is_running:
            if self.program_counter > len(self.ram) - 1:
                self.is_running = False
                continue

            print(self.ram.read(self.program_counter))
            self.program_counter += 1
