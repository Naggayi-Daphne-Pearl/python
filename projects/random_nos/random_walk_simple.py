# Write Random walk function
import random 

def random_walk(n):
    """Return coordinates after 'n' block random walk function"""
    x= 0 
    y =0 
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return (x, y)

for i in range(5):
    walk = random_walk(10)
    # abs(): Return the absolute value of the argument.
    print(walk, "Distance from home = ", abs(walk[0] + abs(walk[1])))        