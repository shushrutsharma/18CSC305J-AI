import time
start_time = time.time()
import re
import itertools
import collections 
import copy
import queue

p=open("input.txt","r")
data=list()
data1= p.readlines()
count=0

n=int(data1[0])
queries=list()
for i in range(1,n+1):
    queries.append(data1[i].rstrip())   
k=int(data1[n+1])
kbbefore=list()


def CNF(sentence):
    temp=re.split("=>",sentence)
    temp1=temp[0].split('&')
    for i in range(0,len(temp1)):
        if temp1[i][0]=='~':
            temp1[i]=temp1[i][1:]
        else:
            temp1[i]='~'+temp1[i]
    temp2='|'.join(temp1)
    temp2=temp2+'|'+temp[1]
    return temp2


variableArray = list("abcdefghijklmnopqrstuvwxyz")
variableArray2 = []
variableArray3 = []
variableArray5 = []
variableArray6 = []
for eachCombination in itertools.permutations(variableArray, 2):
    variableArray2.append(eachCombination[0] + eachCombination[1])
for eachCombination in itertools.permutations(variableArray, 3):
    variableArray3.append(eachCombination[0] + eachCombination[1] + eachCombination[2])
for eachCombination in itertools.permutations(variableArray, 4):
    variableArray5.append(eachCombination[0] + eachCombination[1] + eachCombination[2]+ eachCombination[3])
for eachCombination in itertools.permutations(variableArray, 5):
    variableArray6.append(eachCombination[0] + eachCombination[1] + eachCombination[2] + eachCombination[3] + eachCombination[4])
variableArray = variableArray + variableArray2 + variableArray3 + variableArray5 + variableArray6
capitalVariables = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number=0
  

def standardizationnew(sentence):
    newsentence=list(sentence)
    i=0
    global number
    variables=collections.OrderedDict()
    positionsofvariable=collections.OrderedDict()
    lengthofsentence=len(sentence)
    for i in range(0,lengthofsentence-1):
        if(newsentence[i]==',' or newsentence[i]=='('):
            if newsentence[i+1] not in capitalVariables:
                substitution=variables.get(newsentence[i+1])
                positionsofvariable[i+1]=i+1
                if not substitution :
                    variables[newsentence[i+1]]=variableArray[number]
                    newsentence[i+1]=variableArray[number]
                    number+=1
                else:
                    newsentence[i+1]=substitution
    return  "".join(newsentence)            

def insidestandardizationnew(sentence):
    lengthofsentence=len(sentence)
    newsentence=sentence
    variables=collections.OrderedDict()
    positionsofvariable=collections.OrderedDict()
    global number
    i=0
    while i <=len(newsentence)-1 :
        if(newsentence[i]==',' or newsentence[i]=='('):
            if newsentence[i+1] not in capitalVariables:
               j=i+1
               while(newsentence[j]!=',' and newsentence[j]!=')' ):
                     j+=1
               substitution=variables.get(newsentence[i+1:j])
               if not substitution :
                    variables[newsentence[i+1:j]]=variableArray[number]
                    newsentence=newsentence[:i+1]+variableArray[number]+newsentence[j:]
                    i=i+len(variableArray[number])
                    number+=1
               else:           
                    newsentence=newsentence[:i+1]+substitution+newsentence[j:]
                    i=i+len(substitution)
        i+=1
    return newsentence

def replace(sentence,theta):
    lengthofsentence=len(sentence)
    newsentence=sentence
    i=0
    while i <=len(newsentence)-1 :
        if(newsentence[i]==',' or newsentence[i]=='('):
            if newsentence[i+1] not in capitalVariables:
               j=i+1
               while(newsentence[j]!=',' and newsentence[j]!=')' ):
                     j+=1
               nstemp=newsentence[i+1:j]      
               substitution=theta.get(nstemp)
               if substitution :
                    newsentence=newsentence[:i+1]+substitution+newsentence[j:]
                    i=i+len(substitution)
        i+=1   
    return newsentence    

repeatedsentencecheck=collections.OrderedDict()

def insidekbcheck(sentence):
    lengthofsentence=len(sentence)
    newsentence=pattern.split(sentence)
    newsentence.sort()
    newsentence="|".join(newsentence)
    global repeatedsentencecheck 
    i=0
    while i <=len(newsentence)-1 :
        if(newsentence[i]==',' or newsentence[i]=='('):
            if newsentence[i+1] not in capitalVariables:
               j=i+1
               while(newsentence[j]!=',' and newsentence[j]!=')' ):
                     j+=1
               newsentence=newsentence[:i+1]+'x'+newsentence[j:]
        i+=1
    repeatflag=repeatedsentencecheck.get(newsentence)
    if repeatflag :
        return True
    repeatedsentencecheck[newsentence]=1    
    return False                           



for i in range(n+2,n+2+k):
     data1[i]=data1[i].replace(" ","") 
     if "=>" in data1[i]:
        data1[i]=data1[i].replace(" ","") 
        sentencetemp=CNF(data1[i].rstrip())
        kbbefore.append(sentencetemp)
     else:
        kbbefore.append(data1[i].rstrip())  
for i in range(0,k):
    kbbefore[i]=kbbefore[i].replace(" ","") 

kb={}
pattern=re.compile("\||&|=>") #we can remove the '\|'' to speed up as 'OR' doesnt come in the KB
pattern1=re.compile("[(,]")
for i in range(0,k):   
    kbbefore[i]=standardizationnew(kbbefore[i])
    temp=pattern.split(kbbefore[i])
    lenoftemp=len(temp)
    for j in range(0,lenoftemp):
        clause=temp[j]
        clause=clause[:-1]
        predicate=pattern1.split(clause)
        argumentlist=predicate[1:]
        lengthofpredicate=len(predicate)-1
        if predicate[0] in kb:
            if lengthofpredicate in kb[predicate[0]]:
                kb[predicate[0]][lengthofpredicate].append([kbbefore[i],temp,j,predicate[1:]])
            else:
                kb[predicate[0]][lengthofpredicate]=[kbbefore[i],temp,j,predicate[1:]]
        else:
            kb[predicate[0]]={lengthofpredicate:[[kbbefore[i],temp,j,predicate[1:]]]}

for qi in range(0,n):
    queries[qi]=standardizationnew(queries[qi])

def substituevalue(paramArray, x, y):
    for index, eachVal in enumerate(paramArray):
        if eachVal == x:
            paramArray[index] = y
    return paramArray

def unificiation(arglist1,arglist2):
    theta = collections.OrderedDict()
    for i in range(len(arglist1)):
        if arglist1[i] != arglist2[i] and (arglist1[i][0] in capitalVariables) and (arglist2[i][0] in capitalVariables):
            return []
        elif arglist1[i] == arglist2[i] and (arglist1[i][0] in capitalVariables) and (arglist2[i][0] in capitalVariables):
            if arglist1[i] not in theta.keys():
                theta[arglist1[i]] = arglist2[i]
        elif (arglist1[i][0] in capitalVariables) and not (arglist2[i][0] in capitalVariables):
            if arglist2[i] not in theta.keys():
                theta[arglist2[i]] = arglist1[i]
                arglist2 = substituevalue(arglist2, arglist2[i], arglist1[i])
        elif not (arglist1[i][0] in capitalVariables) and (arglist2[i][0] in capitalVariables):
            if arglist1[i] not in theta.keys():
                theta[arglist1[i]] = arglist2[i]
                arglist1 = substituevalue(arglist1, arglist1[i], arglist2[i])   
        elif not (arglist1[i][0] in capitalVariables) and not (arglist2[i][0] in capitalVariables):
            if arglist1[i] not in theta.keys():
                theta[arglist1[i]] = arglist2[i]
                arglist1 = substituevalue(arglist1, arglist1[i], arglist2[i])
            else:
                argval=theta[arglist1[i]]
                theta[arglist2[i]]=argval
                arglist2 = substituevalue(arglist2, arglist2[i], argval)               
    return [arglist1,arglist2,theta]

def resolution():
    global repeatedsentencecheck
    answer=list()
    qrno=0
    for qr in queries:
        qrno+=1
        repeatedsentencecheck.clear()
        q=queue.Queue()
        query_start=time.time()
        kbquery=copy.deepcopy(kb)
        ans=qr
        if qr[0]=='~':
            ans=qr[1:]
        else:
            ans='~'+qr
        q.put(ans)

        currentanswer="FALSE"
        counter=0
        while True:
            counter+=1
            if q.empty():
                break
            ans=q.get()

            ansclauses=pattern.split(ans)
            lenansclauses=len(ansclauses)
            flagmatchedwithkb=0
            innermostflag=0
            for ac in range(0,lenansclauses):
                insidekbflag=0
                ansclausestruncated=ansclauses[ac][:-1]
                ansclausespredicate=pattern1.split(ansclausestruncated)
                lenansclausespredicate=len(ansclausespredicate)-1
                if ansclausespredicate[0][0]=='~':
                    anspredicatenegated=ansclausespredicate[0][1:]
                else:
                    anspredicatenegated="~"+ansclausespredicate[0]   
                x=kbquery.get(anspredicatenegated,{}).get(lenansclausespredicate)
                if not x:
                    continue      
                else:
                    lenofx=len(x)
                    for numofpred in range(0,lenofx):
                        insidekbflag=0
                        putinsideq=0
                        sentenceselected=x[numofpred]
                        thetalist=unificiation(copy.deepcopy(sentenceselected[3]),copy.deepcopy(ansclausespredicate[1:]))
                        if(len(thetalist)!=0):
                            for key in thetalist[2]:
                                tl=thetalist[2][key]
                                tl2=thetalist[2].get(tl)
                                if tl2:
                                    thetalist[2][key]=tl2
                            flagmatchedwithkb=1
                            notincludedindex=sentenceselected[2]
                            senclause=copy.deepcopy(sentenceselected[1])
                            mergepart1=""
                            del senclause[notincludedindex]
                            ansclauseleft=copy.deepcopy(ansclauses)
                            del ansclauseleft[ac]
                            for am in range(0,len(senclause)):
                                senclause[am]=replace(senclause[am],thetalist[2])
                                mergepart1=mergepart1+senclause[am]+'|'      
                            for remain in range(0,len(ansclauseleft)):
                                listansclauseleft=ansclauseleft[remain]
                                ansclauseleft[remain]=replace(listansclauseleft,thetalist[2])
                                if ansclauseleft[remain] not in senclause:
                                    mergepart1=mergepart1+ansclauseleft[remain]+'|'
                            mergepart1=mergepart1[:-1]
                            if mergepart1=="": 
                               currentanswer="TRUE"
                               break                             
                            ckbflag=insidekbcheck(mergepart1)
                            if not ckbflag:
                                    mergepart1=insidestandardizationnew(mergepart1)  
                                    ans=mergepart1
                                    temp=pattern.split(ans)
                                    lenoftemp=len(temp)
                                    for j in range(0,lenoftemp):
                                        clause=temp[j]
                                        clause=clause[:-1]
                                        predicate=pattern1.split(clause)
                                        argumentlist=predicate[1:]
                                        lengthofpredicate=len(predicate)-1
                                        if predicate[0] in kbquery:
                                            if lengthofpredicate in kbquery[predicate[0]]:
                                                kbquery[predicate[0]][lengthofpredicate].append([mergepart1,temp,j,argumentlist])
                                            else:
                                                kbquery[predicate[0]][lengthofpredicate]=[[mergepart1,temp,j,argumentlist]]
                                        else:
                                            kbquery[predicate[0]]={lengthofpredicate:[[mergepart1,temp,j,argumentlist]]}
                                    q.put(ans)                           
                    if(currentanswer=="TRUE"):
                        break                        
            if(currentanswer=="TRUE"):
               break
            if(counter==2000 or (time.time()-query_start)>20):
                break    
        answer.append(currentanswer)
    return answer  

if __name__ == '__main__': 
    finalanswer=resolution()
    o=open("output.txt","w+")
    wc=0
    while(wc < n-1):
         o.write(finalanswer[wc]+"\n")
         wc+=1
    o.write(finalanswer[wc])
    o.close()