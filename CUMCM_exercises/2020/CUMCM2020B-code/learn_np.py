import numpy as np

weather = ["高温", "高温", "晴朗", "沙暴", "晴朗",
           "高温", "沙暴", "晴朗", "高温", "高温",
           "沙暴", "高温", "晴朗", "高温", "高温",
           "高温", "沙暴", "沙暴", "高温", "高温",
           "晴朗", "晴朗", "高温", "晴朗", "沙暴",
           "高温", "晴朗", "晴朗", "高温", "高温"
           ]

base_consume_water = [5, 8, 10]
base_consume_food = [7, 6, 10]
base_water_price = 5
base_water_weight = 3
base_food_price = 10
base_food_weight = 2
carry_limit = 1200
init_money = 10000
base_income = 1000

Map = []


class Node:
    def __init__(self, id, state, nodes):
        self.id = id
        self.state = state
        self.neibor = []
        for i in nodes:
            self.neibor.append(i)


# 这个函数用于建立地图
def build_map():
    fp = open("Map1.txt", 'r')  # 根据所求地图修改路径
    node_id = 1
    for i in fp:
        if i is not None:
            i = i.split()
            temp_state = i[0]
            temp_list = []
            for j in range(1, len(i)):
                temp_list.append(int(i[j]))
            temp_node = Node(node_id, temp_state, temp_list)
            Map.append(temp_node)
            node_id += 1


build_map()


def get_weather(i):
    if i == "高温":
        return 1
    if i == "晴朗":
        return 0
    else:
        return 2


def check(i, j):
    if 3 * i + 2 * j > 1200 or 5 * i + 10 * j > 10000:
        return False
    else:
        return True


init_food = 0
init_water = 0

# log 记录
log_list = {}


def dp_main():
    dp = np.full((30, 30, 600, 600), -1 * np.inf)

    global init_food
    global init_water
    cur_day = 0

    # 起点购买物资
    for init_food in range(0, 600):
        init_water = (init_money - base_food_price * init_food) // base_water_price
        if check(init_food, init_water):
            dp[0][1][init_food][init_water] = init_money - base_consume_food[get_weather(cur_day)] * init_food - base_consume_water[
                get_weather(cur_day)] * init_water
            print(dp[0, 1, init_food, init_water], init_water, init_food)  # just here show init_money. but i don;t know the contain in the dp array

    for cur_day in range(0, 29):
        for cur_point in range(1, 27):
            # 移动
            for cur_point_new in Map[cur_point].neibor:
                cur_food = init_food - 2 * base_consume_food[get_weather(cur_day)]
                cur_water = init_water - 2 * base_consume_water[get_weather(cur_day)]
                dp[cur_day + 1, cur_point_new, cur_food, cur_water] = dp[cur_day, cur_point, cur_food, cur_water]
                # print(dp[0, 1, init_food, init_water])
                # print(dp[cur_day + 1, cur_point_new, food - 2 * base_consume_water[get_weather(cur_day)], water - 2 *
                #          base_consume_food[
                #              get_weather(cur_day)]])


dp_main()
