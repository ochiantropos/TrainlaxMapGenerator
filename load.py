from pprint import pprint
from queue import Queue
from pandas import DataFrame

import os


def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    start = []
    end = []
    data_frame_data_list = []
    temp_element = []
    index_of_map = 0
    with open(os.path.join(BASE_DIR, "name.txt"), 'r') as name:
        index_of_map = int(name.read())

    index_of_map += 1

    with open(os.path.join(BASE_DIR, "name.txt"), 'w') as name:
        name.write(f"{index_of_map}")

    rail_rout_map = {
        "1 0": ["left", "bottom"],
        "1 90": ["left", "top"],
        "1 180": ["top", "right"],
        "1 270": ["bottom", "right"],

        "0 0": ["left", "right"],
        "0 90": ["bottom", "top"],

        "3 0": ["top", "bottom", "rigth"],
        "3 90": ["right", "left", "top"],
        "3 180": ["top", "bottom", "left"],
        "3 270": ["bottom", "left", "right"],

        "4 0": ["top", "bottom", "rigth"],
        "4 90": ["right", "left", "top"],
        "4 180": ["top", "bottom", "left"],
        "4 270": ["bottom", "left", "right"],

        "2 0": ["top", "left", "bottom", "right"],
        "2 90": ["top", "left", "bottom", "right"],
        "2 180": ["top", "left", "bottom", "right"],
        "2 270": ["top", "left", "bottom", "right"]
    }
    a = {
        "1": [0, 1, None, 0, None, 0, 90, 0],
        "2": [0, 1, None, 0, None, 0, 180, 0],
        "3": [0, 1, None, 0, None, 0, 270, 0],
        "4": [0, 1, None, 0, None, 0, 0, 0],

        "5": [0, 3, None, 0, None, 0, 180, 0],
        "6": [0, 3, None, 0, None, 0, 90, 0],
        "7": [0, 3, None, 0, None, 0, 0, 0],
        "8": [0, 3, None, 0, None, 0, 270, 0],

        "9": [0, 4, None, 0, None, 0, 180, 0],
        "10": [0, 4, None, 0, None, 0, 90, 0],
        "11": [0, 4, None, 0, None, 0, 0, 0],
        "12": [0, 4, None, 0, None, 0, 270, 0],

        "13": [0, 2, None, 0, None, 0, 0, 0],

        "14": [0, 0, None, 0, None, 0, 90, 0],
        "15": [0, 0, None, 0, None, 0, 0, 0],

        "20": [0, 20, None, 0, None, 0, 90, 0],
        "21": [0, 21, None, 0, None, 0, 90, 0],
        "22": [0, 22, None, 0, None, 0, 0, 0],
        "23": [0, 23, None, 0, None, 0, 0, 0]
    }

    class Graph:
        # Constructor
        def __init__(self, num_of_nodes, directed=True):
            self.m_num_of_nodes = num_of_nodes
            self.m_nodes = range(self.m_num_of_nodes)

            # Directed or Undirected
            self.m_directed = directed

            # Graph representation - Adjacency list
            # We use a dictionary to implement an adjacency list
            self.m_adj_list = {node: set() for node in self.m_nodes}

            # Add edge to the graph

        def add_edge(self, node1, node2, weight=1):
            self.m_adj_list[node1].add((node2, weight))

            if not self.m_directed:
                self.m_adj_list[node2].add((node1, weight))

        # Print the graph representation
        def print_adj_list(self):
            for key in self.m_adj_list.keys():
                print("node", key, ": ", self.m_adj_list[key])

        def dfs(self, start, target, path=[], visited=set()):
            path.append(start)
            visited.add(start)
            if start == target:
                return path
            for (neighbour, weight) in self.m_adj_list[start]:
                if neighbour not in visited:
                    result = self.dfs(neighbour, target, path, visited)
                    if result is not None:
                        return result
            path.pop()
            return None

        def bfs(self, start_node, target_node):
            # Set of visited nodes to prevent loops
            visited = set()
            queue = Queue()

            # Add the start_node to the queue and visited list
            queue.put(start_node)
            visited.add(start_node)

            # start_node has not parents
            parent = dict()
            parent[start_node] = None

            # Perform step 3
            path_found = False
            while not queue.empty():
                current_node = queue.get()
                if current_node == target_node:
                    path_found = True
                    break

                for (next_node, weight) in self.m_adj_list[current_node]:
                    if next_node not in visited:
                        queue.put(next_node)
                        parent[next_node] = current_node
                        visited.add(next_node)

            # Path reconstruction
            path = []
            if path_found:
                path.append(target_node)
                while parent[target_node] is not None:
                    path.append(parent[target_node])
                    target_node = parent[target_node]
                path.reverse()
            return path

    def run():
        data_of_points = ""
        dt = os.path.join(BASE_DIR, "main")
        with open(os.path.join(dt, "start_end_points_temp.txt"), "r") as points:
            data_of_points = points.read()
            data_of_points = data_of_points.split("\n")
            _start = data_of_points[0][1:-1].split(",")
            _end = data_of_points[1][1:-1].split(",")
            if len(data_of_points) >= 4:
                _second_start = data_of_points[2][1:-1].split(",")
                _second_end = data_of_points[3][1:-1].split(",")

            print(f"(start [0]: {_start[1]} {_start[-1]}) (end [0]: {_end[1]} {_end[-1]})")

            if len(data_of_points) >= 4:
                print(f"(start [1]: {_second_start[1]} {_second_start[-1]}) (end [1]: {_second_end[1]} {_second_end[-1]})")

            if len(data_of_points) >= 4:
                return _start, _end, _second_start, _second_end, 2
            else:
                return _start, _end, [None, None], [None, None], 1


    # wcf_type : [raill_type, (rotation vector3)]

    def _get_all_rail():
        data = ""
        dt = os.path.join(BASE_DIR, "main")
        try:
            with open(os.path.join(dt, "temp.txt"), "r") as temp:
                data = temp.read()
            data = [item[1:-1].split(",") for item in data.split('\n')]

        except:
            print(os.path.join(dt, "temp.txt"))

        return data[:-1]

    def _is_raill_exist(rail_x, rail_y, _rails_data: list, vector):
        for obj in _rails_data:
            # pprint(f"obj : {obj[2]} {obj[4]} == rail: {rail_x} {rail_y}")
            if int(obj[2]) == int(rail_x) and int(obj[4]) == int(rail_y):
                return True, obj
            else:
                continue
        return False, []

    def get_all_adjacent_rails(value_in__in_roud_map: list, self_position_x: int, self_posotion_z: int,_data_frame_data_list):

        adjacent_rails = []
        adjacent_rail = [None, None]

        for _vector_of_displacement in value_in__in_roud_map:

            if _vector_of_displacement == "left":
                adjacent_rail[0] = int(self_position_x)
                adjacent_rail[1] = int(self_posotion_z) - 4

            elif _vector_of_displacement == "right":
                adjacent_rail[0] = int(self_position_x)
                adjacent_rail[1] = int(self_posotion_z) + 4

            elif _vector_of_displacement == "top":
                adjacent_rail[0] = int(self_position_x) + 4
                adjacent_rail[1] = int(self_posotion_z)

            elif _vector_of_displacement == "bottom":

                adjacent_rail[0] = int(self_position_x) - 4
                adjacent_rail[1] = int(self_posotion_z)

            ex, request = _is_raill_exist(adjacent_rail[0], adjacent_rail[1], _data_frame_data_list,
                                          _vector_of_displacement)
            if ex:
                adjacent_rails.append(request)
            else:
                continue

        return adjacent_rails

    def _point_in_massive(p: list, mass: list):
        for i in mass:
            if i[0] == p[0] and i[1] == p[1]:
                return True
        return False

    def get_all_duo_of_path_way(_data):
        all_way = []

        for _rail in _data:
            _key_in_roud_map = f"{_rail[1]} {_rail[-2]}"

            _adj = get_all_adjacent_rails(rail_rout_map[_key_in_roud_map], _rail[2], _rail[4], _data)
            for _adj_element in _adj:
                if not _point_in_massive(_adj_element, all_way):
                    all_way.append([_rail[0], _adj_element[0]])

        return all_way

    start, end, second_start, second_end, count_of_path = run()

    Data = _get_all_rail()

    '''data_frame_data_list forming'''
    for index, rail_hashed_item in enumerate(Data):
        temp_element = [i for i in a[rail_hashed_item[0]]]
        temp_element[0] = index
        temp_element[2] = rail_hashed_item[1]
        temp_element[4] = rail_hashed_item[-1]
        data_frame_data_list.append(temp_element)

    start_index = None
    end_index = None
    second_start_index = None
    second_end_index = None

    for frame_item in data_frame_data_list:
        if frame_item[2] == start[1] and frame_item[4] == start[-1]:
            start_index = frame_item[0]

        if frame_item[2] == end[1] and frame_item[4] == end[-1]:
            end_index = frame_item[0]

        if count_of_path == 2:
            if frame_item[2] == second_start[1] and frame_item[4] == second_start[-1]:
                second_start_index = frame_item[0]

            if frame_item[2] == second_end[1] and frame_item[4] == second_end[-1]:
                second_end_index = frame_item[0]

    def path_of_stat_raill(data: list, rail: list):
        way = []
        if rail[-2] == 90:
            way = ["top", "bottom"]

        else:
            way = ["left", "right"]

        adjacent_rail = [None, None]
        adjacent_rails = []
        vector = ""

        for _vector_of_displacement in way:
            if _vector_of_displacement == "left":
                adjacent_rail[0] = int(rail[2])
                adjacent_rail[1] = int(rail[4]) - 4

            elif _vector_of_displacement == "right":
                adjacent_rail[0] = int(rail[2])
                adjacent_rail[1] = int(rail[4]) + 4

            elif _vector_of_displacement == "top":
                adjacent_rail[0] = int(rail[2]) + 4
                adjacent_rail[1] = int(rail[4])

            elif _vector_of_displacement == "bottom":

                adjacent_rail[0] = int(rail[2]) - 4
                adjacent_rail[1] = int(rail[4])

            ex, request = _is_raill_exist(adjacent_rail[0], adjacent_rail[1], data,
                                          _vector_of_displacement)

            if not ex:
                vector = _vector_of_displacement

        temp1 = [None, None, None, None, None, None, None, None]
        temp2 = [None, None, None, None, None, None, None, None]
        temp3 = [None, None, None, None, None, None, None, None]
        for index, item in enumerate(rail):
            temp1[index] = item
            temp2[index] = item
            temp3[index] = item


        if vector == "left":
            temp1[4] = str(int(temp1[4]) - 4)
            temp2[4] = str(int(temp2[4]) - 8)
            temp3[4] = str(int(temp3[4]) - 12)

        elif vector == "right":
            temp1[4] = str(int(temp1[4]) + 4)
            temp2[4] = str(int(temp2[4]) + 8)
            temp3[4] = str(int(temp3[4]) + 12)

        elif vector == "top":
            temp1[2] = str(int(temp1[2]) + 4)
            temp2[2] = str(int(temp2[2]) + 8)
            temp3[2] = str(int(temp3[2]) + 12)

        elif vector == "bottom":
            temp1[2] = str(int(temp1[2]) - 4)
            temp2[2] = str(int(temp2[2]) - 8)
            temp3[2] = str(int(temp3[2]) - 12)

        print("\n\n")
        print("\t"+vector)
        pprint(rail)
        pprint(temp1)
        pprint(temp2)
        pprint(temp3)
        data_frame_data_list.append(temp1)
        data_frame_data_list.append(temp2)
        data_frame_data_list.append(temp3)
        return vector

    def add_tonel_by_rail_pos(rail: list, _vector: str):
        temp = [None, None, None, None, None, None, None, None]
        for index, item in enumerate(rail):
            temp[index] = item
        temp[1] = 6

        if _vector == "left":
            temp[-2] = 270

        elif _vector == "right":
            temp[-2] = 90

        elif _vector == "top":
            temp[-2] = 0

        elif _vector == "bottom":
            temp[-2] = 180

        data_frame_data_list.append(temp)

    def add_barier_by_rail_pos(rail: list, _vector: str):
        temp = [None, None, None, None, None, None, None, None]
        for index, item in enumerate(rail):
            temp[index] = item
        temp[1] = 7
        if _vector == "left":
            temp[-2] = 90
            temp[2] = str(int(temp[2]) - 2)

        elif _vector == "right":
            temp[-2] = 270
            temp[2] = str(int(temp[2]) + 2)

        elif _vector == "top":
            temp[-2] = 180
            temp[4] = str(int(temp[4]) + 2)

        elif _vector == "bottom":
            temp[-2] = 0
            temp[4] = str(int(temp[4]) - 2)

        temp[3] = "1.2"
        data_frame_data_list.append(temp)

    ''' Funk to extend map after end-way in herself that extension depends on end-rails types'''
    def add_rails(data: list, index: int):
        last_item = data[index]
        if last_item[1] == 20:
            # tunel
            data_frame_data_list[index][1] = 5

            vector = path_of_stat_raill(data_frame_data_list, data_frame_data_list[index])
            add_tonel_by_rail_pos(data_frame_data_list[index],vector)


        elif last_item[1] == 21:
            # border
            data_frame_data_list[index][1] = 5
            vector = path_of_stat_raill(data_frame_data_list, data_frame_data_list[index])
            add_barier_by_rail_pos(data_frame_data_list[index],vector)

        elif last_item[1] == 22:
            # tunel
            data_frame_data_list[index][1] = 5
            vector = path_of_stat_raill(data_frame_data_list, data_frame_data_list[index])
            add_tonel_by_rail_pos(data_frame_data_list[index],vector)

        elif last_item[1] == 23:
            # border
            data_frame_data_list[index][1] = 5
            vector = path_of_stat_raill(data_frame_data_list, data_frame_data_list[index])
            add_barier_by_rail_pos(data_frame_data_list[index],vector)

        # if last_item[-2]:
        #
        # for item in data:

    add_rails(data_frame_data_list, start_index)
    add_rails(data_frame_data_list, end_index)

    if count_of_path == 2:
        add_rails(data_frame_data_list, second_start_index)
        add_rails(data_frame_data_list, second_end_index)

    data_frame_for_write = []



    for item in data_frame_data_list:
        temp = [None, None, None, None, None, None, None, None]
        temp[0] = int(item[0])
        temp[1] = int(item[1])
        temp[2] = str(item[2])
        temp[3] = str(item[3])
        temp[4] = str(item[4])
        temp[5] = str(item[6])
        temp[6] = str(item[5])
        temp[7] = str(item[7])
        data_frame_for_write.append(temp)

    df = DataFrame(
        data_frame_for_write,
        columns=[
            'index',
            'type',
            'x',
            'y',
            'z',
            'Ry',
            'Rx',
            'Rz',
        ],
        index=[i for i in range(len(data_frame_for_write))]
    )
    # pprint(df)
    result = df.to_json(orient="table", indent=4, force_ascii=False)
    BASE_DIR = os.path.join(BASE_DIR, "main")
    BASE_DIR = os.path.join(BASE_DIR, "data")
    try:
        with open(os.path.join(BASE_DIR, f"infinity_{index_of_map}.json"), 'w', encoding='utf-8') as f:
            f.write(result)

    except:
        print(os.path.join(BASE_DIR, f"infinity_{index_of_map}.json"))
        input()


if __name__ == "__main__":
    main()






# p = get_all_duo_of_path_way(data_frame_data_list)

# graph = Graph(len(Data), directed=False)


# for node in p: 
#     graph.add_edge(node[0], node[1])

# print(f" {start_index} -->> {end_index}")
# result = graph.bfs(start_index, end_index)
# pprint(result)
# path_result = []
# adjacent_rails = []
# adjacent_rail = [None, None]
# after_start = []

# value_in__in_roud_map = ["left" , "right" , "bottom" , "top"]

# self_position_x = start[1]
# self_posotion_z = start[-1]
# vector = ""


# for _vector_of_displacement in value_in__in_roud_map:
        
#     if _vector_of_displacement == "bottom":
#         adjacent_rail[0] = int(self_position_x) - 4
#         adjacent_rail[1] = int(self_posotion_z)

#         vector = "left"


#     elif _vector_of_displacement == "top":
#         adjacent_rail[0] = int(self_position_x) + 4
#         adjacent_rail[1] = int(self_posotion_z)
#         vector = "top"

#     elif _vector_of_displacement == "right":
#         adjacent_rail[0] = int(self_position_x)
#         adjacent_rail[1] = int(self_posotion_z) + 4
#         vector = "right"

#     elif _vector_of_displacement == "left":
            
#         adjacent_rail[0] = int(self_position_x)
#         adjacent_rail[1] = int(self_posotion_z) - 4
#         vector = "left"
            
#     ex, request =  _is_raill_exist(adjacent_rail[0], adjacent_rail[1], data_frame_data_list,vector)
#     if ex:
#         break
#     else:
#         continue
# print(vector)

# start_vector = vector
# for way_index, rail_index in enumerate(result[:-1]):
#     delta_x = int(data_frame_data_list[rail_index][2]) - int(data_frame_data_list[result[way_index+1]][2])
#     delta_y = int(data_frame_data_list[rail_index][4]) - int(data_frame_data_list[result[way_index+1]][4])
#     curent_rail =  data_frame_data_list[rail_index]
#     curent_rail =  data_frame_data_list[rail_index]
#     next_rail = data_frame_data_list[result[way_index+1]]
#     print(vector)
#     print(f"{curent_rail[1]} type ")
#     if curent_rail[1] == 0:
#         if vector == "top":
#             vector = "top"
#             path_result.append(f"type: 0, ry: 90 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
            
#         elif vector == "bottom":
#             vector = "bottom"
#             path_result.append(f"type: 0, ry: 90 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
        
#         elif vector == "right":
#             vector = "right"
#             path_result.append(f"type: 0, ry: 0 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
            
#         elif vector == "left":
#             vector = "left"
#             path_result.append(f"type: 0, ry: 0 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")

#     else:
#         if delta_x != 0:
#             if vector == "left":
#                 if delta_x > 0:
#                     vector = "bottom"
#                     path_result.append(f"type: 1, ry: 90 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
#                 else:
#                     vector = "top"
#                     path_result.append(f"type: 1, ry: 180 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
                
#             elif vector == "right":
#                 if delta_x > 0:
#                     vector = "bottom"
#                     path_result.append(f"type: 1, ry: 0 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
#                 else:
#                     vector = "top"
#                     path_result.append(f"type: 1, ry: 270 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
        
#             elif vector == "top":
#                 vector = "top"
#                 path_result.append(f"type: 0, ry: 90 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
            
#             elif vector == "bottom":
#                 vector = "bottom"
#                 path_result.append(f"type: 0, ry: 90 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
        
                         
        
#         elif delta_y != 0:
#             if vector == "bottom":
#                 if delta_y < 0:
#                     vector = "right"
#                     path_result.append(f"type: 1, ry: 180 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
#                 else:
#                     vector = "left"
#                     path_result.append(f"type: 1, ry: 270 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
                
#             elif vector == "top":
#                 if delta_y < 0:
#                     vector = "right"
#                     path_result.append(f"type: 1, ry: 90 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
#                 else:
#                     vector = "left"
#                     path_result.append(f"type: 1, ry: 0 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
            
#             elif vector == "right":
#                 vector = "right"
#                 path_result.append(f"type: 0, ry: 0 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
            
#             elif vector == "left":
#                 vector = "left"
#                 path_result.append(f"type: 0, ry: 0 {data_frame_data_list[rail_index][2]} {data_frame_data_list[rail_index][3]} {data_frame_data_list[rail_index][4]}")
         



# map_df = []


# for index,item in enumerate(path_result):
#     temp = [None,None,None,None,None,None,None,None]
    
#     points = item[12:].split()
#     r_type = item.split(",")[0].split()[1]
#     temp[0] = index
#     temp[1] = int(r_type)
#     temp[2] = str(points[1])
#     temp[3] = str(points[2])
#     temp[4] = str(points[3])
#     temp[5] = str(points[0])
#     temp[6] = "0"
#     temp[7] = "0"
#     map_df.append(temp)
    
    
# path_df = DataFrame(
#     map_df,
#     columns=[
#     'index',
#     'type',
#     'x',
#     'y',
#     'z',
#     'Ry',
#     'Rx',
#     'Rz',
#     ],
#     index=[i for i in range(len(map_df))]
# )

# pprint(path_df)
# result = path_df.to_json(orient="table", indent=4,force_ascii=False)
# with open(os.path.join(BASE_DIR, "infinity_path.json"), 'w', encoding='utf-8') as f:
#     f.write(result)
