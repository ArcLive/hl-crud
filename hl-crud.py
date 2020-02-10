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
    data = {"BoardSN": 1.61, "CompName": "AAA", "Type": "032-1113-000HF", "cModel": "690-6G189-0600-305RH1_BOT",
            "DLinference_result": "PASS_Hig_0.97",
            "directory": "TEST_690-6G189-0600-305RH1_1614919000211_AOI_20191217042523", "ConfirmDefect": "PASS",
            "MachineDefect": "PASS", "Status": "PASS",
            "image_name": "690-6G189-0600-305RH1_BOT~032-1113-000HF~C1002_1~1614919000211_	SolderLight.jpg_LowAngleLight.jpg_UniformLight.jpg_WhiteLight.jpg",
            "LightingCondition": "ss", "image_scantime": "33", "BoardRESULT": "sfs"}
    db.show_data("data")
    db.insert_data("data", data)
    db.search_data("data", "CompName='AAA'")
    db.delete_data("data", "CompName='AAA'")
