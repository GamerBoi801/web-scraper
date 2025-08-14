import yfinance as yf

ticker = 'AAPL'

data = yf.download(ticker, start='2020-01-01', end='2023-01-01')
data.to_csv(f'{ticker}_stock_data.csv')
print(f"Stock data for {ticker} has been downloaded and saved to {ticker}_stock_data.csv")
data.head()