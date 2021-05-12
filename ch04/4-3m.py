input_data = input("Start: ")
row = int(input_data[1])
col = ord(input_data[0]) - ord('a') + 1
result = 8

##########################################################################################
# 1
steps = [(-2, -1), (-2, +1), (-1, -2), (-1, +2),
         (+2, -1), (+2, +1), (+1, -2), (+1, +2)]

new_list = [(steps[i][0] + row, steps[i][1] + col) for i in range(len(steps))]

for i in range(len(steps)):
    if new_list[i][0] < 1 or 8 < new_list[i][0]:
        result -= 1
    elif new_list[i][1] < 1 or 8 < new_list[i][1]:
        result -= 1

print(result)

##########################################################################################
# # or 2
# steps = [(row-2, col-1), (row-2, col+1), (row-1, col-2), (row-1, col+2),
#         (row+2, col-1), (row+2, col+1), (row+1, col-2), (row+1, col+2)]
#
# for i in range(len(steps)):
#     if steps[i][0] < 1 or 8 < steps[i][0]:
#         result -= 1
#     elif steps[i][1] < 1 or 8 < steps[i][1]:
#         result -= 1
#
# print(result, toc - tic)
##########################################################################################
