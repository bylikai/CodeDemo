
import string
import pymysql
import pymysql.cursors
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

import datetime
from datetime  import date
import time
import  numpy  as np
from scipy import stats
from sklearn.linear_model import BayesianRidge, LinearRegression

# import our configure of the database
from database_config import func_database_config


print( func_database_config() )

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

# -----------------------------------------------------------------------
# Market class

class Market:
    """ Market class, is the bitcoin or letcoin market price

    Parameters
    ----------
    data : numpy ndarray (structured or homogeneous), dict, or DataFrame
        Dict can contain Series, arrays, constants, or list-like objects
    index : Index or array-like
        Index to use for resulting frame. Will default to np.arange(n) if
        no indexing information part of input data and no index provided
    columns : Index or array-like
        Column labels to use for resulting frame. Will default to
        np.arange(n) if no column labels are provided
    dtype : dtype, default None
        Data type to force, otherwise infer
    copy : boolean, default False
        Copy data from inputs. Only affects DataFrame / 2d ndarray input

    Examples
    --------
    >>> d = {'col1': ts1, 'col2': ts2}
    >>> df = DataFrame(data=d, index=index)
    >>> df2 = DataFrame(np.random.randn(10, 5))
    >>> df3 = DataFrame(np.random.randn(10, 5),
    ...                 columns=['a', 'b', 'c', 'd', 'e'])

    See also
    --------
    DataFrame.from_records : constructor from tuples, also record arrays
    DataFrame.from_dict : from dicts of Series, arrays, or dicts
    DataFrame.from_items : from sequence of (key, value) pairs
    pandas.read_csv, pandas.read_table, pandas.read_clipboard
    """

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
        self._X = []
        self._Y = []
        self._X1 = DataFrame( columns=["id", "vtime", "webid", "coinid", "high", "low", "buy", "sell", "open", "last" ],
            dtype=float )


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
        # query record for sql
        sql = ('''select id, vtime, webid, coinid, 
                    high, low, sell, buy, last, vol, open  
                from {db}.{tb} 
                where webid = 1 and coinid = 1
                order by id asc
                limit {skip}, {limit}''').format(
            db = self.__dbname,
            tb = tbname,
            skip = skip,
            limit = limit
        )

        cursor = None
        try:
            cursor = self.__db.cursor()
            cursor.execute(sql)
            rowcount = cursor.rowcount
            if(rowcount > 0):
                results = cursor.fetchall()
            
            cursor.close()
            return  True, rowcount, results

        except:
            print("Error : unable to fetch data")
            if cursor is not None :
                cursor.close()
            return False, 0, 0

    def query_records_by_starttime(self, tbname, startTime, timeSpan ):
        """
        query record for sql for startTime and timeSpan
        """
        # Step 1  constructor the condition 
        sql = ('''select id, vtime, webid, coinid, 
                    high, low, sell, buy, last, vol, open  
                from {db}.{tb} 
                where webid = 1 and coinid = 1 and vtime >= {startTime} and vTime < {endTime}
                order by id asc ''').format(
            db = self.__dbname,
            tb = tbname,
            startTime = startTime,
            endTime = startTime+timeSpan
        )

        
        cursor = None
        try:
            # Step 2 execute the sql 
            cursor = self.__db.cursor()
            cursor.execute(sql)
            rowcount = cursor.rowcount
            results  = None

            # Step 3 parse the results 
            if(rowcount > 0):
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
            
            # Create record by _vtime,..., and Add record to _X
            # And add _last into _Y
            record = np.arange(3)
            record[0] = _sell
            record[1] = _buy
            record[2] = _vol
            #record[3] = _high
            #record[4] = _low
           
            #print(record)

            self._X.append( record )
            self._Y.append( _last )

            #self._X1.append("id"=_id, "vtime"=_vtime, "webid"=_webid, "coinid"=_coinid, "high"=_high, "low"=_low, "buy"=_buy,"sell"=_sell, "open"=_open, "last"=_last)

            self._stime.append( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(_vtime) ) )
            
        return True

    def process_data_2( self ):
        '''
        process data for diff , logdiff, volatility(波动率)
        '''
        # diff log
        logdiff = np.diff( np.log(self._last) )
        #print( logdiff )

        # volatility
        volatility_last = np.std(logdiff) / np.mean( logdiff )
        #print( volatility_last )

        volatility_last = volatility_last / np.sqrt( 1./ logdiff.size )
        #print( volatility_last )


    def process_data_for_weighted_average(self, results):
        """ 
        calculate the btc price average from results 
        """
        if results is None:
            return False

        vtime=[]
        buy = []
        vol = []

        # parse the buy price and volume
        for row in results:
            [_id,   _vtime, _webid, _coinid, 
             _high, _low,   _sell,  _buy, 
             _last, _vol,   _open ] = tuple( row )
        
            vtime.append(_vtime)
            buy.append(_buy)
            vol.append(_vol)

        return True, vtime, buy, vol


    def show_data(self):
        #plt.scatter( self._vtime, self._buy, color='blue' )
        #stime = self._vtime
        '''
        # show the curve of buy , sell, last
        stime = self._vtime
        plt.plot(stime, self._buy, color='blue', label='buy')
        plt.plot(stime, self._sell, color='red', label='sell')
        plt.plot(stime, self._last, color='green',label='last')

        plt.grid()

        plt.xlabel('time')

        plt.show()
        '''
        x = self._vtime

        plt.subplot(321)
        plt.plot(x, self._last, label="lastprice", color="#054E9F", linestyle=':')

        plt.subplot(322)
        plt.plot(x, self._buy,  label="buy price",  color="#FF0000", linestyle='-')

        plt.subplot(323)
        plt.plot(x, self._sell, label="sell price", color="green",   linestyle='-')

        plt.subplot(324)
        plt.plot(x, self._vol,  label="volume",     color="#B22222",  linestyle='-')

        # show the curve with Bayesian
        # print X, Y
        #print(self._X)
        #print(self._Y)

        clf = BayesianRidge(
            n_iter=300, 
            tol=1.e-3, 
            alpha_1=1.e-6, 
            alpha_2=1.e-6, 
            lambda_1=1.e-6, 
            lambda_2=1.e-6, 
            compute_score=True, 
            fit_intercept=True, 
            normalize=False, 
            copy_X=True, 
            verbose=False)
            
        clf.fit(self._X, self._Y)

        plt.subplot(325)
        plt.plot(clf.coef_, color='lightgreen', linewidth=1, label="Bayesian Ridge estimate")
        
        #plt.title("matploylib.pyplot")

        plt.show()
        

        '''
        # show the curve with 
        clf = BayesianRidge(compute_score=True)
        clf.fit(self._vtime, self._X)

        plt.plot(clf.coef_, color='lightgreen', linewidth=1, label="Bayesian Ridge estimate")
        
        plt.show()
        '''

    def minmax(self):
        """
        Calculate the max and min for the buy/sell price
        """
        max_sell = np.max( self._sell )
        min_sell = np.min( self._sell )
        avg_sell = np.average( self._sell )
        avg_w_sell = np.average( self._sell, weights=self._vol)

        max_buy = np.max( self._buy )
        min_buy = np.min( self._buy )
        avg_buy = np.average( self._buy)
        avg_w_buy = np.average( self._buy, weights=self._vol )

        print( ("Sell, max: {0}, min:{1}, average: {2}, weights average:{3}")
            .format( max_sell, min_sell, avg_sell, avg_w_sell  ) )

        print( ("Buy, max: {0}, min:{1}, average: {2}, weights average:{3}")
            .format( max_buy, min_buy, avg_buy, avg_w_buy  ) )
        
        

            
    def close_database(self):
        try:
            print("close")
        finally:
            self.__db.close()

def func_db_test():
    """
    predict the price of the btc with Bayesian Regularation
    """
    tbname = "t_market"
    host,username, password, dbname = func_database_config()
    obj = Market(host, username, password, dbname)

    if obj.connection_database() is False:
        print("connect the database failed!")
        exit
        
    count = obj.get_records_count(tbname)
    
    if count>1000:
        count = 1000
  
    step = 500
    start = 0
    while start<=count:
        status, rowcount, results = obj.query_records(tbname,start,step)
        if( (status is True) and (rowcount > 0) ):
            obj.process_data( results )
        else :
            print ("query records error")
            break

        start += rowcount

    # process_data_2
    obj.process_data_2()

    obj.minmax()

    obj.show_data()

    obj.close_database()


def func_weighted_average( results ) :
    """ Calculation the weighted average price
    """



if __name__ == '__main__':
    """ Main function for the t_market

    startTime 1498838400 (2017-07-01 00:00:00)
    endTime   1504022400 (2017-08-30 00:00:00)
    timeSpan  10

    =========================================
    There are three segment : 
    first   as training the algorithm
    second  as predict  the btc price
    third   as estimate the algorithm
    """
    
    # connnect the database 
    host,username, password, dbname = func_database_config()

    tbname = "t_market"
    obj = Market(host, username, password, dbname)

    if obj.connection_database() is False:
        print("connect the database failed!")
        exit

    count = obj.get_records_count(tbname)

    
    # Reset the condition
    # startTime = 1498838400
    startTime = 1496935222
    endTime   = 1502563797

    endTime1  = startTime + ( endTime - startTime )/3
    endTime2  = endTime1  + ( endTime - startTime )/3
    endTime3  = endTime

    timeSpan  = 1000
    calTiems  = 0

    '''
    Bayesian Regularation 
    '''
    X = []
    Y1 = []
    Y2 = []

    countNumber = 0
    currentTime = time.time()
    indexTime = startTime
    while indexTime <= endTime1 :
        """
        iterator the time and get the results
        and calculate the Weighted Average Price
        and count the times
        """
        # Step1 get the records
        status , rowcount, results = obj.query_records_by_starttime( tbname, indexTime, timeSpan )
        if (status is True) and (rowcount > 0):
            # calculate the weighted avarage price of btc
            status, vtime, buy, vol = obj.process_data_for_weighted_average( results )
            # print( buy )
            # buy is an array 
            X.append( vtime[rowcount-1] )  # store the unix timestamp
            y1 = np.average( buy )
            y2 = np.average( buy, weights=vol )
            Y1.append(y1)
            Y2.append(y2)
        else :
            # print("There is no more data!")
            pass

        # Step2 iterator the index timeSpan
        indexTime += timeSpan
        calTiems += 1
        countNumber += rowcount
        print( "countNumber: {0},  Time: {1}".format( countNumber, time.time() ) )
    
    print( "Process Time : {0}".format( time.time() - currentTime ) )

    # plot the data
    plt.subplot(211)
    plt.plot( X, Y1, 'g')
    plt.title("BTC AVERAGE PRICE")

    plt.subplot(212)
    plt.plot( X, Y2, 'b')
    plt.title("BTC WEIGHTED PRICE")

    '''
    Predict the price for X
    
    =============================================
    X = w0 + w1*X1 + w2*X2 + w3*X3 + w4*r
    
    where  
    w = (w0, w1, w2, w3, w4) are learnt parameters.
    Sj, 1 ≤ j ≤ 3 are collected; and how w is learnt.
    '''
    #reg = BayesianRidge()
    #reg.fit(X, Y1)
    #plt.plot( reg.coef_ )

    obj.close_database()

    plt.show()