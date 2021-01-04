# 2 * 2 grid, move only to the right or down
# each path in 2/2 is 4 squeares long
# is it the same for 3/3?
# *‾‾|‾‾|‾‾|
# |--|--|--|
# |__|__|__|


positions = []
position_paths = []
position = [0, 0]
for x in range(1000):   # all paths
    path = '000000'+str(bin(x))
    position = [0, 0]
    for i in path[::-1]:
        if i == '0':
            position[0] = position[0] + 1
            positions.append(position)
        else:
            position[1] = position[1] + 1
            positions.append(position)
    if positions[-1] == [20, 20]:
        position_paths.append(positions)
print(position_paths)
