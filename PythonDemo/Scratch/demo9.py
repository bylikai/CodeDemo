import sqlite3

connection = sqlite3.connect('db_project.sqlite')
cursor = connection.cursor()

cursor.execute("""
        create table project_list(
            id integer primary key autoincrement unique not null,
            title text not null,
            url   text not null
        )
    """)
connection.commit()
connection.close()