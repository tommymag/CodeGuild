# file = open('829.txt', 'r')
# contents = file.readlines()
# for line in contents:
#     print(line)
# print(contents)
# file.close()

# with open('829.txt', 'r') as file:
#     contents = file.readlines()
#     for ine in contents:
#         print(line)

def read_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.readlines()
        for line in contents:
            print(line)
    print(contents)

# def write_file(file_path):
#     with open(file_path, 'w') as file:
#         times = int(input('How many lines would you like to add?: '))
#         ran = 0
#         list_of_lines = []
#         while ran < times:
#             list_of_lines.append(input("What would you like to write to this file?"))
#             ran += 1
#         for line in list_of_lines:
#             file.write(line + '\n')

def append_file(file_path):
    with open(file_path, 'a') as file:
        times = int(input('How many lines would you like to add?: '))
        ran = 0
        list_of_lines = []
        while ran < times:
            list_of_lines.append(input("What would you like to write to this file?"))
            ran += 1
        for line in list_of_lines:
            file.write(line + '\n')


# write_file('829.txt')
append_file('829.txt')
read_file('829.txt')