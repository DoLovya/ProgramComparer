import sys
from FileManage import ReadFileToStr


def main(argv):
    print(ReadFileToStr(argv[1]))
    pass


if __name__ == "__main__":
    main(sys.argv)