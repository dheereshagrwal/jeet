from finvizfinance.quote import finvizfinance
def get_finviz_data(ticker):
    shs_float = None
    inst_own = None
    short_float_percent = None
    insider_own = None
    atr = None
    try:
        stock = finvizfinance(ticker)
        ticker_fundament = stock.ticker_fundament()
        shs_float = ticker_fundament["Shs Float"]
        inst_own = ticker_fundament["Inst Own"]
        short_float_percent = ticker_fundament["Short Float / Ratio"]
        short_float_percent = short_float_percent.split("/")[0].strip()
        insider_own = ticker_fundament["Insider Own"]
        atr = ticker_fundament["ATR"]
    except:
        pass
    return shs_float, inst_own, short_float_percent, insider_own, atr
    

