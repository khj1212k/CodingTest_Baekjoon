
def solution(operations):
        pq = []
        for ops in operations:
            o,v = ops.split(' ')
            if o == 'I':
                pq.append(int(v))
                pq.sort()
            else: # o == 'D'
                if pq:
                    if v == '-1':
                        pq = pq[1:]
                    else : # v == 1
                        pq.pop() # 최댓값
        return [max(pq),min(pq)] if pq else [0,0]
