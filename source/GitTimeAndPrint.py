from ast import operator
import datetime
from fileinput import filename
from inspect import _void

FILE_NAME = "time.txt"


def Main() -> _void:
    # ��ȡ��ǰʱ��
    current_time = datetime.datetime.now()
    with open(FILE_NAME, "w") as file:
        file.write(str(current_time))
    return


if __name__ == "__main__":
    Main()