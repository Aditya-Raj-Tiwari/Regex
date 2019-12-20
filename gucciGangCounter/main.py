import re

def count_word(file_name):
    with open(file_name,'r') as f:
        # lyrisc = f.read()
        # counter = re.compile()
        matches = re.findall(r'(\()?[Gg]ucci [Gg]ang(!)?(\))?',f.read())
        count = 0
        for match in matches:
            count += 1
            print(match)
        print('The number of Gucci gang being said is {}'.format(count))

def main():
    print('Please make a text file of the lyrisc like abcd.txt')
    # file_name = input('Please input the file name : ')
    count_word('gucci_gang_lyrisc.txt')

main()
