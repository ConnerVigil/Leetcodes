def zigzag_string(string, numRows):
    if numRows == 1 or len(string) < numRows:
        return string

    # Initialize empty arrays
    arrays = ["" for i in range(len(string))]
    reverse = False
    currentRow = 0

    for i in range(len(string)):
        arrays[currentRow] += string[i]  # Append current char to current row

        if currentRow == numRows - 1:  # If last row is reached, reverse direction
            reverse = True
        elif currentRow == 0:  # If first row is reached, reverse
            reverse = False

        if reverse:
            currentRow -= 1
        else:
            currentRow += 1

    result = ""
    for i in range(len(arrays)):  # piece together the rows into result
        result += arrays[i]

    return result


if __name__ == '__main__':
    s = 'coderbyte'
    k = 3

    print(zigzag_string(s, k))

    s = 'cat'
    k = 5

    print(zigzag_string(s, k))

#  c       r       e
#    o   e   b   t
#      d       y
