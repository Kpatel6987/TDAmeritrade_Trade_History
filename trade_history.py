import sys
import json
import datetime

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
        "pl": 0,
        "commission": 0,
        "total_pl": 0,
        "legs": legs,
        "num_legs": len(legs)
    }


def build_leg_dictionary(order, base_order):
    return {
        "date": base_order[1],
        "spread": base_order[2],
        "side": order[3],
        "quantity": order[4],
        "position_effect": order[5],
        "expiration": order[7],
        "strike": order[8],
        "option_type": order[9],
        "price": order[10]
    }


def handle_two_legs(order, legs, lines, i):
    new_order = lines[i].split(",")
    legs.append(build_leg_dictionary(new_order, order))


def handle_four_legs(order, legs, lines, i):
    for x in range(1, 4):
        new_order = lines[i + x].split(",")
        legs.append(build_leg_dictionary(new_order, order))


def add_position(order, key, legs):
    if key in positions.keys():
        old_legs = positions[key]["legs"]
        legs += old_legs
        positions[key]["legs"] = legs
    else:
        value = build_position_dictionary(order, legs)
        positions[key] = value
    update_pl(order, key, legs)


def update_pl(order, key, legs):
    pl = 0.0
    commission = 0.0
    for x in legs:
        pl += (float(x["price"]) * float(x["quantity"]) * -1)
        commission += .015 * abs(float(x["quantity"]))
    positions[key]["total_pl"] = "{0:.2f}".format((pl - commission) * 100)
    positions[key]["pl"] = "{0:.2f}".format(pl * 100)
    positions[key]["commission"] = "{0:.2f}".format(commission * 100)


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
            # symbol
            key = order[6]
            legs = [build_leg_dictionary(order, order)]
            if order[2] == "VERTICAL":
                i += 1
                handle_two_legs(order, legs, lines, i)
            elif order[2] == "IRON CONDOR" or order[2] == "VERT ROLL":
                handle_four_legs(order, legs, lines, i)
                i += 3
            add_position(order, key, legs)
        i += 1


def main():
    file = open(sys.argv[1])
    lines = file.readlines()
    file.close()
    if not ("Account Statement for" in lines[0] and "TDA" in lines[0]):
        print("Sorry cannot parse this file")
        return
    pos = parse_file(lines)
    print(json.dumps(pos, indent=4))
    filename = "{}_trade_history.txt".format(datetime.datetime.now().strftime ("%m%d%Y"))
    with open(filename, "w") as out:
        json.dump(pos, out, indent=4)



if __name__ == "__main__":
    positions = {}
    main()