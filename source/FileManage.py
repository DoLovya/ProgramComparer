def ReadFileToStr(file_path: str) -> str:
    file_value: str = ""
    with open(file_path) as file:
        file_value = file.read()
    return file_value