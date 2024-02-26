def print_pascal_triangle(height):
    previous_row = []
    for row in range(height):
        current_row = []
        for index in range(row+1):
            # handle the first two rows
            if row < 2:
                current_row.append(1)
            # append 1 to the beginning and end of rows 3 and above
            elif index == 0 or index == row:
                current_row.append(1)
            # append the sum of the two numbers above the current number
            else:
                num = previous_row[index-1] + previous_row[index]
                current_row.append(num)
        
        previous_row = current_row
        formatRow = str(current_row[0]) if row == 0 else ' '.join(str(i) for i in current_row)
        print(formatRow.center(height*4))



while True:
    
    try:
        a = int(input("\n\nEnter the height of the Pascal's Triangle: "))
        print_pascal_triangle(a)
        continue
    except ValueError or TypeError:
        print("\n\nPlease enter a valid number")
    else:
        break
    