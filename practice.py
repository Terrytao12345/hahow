
#class hahow 2-1

#使用者輸入自己的姓名和分數,我們讓第二個字取代成*,讓分數出來+10分
#王大明的分數 > 王*名的分數是68分

user = input('請輸入姓名 : \n ')
#user = user.replace(1,*)
score = input('請輸入分數 : \n ')
exscore = 10

print(user, score, '>', user.replace(user[1],"*"), '的分數是', int(score)+exscore, '分')


#老師解答 

name = input('whats your name : \n')
score1 = input('whats your score : \n')
hidename = name[0] + "*" + name[2:]
score1 = float(score1) + 10
print(hidename+'的分數是'+str(score1))