import math

def solution(arr):
    lcm = arr[0]
    for i in arr:
        # A*B = LCM(A*B) * GCB(A*B)
        lcm = i * lcm // math.gcd(i,lcm)

    return lcm