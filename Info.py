import pymysql

conn=pymysql.connect(user = "root",password="")
cursor =conn.cursor()
cursor.execute("Use tabulationSystemKU")

class Info():
    def get_batch(self):
        try:
            cursor.execute("Select DISTINCT LEFT (rollNo,2) from registration")
        except pymysql.Error as err:
            print(err)

        batch_list1 = list(cursor.fetchall())

        try:
            cursor.execute("Select DISTINCT LEFT (roll,2) from theory_result")
        except pymysql.Error as err:
            print(err)

        batch_list2 = cursor.fetchall()

        try:
            cursor.execute("Select DISTINCT LEFT (roll,2) from sessional_result")
        except pymysql.Error as err:
            print(err)

        batch_list3 =cursor.fetchall()


        for i in batch_list2:
            if i not in batch_list1:
                batch_list1.append(i)

        for i in batch_list3:
            if i not in batch_list1:
                batch_list1.append(i)

        return batch_list1

    def get_session(self):
        try:
            cursor.execute("Select DISTINCT es from registration")
            session_1 =cursor.fetchall()
            cursor.execute("Select DISTINCT session from theory_result")
            session_2= cursor.fetchall()
            cursor.execute("Select DISTINCT session from sessional_result")
            session_3 =cursor.fetchall()
        except pymysql.Error as err:
            print(err)

        final_list =list()

        for i in session_1:
            if i[0] not in final_list:
                final_list.append(i[0])
        for i in session_2:
            if i[0] not in final_list:
                final_list.append(i[0])
        for i in session_3:
            if i[0] not in final_list:
                final_list.append(i[0])
        return  final_list

    def discipline_code(self):
        try:
            cursor.execute("Select disciplineCode from disciplineInfo")
            code =cursor.fetchone()[0]
        except pymysql.Error as err:
            print(err)

        return code