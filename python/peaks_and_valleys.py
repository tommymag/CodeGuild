# Define the following functions:

# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

# valleys - Returns the indices of ‘valleys’. A valley is a number with a higher number on both the left and the right.

# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.



# data_set = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


input_str_data = input("Let's find peaks and valleys in your data!\nPlease insert values by spaces and commas:\n")

data_set = [int(s) for s in input_str_data.split(',')]
# print(data_set)


def peaks(data):
    pks_lst = []
    for i in range(1, len(data)-1,  1):
        if data[i-1] < data[i] and data[i] > data[i +1]:
            pks_lst.append(i)
    return pks_lst

def valleys(data):
    vly_lst = []
    for i in range(1, len(data)-1,  1):
        if data[i-1] > data[i] and data[i] < data[i +1]:
            vly_lst.append(i)
    return vly_lst

def peaks_and_valleys(data):
    pksvly_lst = peaks(data) + valleys(data)

    return sorted(pksvly_lst)


    # if i > data[i]-1) and [data]+1


print(peaks(data_set))
print(valleys(data_set))
print(peaks_and_valleys(data_set))


# >>> peaks(data)
# [6, 14]
# >>> valleys(data)
# [9, 17]
# >>> peaks_and_valleys(data)
# [6, 9, 14, 17]



