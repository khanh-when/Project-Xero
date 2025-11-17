import mariadb
from dataparsers.ticker_data_parser import stock_data
from dataparsers.stock_etf_parser import price_data


def connection(db_name):
    '''Establish Database Connection to MariaDB'''

    try:
        return mariadb.connect(
                user = 'root',
                password = '2123<>69',
                host = 'localhost',
                port = 3306,
                database = db_name
            )
    except mariadb.Error as e:
        print(f"Error: MariaDB Connection {e}")
        raise mariadb.Error


def main():

    stocksData = stock_data()
    pricesData = price_data('archive/stocks/*.csv')
    
    print(stocksData['AMD'])
    print(pricesData['AMD']['2020-04-01'])

    try:
        conn = connection('stock_market')

    except Exception as e:
        print(f'Error: {e}')

    finally:
        conn.close()



if __name__ == '__main__':
    main()

