import re

a='D:/627/Project/Python/YahooMusic_MatrixFactorization/Python_dataProcess/Data/Album_result.txt'
b='D:/627/Project/Python/YahooMusic_MatrixFactorization/Python_dataProcess/Data/Artist_result.txt'
c='D:/627/Project/Python/YahooMusic_MatrixFactorization/Python_dataProcess/Data/Track_result.txt'
output_file='D:/627/Project/Python/YahooMusic_MatrixFactorization/Python_dataProcess/Data/MF_combine.txt'


fa=open(a,'r')
fb=open(b,'r')
fc=open(c,'r')
fOut=open(output_file,'w')
count=0
#key-value data structure ---- store scores
for line in fc:
    arr_track=line.strip().split('|')
    
    line_album=fa.readline()
    arr_album=line_album.strip().split('|')
    
    line_artist=fb.readline()
    arr_artist=line_artist.strip().split('|')

    outStr=arr_track[0]+'|'+arr_track[1]+'|'+arr_track[2]+'|'
    if arr_album[1]=='0':
        outStr=outStr+'-1'+'|'
    else:
        outStr=outStr+arr_album[2]+'|'
    if arr_artist[1]=='0':
        outStr=outStr+'-1'
    else:
        outStr=outStr+arr_album[2]
    count+=1
    fOut.write(outStr+'\n')
    outStr=''

    
fa.close()
fb.close()
fc.close()
fOut.close()

