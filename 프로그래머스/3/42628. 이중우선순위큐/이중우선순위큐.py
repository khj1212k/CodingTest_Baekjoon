
def solution(operations):
        pq = []
        for ops in operations:
            o,v = ops.split(' ')
            
            if o == 'I': [pq.append(int(v)), pq.sort()]
            elif pq and o == 'D' and v == '-1': pq = pq[1:]
            elif pq and o == 'D' and v == '1' : pq.pop()
            
        return [max(pq),min(pq)] if pq else [0,0]
