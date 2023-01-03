# 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    second = 0
    bridge = [0 for i in range(bridge_length)]
    bridge_weight = 0
    while 1:
        if len(truck_weights) == 0 and bridge.count(0) == len(bridge):
            break

        if bridge.count(0) == len(bridge):
            bridge[-1] = truck_weights.pop(0)
            bridge_weight += bridge[-1]
        else:
            bridge_weight -= bridge.pop(0)
            bridge.append(0)
            if len(truck_weights) > 0 and truck_weights[0] + bridge_weight <= weight:
                bridge[-1] = truck_weights.pop(0)
                bridge_weight += bridge[-1]

        second += 1
    return second
