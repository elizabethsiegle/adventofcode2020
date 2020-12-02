with open('input.txt', 'r') as file:
    fileText = file.read().splitlines()

#is the pw valid? take in min, max, char to check, and password
def part1(minn, maxn, char, pw):
    if pw.count(char) >= minn and pw.count(char) <= maxn:
        return True

def part2(minn, maxn, char, pw):
    if (pw[minn] == char and pw[maxn] != char) or (pw[maxn] == char and pw[minn] != char): # is min valid 1st letter and not max
        return True

sum = 0 #set counter to keep track of valid passwords
sum2 = 0
for line in fileText: #loop through
    divider = str(line.partition(":")[0]) #get range, char
    maxn = int(divider.partition("-")[2].partition(' ')[0])
    minn = int(divider.partition("-")[0])
    char = str(divider.partition("-")[2].partition(' ')[2])
    pw = str(line.partition(":")[2])
    if part1(minn, maxn, char, pw):
        sum +=1
        print(sum)

    #part 2
    if part2(minn, maxn, char, pw):
        sum2 +=1
        print(sum2)

    
    

