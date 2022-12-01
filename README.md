# ProgramComparer

## 1. 项目背景
1. 程序比较器的开发目的是用来比较BigInteger与Python中的高精度的算法，以便不需要人工的去测试代码的正确性。
## 2. 安装
1. 本机需要具备Python的环境。
2. 克隆源代码。
```git
git clone git@github.com:DoLovya/ProgramComparer.git
```
## 3. 使用
1. 将source文件夹的绝对路径添加到环境变量。
2. ProgramComparer.py为比较器主程序，后面需要附加3个参数，参数必须是可执行文件或脚本文件。
   参数1：随机生成器的相对路径或绝对路径；
   参数2：cpp程序的相对路径或绝对路径；
   参数3：py程序的相对路径或绝对路径；
3. 在终端中输入`ProgramComparer.py [参数1] [参数2] [参数3]`，即可将两个程序的异数据存在在数据库中；
4. 利用vscode的Sqlite插件可以看到数据库中数据，以便Debug。
## 4. Badge

## 5. 相关项目
1. 此项目主要是为了Debug BigNumber项目。
## 6. 主要负责人
1. DoLovya
## 7. 开源协议