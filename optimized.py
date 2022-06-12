import time
import csv


actions_lite = [{"name": "Action-01", "price": 20, "profit": 5},
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


#  O(n*m)
def knap_sack(funds, actions, n):  # O(n*m)
    k = [[0 for column in range(funds + 1)] for row in range(n + 1)]
    for i in range(n + 1):
        for w in range(funds + 1):
            action = actions[i - 1]
            price = action["price"]
            profit = action["price"] * (action["profit"] * 0.01)
            k_n = k[i - 1]
            if i == 0 or w == 0:
                k[i][w] = 0
            elif price <= w:

                k[i][w] = max(profit + k_n[int(w - price)],
                              k_n[w])
            else:
                k[i][w] = k_n[w]
    # for think in K:
    #     print(think)
    return k[n][funds], k

# pour chaques actions: compare avec l'évaluation de l'action précédent,
# le profit maximum pour ce prix là.
# Si prix plus grand que monnaie: alors prix précédent est enregistré
# Si profit précédent est plus haut alors il est gardé.
# Sinon. Profit d'action actuel + profit gagné avec fonds restants
# (k_n[int(w - price)) est gardé


def items(i, j, k, actions, factor):  # O(n)
    global total_price
    if i == 0:
        return total_price
    if k[i][j] > k[i-1][j]:
        if len(actions) < 21:
            price = actions[i-1]["price"]
        else:
            price = actions[i - 1]["price"]/factor
        print(actions[i - 1]["name"], price)
        total_price += price
        return items(i-1, j-int(actions[i-1]["price"]), k, actions, factor)
    else:
        return items(i-1, j, k, actions, factor)


def algo_optimized(factor=1, csv_file_name=False, csv_is=True):  # O(n)
    global total_price
    total_price = 0
    if csv_is:
        with open(csv_file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            actions = []
            for row in reader:
                if float(row["price"]) > 0:
                    if float(row["profit"]) > 0:
                        row["profit"] = float(row["profit"]) * factor
                        row["price"] = float(row["price"]) * factor
                        actions.append(row)
            # print(actions[530: 540])
        funds = 500*factor
    else:
        actions = actions_lite
        funds = 500
    t = time.time()

    n = len(actions)
    total_profit, k = knap_sack(funds, actions, n)
    if funds == 500:
        print("total_price: ", items(n, funds, k, actions, factor))
        print("total_profit: ", total_profit)
    else:
        print("total_price: ", items(n, funds, k, actions, factor))
        print("total_profit: ", total_profit/(factor*factor))
    print("timer: ", time.time() - t)


total_price = 0
algo_optimized(factor=100, csv_file_name='dataset1_Python+P7.csv')
# best_profit = 198.x ?
algo_optimized(factor=100, csv_file_name='dataset2_Python+P7.csv')
# best_profit = ?
algo_optimized(csv_is=False)
