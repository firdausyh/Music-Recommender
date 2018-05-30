import numpy as np
dataDir = 'D:/627/Project/Python/YahooMusic_Attributes&ML/'
file_track = dataDir + 'trackData2.txt'
file_train = dataDir + 'trainIdx2_matrix.txt'
file_test = dataDir + 'testTrack_hierarchy_win.txt'
file_out = dataDir + 'test_attributs.txt'
file_hashMap = 'D:/627/Project/Python/DataProcess/Files/train_hashmap.pkl'
       

############################################# Pre-Processing ################################################
#Creating a array, whose index is itemId.
#Array cell store similar items.
#For example: track 1 and track 2 have the same Album 3. Consequently, it store 1 and 2 in items[3].
items=[[] for i in range(300000)]
fRead = open(file_track,'r')
for line in fRead:
    genreId=[]
    arr=line.strip().split('|')
    if arr[1]=='None':
        arr[1]='299998'
    if arr[2]=='None':
        arr[2]='299998'
    albumId=int(arr[1])
    artistId=int(arr[2])
    TrackId=int(arr[0])
    for i in range(3,len(arr)):
        genreId.append(int(arr[i]))        
    items[albumId].append(TrackId)
    items[artistId].append(albumId)
    for i in range(len(genreId)):
        items[genreId[i]].append(artistId)
fRead.close()

#This function creates a key for Hashmap object
def createKey(arr1,arr2):
    return str(arr1+','+arr2)

#This function searchs similar artist
#It selects two set of similar artist set by set size
def SimArtist(userId,simArtist,hashmap,length):
    if length==0:
        str0=['0 0 0 0','0 0 0 0']
        return str0
    elif length==1:
        vec_artist=[]
        count_artist=0
        for i in range(len(simArtist)):
            temp=createKey(userId,str(simArtist[i]))
            if hashmap.get(temp)!= None:
                vec_artist.append(float(hashmap.get(temp)))
                count_artist+=1
        if len(vec_artist)==0:
            mean_artist = 0     
            max_artist = 0    
            min_artist = 0   
        else:
            mean_artist=np.mean(vec_artist)     
            max_artist=max(vec_artist)    
            min_artist=min(vec_artist)
        str1=[str(min_artist)+' '+str(max_artist)+' '+str(mean_artist)+' '+str(count_artist),'0 0 0 0']
        return str1
    
    else:
        vec_artist=[[] for i in range(length)]
        count_artist=[0]*length
        for m in range(length):
            for i in range(len(simArtist[m])):
                temp=createKey(userId,str(simArtist[m][i]))        
                if hashmap.get(temp)!=None:
                    vec_artist.append(float(hashmap.get(temp)))
                    count_artist[m]+=1
        mark=[0,0]
        for i in range(length):
            if count_artist[i]==max(count_artist):
                mark[0]=i
                temp=count_artist[i]
                count_artist[i]=-1
                break
        for i in range(length):
            if count_artist[i]==max(count_artist):
                mark[1]=i
                count_artist[mark[0]]=temp
                break
        
        output=[]
        if len(vec_artist[mark[0]])==0:
            mean_artist1 = 0     
            max_artist1 = 0    
            min_artist1 = 0   
        else:
            mean_artist1=np.mean(vec_artist[mark[0]])     
            max_artist1=max(vec_artist[mark[0]])   
            min_artist1=min(vec_artist[mark[0]])
            
        output.append(str(min_artist1)+' '+str(max_artist1)+' '+str(mean_artist1)+' '+str(count_artist[mark[0]]))
        if len(vec_artist[mark[1]])==0:
            mean_artist2 = 0     
            max_artist2 = 0    
            min_artist2 = 0   
        else:
            mean_artist2=np.mean(vec_artist[mark[1]])    
            max_artist2=max(vec_artist[mark[1]])    
            min_artist2=min(vec_artist[mark[1]])
        output.append(str(min_artist1)+' '+str(max_artist1)+' '+str(mean_artist1)+' '+str(count_artist[mark[1]]))
        return output


                                
#############################################creating attributes############################################
fTest = open(file_test,'r')
fOut = open(file_out,'w')
ii=0

for line in fTest:
    vec_track=[]
    vec_album=[]
    count_track=0
    count_album=0
    temp=''
    arr = line.strip().split('|')
    
    if arr[2]=='None':
        albumId=299999
    else:
        albumId=int(arr[2])
        
    if arr[3]=='None':
        artistId=299999
    else:
        artistId=int(arr[3])
                        
    genreId=[]
    genre_num=len(arr)-4                    
    for i in range(4,len(arr)):
        genreId.append(int(arr[i]))
        
    simArtist=[[] for i in range(genre_num)]
    for i in range(genre_num):
        simArtist[i]=items[genreId[i]]    
    userId=int(arr[0])
    trackId=int(arr[1])
    #Search similar tracks
    simTrack=items[albumId]
    #Search similar albums
    simAlbum=items[artistId]

    
    for i in range(len(simTrack)):
        temp=createKey(arr[0],str(simTrack[i]))
        if hashmap.get(temp)!=None:
            vec_track.append(float(hashmap.get(temp)))
            count_track+=1
        
    for i in range(len(simAlbum)):
        temp=createKey(arr[0],str(simAlbum[i]))        
        if hashmap.get(temp)!=None:
            vec_track.append(float(hashmap.get(temp)))
            count_album+=1
        
                        
    artistAtt = SimArtist(arr[0],simArtist,hashmap,genre_num)
    
    #Computing the attributes scores
    if len(vec_track)==0:
        mean_track = 0
        max_track = 0
        min_track = 0
    else:
        mean_track=np.mean(vec_track)
        max_track=max(vec_track)
        min_track=min(vec_track)
    if len(vec_album)==0:
        mean_album = 0     
        max_album = 0    
        min_album = 0   
    else:
        mean_album=np.mean(vec_album)     
        max_album=max(vec_album)    
        min_album=min(vec_album)
    
    
    outStr=arr[0]+' '+arr[1]+' '+str(min_track)+' '+str(max_track)+' '+str(mean_track)+' '+str(count_track)+' '+str(min_album)+' '+str(max_album)+' '+str(mean_album)+' '+str(count_album)+' '
    fOut.write(outStr+' '+artistAtt[0]+' '+artistAtt[1]+'\n')
    ii+=1

    for i in range(len(simTrack)):
        temp=createKey(arr[0],str(simTrack[i]))
    
print(ii)
fOut.close()
fTest.close()
fOut.close()
