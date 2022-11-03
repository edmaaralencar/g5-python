# Transformar tuplas em dicionarios
    # atracoes = []
    # tupla_nomes = ('id', 'nome', 'descricao', 'tipo', 'horarios')
    # for roxx in rows:
        # atracoes.append((dict(zip(tupla_nomes, row))))

# try:
#     sqliteConnection = sqlite3.connect('SQLite_Python.db')

#     cursor = sqliteConnection.cursor()

    # # # sqlite_create_table_query = '''CREATE TABLE atracoes (
    # # #                             id INTEGER PRIMARY KEY,
    # # #                             nome TEXT NOT NULL,
    # # #                             descricao text NOT NULL,
    # # #                             tipo text NOT NULL,
    # # #                             horarios text NOT NULL
    # # #                             );'''

    # # # # Create table EMPLOYEES and INSERT into table EMPLOYEES values
    # # # cursor.execute(sqlite_create_table_query)
    # # # cursor.execute("INSERT INTO atracoes VALUES(2, 'Atracao 1', 'Lorem quis scelerisqu rutrum.', 'restaurante', 'manha,tarde');")
    # # # sqliteConnection.commit()

    # Select FIRSTNAME and LASTNAME from table EMPLOYEES
#     cursor.execute("SELECT nome, descricao, tipo, horarios FROM atracoes;")
#     for atracao in cursor.fetchall():
#         print(atracao)

#     cursor.close()

# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("The SQLite connection is closed")

# try:
#     sqliteConnection = sqlite3.connect('SQLite_Python.db')

#     cursor = sqliteConnection.cursor()

#     # Create table EMPLOYEES and INSERT into table EMPLOYEES values
#     cursor.execute("CREATE TABLE employees (firstname varchar(32), lastname varchar(32), title varchar(32));")
#     cursor.execute("INSERT INTO employees VALUES('Kelly', 'Koe', 'Engineer');")
#     sqliteConnection.commit()

#     # Select FIRSTNAME and LASTNAME from table EMPLOYEES
#     cursor.execute("SELECT firstname, lastname FROM employees;")
#     for firstname, lastname in cursor.fetchall():
#         print(firstname, lastname)

#     cursor.close()

# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("The SQLite connection is closed")


# NULL: – The value is a NULL value.
# INTEGER: – To store the numeric value. The integer stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the number.
# REAL: – The value is a floating-point value, for example, 3.14 value of PI
# TEXT: – The value is a text string, TEXT value stored using the UTF-8, UTF-16BE or UTF-16LE encoding.
# BLOB: – The value is a blob of data, i.e., binary data. It is used to store images and files.
