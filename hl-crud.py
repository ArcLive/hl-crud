import mysql.connector
import configparser


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
        whr = ''
        for k, v in where.items():
            temp = "`" + k + "` = " + "'" + v + "'"
            whr += " ," + temp if whr else temp
        sql = "DELETE FROM `%s` WHERE %s " % (table, whr)
        x = self.db.cursor()
        x.execute(sql)
        self.db.commit()
        return

    def search_data(self, table, where):
        x = self.db.cursor()
        sql = "SELECT FROM `%s` WHERE %s" % (table, where)
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

    db.show_data("data")
