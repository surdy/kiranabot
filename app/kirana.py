filename="list.txt"

list_map = {}

def read_list():
    list_file = open(filename, "r")
    for line in list_file:
        list_map[line.strip()] = False
    return list_map

def add_to_list(item):
    list_map[item] = False


def remove_from_list(item):
    del list_map[item]

if __name__ == '__main__':
    map=read_list('list.txt')
    print(map)

