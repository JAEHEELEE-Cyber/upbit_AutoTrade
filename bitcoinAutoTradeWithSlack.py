import time
import pyupbit
import datetime
import requests
import numpy as np
access = "hMUSORUTZ5clnvN38OPDkAivxUGrSlRnNpsr7OLb"          # 본인 값으로 변경
secret = "cNseT1xx8Wyx0bCVbcWc5rOhG5Jfb7O3c64PfiPk"   
myToken = "xoxb-2681758283601-2662431550918-EL2bwfXW5SG5PG1SoF6udMOS"

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=3)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

def get_ror(k):
    df = pyupbit.get_ohlcv("KRW-BTC",count=3)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,
                         1)

    ror = df['ror'].cumprod()[-2]
    #print(df['target'])
    #print(df['ror'])
    return ror

def get_bestk():
    bestror=0
    bestk=0
    for k in np.arange(0.1, 1.0, 0.1):
        ror = get_ror(k)
        #print("ror:",ror,"k:",k)
        if ror>bestror:
            bestror=ror
            bestk=k    
    #print("bestk: ",bestk)
    return bestk

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
# 시작 메세지 슬랙 전송
post_message(myToken,"#sw_develope", "autotrade start")

# bitcoin에 대한 변동폭 비율 bestk 값부터 구하기
k=get_bestk()

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", k)
            ma15 = get_ma15("KRW-BTC")
            current_price = get_current_price("KRW-BTC")
            #print(target_price,ma15)
            if target_price < current_price: #and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    #buy_result = upbit.buy_market_order("KRW-BTC", krw*0.9995)
                    post_message(myToken,"#sw_develope", "BTC buy : ")
                    #post_message(myToken,"#sw_develope", "BTC buy : " +str(buy_result))
        else:
            
            btc = get_balance("BTC")
            if btc > 0.00008:
                #sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                post_message(myToken,"#sw_develope", "BTC sell : ")
                #post_message(myToken,"#sw_develope", "BTC sell : " +str(sell_result))
        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(myToken,"#sw_develope", e)
        time.sleep(1)