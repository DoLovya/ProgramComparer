import sys, os
import subprocess
from FileManage import ReadFileToStr
from DebugMessage import debugError
from DebugMessage import debugSuccess

IN_FILE: str = "in.txt"
CPP_OUT_FILE: str = "cpp_out.txt"
PY_OUT_FILE: str = "pyt_out.txt"
REDIRECT_CMD_FORMAT: str = "Get-Content {} | {} > {}"


# Get-Content .\output.txt | .\random_plus.py > output.txt
def GetRandomRedirectCmd(file_path: str) -> str:
    redirect_cmd: str = REDIRECT_CMD_FORMAT
    redirect_cmd = redirect_cmd.format(IN_FILE, file_path, IN_FILE)
    return redirect_cmd


def GetCppRedirectCmd(file_path: str) -> str:
    redirect_cmd: str = REDIRECT_CMD_FORMAT
    redirect_cmd = redirect_cmd.format(IN_FILE, file_path, CPP_OUT_FILE)
    return redirect_cmd


def GetPythonRedirectCmd(file_path: str) -> str:
    redirect_cmd: str = REDIRECT_CMD_FORMAT
    redirect_cmd = redirect_cmd.format(IN_FILE, file_path, PY_OUT_FILE)
    return redirect_cmd


def JudgeFileAndHint(file_path: str):
    if os.path.exists(file_path) == False:
        debugError("文件%s不存在！" % file_path)


def ExecutePowshellCmd(cmd: str) -> str:
    subprocess.call(["powershell.exe", cmd])
    return cmd


def main(argv):
    if len(argv) != 4:
        debugError("参数个数错误！")

    random_path: str = argv[1]
    cpp_path: str = argv[2]
    python_path: str = argv[3]

    JudgeFileAndHint(cpp_path)
    JudgeFileAndHint(python_path)
    JudgeFileAndHint(random_path)

    debugSuccess(ExecutePowshellCmd(GetRandomRedirectCmd(random_path)))
    debugSuccess(ExecutePowshellCmd(GetCppRedirectCmd(cpp_path)))
    debugSuccess(ExecutePowshellCmd(GetPythonRedirectCmd(python_path)))
    pass


if __name__ == "__main__":
    main(sys.argv)