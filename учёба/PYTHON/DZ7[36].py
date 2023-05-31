def table(operation, num_rows=6, num_columns=6 ):
    header = " "*7
    for col in range(1, num_columns+1):
        header +=f"{col:4d}"
    print(header)
    print(" "*7, "-"*num_columns*4)
    for row in range(1, num_rows+1):
        row_str = f"{row:4d} | "

        for col in range(1, num_columns+1):
            row_str += f"{operation(row, col):4d}"

        print(row_str)

table(lambda x,y: x*y)