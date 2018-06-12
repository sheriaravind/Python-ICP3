def Read_Data():
    data_dict = {}
    list = []
    with open(r'C:\Users\aravi\OneDrive\Desktop\Sample.txt', 'r') as input_data:
        for line in input_data:
            data = line.strip().split()
            for word in data:
                list.append(word)

    for item in set(list):
        count = list.count(item)
        data_dict[item] = count

    print(data_dict)

if __name__ == '__main__':
    Read_Data()