snake = [(0, 0) for i in range(10)]
positions = {snake[-1]}

with open("input") as f:
    for line in f:
        d, l = line.strip().split()
        for _ in range(int(l)):
            if d == "R":
                snake[0] = (snake[0][0] + 1, snake[0][1])
            elif d == "L":
                snake[0] = (snake[0][0] - 1, snake[0][1])
            elif d == "U":
                snake[0] = (snake[0][0], snake[0][1] + 1)
            elif d == "D":
                snake[0] = (snake[0][0], snake[0][1] - 1)
            else:
                raise ValueError

            for i in range(9):
                if max(abs(snake[i][0]-snake[i+1][0]), abs(snake[i][1]-snake[i+1][1])) > 1:
                    if snake[i][0] == snake[i+1][0] or (snake[i][0] != snake[i+1][0] and snake[i][1] != snake[i+1][1]):
                        if snake[i][1] > snake[i+1][1]:
                            snake[i+1] = (snake[i+1][0], snake[i+1][1] + 1)
                        else:
                            snake[i+1] = (snake[i+1][0], snake[i+1][1] - 1)
                    if snake[i][1] == snake[i+1][1] or (snake[i][0] != snake[i+1][0] and snake[i][1] != snake[i+1][1]):
                        if snake[i][0] > snake[i+1][0]:
                            snake[i+1] = (snake[i+1][0] + 1, snake[i+1][1])
                        else:
                            snake[i+1] = (snake[i+1][0] - 1, snake[i+1][1])
            positions.add(snake[-1])
print(len(positions))
