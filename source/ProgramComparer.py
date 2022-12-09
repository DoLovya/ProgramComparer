#!/usr/bin/python

import sys, os
import subprocess
from FileManage import FileToIntList
from FileManage import FileToStrList
from DebugManage import DebugError
from DebugManage import DebugSuccess
from DebugManage import DebugHint
from DataManage import InsertData

IN_FILE: str = "in.txt"
CPP_OUT_FILE: str = "cpp_out.txt"
PY_OUT_FILE: str = "py_out.txt"
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
        DebugError("文件%s不存在！" % file_path)


def ExecutePowshellCmd(cmd: str) -> str:
    subprocess.call(["powershell.exe", cmd])
    return cmd


def FindTheDiffInIntList(in_list: list[str], list1: list[str],
                         list2: list[str]) -> list[tuple[str, str, str]]:
    list_len: int = len(list1)
    ret_list: list[tuple[str, str, str]] = []
    for i in range(0, list_len):
        if list1[i] != list2[i]:
            ret_list.append((in_list[i], str(list1[i]), str(list2[i])))

    return ret_list


def ProgramComparer(random_path: str, cpp_path: str, python_path: str):
    DebugSuccess(ExecutePowshellCmd(GetRandomRedirectCmd(random_path)))
    DebugSuccess(ExecutePowshellCmd(GetCppRedirectCmd(cpp_path)))
    DebugSuccess(ExecutePowshellCmd(GetPythonRedirectCmd(python_path)))

    in_list: list[str] = FileToStrList(IN_FILE)

    cpp_out_list: list[str] = FileToStrList(CPP_OUT_FILE)
    py_out_list: list[str] = FileToStrList(PY_OUT_FILE)

    if len(cpp_out_list) != len(py_out_list):
        DebugError("输出文件个数不同！")

    diff_list = FindTheDiffInIntList(in_list, cpp_out_list, py_out_list)

    if len(diff_list):
        InsertData(diff_list)
        DebugHint("找到%d条不同的数据" % (len(diff_list)))
        DebugHint("不同数据已存入数据库")
    else:
        DebugSuccess("未找到异数据")


def main(argv):
    if len(argv) != 4:
        DebugError("参数个数错误！")

    random_path: str = argv[1]
    cpp_path: str = argv[2]
    python_path: str = argv[3]

    JudgeFileAndHint(cpp_path)
    JudgeFileAndHint(python_path)
    JudgeFileAndHint(random_path)
    ProgramComparer(random_path, cpp_path, python_path)


if __name__ == "__main__":
    main(sys.argv)