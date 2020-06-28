
f = open("工作簿1.csv", "r")
lines = f.readlines()
for line in lines:
    line = line.split(",")
    if len(line[3]) !=0:
        tai= str(line[4]).replace('\n', '')
        tai = tai.replace(".00","")
        tai = tai.replace(" ", "")
        print(f'型号为{line[3]}的{line[2]}共{tai}台，')
