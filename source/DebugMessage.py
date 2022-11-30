def debugHint(msg: object):
    print("\033[36mHint : " + str(msg) + "\033[0m")


def debugWarning(msg: object):
    print("\033[33mWarning : " + str(msg) + "\033[0m")


def debugSuccess(msg: object):
    print('\033[32mDone : ' + str(msg) + '\033[0m')


def debugError(msg: object, abort: bool = True):
    print('\033[31mError : ' + str(msg) + '\033[0m')
    if abort == True:
        exit(0)