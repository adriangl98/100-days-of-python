row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? RC (Row and Column; no space ")

# Count from 0 in lists so we remove 1 to get true position
horizontal = int(position[0])-1
vertical = int(position[1])-1

#Select the vertical placement in the map
selected_row = map[vertical]
#Select the horizontal placement in the map and replace it with X
selected_row[horizontal]= "X"

print(f"{row1}\n{row2}\n{row3}")