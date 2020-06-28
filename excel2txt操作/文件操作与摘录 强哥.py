
f = open("强哥.csv", "r")
lines = f.readlines()

for line in lines:
    line = line.split(",")
    # print(line)
    if len(line[3]) == 0:
        print('\n',line[2])
    elif len(line[3]) !=0:
        tai= str(line[4]).replace('\n', '')
        tai = tai.replace(".00","")
        tai = tai.replace(" ", "")
        print(f'型号为{line[3]}的{line[2]}共{tai}台，')
