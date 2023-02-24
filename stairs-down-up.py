num_steps = 5

for steps in range(0, num_steps):
    print(" " * steps * 2 + "--")

for step in range(0, num_steps):
    space = " " * (num_steps - step - 1) * 2
    print(space + "--")