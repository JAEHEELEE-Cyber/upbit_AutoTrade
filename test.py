import pyupbit

access = "hMUSORUTZ5clnvN38OPDkAivxUGrSlRnNpsr7OLb"          # 본인 값으로 변경
secret = "cNseT1xx8Wyx0bCVbcWc5rOhG5Jfb7O3c64PfiPk"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print("ADA: ")
print(upbit.get_balance("KRW-ADA"))     # KRW-XRP 조회
print("KRW: ")
print(upbit.get_balance("KRW"))         # 보유 현금 조회