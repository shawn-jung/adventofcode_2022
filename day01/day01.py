# open the text file
with open('puzzle_input.txt') as file_txt:
    lines = [line.rstrip().lstrip() for line in file_txt]

# setting up variables     
elfno = 0 #counting each elf 
carries = {} #dict to get sum of fruits per each elf 

for i in range(len(lines)):
    if lines[i] == '':
        elfno += 1
    else:
        fruit = int(lines[i])
        carries[elfno] = carries.get(elfno,0) + fruit #sum up fruits of each elf's bag


# wanted to use lambda to get second item, value
sorted(carries.items(), key = lambda x: x[1], reverse=True)[0:3]

# May I can use itemgetter 
from operator import itemgetter 
sorted(carries.items(), key = itemgetter(1), reverse=True)[0:3]

top_elf = sorted(carries.items(), key = lambda x: x[1], reverse=True)[0]
elf_no = top_elf[0]
elf_fruit = top_elf[1]

print(f'elf #{elf_no+1} has total calorie of {elf_fruit} in the bag!')
# Elves do not count from zero! So I will add one. 
print('the answer is: ', elf_fruit)

print(elf_fruit)


