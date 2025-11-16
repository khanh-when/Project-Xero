import csv
import glob
from icecream import ic as print

def stock_price_data() -> dict[dict]:
    price_data_stock = {}
    file_path = 'archive/stocks/*.csv'
    all_files = glob.glob(file_path, recursive=True)


    for file in all_files:
        with open(file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader) # skip header

            ticker = file.split('/')[-1].strip('.csv') # parse for filename
            price_data_stock[ticker] = {}

            for line in csv_reader:
                date = line[0]

                try:
                    price_data_stock[ticker][date] = {
                                            'Date': date,
                                            'Open': float(line[1]),
                                            'High': float(line[2]),
                                            'low': float(line[3]),
                                            'AdjClose': float(line[5]),
                                            'Volume': float(line[6]),       
                                        }  
                except ValueError:
                    continue

    return price_data_stock

def main():
    data = stock_price_data()
    print(len(data))

if __name__ == '__main__':
    main()








