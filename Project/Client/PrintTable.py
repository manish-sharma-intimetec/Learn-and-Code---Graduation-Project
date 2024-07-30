def printTable(data, columnNames):
    
    columnWidths = [max(len(str(item)) for item in column) for column in zip(*data, columnNames)]
    print(columnWidths)
    
    headerRow = " | ".join(f"{name:<{columnWidths[i]}}" for i, name in enumerate(columnNames))
    
    
    separatorRow = "-+-".join('-' * width for width in columnWidths)
    
    
    print(headerRow)
    print(separatorRow)
    
   
    for row in data:
        rowStr = " | ".join(f"{str(item):<{columnWidths[i]}}" for i, item in enumerate(row))
        print(rowStr)


data = [
    ('#100', 'Chicken', 200, 1, 'North Indian', 'High', 'Non Veg', 'No'),
    ('#10', 'Paneer', 2000, 1, None, None, None, None),
    ('#10', 'Lacha Paratha', 100, 1, None, None, None, None),
    ('#99', 'Boiled Egg', 30, 1, 'North Indian', 'Low', 'Eggetarian', 'No')
]

column_names = ['ID', 'Item Name', 'Price', 'Availability', 'Cuisine', 'Spice Level', 'Veg Type', 'Is Sweet']

# printTable(data, column_names)