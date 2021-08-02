def say_hello():
    print("Hello World.")

def say_hello2(name):
    print(f"Mr.{name} Hello.")

def calc_square(side):
    result = side * side
    return result

def calc_tri(side, high):
    return (side * high) / 2

say_hello()
say_hello2("tom")

# result = calc_square(10)
result = calc_tri(10, 20)
print(result)


