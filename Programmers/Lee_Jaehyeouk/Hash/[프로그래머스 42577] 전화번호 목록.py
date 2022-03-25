def solution(phone_book):

    phone_book.sort()

    for i in range(len(phone_book)-1):
        t = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][0:t]:
            return False

    return True