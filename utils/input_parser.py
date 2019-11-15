import sys


class InputParser():
    def __init__(self, required_args_length=1):
        self.required_args_length = required_args_length
        self.args = sys.argv[1:]

    def __str__(self):
        return ",".join(self.args)

    def __getitem__(self, index):
        """Returns the provided list of arguments, not including the first argument"""
        try:
            return self.args[index]
        except:
            argument_word = "argument" if self.required_args_length else "arguments"
            raise TypeError(
                f"You must supply at least {self.required_args_length} {argument_word}")
