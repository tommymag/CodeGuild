
phone_number = input('Please enter a ten digit phone number to "prettify": ')

def prettify(phone_number):
    pretty = phone_number[0:3] + "-" + phone_number[3:6] + "-" + phone_number[6:10]
    return pretty

print(prettify(phone_number))

# phone_number = input("Please enter an all digits phone number. ")
#
# pretty = phone_number[0:3] + "-" + phone_number[3:6] + "-" + phone_number[6:10]
# print(pretty)

