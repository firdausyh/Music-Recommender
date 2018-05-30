import numpy
dataDir='D:/627/Project/Python/YahooMusic_MatrixFactorization/Python_dataProcess/Data/'
file_name_output1=dataDir + 'MF_combine.txt'
score_file= dataDir + 'subresult_MF_simpleRule.txt'
result_file= dataDir + 'result_MF_simpleRule.txt'

fOutput= open(file_name_output1, 'r')
fOut = open(score_file, 'w')

weigh=[1,0.34,0.6]
for line in fOutput:
    arr_output=line.strip().split('|')
    arr_len=len(arr_output)#Redudant elements existed, since '|' at end of data
    m=0
    subResult=0
    for j in range(2,5):
        rates=float(arr_output[j])
        if rates!=-1.0:
            m=m+1
            subResult=subResult+weigh[m-2]*rates
            
    if subResult==0:
        subResult==0                
    #else:
        #subResult=subResult/m
                    
    
    
    fOut.write(str(subResult)+'\n')    
    
                                      


    
fOutput.close()
fOut.close()

fScore= open(score_file, 'r')
fOut = open(result_file, 'w')

fScore= open(score_file, 'r')
fOut = open(result_file, 'w')

ii=0
count=0
outstr=''
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
            #put the highest three value as"1"
            #could be changed to lowest 3 value as"0" by change zeros martix to ones
            #max function to min 

            
            for jj in range(0,6):
                
                outstr=str(int(pt[jj,0]))
                fOut.write(outstr+'\n')




        outstr=''
        pt=numpy.zeros(shape=(6,1))
 

print('The number of result:',count)       
fScore.close()
fOut.close()
