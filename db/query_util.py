import pymysql

# brew services start mysql
# mysql -uroot
# lsof -i :5000 => pid
# kill -9 $pid
"""
    show databases;
    create database feedback;
    use feedback;
    show tables;
    create table user(name varchar(255), email varchar(255), password varchar(255));
    insert into user(name,email,password) values('Abhishek Sharma', 'abhishekmdngr@gmail.com', 'abhi');
    select * from user;
"""


def execute(query, inputs):
    """
    query: string
    inputs: tuple
    """
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="feedback",
    )
    cur = conn.cursor()
    cur.execute(query, inputs)
    conn.commit()
