import weakref

from .ram import RAM
from .opcode_processor import OpcodeProcessor


class CPU():
    def __init__(self):
        self.is_running = False

        # Registers
        self.main_register = [0b0] * 8
        self.program_counter = 0
        self.current_mem_address = 0
        self.current_mem_data = 0
        self.current_instruction = 0
        self.current_flags = 0

        self.ram = RAM()
        self.opcode_processor = weakref.ref(OpcodeProcessor(self))()

    def load_program(self, program=[]):
        address = 0

        for loc in program:
            self.ram.write(address, loc)
            address += 1

    def start(self):
        self.is_running = True

        while self.is_running:
            self.current_mem_address = self.ram.read(self.program_counter)

            if self.opcode_processor.is_valid_opcode(self.current_mem_address):
                pc_delta = self.opcode_processor.instruction_for_opcode(
                    self.current_mem_address)()
                self.program_counter += pc_delta
                continue

            self.program_counter += 1
