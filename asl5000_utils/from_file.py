import re


class Vr3Line:
    """
    Line of a Vr3 file
    """

    patterns = {
        0: re.compile(r"\s*\((\w*)\)\s+(\w+)\s+\((\w*)\)\s+(\w+)\s+=\s+(.*?)\s+\((.*)\)\s+\((.)*\)\s+\((.*)\)"),
        1: re.compile(r"\s*\((\w*)\)\s+(\w+)\s+\((\w*)\)\s+(\w+)\s+=\s+(.*?)\s+\((.*)\)\s+\((.*)\)"),
        2: re.compile(r"\s*\((\w*)\)\s+(\w+)\s+\((\w*)\)\s+(\w+)\s+=\s*?(.+?)"),
        3: re.compile(r"\s*\((\w*)\)\s+(\w+)\s*")
    }

    def __init__(self, line:str):
        self.line = line
        self.pattern = -1
        self.values = list()

    def from_pattern(self, pattern:int):
        if self.pattern == pattern:
            return self.values

        if pattern in self.patterns:
            self.pattern = pattern
            self.values = self.patterns[pattern].findall(self.line)
            return self.values


class Vr3File:
    def __init__(self, fid):
        self.fid = fid

    def readline(self):
        return Vr3Line(self.fid.readline())

    def __iter__(self):
        for line in self.fid:
            yield Vr3Line(line)


def read_vr3(filename):
    """
    Read a vr3 file and return its parameters

    Args:
        filename (str): path to file
    """

    data = dict()
    with open(filename) as f:
        vr3_file = Vr3File(f)
        vr3_file.readline()  # Header
        vr3_file.readline()  # Empty line
        for line in vr3_file:
            if len(re.sub(r"\s", "", line.line)) == 0:
                continue

            if line.from_pattern(0):
                x = line.from_pattern(0)
                module, description, tp, var, value, unit, mini, maxi = x[0]
                data[var] = {
                    "module": module,
                    "description": description,
                    "type": tp,
                    "value": value,
                    "unit": unit,
                    "min": mini,
                    "max": maxi
                }
            elif line.from_pattern(1):
                x = line.from_pattern(1)
                module, description, tp, var, value, mini, maxi = x[0]
                data[var] = {
                    "module": module,
                    "description": description,
                    "type": tp,
                    "value": value,
                    "unit": "",
                    "min": mini,
                    "max": maxi
                }
            elif line.from_pattern(2):
                x = line.from_pattern(2)
                module, description, tp, var, value = x[0]
                data[var] = {
                    "module": module,
                    "description": description,
                    "type": tp,
                    "value": value,
                    "unit": "",
                    "min": "",
                    "max": ""
                }
            elif line.from_pattern(3):
                x = line.from_pattern(3)
                module, description = x[0]
                data[var] = {
                    "module": module,
                    "description": description,
                    "type": "",
                    "value": "",
                    "unit": "",
                    "min": "",
                    "max": ""
                }
            else:
                print("not processed:", line.line)
                continue

    return data


if __name__ == "__main__":
    filename = "F:/User/Data/ASL5000/Scenarios/Efforts_BR15/Efforts_BR15_00_Normal_Normal.vr3"
    x = read_vr3(filename)
    for var, value in x.items():
        print(var, value)
