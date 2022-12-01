def DebugHint(msg: object):
    print("\033[36mHint : " + str(msg) + "\033[0m")


def DebugWarning(msg: object):
    print("\033[33mWarning : " + str(msg) + "\033[0m")


def DebugSuccess(msg: object):
    print('\033[32mDone : ' + str(msg) + '\033[0m')


def DebugError(msg: object, abort: bool = True):
    print('\033[31mError : ' + str(msg) + '\033[0m')
    if abort == True:
        exit(0)