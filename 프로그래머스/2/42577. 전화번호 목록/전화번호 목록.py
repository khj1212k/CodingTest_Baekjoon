def solution(phone_book):
    answer = True
    phone_book = set(phone_book)
    
    for num in phone_book:
        for i in range(1, len(num)):
            if num[:i] in phone_book:
                return False
            
    return True