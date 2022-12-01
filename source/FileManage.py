def FileToStr(file_path: str) -> str:
    file_value: str = ""
    with open(file_path, encoding="utf16", errors="ignore") as file:
        file_value = file.read()
    return file_value


def FileToIntList(file_path: str) -> list[int]:
    file_value: str = FileToStr(file_path)

    file_str_list: list[str] = file_value.split("\n")
    file_str_list.pop()

    file_int_list: list[int] = [int(i) for i in file_str_list]
    return file_int_list


def FileToStrList(file_path: str) -> list[int]:
    file_value: str = FileToStr(file_path)

    file_str_list: list[str] = file_value.split("\n")
    file_str_list.pop()

    return file_str_list