
-- Create Stock Entity Table
-- @block
CREATE TABLE Stocks(
    StockID VARCHAR(5) PRIMARY KEY,
    SecurityName VARCHAR(100),
    ListingExchange CHAR NULL,
    MarketCategory CHAR NULL,
    ETF BOOLEAN
);


-- Create Price_Data Entity Table
-- @block
CREATE TABLE PriceData(
    StockID VARCHAR(5),
    TradeDate DATE,
    OpenPrice Decimal(10, 2) UNSIGNED,
    HighPrice Decimal(10, 2) UNSIGNED,
    LowPrice DECIMAL(10, 2) UNSIGNED,
    AdjClosePrice DECIMAL(10, 2) UNSIGNED,
    Volume INT UNSIGNED,
    PRIMARY KEY(StockID, TradeDate),
    FOREIGN KEY (StockID) REFERENCES Stocks(StockID)
)

