library(readxl)
rData <- read_excel("Train_data.xlsx", col_names = FALSE)
rData1 <- rData[-1]
Train <- rData1[-1]
dim(Train)

tData <- read_excel("Test_data.xlsx", col_names = FALSE)
tData1 <- tData[-1]
Test <- tData1[-1]
dim(Test)

library(rpart)
library(rpart.plot)
library(rattle)
library(RColorBrewer)

treemodel <- rpart(Train$X20~., data=Train,method ="class", parms = list(prior = c(.503,.497),split = "information"), control = rpart.control(minsplit = 3, cp = 0))
plot(treemodel)
text(treemodel)
fancyRpartPlot(treemodel)

treemodel2<- prune(treemodel, cp = 0.1)
plot(treemodel2)
fancyRpartPlot(treemodel2)
prediction1 <- predict(treemodel2, Test, type="class")
write.csv(prediction1, "result_tree2.csv", row.names=FALSE)


