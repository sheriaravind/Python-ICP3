vowels = ['a','e','i','o','u']
count = 0
with open(r'C:\Users\aravi\OneDrive\Desktop\Sample.txt', 'r') as input_data:
    for line in input_data:
        for word in line:
            if(word in vowels):
                count += 1

    print("Vowel Count in the file is: ",count)