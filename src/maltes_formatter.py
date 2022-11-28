""" Please ignore this please """
import os

class MaltesFormatter():

    def __init__(self, target_path):
        self.target_path = target_path
        self.output = []

    def _trim_extra_whitespaces(self):
        """ Trim extra whitespace """
        for ix, line in enumerate(self.output):
            self.output[ix] = line.rstrip()

    def _add_final_newline(self):
        """ Checks and adds final newline """
        if self.output[:-1] != "":
            self.output.append("")

    def _fix_function_def(self):
        start = ""
        for ix, line in enumerate(self.output):
            if start != "":
                # Apply correct indentation
                content = line.strip()
                padded_content = " " * start + content
                self.output[ix] = padded_content
                # If function ends here:
                if  ")" in line:
                    start = ""
            # identify function and whether arguments are not closed on the same line
            if "def " in line and ")" not in line:
                # Find start of argument
                start = line.find("(") + 1

    def _format(self):
        """ Formatter main function """
        self._trim_extra_whitespaces()
        self._add_final_newline()
        self._fix_function_def()
        output = "\n".join(self.output)
        return output

    def run(self):
        """ Runs formatting"""
        checked_file_counter = 0
        for root, _, files in os.walk(self.target_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as filehandle:
                        self.output = filehandle.readlines()
                    output = self._format()
                    with open(file_path, "w", encoding="utf-8") as filehandle:
                        filehandle.write(output)
                    checked_file_counter += 1
        print(f"Went thru {checked_file_counter} files.")

    def run_test_mode(self):
        """ Runs formatting"""
        with open(self.target_path, "r", encoding="utf-8") as filehandle:
            self.output = filehandle.readlines()
        output = self._format()
        return output
