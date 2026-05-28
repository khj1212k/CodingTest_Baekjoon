def solution(cacheSize, cities):
    
    answer = 0
    stack = []
    cities = [city.lower() for city in cities]
    
    for city in cities:
        
        if city in stack:
            answer += 1
            stack.remove(city)
            stack.append(city)
                
        else:
            stack.append(city)
            answer += 5
            if len(stack) > cacheSize:
                stack.pop(0)
        # print(stack)
    return answer