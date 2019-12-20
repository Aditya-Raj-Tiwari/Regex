# first importing the regex module
import re

# TODO: re.compile() returns a Regex pattern object (or simply, a Regex object).
phone_num_regex = re.compile(r'\d{3}-\d{10}')

# TODO: search() method searches the string it is passed
mo = phone_num_regex.search('My phone number is 977-9861281545')

# returns none if not found : Match obj if found

# TODO: group() method that will return the actual matched text from the searched string
print('the number found is {}'.format(mo.group()))


# TODO: grouping and finding the object
phone_num_regex_grouped = re.compile(r'(\d{3})-(\d{10})')
nep = phone_num_regex_grouped.search('My phone number is 977-9861281545')
print('The regional code is {}'.format(nep.group(1)))

# TODO:If you would like to retrieve all the groups at once, use
#  the groups() method—note the plural form for the name.
area_code , phone_number = nep.groups()
print('The regional code is {}'.format(area_code))


# * [^matches except this this]
