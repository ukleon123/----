import sys


if __name__ == "__main__":
    num_node, id_start, id_end, num_edge = map(int, sys.stdin.readline().split())

    edges = []
    values = []
    for i in range(num_edge):
        edges.append(list(map(int, sys.stdin.readline().split())))
        