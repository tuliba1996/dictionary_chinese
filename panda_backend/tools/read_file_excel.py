# import xlrd
# import psycopg2

# from openpyxl import load_workbook
#
# loc = ('/Users/huynhchiduan/Code/panda_backend/tools/common.xlsx')
# list_word = []
# wb = load_workbook(loc)
# ws_names = wb.sheetnames
# sheet = wb[ws_names[0]]
# print(sheet)
# sheet = wb.sheet_by_index(0)
# sheet.cell_value(0, 0)
#




# for i in range(sheet.nrows - 2990):
#     chinese = sheet.cell_value(i, 0)
#     pinyin = sheet.cell_value(i, 7)
#     data = {
#         'chinese': chinese,
#         'pinyin': pinyin
#     }
#     list_word.append(data)
# print('list', list_word)
import sqlite3

db_path = '/Users/huynhchiduan/Code/panda_backend/db.sqlite3'


loc = ('/Users/huynhchiduan/Code/panda_backend/tools/dict')


def join_string(arr):
    sub_arr = arr[3:]
    # print(arr[3:])
    return " ".join(sub_arr)


def read_file():
    f = open(loc, "r")
    lines = f.readlines()
    result = []
    for _line in lines:
        a = _line.split()
        _res = []
        if len(a) > 4:
            _res = a[:3]
            _res.append(join_string(a))
            result.append(_res)
        else:
            result.append(a)

    return result


try:


    data = read_file()


    # connection = psycopg2.connect(user="postgres",
    #                               password="12345",
    #                               host="127.0.0.1",
    #                               port="5432",
    #                               database="learn_chinese")

    connection = sqlite3.connect(db_path)

    # connection.autocommit = False
    cursor = connection.cursor()

    # for i in data:
    #     if len(i) > 3:
    #         print("as")
    #         d = (i[1], i[2], i[3])
    #         insert_query = """ INSERT INTO api_charactercommon (chinese, pinyin, vietnamese) VALUES (?,?,?)"""
    #         cursor.execute(insert_query, d)
    #
    # print(cursor.lastrowid)
    # connection.commit()
    #

    cursor.execute("SELECT * FROM api_charactercommon;")

    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        print(row)

    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # print(cursor.fetchall())

    # for row in sheet.iter_rows():
    #
    #     chinese = row[0].value
    #     pinyin = row[7].value
    #     print(chinese, pinyin)
        # record_to_insert = (chinese, pinyin)
        # cursor.execute(postgres_insert_query, record_to_insert)
    #
    # connection.commit()
    # count = cursor.rowcount
    # print("Record inserted successfully into common table")


    # Print PostgreSQL Connection properties
    # sql_check_table = '''select * from information_schema.tables where table_name=api_book;'''
    # test_select = '''SELECT * FROM api_book;'''

    # cursor.execute(test_select)
    # records = cursor.fetchall()
    # connection.commit()
    # print('records', records)
except Exception as error:
    print("Error in transction Reverting all other operations of a transction ", error)
    connection.rollback()
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("SQLite connection is closed")




