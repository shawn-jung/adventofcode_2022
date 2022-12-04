# open the text file
with open('puzzle_input.txt') as file_txt:
    lines = [line.rstrip().lstrip() for line in file_txt]

elfno = 0 #counting each elf 
carries = {} #dict to get sum of fruits per each elf 

for i in range(len(lines)):
    if lines[i] == '':
        elfno += 1
    else:
        fruit = int(lines[i])
        carries[elfno] = carries.get(elfno,0) + fruit #sum up fruits of each elf's bag


# wanted to use itemgetter 
from operator import itemgetter 
sorted(carries.items(), key = itemgetter(1), reverse=True)[0:3]

sorted(carries.items(), key = lambda x: x[1], reverse=True)

elf_no = sorted(carries.items(), key = lambda x: x[1], reverse=True)[0][0]
elf_fruit = sorted(carries.items(), key = lambda x: x[1], reverse=True)[0][1]

print(f'elf #{elf_no+1} has total calorie of {elf_fruit} in the bag!')
# Elves do not count from zero! So I will add one. 

