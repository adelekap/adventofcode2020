from day12.boat_mechanics import change_heading

directions = ['N', 'S', 'E', 'W']
degrees = [90, 180, 270]
turns = ['L', 'R']

inputs = []
outputs = ['W', 'E', 'S', 'S', 'E', 'W', 'E', 'W', 'N', 'N', 'W', 'E', 'N', 'S', 'W', 'W', 'S', 'N', 'S', 'N', 'E', 'E', 'N', 'S']

for direction in directions:
    for degree in degrees:
        for turn in turns:
            inputs.append((direction, turn, degree))

for input, output in zip(inputs, outputs):
    print(f'{input}')
    result = change_heading(input[0], input[1], input[2])

    if result != output:
        print('FAILED')
    else:
        print('PASSED')
