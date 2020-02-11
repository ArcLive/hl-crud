#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error
import configparser
import getopt, sys
import json

class HlCrud:
    config = configparser.ConfigParser()

    def __init__(self, config_file):
        self.config.read(config_file)
        self.db = mysql.connector.connect(host=self.config["mysql"]["host"],
                                          user=self.config["mysql"]["user"],
                                          password=self.config["mysql"]["password"],
                                          database=self.config["mysql"]["database"],
                                          port=self.config["mysql"]["port"])
        self.create_tables()
    
    def create_tables(self):
        try:
            sql="""CREATE TABLE IF NOT EXISTS boards (
                BoardSN double DEFAULT NULL,
                CompName text,
                Type text,
                cModel text,
                DLinference_result text,
                directory text,
                ConfirmDefect text,
                MachineDefect text,
                Status text,
                image_name text,
                LightingCondition text,
                image_scantime text,
                BoardRESULT text
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
            x = self.db.cursor()
            x.execute(sql)
            self.db.commit()

            sql="""CREATE TABLE IF NOT EXISTS filenames (
                col1 text,
                col2 text,
                col3 text,
                col4 text,
                col5 text
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
            x = self.db.cursor()
            x.execute(sql)
            self.db.commit()
        except Error as err:
            print("Fail: {}".format(err))

    def insert(self, table, data):
        try:
            col = '\',\''.join(data.keys())
            col = col.replace("'", "`")
            sql = "INSERT INTO %s (`%s`) VALUES %s;" % (table, col, tuple(data.values()))
            print(sql)
            x = self.db.cursor()
            x.execute(sql)
            self.db.commit()
            print('Succefully inserted'.format(x.rowcount))
        except Error as err:
            print("Fail: {}".format(err))

    def show(self, table):
        try:
            x = self.db.cursor()
            sql = "select * from %s " % table
            x.execute(sql)
            rows = x.fetchall()
            for row in rows:
                print(row)
        except Error as err:
            print("Fail: {}".format(err))

    def update(self, table, data, where):
        try:
            col = ''
            for k, v in data.items():
                t = "`" + k + "` = " + "'" + v + "'"
                col += " ," + t if col else t
            sql = "UPDATE `%s` SET %s WHERE %s " % (table, col, where)
            x = self.db.cursor()
            x.execute(sql)
            self.db.commit()
        except Error as err:
            print("Fail: {}".format(err))

    def delete(self, table, where):
        try:
            sql = "DELETE FROM %s WHERE %s " % (table, where)
            x = self.db.cursor()
            x.execute(sql)
            self.db.commit()
        except:
            print("wrong query")

    def search(self, table, where):
        try:
            x = self.db.cursor()
            sql = "SELECT * FROM %s WHERE %s" % (table, where)
            x.execute(sql)
            result = x.fetchall()
            if x.rowcount < 0:
                print("No Data")
            else:
                for data in result:
                    print(data)
        except:
            print("wrong query")

    def __del__(self):
        self.db.close()

if __name__ == '__main__':
    db = HlCrud("config.ini")
    option = ''
    tablename = ''
    data = {}
    where = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:t:d:w:")
    except getopt.GetoptError:
        print('hl-crud.py -s [command] -t [tablename] -d [data] -w [where]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: hl-crud.py -s [command] -t [tablename] -d [data] -w [where]')
            print('Run CRUD commands on MySQL Database\n')
            print(' -s\t\t command name - insert/delete/show/search/update')
            print(' -t\t\t tablename - boards/filenames')
            print(' -d\t\t data - JSON format')
            print(' -w\t\t condition\n')
            sys.exit()
        elif opt in ("-s"):
            option = arg
        elif opt in ("-t"):
            tablename = arg
        elif opt in ("-d"):
            try:
                data = json.loads(arg)
            except:
                print("Exception: data is not JSON")
                sys.exit()
        elif opt in ("-w"):
            where = arg
    if option == "insert":
        db.insert(tablename, data)
    elif option == "delete":
        db.delete(tablename, where)
    elif option == "show":
        db.show(tablename)
    elif option == "search":
        db.search(tablename, where)
    elif option == "update":
        db.update(tablename, data, where)