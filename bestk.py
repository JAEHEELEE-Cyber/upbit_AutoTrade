import pyupbit
import numpy as np

def get_ror(k):
    df = pyupbit.get_ohlcv("KRW-BTC",count=7)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror

def get_bestk():
    bestror=0
    bestk=0
    for k in np.arange(0.1, 1.0, 0.1):
        ror = get_ror(k)
        if ror>bestror:
            bestror=ror
            bestk=k    
    return bestk

k=get_bestk()
print("%.1f" % (k))

