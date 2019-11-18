import os
import re
import struct


# =============================================================================
# =
# = Tools
# =
# =============================================================================


def __is_label(line):
    """
    Return if the line is a label or not

    Args:
        line (str): line to test

    Returns:
        bool: True if the line is a label
    """

    if line == "":
        return False
    elif "xxx" in line:
        return False
    elif "The x's" in line:
        return False
    else:
        return True


    """
    Read an ASL binary file

    Args:

    `file`: the file to be read
    `size_header`: binary size of the header
    `start_labels`: first row with the labels
    `endian`: big (">") or little ("<")
    `dtype`: type of the data ("f" for float, ...)

    Return:
    -------

    `labels`: list of all the labels
    `array`: 2D matrix containing the data
    """
def __read_binary(file, size_header, start_labels, endian=">", dtype="f"):
    """
    Read a n ASL binary file

    Args:
        file (str): path to file
        size_header (int): header byte size
        start_labels (int): line number where the labels start
        endian (str): big (>) or little (<) endian
        dtype (str): data type (f is float32)

    Returns:
        list: list of labels
        list: data array
    """

    with open(file, "rb") as f:
        # Read the header
        header = f.read(size_header)
        header = header.decode()
        header = re.sub("\r", "", header)
        header = header.split("\n")
        labels = header[start_labels:]
        labels = list(filter(__is_label, labels))

        # Read the data
        n_cols = len(labels)
        array = [list() for _ in range(n_cols)]
        block = n_cols * 4  # Size of data in a line
        fmt = f"{endian}{n_cols}{dtype}"  # example: ">16f"
        line = f.read(block)
        while len(line) == block:
            # Extract data from line
            line = struct.unpack(fmt, line)  # Big Endian Float
            for i in range(n_cols):
                array[i].append(line[i])
            # Read next line
            line = f.read(block)

    return labels, array


# =============================================================================
# =
# = Read files
# =
# =============================================================================


def read_rwa(file):
    """
    Read an ASL5000 RWA file

    Parameters:
    -----------

    `file`: the file to be read

    Return:
    -------

    `labels`: list of all the labels
    `array`: 2D matrix containing the data
    """

    f = open(file, "r", encoding="utf-8")

    # > Read labels -----------------------------------------------------------

    for _ in range(2):
        f.readline()  # How to read the data

    labels = f.readline().rstrip("\n")
    labels = labels.split("\t")

    f.readline()  # The blanck line

    # > Read data -------------------------------------------------------------

    array = list()
    for line in f:
        # Extract data from line
        line = line.rstrip(" \n")
        line = re.split(r"\s+", line)
        line = list(map(float, line))
        array.append(line)

    f.close()

    return labels, array


def read_rwb(file):
    """
    Read an ASL5000 RWB file

    Parameters:
    -----------

    `file`: the file to be read

    Return:
    -------

    `labels`: list of all the labels
    `array`: 2D matrix containing the data
    """

    return __read_binary(file, size_header=500, start_labels=4)


def read_avb(file):
    """
    Read an ASL5000 AVB file

    Parameters:
    -----------

    `file`: the file to be read

    Return:
    -------

    `labels`: list of all the labels
    `array`: 2D matrix containing the data
    """

    return __read_binary(file, size_header=2000, start_labels=6)


def read_brb(file):
    """
    Read an ASL5000 BRB file

    Parameters:
    -----------

    `file`: the file to be read

    Return:
    -------

    `labels`: list of all the labels
    `array`: 2D matrix containing the data
    """

    return __read_binary(file, size_header=4096, start_labels=4)
