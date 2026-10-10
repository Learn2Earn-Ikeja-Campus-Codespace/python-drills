def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):           # range stops before its end, so n + 1 includes n
        if i % 15 == 0:                 # divisible by both 3 and 5
            result.append("FizzBuzz")   # must comes first, or 15 would be caught by the 3 or 5 check
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))       # number becomes strings so the list holds one type
    return result