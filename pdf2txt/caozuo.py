"""把PDF转成excel或txt"""
import pandas as pd





def pdf2excel(path):
    pass


def pdf2txt(path):
    pass

def txt2excel(path,savename):
    df =[]
    with open(path,"r",encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if len(line) >0 :
                line=line.replace("\n","")
                df.append(line)
        df = pd.DataFrame(df)
        df.to_excel(savename+'.xlsx')
        print(df)



if __name__=="__main__":
    path = "text.txt"
    savename= "尝试"
    txt2excel(path,savename)
