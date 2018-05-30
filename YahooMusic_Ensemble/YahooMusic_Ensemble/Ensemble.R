result1<-read.table("result_MF_simpleRule.txt")
result2<-read.table("result_simpleRule.txt")
result3<-read.table("Bresult_simpleRule_[0.8,0.45,0.06].txt")
result4<-read.table("forward-backward method.txt")
result5<-read.table("forward-backward weighted method (0.7 0.25 0.05).txt")
result6<-read.table("Result_simTrack_binary.txt")
result7<-read.table("tree2.txt")


#result1<-rbind(1,result1)
#result2<-rbind(0,result2)
#result3<-rbind(0,result3)
#result4<-rbind(0,result4)
#result5<-rbind(0,result5)
#result6<-rbind(0,result6)
#result7<-rbind(0,result7)



result=cbind(result1,result2,result3,result4,result5,result6,result7)
result=as.matrix(2*result-1)

s=matrix(c(0.7064,0.7957,0.8554,0.8566,0.8678,0.7282,0.6287),nrow=7)
s=2*s-1

a=solve(t(result)%*%result)%*%(s*(94290))

re_result=result%*%a

write.csv(re_result,file="re_result.csv")