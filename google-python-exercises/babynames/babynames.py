#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  with open(filename,'r') as f:
    # baby_number = re.findall(r'((?<=<td>)\d{1,4})((?<=<td>)[A-Z]\w*)',f.read())
    baby_detail = re.findall(r'<td>(.*?)</td>',f.read(),re.DOTALL)
    # year = re.findall(r'>(.*?)</h3>',f.read(),re.DOTALL)
    return  baby_detail


def main():
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  f = open('babynames.txt','w')
  f.write('Rank\t Boy\t Girl\n')
  lst = extract_names('baby1990.html')
  dict_list_1990 = [{lst[i]: lst[i + 1]+' '+lst[i+2]} for i in range(0, len(lst)-2,3)]
  name_rank = []
  for dicts in dict_list_1990:
    for rank,names in dicts.items():
      nameOfBoy,nameOfGirl = names.split(' ')
      name_rank.append('{} {}'.format(nameOfBoy,rank))
      name_rank.append('{} {}'.format(nameOfGirl,rank))
      f.write('{}.\t\t {} \t\t {}\n'.format(rank,nameOfBoy,nameOfGirl))
  print('Done!')
  print(name_rank)

if __name__ == '__main__':
  main()
