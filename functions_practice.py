def hello():
    print("Hello!!! Welcome to the world of Python!!!")

def pack(x, y, z):
    return [x, y, z]

# python function, function takes list as an argument
def eat_lunch(my_list):
  if len(my_list) == 0:
    print("My lunchbox is empty!")
  else:
    # loop checks if current element is the first on the list
    for i in range(len(my_list)):
      if i == 0:
        print(f"First I eat a {my_list[0]}")
      else:
        print(f"Next I eat {my_list[i]}")
# output prints
hello()
print(pack("x", "y", "z"))
eat_lunch([])
eat_lunch(["burger"])
eat_lunch(["burger", "fries", "slice of cake"])