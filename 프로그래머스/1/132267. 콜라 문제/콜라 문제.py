def solution(a, b, n):
    result = 0
    
    while n >= a:
        k = n // a
        r = n % a
        n = n - (a*k)
        n = n + (k * b)
        
        result += (k * b)

    return result