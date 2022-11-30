"""
1. 通过脚本调用make将测试代码编译为exe文件
2. 通过脚本生成随机数据，并且可以自定义一些数据，非覆盖，而是追加
3. 利用脚本将测试exe的输入重定向到随机数据，将输出数据重定向到一个输出文件中
4. 利用脚本将正确py的输入重定向到随机数据，将输出数据重定向到一个输出文件中
5. 利用脚本对两个输出文件比对，发现不同时及时保存至文件中
"""

import os
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.description = 'please enter two parameters a and b ...'
    parser.add_argument("-c",
                        "--cpp",
                        help="This is cpp file",
                        dest="cpp",
                        type=str,
                        default=False)
    parser.add_argument("-p",
                        "--output",
                        help="This is python file",
                        dest="python",
                        type=str,
                        default=False)
    parser.add_argument("-r",
                        "--rand",
                        help="This is rand file",
                        dest="rand",
                        type=str,
                        default=False)
    parser.add_argument("OUTPUT",
                        default=None,
                        action="store",
                        help="This is output file")
    return parser.parse_args()


def main():
    args = get_args()
    os.system("code " + args.cpp)


if __name__ == "__main__":
    main()
