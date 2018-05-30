#accuracy: 0.8554.
#algorithm: Hierarchy search with weigh value. Score=sum(weigh*score)
#input file: "ConciseData.txt" Format: UserId|ItemId|AlbumScore|ArtistScore|GenreScore(if have).
#output file: "score_simpleRule_[0.8,0.45,0.06].txt" Format:Scores range from 0 to 100.
#output file: "Bresult_simpleRule_[0.8,0.45,0.06].txt" Format:Like(1) or not(0).

import numpy

############################################## Directory & File setting ########################################################

dataDir='D:/627/Project/Python/YahooMusic_Collection/Files/'
file_name_output1=dataDir + 'ConciseData.txt'
score_file= dataDir + 'score_simpleRule_[0.8,0.45,0.06].txt'
result_file= dataDir + 'Bresult_simpleRule_[0.8,0.45,0.06].txt'
fOutput= open(file_name_output1, 'r')
fOut = open(score_file, 'w')

weigh=[0.8,0.45,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06]

############################################## Data Reading & Processing ########################################################
for line in fOutput:
    arr_output = line.strip().split('|')
    arr_len = len(arr_output)-1 #Redudant elements existed, since '|' at end of data
    m = 0
    subResult = 0
    
    for j in range(2,arr_len):
        rates=float(arr_output[j])
        if rates != -1.0:
            m = m+1
            subResult = subResult+weigh[j-2]*rates            
            
    if subResult == 0:
        subResult == 0                
    else:
        subResult = subResult
    #Output file: "score_simpleRule_[0.8,0.45,0.06].txt"   
    fOut.write(str(subResult)+'\n')    
    
fOutput.close()
fOut.close()


fScore= open(score_file, 'r')
fOut = open(result_file, 'w')


#put the highest three value as"1"
#could be changed to lowest 3 value as"0" by change zeros martix to ones 
ii=0
count=0
su_vec=[0]*6
pt=numpy.zeros(shape=(6,1))

for line in fScore:        
        arr_test=line.strip()
        su_vec[ii]= float(arr_test)
        count+=1
        ii=ii+1
        #every 6 lines output once
        if ii==6:
            ii=0
            for nn in range(0,6):
                if su_vec[nn]==max(su_vec):
                    pt[nn,0]=1
                    su_vec[nn]=-2000000
                    break
            
            for nn in range(0,6):
                if su_vec[nn]==max(su_vec):
                    pt[nn,0]=1
                    su_vec[nn]=-2000000
                    break
            for nn in range(0,6):
                if su_vec[nn]==max(su_vec):
                    pt[nn,0]=1
                    su_vec[nn]=-2000000
                    break
            
            for jj in range(0,6):                
                outstr=str(int(pt[jj,0]))
                #Output file: "Bresult_simpleRule_[0.8,0.45,0.06].txt"
                fOut.write(outstr+'\n')

        pt=numpy.zeros(shape=(6,1))
 

print('The number of result:',count)       
fScore.close()
fOut.close()



