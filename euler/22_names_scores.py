
def sorting(filename):
    infile=open(filename)
    words=[]
    total_score=0
    for line in infile:

        temp=line.split('","')

        for i in temp:
            if i=='"MARY':
                i='MARY'
            elif i=='ALONSO"':
                i='ALONSO'
            words.append(i)
    infile.close()
    words.sort()
    outfile=open('sorted_names.txt','w')
    for index,name in enumerate(words):
        total_score+=calculate_score(index+1,name)
        outfile.writelines(name)
        outfile.writelines(",")
    outfile.close()
    return total_score

def calculate_score(order,name):
    alpha_scores={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    score=0
    for letter in name:
        score+=alpha_scores[letter]
    score*=order
    return score
if __name__=='__main__':
    print(sorting('names.txt'))