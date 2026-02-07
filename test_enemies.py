
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


i = 50
def foo():
    i = 100
    return i
 
print(foo())
print(i)