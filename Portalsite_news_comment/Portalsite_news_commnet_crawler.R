# Download Packages

install.packages("openxlsx")
install.packages("N2H4")
install.packages("vctrs")
install.packages("curl")
source("https://install-github.me/forkonlp/DNH4")
install.packages("remotes")
remotes::install_github("forkonlp/DNH4")
library(openxlsx)
library(dplyr)
library(N2H4)
library(DNH4)

getwd()
setwd()

# Naver's News comments crawling function

naver <- function(x){
  comments <- N2H4::getAllComment(turl = x)
  comments<-as.data.frame(comments)
  userName <- comments$userName
  contents <- comments$contents
  like <- comments$sympathyCount
  dislike <- comments$antipathyCount
  comments_fin <- data.frame(userName,contents,like,dislike)
  comments_fin<-comments_fin %>% arrange(desc(like)) 
  write.csv(comments_fin,paste0(substr(x,76,85),".csv"
  ),fileEncoding="euc-kr")
  
}

naver_url<-c()

naver_list<-c(naver_url)

for (i in naver_list){
  naver(i)
}

# Daum's News comments crawling function 

daum<-function(x){
  comments1<-DNH4::getComment(x, limit=100)
  comments1<-as.data.frame(comments1)
  userName<-comments1$user_displayName
  contents <- comments1$content
  like <- comments1$likeCount
  dislike <- comments1$dislikeCount
  Dcomments_fin <- data.frame(userName,contents,like,dislike)
  Dcomments_fin<-Dcomments_fin %>% arrange(desc(like)) 
  write.csv(Dcomments_fin,paste0(substr(x,40,43),".csv"),fileEncoding="euc-kr")
}

daum_url <- c()

daum_list<-c(daum_url)

for (i in daum_list){
  daum(i)
}