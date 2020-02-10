#!/usr/bin/env python3

import mysql.connector
import configparser
import getopt, sys


class HlCrud:
    config = configparser.ConfigParser()

    def __init__(self, config_file):
        self.config.read(config_file)
        self.db = mysql.connector.connect(host=self.config["mysql"]["host"],
                                          user=self.config["mysql"]["user"],
                                          passwd=self.config["mysql"]["passwd"],
                                          database=self.config["mysql"]["database"])

    def insert_data(self, table, data):
        cursor = self.db.cursor()
        col = '\',\''.join(data.keys())
        col = col.replace("'", "`")
        sql = "INSERT INTO %s (`%s`) VALUES %s " % (table, col, tuple(data.values()))
        x = self.db.cursor()
        x.execute(sql)
        self.db.commit()
        print('Succefully inserted'.format(cursor.rowcount))

    def show_data(self, table):
        x = self.db.cursor()
        sql = "select * from %s " % table
        x.execute(sql)
        rows = x.fetchall()
        for row in rows:
            print(row)
        return

    def update_data(self, table, data, where):
        col = ''
        whr = ''
        for k, v in data.items():
            temp = "`" + k + "` = " + "'" + v + "'"
            col += " ," + temp if col else temp
        for k, v in where.items():
            temp = "`" + k + "` = " + "'" + v + "'"
            whr += " ," + temp if whr else temp
        sql = "UPDATE `%s` SET %s WHERE %s " % (table, col, whr)
        x = self.db.cursor()
        x.execute(sql)
        self.db.commit()
        return

    def delete_data(self, table, where):
        sql = "DELETE FROM %s WHERE %s " % (table, where)
        x = self.db.cursor()
        x.execute(sql)
        self.db.commit()
        return

    def search_data(self, table, where):
        x = self.db.cursor()
        sql = "SELECT * FROM %s WHERE %s" % (table, where)
        try:
            x.execute(sql)
            result = x.fetchall()
            if x.rowcount < 0:
                print("No Data")
            else:
                for data in result:
                    print(data)
        except:
            print("wrong condition")


if __name__ == '__main__':
    db = HlCrud("config.ini")
    option = ''
    tablename = ''
    where = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:t:w:")
    except getopt.GetoptError:
        print('hl-crud.py -s <crud type> -t <tablename> -w <where or data>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('hl-crud.py -s <crud type> -t <tablename> -w <where or data>')
            sys.exit()
        elif opt in ("-s"):
            option = arg
        elif opt in ("-t"):
            tablename = arg
        elif opt in ("-w"):
            where = arg
    if option == "insert":
        try:
            db.insert_data(tablename, where)
        except:
            print("Wrong data or table name")
    elif option == "delete":
        try:
            db.delete_data(tablename, where)
        except:
            print("Wrong delete condition")
    elif option == "show":
        try:
            db.show_data(tablename)
        except:
            print("Wrong table name")
    elif option == "search":
        try:
            db.search_data(tablename, where)
        except:
            print("Wrong data or table name")
