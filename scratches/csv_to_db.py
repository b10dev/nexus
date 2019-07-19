'''
This snippit takes the csv file and parses it to a
db named 'csv.db'.  that db file is then put into the external_files
folder.
With that db, we can iterate thru the data with sql
'''
import csv, sqlite3

con = sqlite3.connect("csv.db")
print("db created")
cur = con.cursor()
print("cursor init")
cur.execute("""CREATE TABLE t (STATEMENT_ID, STATEMENT_DATE,
            DRIVER_ID, DRIVER_NAME,
             ADDRESS_1, ADDRESS_2,
            CITY, PROVINCE,
             POSTAL_CODE, PMT_STATE,
             CURRENCY_CODE, LEG_DATE,
             PUNIT, DETAIL_LINE_ID,
             BILL_NUMBER, PAY_CODE,
            PAY_DESCRIPTION, LEG_FROM_ZONE_DESC,
             LEG_TO_ZONE_DESC,
            FB_TOTAL_CHARGES, DED_RATE,
             TOTAL_PAY_AMT, ORIG_STMT,
            LOADED_MILES2);""")
print("table created")

with open('csvfile.csv', 'r') as fin:
    print("opened")
    dr = csv.DictReader(fin)
    print("csv read")
    to_db = [(i['STATEMENT_ID'], i['STATEMENT_DATE'],
              i['DRIVER_ID'], i['DRIVER_NAME'],
              i['ADDRESS_1'], i['ADDRESS_2'],
              i['CITY'], i['PROVINCE'],
              i['POSTAL_CODE'], i['PMT_STATE'],
              i['CURRENCY_CODE'], i['LEG_DATE'],
              i['PUNIT'], i['DETAIL_LINE_ID'],
              i['BILL_NUMBER'], i['PAY_CODE'],
              i['PAY_DESCRIPTION'], i['LEG_FROM_ZONE_DESC'],
              i['LEG_TO_ZONE_DESC'],
              i['FB_TOTAL_CHARGES'], i['DED_RATE'],
              i['TOTAL_PAY_AMT'], i['ORIG_STMT'],
              i['LOADED_MILES2'])
             for i in dr]
print("db iterated")
cur.executemany("INSERT INTO t (STATEMENT_ID, STATEMENT_DATE,"
                "DRIVER_ID, DRIVER_NAME,"
                " ADDRESS_1, ADDRESS_2,"
                "CITY, PROVINCE,"
                " POSTAL_CODE, PMT_STATE,"
                " CURRENCY_CODE, LEG_DATE,"
                " PUNIT, DETAIL_LINE_ID,"
                " BILL_NUMBER, PAY_CODE,"
                "PAY_DESCRIPTION, LEG_FROM_ZONE_DESC,"
                " LEG_TO_ZONE_DESC,"
                "FB_TOTAL_CHARGES, DED_RATE,"
                " TOTAL_PAY_AMT, ORIG_STMT,"
                "LOADED_MILES2) VALUES (?, ?, ?, ?, ?, ?, ?,"
                "?, ?, ?, ?, ?, ?, ?"
                ", ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()
