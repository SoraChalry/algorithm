lst = [list(map(int, input().split())) for _ in range(3)]
new_x = []
new_y = []
result_x = 0
result_y = 0
for x,y in lst :
    new_x.append(x)
    new_y.append(y)
else :
    x_set = set(new_x)
    y_set = set(new_y)
    for i in x_set:
        if new_x.count(i) == 1:
            result_x = i
    for j in y_set:
        if new_y.count(j) == 1:
            result_y = j

print(result_x, result_y)