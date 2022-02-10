source1 = input('input string 1> ')
source2 = input('input string 2> ')

print(source1 * 5)  # str duplication
print(source1 + source2)  # str concatenation
print(len(source1) + len(source2))  # str length concatenation
if source1.find(source2):  # always finds substring if str2 has any character
    print('substring found')
else:
    print('substring not found')
