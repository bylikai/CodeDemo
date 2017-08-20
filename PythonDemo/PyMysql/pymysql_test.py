
import string
import pymysql
import pymysql.cursors
import matplotlib.pyplot as plt
from pandas import Series,DataFrame

import datetime
from datetime  import date
import time


def mysql_test(): 
    # connect mysql
    connection = pymysql.connect(
        "localhost",
        "username",
        "password",
        "dbname",
        "utf8")

    try:
        # cursor() 
        cursor  = connection.cursor()

        # executor
        cursor.execute("select version()")

        cursor.execute("show tables")

        # fetchone 
        data = cursor.fetchone()

        print ("Database version: %s " %data)

    finally:
        # close
        connection.close()


'''
class Market  for Trade
'''
class Market:
    # Initialize the Market
    def __init__(self, host, username, password, dbname):
        
        self.__host       = host
        self.__username   = username
        self.__password   = password
        self.__dbname     = dbname
        self._id = []
        self._webid = []
        self._coinid = []
        self._vtime = []
        self._vol = []
        self._high = []
        self._last = []
        self._low = []
        self._sell = []
        self._buy = []
        self._open = [] 
        self._stime= []


    # connection the database with __dbname
    def connection_database(self):
        
        self.__db = pymysql.connect( 
            self.__host, 
            self.__username, 
            self.__password, 
            self.__dbname )

        if self.__db is None:
            return False
        else:
            return True


    # get the records count 
    # return Number type
    def get_records_count( self, tbname ):
        
        if self.__db is None:
            return 0
        sql = "select count(id) from " + self.__dbname + "." + tbname
        cursor = self.__db.cursor()
        
        cursor.execute(sql)
        count = 0
        if( cursor.rowcount > 0 ):
            count = cursor._rows[0][0]
        
        cursor.close()
        return count


    def query_records(self, tbname, skip, limit ):
        
        sql = '''select id, vtime, webid, coinid, 
                    high, low, sell, buy, last, vol, open  
                from {db}.{tb} limit {skip}, {limit}'''.format(
            db = self.__dbname,
            tb = tbname,
            skip = skip,
            limit = limit
        )

        cursor = None
        try:
            cursor = self.__db.cursor()
            cursor.execute(sql)
            rowcount = cursor.rowcount;
            if( rowcount > 0 ):
                results = cursor.fetchall()
            
            cursor.close()
            return  True, rowcount, results

        except:
            print("Error : unable to fetch data")
            if cursor is not None :
                cursor.close()
            return False, 0, 0


    def process_data(self, results):
        if results is None:
            return False
        
        for row in results:
            [_id,   _vtime, _webid, _coinid, 
             _high, _low,   _sell,  _buy, 
             _last, _vol,   _open ] = tuple( row )

            '''print(_id,   _vtime, _webid, _coinid, 
             _high, _low,   _sell,  _buy, 
             _last, _vol,   _open)
             '''

            self._id.append(_id)
            self._vtime.append(_vtime)
            self._webid.append(_webid)
            self._coinid.append(_coinid)
            self._high.append(_high)
            self._low.append(_low)
            self._sell.append(_sell)
            self._buy.append(_buy)
            self._last.append(_last)
            self._vol.append(_vol)
            self._open.append(_open)
            self._stime.append( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(_vtime) ) )
            
        return True

    def show_data(self):
        #plt.scatter( self._vtime, self._buy, color='blue' )
        #stime = self._vtime
        stime = self._vtime
        plt.plot(stime, self._buy, color='blue', label='buy')
        plt.plot(stime, self._sell, color='red', label='sell')
        plt.plot(stime, self._last, color='green',label='last')

        plt.grid()

        plt.xlabel('time')

        plt.show()
            
    def close_database(self):
        try:
            print("close")
        finally:
            self.__db.close()



if __name__ == '__main__':
#    mysql_test()
    tbname = "t_market";
    obj = Market("localhost", "root", "root", "dbname")
    if obj.connection_database() is False:
        print("connect the database failed!")
        exit
    count = obj.get_records_count(tbname)
    
    if count>1000:
        count = 1000
  
    step = 20
    start = 0;
    while start<=count:
        status, rowcount, results = obj.query_records(tbname,start,step)
        if( (status is True) and (rowcount > 0) ):
            obj.process_data( results )
        else :
            print ("query records error")
            break

        start += rowcount
    obj.show_data()

    obj.close_database()

    print ("---------------------")