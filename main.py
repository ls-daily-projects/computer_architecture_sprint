from utils import InputParser
from ls8_emulator import LS8Parser, CPU

if __name__ == "__main__":
    input_parser = InputParser()
    filename = input_parser[0]

    ls8_parser = LS8Parser()
    ls8_parser.parse(filename)

    cpu = CPU()
    cpu.load_program(ls8_parser.lines_of_code)
    cpu.start()
