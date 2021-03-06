from math import tanh,exp
import matplotlib.pyplot as plt
import numpy as np
def sigmoid(x):
	return(1/(1+np.exp(-x)))
stopwords = {'a',
 'about',
 'above',
 'after',
 'again',
 'against',
 'ain',
 'all',
 'am',
 'an',
 'and',
 'any',
 'are',
 'aren',
 "aren't",
 'as',
 'at',
 'be',
 'because',
 'been',
 'before',
 'being',
 'below',
 'between',
 'both',
 'but',
 'by',
 'can',
 'couldn',
 "couldn't",
 'd',
 'did',
 'didn',
 "didn't",
 'do',
 'does',
 'doesn',
 "doesn't",
 'doing',
 'don',
 "don't",
 'down',
 'during',
 'each',
 'few',
 'for',
 'from',
 'further',
 'had',
 'hadn',
 "hadn't",
 'has',
 'hasn',
 "hasn't",
 'have',
 'haven',
 "haven't",
 'having',
 'he',
 'her',
 'here',
 'hers',
 'herself',
 'him',
 'himself',
 'his',
 'how',
 'i',
 'if',
 'in',
 'into',
 'is',
 'isn',
 "isn't",
 'it',
 "it's",
 'its',
 'itself',
 'just',
 'll',
 'm',
 'ma',
 'me',
 'mightn',
 "mightn't",
 'more',
 'most',
 'mustn',
 "mustn't",
 'my',
 'myself',
 'needn',
 "needn't",
 'no',
 'nor',
 'not',
 'now',
 'o',
 'of',
 'off',
 'on',
 'once',
 'only',
 'or',
 'other',
 'our',
 'ours',
 'ourselves',
 'out',
 'over',
 'own',
 're',
 's',
 'same',
 'shan',
 "shan't",
 'she',
 "she's",
 'should',
 "should've",
 'shouldn',
 "shouldn't",
 'so',
 'some',
 'such',
 't',
 'than',
 'that',
 "that'll",
 'the',
 'their',
 'theirs',
 'them',
 'themselves',
 'then',
 'there',
 'these',
 'they',
 'this',
 'those',
 'through',
 'to',
 'too',
 'under',
 'until',
 'up',
 've',
 'very',
 'was',
 'wasn',
 "wasn't",
 'we',
 'were',
 'weren',
 "weren't",
 'what',
 'when',
 'where',
 'which',
 'while',
 'who',
 'whom',
 'why',
 'will',
 'with',
 'won',
 "won't",
 'wouldn',
 "wouldn't",
 'y',
 'you',
 "you'd",
 "you'll",
 "you're",
 "you've",
 'your',
 'yours',
 'yourself',
 'yourselves'}
"""
HAM  = 4827
SPAM = 747
Total= 5574
Training Data First 4460  Rows
Testing  Data Remaining 1114 Rows
"""
from nltk.stem.porter import PorterStemmer
import re
import random

data      = []
traindata = []
testdata  = []
datafl    = []
pred      = []
classify  = []
stemmer = PorterStemmer()
#stopwords = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
#PreProcessing
count = 0
tokens = set()
with open('Assignment_2_data.txt') as inputfile:
    for line in inputfile:
        temp = re.split("[\t]",line)
        x=re.split("[:;?!., \t\n-/()]",temp[1])
        for p in x:
            if p in stopwords:
                continue
            if p == '':
                continue
            q = stemmer.stem(p)
            tokens.add(q)
  
#SAMPLING 80% Random Data      
count = 0
for x in tokens:
    count += 1
print("Number of Distinct Tokens:",count)
#Number of Distinct Tokens: 7668
sampleindex = set()
data_index = []
for x in range(5574):
    data_index.append(x)
 
#Randomly Sampling 80% data for training
rand_smpl = random.sample(data_index, 4460)
#rand_smpl = range(4460)

temp = 0
trainoutput = []
testoutput  = []
with open('Assignment_2_data.txt') as inputfile:
    for line in inputfile:
        lp = re.split("[\t]",line)
        tp = re.split("[:;?!., \t\n-/()]",lp[1])
        if temp in rand_smpl:
            traindata.append(tp)
            if lp[0]=='ham':
                trainoutput.append(0)
            else:
                trainoutput.append(1)
        else:
            testdata.append(tp)
            if lp[0]=='ham':
                testoutput.append(0)
            else:
                testoutput.append(1)
        count += 1
        temp += 1
        
traintokens = []
testtokens  = []
for data in traindata:
    pr = []
    for x in data:
        if x in stopwords:
            continue
        q = stemmer.stem(x)
        pr.append(q)
    traintokens.append(pr)
for data in testdata:
    pr = []
    for x in data:
        if x in stopwords:
            continue
        q = stemmer.stem(x)
        pr.append(q)
    testtokens.append(pr)

tokenvec = []
tokenmap = []
tempval  = 1
for x in tokens:
    if not x:
        continue
    tokenvec.append(x)
    tokenmap.append(tempval)
    tempval += 1
print("YO",tempval)

"""
NEURAL NETWORK ARCHITECTURE:
    Input Layer    : 9485 tokens One Hot Encoding
    Hidden Layer 1 : 100 Neurons
    Hidden Layer 2 : 50  Neurons
    Output Layer   : 1 value (0 for HAM & 1 for SPAM)
"""
#PART 1A : Using sigmoid activation function
#Initializing weights by 1
layer1 = np.abs(np.random.randn(9485,100))/1000000
layer2 = np.abs(np.random.randn(100,50))/1000000
layer3 = np.abs(np.random.randn(50,1))/10000000

bias1  = np.array([0.1 for j in range(100)])
bias2  = np.array([0.1 for j in range(50)])
bias3  = np.array([0.1 for j in range(1)])

X0      = np.array([0.0 for j in range(9485)])
X1      = np.array([0.1 for j in range(100)])
X2      = np.array([0.1 for j in range(50)])
X3      = np.array([0.1 for j in range(1)])

S0      = np.array([0.1 for j in range(9485)])
S1      = np.array([0.1 for j in range(100)])
S2      = np.array([0.1 for j in range(50)])
S3      = np.array([0.1 for j in range(1)])

delta0      = np.array([0.1 for j in range(9485)])
delta1      = np.array([0.1 for j in range(100)])
delta2      = np.array([0.1 for j in range(50)])
delta3      = np.array([0.1 for j in range(1)])

err = []
accr = []
ind = []
qq = 1
learning_rate = 0.1
iteration = 15
while iteration>0:
    print(101-iteration)
    rand_pos = -1
    for x in traintokens:
        rand_pos += 1
        X0      = np.array([0.0 for j in range(9485)])
        #FEED FORWARD
        #INPUT LAYER
        temp = 0
        ll = 0
        for i in tokenvec:
        		status = 0
        		for j in x:
        			if i==j:
        				status = 1
        				break
        		if status == 1:
        			X0[temp] = 1
        		else:
        			X0[temp] = 0
        		temp += 1
        #print(X0)
        #HIDDEN LAYER 1
        S1 = np.dot(layer1.T,X0) + bias1
        X1 = sigmoid(S1)
        #HIDDEN LAYER 2
        S2 = np.dot(layer2.T,X1) + bias2
        X2 = sigmoid(S2)
        S3 = np.dot(layer3.T,X2) + bias3
        X3 = sigmoid(S3)
        #BACKPROP
        delta3 = 2*	(trainoutput[rand_pos] - X3)*X3*(1-X3)
        delta2 = X2*(1-X2)*np.dot(delta3,np.transpose(layer3))
        delta1 = X1*(1-X1)*np.dot(delta2,np.transpose(layer2))
        #print(delta3,trainoutput[rand_pos],X3)
        #delta0 = np.dot(delta1,np.transpose(layer1)*X0*(1-X0))
        #Updating Weights
        bias3 += learning_rate*delta3
        bias2 += learning_rate*delta2
        bias1 += learning_rate*delta1
        for j in range(100):
            layer1[:,j] += learning_rate*X0*delta1[j]
        for j in range(50):
            layer2[:,j] += learning_rate*X1*delta2[j]
        for i in range(50):
            layer3[i][0] += learning_rate*X2[i]*delta3[0]
    iteration-=1
    error = 0
    count = 0
    xxx   = 0
    yyy   = 0
    ans = []
    for x in traintokens:   """For Out Sample""" #for x in testtokens:
		    X0      = np.array([0.0 for j in range(9485)])
		    temp = 0
		    for i in tokenvec:
		        status = 0
		        for j in x:
		            if i==j:
		                status = 1
		                break
		        if status==1:
		            X0[temp] = 1
		        else:
		            X0[temp] = 0
		        temp += 1
		    S1 = np.dot(layer1.T,X0) + bias1
		    X1 = sigmoid(S1)
		    #HIDDEN LAYER 2
		    S2 = np.dot(layer2.T,X1) + bias2
		    X2 = sigmoid(S2)
		    S3 = np.dot(layer3.T,X2) + bias3
		    X3 = sigmoid(S3)
		    ans = 0
		    if X3[0]>=0.5:
		        ans = 1
		    else:
		        ans = 0
		    error +=  (trainoutput[count]-X3[0])**2        """For Out Sample""" #(testoutput[count]-X3[0])**2
		    if ans == trainoutput[count]:                  """For Out Sample""" #testoutput[count]
		        xxx += 1  
		    yyy += 1
		    count += 1
    print(" Error = ",error,xxx,yyy)
    print("Accuracy = ", xxx*100/yyy,"%")
    err.append(error)
    accr.append(xxx*100/yyy)
    ind.append(qq)
    qq += 1
    
plt.plot(ind,err)
plt.show()
plt.plot(ind,accr)
plt.show()
