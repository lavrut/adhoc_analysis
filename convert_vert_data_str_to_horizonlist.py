# Veritical data as string
vertical_data_str = '''0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10
'''

# Convert the vertical_data_str to a horizontal list
horizontal_list = [int(x) for x in vertical_data_str.split('\n')]

print(horizontal_list)
