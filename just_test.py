# import sklearn
# import matplotlib.pyplot as plt
# import random
# import re
import pandas as pd

df = pd.read_excel("2result.xlsx")

def cut(content):
    content=str(content).replace("\n","")
    return content

df['题干'] =df['题干'].apply(cut)
print(df.shape)
df.to_csv("清理后.csv")