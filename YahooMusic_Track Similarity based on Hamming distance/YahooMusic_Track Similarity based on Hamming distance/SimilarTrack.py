#accuracy: 0.7282.
#algorithm: Estimation based on Similarity. Score=sum(similarity*score)/sum(similarity).
#input file: "trackData2.txt"; "testIdx2_matrix.txt" ; "trainIdx2.txt"
#output file: "Result_simTrack.txt" Format:Score range from 0 to 100.

############################################## Directory & File setting ########################################
dataDir = 'D:/627/Project/Python/YahooMusic_Similarity/'
file_track = dataDir + 'trackData2.txt'
file_test = dataDir + 'testIdx2_matrix.txt'
file_train = dataDir + 'trainIdx2.txt'
file_result = dataDir + 'Result_simTrack.txt'

############################################## Track_Hierarchy Reading & Store ##########################
#Creating a array, whose index in trackId and contents are album, artist and genre of this track.

track_hierachy=[[] for i in range(296111)]
fTrack = open(file_track,'r')
for line in fTrack:
    arr=line.strip().split('|')
    trackId=int(arr[0])
    length=len(arr)
    for i in range(length):
        track_hierachy[trackId].append(arr[i])    
    
fTrack.close()

############################################## Similarity Computing ####################################
#Hamming Distance.
#Features are album,artist and genres of a track.
#Tracks that have more than five matched featurescan be said totally same.
def similarity_track(test,train):
    if train==[]:
        return 0
    else:
        trackId_test=test[0]
        trackId_train=train[0]
        #record identical items
        sim_count=0
        length_test=len(test)
        length_train=len(train)
        for i in range(length_test):
            if test[i]=='None':
                continue
            for j in range(0,length_train):
                if test[i]==train[j]:
                    sim_count+=1
        if sim_count>=5:
            sim=1
        elif sim_count==0:
            sim=0
        else:
            sim=sim_count/5
        return sim
#Weigh on features for similarity calculation    
def similarity_track_weigh(test,train):
    if train==[]:
        return 0

    else:
        trackId_test=test[0]
        trackId_train=train[0]
        #record identical items
        sim_count=0
        length_test=len(test)
        length_train=len(train)
        if test[1]==train[1]:
            if test[1]!='None':
                sim_count+=3.5
        if test[2]==train[2]:
            if test[2]!='None':
                sim_count+=4.5
        for i in range(2,length_test):
            if test[i]=='None':
                continue
            for j in range(3,length_train):
                if test[i]==train[j]:
                    sim_count+=1
        if sim_count>10:
            sim=1
        elif sim_count==0:
            sim=0
        else:
            sim=sim_count/10
        return sim

############################################## Retrieving Scores of Similar tracks ####################################
def RetrieveTrain(TrainStream,userId_test):
    line=TrainStream.readline()
    arr=line.strip().split('|')
    userId = arr[0]
    ratings = int(arr[1])
    train=[[],[]]
    if len(arr)!=2:
        print('Error occurs while extract training infor')
    elif userId != userId_test:
        for i in range(ratings):
            TrainStream.readline()
        return [True]
    elif userId == userId_test:
        for i in range(ratings):
            line = TrainStream.readline()
            arr_train = line.strip().split('\t')
            train[0].append(arr_train[0])
            train[1].append(arr_train[1])
        return [False,train]
    else:
        print('Error!')
            
    
        

fTrain = open(file_train,'r')
fTest = open(file_test,'r')
fOut = open(file_result,'w')

############################################## Estimation based on Similarity ####################################
test=[]
train=[[],[]]
m=0
count=0
for line in fTest:
    arr_test = line.strip().split('|')
    userId_test=arr_test[0]
    test.append(arr_test[1])    
    m+=1
    if m==6:
        run=True
        while run:
            temp=RetrieveTrain(fTrain,userId_test)
            run=temp[0]
            if run==False:
                train[0] = temp[1][0]
                train[1] = temp[1][1]
        #Estimation using first highest three similarity 
        for i in range(6):
            first_sim=-1
            first_score=0
            second_sim=-1
            second_score=0
            third_sim=-1
            third_score=0
            den=0
            sum_sim=0
            for j in range(len(train[0])):
                index_test=int(test[i])
                index_train=int(train[0][j])
                score=float(train[1][j])
                sim=similarity_track(track_hierachy[index_test],track_hierachy[index_train])
                if sim>first_sim:
                    third_sim=second_sim
                    third_score=second_score
                    
                    second_sim=first_sim
                    second_score=first_score
                    
                    first_sim=sim
                    first_score=score
                    continue
                elif sim>second_sim:
                    third_sim=second_sim
                    third_score=second_score

                    second_sim=sim
                    second_score=score
                    continue
                elif sim>third_sim:
                    third_sim=sim
                    third_score=score
                    continue
                    
            den = first_sim + second_sim + third_sim
            sum_sim = first_sim*first_score + second_sim*second_score + third_sim*third_score
            
            if den==0:
                result=0
            else:
                result=sum_sim/den
            #Output file: "Result_simTrack.txt"
            fOut.write(str(result)+'\n')
            count+=1
        test=[]
        m=0
        train=[[],[]]
            

fTrain.close()
fTest.close()
fOut.close()
