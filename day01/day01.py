# open the text file
file_name = 'puzzle_input.txt')
with open(file_name) as file_txt:
    lines = [line.rstrip().lstrip() for line in file_txt]

# setting up variables     
elfno = 0 #counting each elf 
carries = {} #dict to get sum of fruits per each elf 

for i in range(len(lines)):
    if lines[i] == '':
        elfno += 1
    else:
        fruit = int(lines[i])
        carries[elfno] = fruit + carries.get(elfno,0) #sum up fruits of each elf's bag


# wanted to use itemgetter 
from operator import itemgetter 
sorted(carries.items(), key = itemgetter(1), reverse=True)[0:3]

# or lambda 
sorted(carries.items(), key = lambda x: x[1], reverse=True)

elf_fruit = sorted(carries.items(), key = lambda x: x[1], reverse=True)[0][1]
elf_no = sorted(carries.items(), key = lambda x: x[1], reverse=True)[0][0]


print(f'elf #{elf_no+1} has total calorie of {elf_fruit} in the bag!')
# Elves do not count from zero! So I will add one. 
print('the answer is: ', elf_fruit)

