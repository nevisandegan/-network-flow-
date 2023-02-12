import copy
import random
import time

import numpy as np

firstnode=np.array([(0,20,20,20,20,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                    (0,0,0,0,0,0,10,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                    (0,0,0,0,0,0,6,5,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                    (0,0,0,0,0,0,0,5,6,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                    (0,0,0,0,0,0,0,0,10,4,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                    (0,0,0,0,0,0,0,0,0,10,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0) ,
                    (0,0,0,0,0,0,0,0,0,0,0,15,0,15,0,0,0,0,0,0,0,0,0,0,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,15,0,15,0,0,0,0,0,0,0,0,0,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,15,0,0,0,0,0,0,0,0,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,0,0,0,0,0,0,0,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,0,0,0,0,0,0,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,0,0,0,0,0,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,0,0,0,0,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,0,0,0,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,25,0,0,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,25,20,0,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,10,25,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,25,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40),
                    (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                  ],dtype="object")

din=copy.deepcopy(firstnode)
din=din.T
def c(data):
  temp=[]
  for x in range(len(data)):
    temp2=-1
    for y in range(len(data[x])):
     if data[x][y] != 0:
       if temp2!=x:
        temp.append([])
       temp2=x
       temp[x].append(y)
  count=[]
  sumin=[]
  for x in temp:
    count.append(len(x))
  for x in data.T:
    sumin.append(sum(x))
  return sumin
def out(data):
    temp = []
    for x in range(len(data)):
        temp2 = -1
        for y in range(len(data[x])):
            if data[x][y] != 0:
                if temp2 != x:
                    temp.append([])
                temp2 = x
                temp[x].append(y)
    count = []
    sumout = []
    for x in temp:
        count.append(len(x))
    for x in data:
        sumout.append(sum(x))

    return sumout
rand = [[0]]
def generation(data, k=1):
    global rand
    temp = []
    for x in range(len(data)):
        temp2 = -1
        for y in range(len(data[x])):
            if data[x][y] != 0:
                if temp2 != x:
                    temp.append([])
                temp2 = x
                temp[x].append(y)
    count = []
    for x in temp:
        count.append([len(x)])
    count.append([0])
    for x in count[k]:
        t = -1
        for y in range(x):
            if t != x:
                rand.append([])
                t = x
            tempout = out(data)
            tempin=c(data)
            if (tempout[k] != 0):
              if x==1:
                try:
                  rand[k].append(random.randint(tempin[k], tempin[k]))
                except:
                  rand[k].append(random.randint(1, tempin[k]))
              if x==2:
                if y==0:
                  try:
                     tt=random.randint(1, (tempin[k]-10))
                     rand[k].append(tt)
                  except:
                    tt=random.randint(1, (tempin[k]-2))
                    rand[k].append(tt)
                if y==1:
                  rand[k].append((tempin[k]-tt))
              if x==3:
                rand[k].append(random.randint(1, tempin[k]))
                while sum(rand[k])>tempin[k]:
                  rand[k].clear()
                  for y in range(x):
                    rand[k].append(random.randint(1, tempin[k]))
    for x in range(k, k + 1):
        z = 0
        for y in range(len(data[x])):
            if data[x][y] != 0:
                data[x][y] = rand[x][z]
                z += 1
    if k < len(data) - 2:
        k += 1
        generation(data, k)
    elif k == 23:
        for x in count[k]:
            t = -1
            for y in range(x):
                if t != x:
                    rand.append([])
                    t = x
                tempout = out(data)
                if (tempout[k] != 0):
                    rand[k].append(random.randint(1, tempout[k]))

            while sum(rand[k]) != tempout[k]:
                rand[k].clear()
                for y in range(x):
                    rand[k].append(random.randint(1, tempout[k]))
    return data
def fitness(data):
    tempin=c(data)
    tempout=out(data)
    tempfitness=[]
    for x in range(1,24):
        t=(tempin[x]-tempout[x])
        tempfitness.append(t)
    fit=0
    for x in tempfitness:
        if x==0:
            fit+=10
    t=[]
    for x in range(21,24):
        t.append(tempout[x])
    fit+=sum(t)
    # if 80<sum(t):
    #     fit+=1
    for x in range(1,24):
        tw=(tempin[x]-tempout[x])
        if tw<0:
            fit+=tw
    return fit


def crossover(a,b):
    randa=random.randint(1,24)
    randb=random.randint(15,24)
    childa=copy.deepcopy(a)
    childb=copy.deepcopy(b)
    for x in range(randa):
        childa[x]=b[x]
        childb[x] = a[x]
    # while randb<24:
    #     childa[randb] = b[randb]
    #     childb[randb] = a[randb]
    #     randb+=1


    return childa,childb

def insertion_sort(arr, simulation=False):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] < cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor


    return arr
# def mtn(data):
#     r=random.randint(1,24)
#     tempin=copy.deepcopy(c(data))
#     tempout=copy.deepcopy(out(data))
#     tempindata=tempin[r]
#     tempoutdata=tempout[r]
#     if tempindata-tempoutdata!=0:
#         rr=random.randint(1,tempindata)
#
#
#
#     return data
#


fit=0
tempfit=[0,0,0,0]
x=[0,0,0,0]
x[0]=copy.deepcopy(firstnode)
x[1]=copy.deepcopy(generation(firstnode))
x[2]=copy.deepcopy(generation(firstnode))
x[3]=copy.deepcopy(generation(firstnode))
while fit<100:
    child=[]
    tempfit[0]=copy.deepcopy(fitness(x[0]))
    tempfit[1]=copy.deepcopy(fitness(x[1]))
    tempfit[2]=copy.deepcopy(fitness(x[2]))
    tempfit[3]=copy.deepcopy(fitness(x[3]))
    fitsort=copy.deepcopy(sorted(tempfit,reverse=True))
    for w in range(4):
        for y in range(4):
            if fitsort[w]==tempfit[y]:
                temp=copy.deepcopy(x[y])
                x[w]=copy.deepcopy(x[y])
                x[y]=copy.deepcopy(temp)

    child=copy.deepcopy(crossover(x[0],x[1]))
    x[2]=copy.deepcopy(child[0])
    x[3] = copy.deepcopy(child[1])

    fit+=1
    f=fit%5
    # if f==0:
    #     x[0]=copy.deepcopy(mtn(x[0]))
    finish=copy.deepcopy(x[0])

print(c(finish))
print(out(finish))
print(finish)
