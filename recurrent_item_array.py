 # with same frequency, will return the first encountered number
def most_recurrent_item(list):
    dict = {}
    freq = 0
    num = None
    for i in range(len(list)):
        item = list[i]
        dict[item] = dict.get(item, 0) + 1 #get key = item, if not exists, return default value 0. Easiest way to check whether a key exits
        if dict[item] > freq:
            freq = dict[item]
            num = item
    return num
print most_recurrent_item([1, 2, 4, 2, 3, 1, 2, 0, 2, 3, 0, 9])
print most_recurrent_item([0, 0, 2, 2, 2, 0, 0])




#why min needs to iterate twice?
def least_recurrent_item(list):
    dict = {}
    freq = '+inf'
    num = None
    for i in range(len(list)):
        item = list[i]
        dict[item] = dict.get(item, 0) + 1
    for k, v in dict.items():
        if v < freq:
            freq = v
            num = k
    return num
print least_recurrent_item([1, 2, 4, 2, 3, 1, 2, 0, 2, 3, 0, 9])
print least_recurrent_item([0, 0, 2, 2, 2])



#first nonrecurring element in a list
def first_non_recurrent_item(list):
    num = None
    pos = '+inf'
    dict = {}
    for i in range(len(list)):
        item = list[i]
        if item in dict.keys():
            dict[item][1] += 1 #occurence + 1
        else:
            dict[item] = [i, 1] #first apparance
    for k, v in dict.items():
        if dict[k][1] == 1 and  dict[k][0]< pos:
            pos = v[0]
            num = k
    return num
print first_non_recurrent_item([1, 2, 4, 2, 3, 1, 2, 0, 2, 3, 0, 9])
print first_non_recurrent_item([0, 0, 2, 2, 2])