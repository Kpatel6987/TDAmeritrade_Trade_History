'''
,Exec Time,Spread,Side,Qty,Pos Effect,Symbol,Exp,Strike,Type,Price,Net Price,Order Type

,8/14/17 15:23:00,VERTICAL,SELL,-1,TO OPEN,NFLX,1 SEP 17,165,PUT,2.40,1.08,LMT

,,,BUY,+1,TO OPEN,NFLX,1 SEP 17,160,PUT,1.32,CREDIT,
'''

'''
    exec_time = order[1]
    spread = order[2]
    side = order[3]
    quantity = order[4]
    position_effect = order[5]
    symbol = order[6]
    expiration = order[7]
    strike = order[8]
    option_type = order[9]
    price = order[10]
    net_price = order[11]
    order_type = order[12]
'''

def build_position_dictionary(order, legs):
    return {
        "spread": order[2],
        "side": order[3],
        "quantity": order[4],
        "net_price": order[11],
        "legs": legs
    }

def build_leg_dictionary(order):
    return {
        "quantity": order[4],
        "expiration": order[7],
        "side": order[3],
        "strike": order[8],
        "price": order[10],
        "option_type": order[9]
    }


def parse_file(lines):
    check = False
    i = 0
    while i < len(lines):
        if i > 2 and lines[i - 2].strip() == "Account Trade History":
            check = True
        if check and lines[i].strip() == "":
            return positions
        if check:
            order = lines[i].split(",")
            key = (order[6], order[2], order[7])
            # position effect
            if order[5] == "TO CLOSE" and key in positions.keys():
                print(positions[key])
            else:
                legs = [build_leg_dictionary(order)]
                # spread
                if order[2] == "VERTICAL":
                    i += 1
                    new_order = lines[i].split(",")
                    # check if debit or credit
                    if new_order[11] == "DEBIT":
                        order[11] = str(float(order[11]) * -1)
                    legs.append(build_leg_dictionary(new_order))
                elif order[2] == "IRON CONDOR" or order[2] == "VERT ROLL":
                    for x in range(1, 4):
                        new_order = lines[i + x].split(",")
                        if x == 1 and new_order[11] == "DEBIT":
                            order[11] = str(float(order[11]) * -1)
                        # position effect
                        if new_order[5] == "TO CLOSE" and key in positions.keys():
                            # net price
                            positions[key]["net_price"] =
                                str(float(positions[key]["net_price"]) + float(order[11]))
                        legs.append(build_leg_dictionary(new_order))
                    i += 3
                value = build_position_dictionary(order, legs)
                positions[key] = value
        i += 1

def main():
    file = open("2017-08-15-AccountStatement.csv")
    lines = file.readlines()
    file.close()
    parse_file(lines)
    #print(parse_file(lines))

if __name__ == "__main__":
    positions = {}
    main()