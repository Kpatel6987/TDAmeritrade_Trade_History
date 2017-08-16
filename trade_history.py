'''
,Exec Time,Spread,Side,Qty,Pos Effect,Symbol,Exp,Strike,Type,Price,Net Price,Order Type

,8/14/17 15:23:00,VERTICAL,SELL,-1,TO OPEN,NFLX,1 SEP 17,165,PUT,2.40,1.08,LMT

,,,BUY,+1,TO OPEN,NFLX,1 SEP 17,160,PUT,1.32,CREDIT,
'''

file = open("2017-08-15-AccountStatement.csv")
lines = file.readlines()
positions = {}
check = False
i = 0
while i < len(lines):
    if i > 2 and lines[i - 2].strip() == "Account Trade History":
        check = True
    if check and lines[i].strip() == "":
        break
    if check:
        data = lines[i].split(",")
        exec_time = data[1]
        spread = data[2]
        side = data[3]
        quantity = data[4]
        position_effect = data[5]
        symbol = data[6]
        expiration = data[7]
        strike = data[8]
        option_type = data[9]
        price = data[10]
        net_price = data[11]
        order_type = data[12]
        print(symbol)
        if spread == "VERTICAL":
            print(spread + " change---------------")
            i += 1
        elif spread == "IRON CONDOR" or spread == "VERT ROLL":
            i += 3
        #break
    i += 1

file.close()