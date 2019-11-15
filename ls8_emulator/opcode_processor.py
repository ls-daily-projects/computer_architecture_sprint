class OpcodeProcessor():
    def __init__(self, cpu):
        self.cpu = cpu
        self.dispatch_table = {
            0b10000010: self.load_data_immediately,
            0b01000111: self.print_data,
            0b00000001: self.halt_cpu,
            0b10100010: self.multiply,
            0b10100111: self.compare,
            0b01010101: self.jump_if_equal,
            0b01010110: self.jump_if_not_equal,
            0b01010100: self.jump
        }

    def load_data_immediately(self):
        current_count = self.cpu.program_counter
        register = self.cpu.ram.read(current_count + 1)
        self.cpu.main_register[register] = self.cpu.ram.read(current_count + 2)
        return 2

    def print_data(self):
        register_location = self.cpu.ram.read(self.cpu.program_counter + 1)
        register_value = self.cpu.main_register[register_location]
        print(register_value)
        return 1

    def multiply(self):
        num_1_location = self.cpu.ram.read(self.cpu.program_counter + 1)
        num_2_location = self.cpu.ram.read(self.cpu.program_counter + 2)
        num_1 = self.cpu.main_register[num_1_location]
        num_2 = self.cpu.main_register[num_2_location]
        print(num_1 * num_2)
        return 2

    def compare(self):
        current_count = self.cpu.program_counter
        register_a_index = self.cpu.ram.read(current_count + 1)
        register_b_index = self.cpu.ram.read(current_count + 2)
        a = self.cpu.main_register[register_a_index]
        b = self.cpu.main_register[register_b_index]

        # TODO: Use bitshifting instead
        if a < b:
            self.cpu.current_flags = 0b100
        elif a > b:
            self.cpu.current_flags = 0b010
        else:
            self.cpu.current_flags = 0b001

        return 2

    def jump(self):
        register = self.cpu.ram.read(self.cpu.program_counter + 1)
        self.cpu.program_counter = self.cpu.main_register[register]
        return -1

    def jump_if_equal(self):
        current_count = self.cpu.program_counter
        is_equal_set = self.cpu.current_flags == 0b001

        if not is_equal_set:
            return 1

        register = self.cpu.ram.read(current_count + 1)
        self.cpu.program_counter = self.cpu.main_register[register]
        return -1

    def jump_if_not_equal(self):
        current_count = self.cpu.program_counter
        current_flags = self.cpu.current_flags
        is_equal_set = current_flags == 0b001

        if is_equal_set:
            return 1

        register = self.cpu.ram.read(current_count + 1)
        self.cpu.program_counter = self.cpu.main_register[register]
        return -1

    def halt_cpu(self):
        self.cpu.is_running = False
        return 0

    def is_valid_opcode(self, opcode):
        return opcode in self.dispatch_table

    def instruction_for_opcode(self, opcode):
        return self.dispatch_table[opcode]
