import time

def karatsuba_mult(x, y):
    # Base case for recursion
    if len(x) == 1 or len(y) == 1:
        return int(x) * int(y)

    # Make the lengths of the numbers equal
    if len(x) < len(y):
        x = x.zfill(len(y))
    elif len(y) < len(x):
        y = y.zfill(len(x))

    n = len(x)
    half = n // 2

    # Split the digit sequences in the middle
    a = x[:half]
    b = x[half:]
    c = y[:half]
    d = y[half:]

    # Recursive calls
    ac = karatsuba_mult(a, c)
    bd = karatsuba_mult(b, d)
    ad_plus_bc = karatsuba_mult(str(int(a) + int(b)), str(int(c) + int(d))) - ac - bd

    # Combine the results
    result = ac * 10**(2 * (n - half)) + (ad_plus_bc * 10**(n - half)) + bd

    return result

num1 = '3141592653589793238462643383279502884197169399375105820974944592'
num2 = '2718281828459045235360287471352662497757247093699959574966967627'


start_time_kar = time.time()
kar = karatsuba_mult(num1, num2)
end_time_kar = time.time()

start_time_us = time.time()
us = int(num1) * int(num2)
end_time_us = time.time()

print(kar)
print(end_time_kar - start_time_kar)
print(us)
print(end_time_us - start_time_us)
print(kar == us)
print((end_time_kar - start_time_kar)/(end_time_us - start_time_us))

num3 = '3141592653589793238462643383279502884197169399375105820974944592314159265358979323846264338327950288419716939937510582097494459231415926535897932384626433832795028841971693993751058209749445923141592653589793238462643383279502884197169399375105820974944592'
num4 = '2718281828459045235360287471352662497757247093699959574966967627271828182845904523536028747135266249775724709369995957496696762727182818284590452353602874713526624977572470936999595749669676272718281828459045235360287471352662497757247093699959574966967627'

start_time_kar_2 = time.time()
kar_2 = karatsuba_mult(num3, num4)
end_time_kar_2 = time.time()

start_time_us_2 = time.time()
us_2 = int(num3) * int(num4)
end_time_us_2 = time.time()

print(kar_2)
print(end_time_kar_2 - start_time_kar_2)
print(us_2)
print(end_time_us_2 - start_time_us_2)
print(kar_2 == us_2)
print((end_time_kar_2 - start_time_kar_2)/(end_time_us_2 - start_time_us_2))
