def hello():
    print("Welcome to learning Python!")

def pack(x, y, z):
    return (x, y, z)


def eat_lunch(food_list):
    if not food_list:
        print("First I eat", food_list[0])
        for food in food_list[1:]:
            print("Next I eat", food)