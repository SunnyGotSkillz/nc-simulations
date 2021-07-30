"""
Node cardinality using Mobile Base Station Simulations

Test Simulation 1
Number of active nodes within each types is the same = D
"""

import math
import simpy
import random
import statistics
import numpy as np

M = 4  # number of stops by MBS
q = 0.3  # probability with which a given node of Type b is active
D = 300  # number of nodes for each type
T = 4  # number of types of nodes
S = 0.2  # error probability
W = 30  # number of trials
t = math.ceil(math.log2(D * T))  # time slots per trial

nodes = []
time_slots = 0


class Network(object):
    def __init__(self, env):
        self.env = env


class Node(object):
    def __init__(self, x_coord, y_coord, type, active):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.type = type
        self.active = active


def main():
    # Generate nodes
    for i in range(D):
        for j in range(T):
            a = random.randint(1, 11)
            nodes.append(Node(random.random(), random.random(), j + 1, True if a <= 3 else False))

    Y_m_w = [[[0]*t]*W]
    for m in range(1, M+1):
        Y_m_w.append([])
        for w in range(1, W+1):
            Y_m_w[m].append([0]*t)

    total = [0, 0, 0, 0]
    for type in range(1, T+1):
        for m in range(1, M + 1):
            MBS_x, MBS_y = 0.25, 0.25
            p_m = []

            if m == 2:
                MBS_x, MBS_y = 0.25, 0.75
            if m == 3:
                MBS_x, MBS_y = 0.75, 0.75
            if m == 4:
                MBS_x, MBS_y = 0.75, 0.25

            for i in range(1, t + 1):
                if i != t:
                    p_m.append(2 ** (-i))
                else:
                    p_m.append(2 ** (-(t - 1)))

            v_sum = 0
            for w in range(1, W + 1):
                S_m_w = [0] * (t)
                for node in nodes:
                    if node.active and node.type == type and (math.sqrt(((node.x_coord-MBS_x)**2) + ((node.y_coord-MBS_y)**2))) <= 0.5:
                        slot = np.random.choice(range(1, t + 1), t, True, p_m)
                        S_m_w[slot] = 1
                for i in range(0, t):
                    Y_m_w[m][w][i] = (Y_m_w[m - 1][w][i] | S_m_w[i])
                #Y_m_w[m][w] = Y_m_w[m - 1][w] | S_m_w

                j_ = t
                for j in range(1, t + 1):
                    i = 2 ** (j - 1)
                    if Y_m_w[m][w][i] == 0:
                        j_ = j

                v_m_w = maxSearch(j_, Y_m_w, m, w)
                v_sum += v_m_w

            n_m_t = 0.794 * 2 ** (v_sum / W)
            total[type-1] += n_m_t

    print("Predicted Type 1: ", total[0])
    print("Predicted Type 2: ", total[1])
    print("Predicted Type 3: ", total[2])
    print("Predicted Type 4: ", total[3])

    # Calculate actual numbers
    actual = [0,0,0,0]
    for node in nodes:
        actual[node.type-1] += 1

    print("Actual Type 1: ", actual[0])
    print("Actual Type 2: ", actual[1])
    print("Actual Type 3: ", actual[2])
    print("Actual Type 4: ", actual[3])

def maxSearch(j_, Y_m_w, m, w):
    left = 2**(j_-2)
    right = (2**(j_-1))-1
    ans = t
    while left <= right:
        mid = left + ((right-left) // 2)
        if Y_m_w[m][w][mid] == 1:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1

    return ans

if __name__ == "__main__":
    main()
