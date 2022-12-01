import sqlite3

DIFF_DATA_DB: str = "diff.db"


def OpenDB():
    #创建SQLite数据库
    con = sqlite3.connect(DIFF_DATA_DB)
    #创建表DiffData:包含3列，输入，cpp输出，py输出
    con.execute("create table if not exists DiffData( \
                random_in TEXT PRIMARY KEY,\
                cpp_out TEXT NOT NULL,\
                py_out TEXT NOT NULL)")
    #创建游标对象
    cur = con.cursor()
    return con, cur


def InsertData(data: list[tuple[str, str, str]]):
    con, cur = OpenDB()
    for random_in, cpp_out, py_out in data:
        insert_sql = "INSERT INTO DiffData VALUES(\"{}\", \"{}\", \"{}\")"
        insert_sql = insert_sql.format(random_in, cpp_out, py_out)
        print(insert_sql)
        cur.execute(insert_sql)

    con.commit()
    con.close()