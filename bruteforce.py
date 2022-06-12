from itertools import combinations

actions = [{"name": "Action-01", "price": 20, "profit": 5},
           {"name": "Action-02", "price": 30, "profit": 10},
           {"name": "Action-03", "price": 50, "profit": 15},
           {"name": "Action-04", "price": 70, "profit": 20},
           {"name": "Action-05", "price": 60, "profit": 17},
           {"name": "Action-06", "price": 80, "profit": 25},
           {"name": "Action-07", "price": 22, "profit": 7},
           {"name": "Action-08", "price": 26, "profit": 11},
           {"name": "Action-09", "price": 48, "profit": 13},
           {"name": "Action-10", "price": 34, "profit": 27},
           {"name": "Action-11", "price": 42, "profit": 17},
           {"name": "Action-12", "price": 110, "profit": 9},
           {"name": "Action-13", "price": 38, "profit": 23},
           {"name": "Action-14", "price": 14, "profit": 1},
           {"name": "Action-15", "price": 18, "profit": 3},
           {"name": "Action-16", "price": 8, "profit": 8},
           {"name": "Action-17", "price": 4, "profit": 12},
           {"name": "Action-18", "price": 10, "profit": 14},
           {"name": "Action-19", "price": 24, "profit": 21},
           {"name": "Action-20", "price": 114, "profit": 18}
           ]

funds = 500
dict_prices = {}
for action in actions:
    dict_prices[action["name"]] = action["price"]

all_combs = []
i = 1
valid_combinations = []
while i <= len(actions):
    for combination in combinations(dict_prices, i):
        total_price = 0
        combination_name = ''
        total_profit = 0
        for key in combination:
            price = dict_prices[key]
            profit = [act["profit"] for act in actions if act["name"] == key][
                0]
            total_price += price
            total_profit += price * (profit * 0.01)
            combination_name += key + '_'
            if total_price <= funds:
                combine_dict = {'name': combination_name,
                                'total_price': total_price,
                                'total_profit': total_profit}
                # print(combine_dict)
                valid_combinations.append(combine_dict)
    i += 1
print(type(valid_combinations), len(valid_combinations))
for thing in sorted(valid_combinations, key=lambda d: d['total_profit'],
                    reverse=True)[0:10]:
    print(thing)

bruteforce_solution = {'name': 'Action-04_Action-05_Action-06_Action-08_'
                               'Action-10_Action-11_Action-13_Action-18_'
                               'Action-19_Action-20_',
                       'total_price': 498, 'total_profit': 99.08000000000001}
