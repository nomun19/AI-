
#%%
import numpy as nm
import pandas as pd
from sklearn import preprocessing
#from sklearn import preprocessing

lr=0.2
iteration= 5
lr

#%%
#testiin ogogdloo unshih
testdf=pd.read_csv("cs-test.csv")
testdf.head(10)
#%%
#surgaltiiin ogogdloo unshih
trainingdf=pd.read_csv("cs-training.csv")
#surgaltiin ogogdol deerh NA utguudiig hasah
trainingdf = trainingdf.dropna()
trainingdf.head(10)
#%%
#surgaltiin ogogdliin bagnuudiin neriig harh
columnName=trainingdf.columns
columnName

#%%
#surgaltiin ogogdluudiin baga dahi utguudiidg avh
train_y=trainingdf["SeriousDlqin2yrs"].values
train_x=trainingdf[['RevolvingUtilizationOfUnsecuredLines', 'age',
       'NumberOfTime30-59DaysPastDueNotWorse', 'DebtRatio', 'MonthlyIncome',
       'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
       'NumberRealEstateLoansOrLines', 'NumberOfTime60-89DaysPastDueNotWorse',
       'NumberOfDependents']].values
#train_x-iin utgiig normalchilah
train_x=preprocessing.normalize(train_x)
train_x



#%%
#testiin ogogdliin bagana dahi utguudiig avah
test_y=testdf["SeriousDlqin2yrs"].values
testNotNan=testdf[['RevolvingUtilizationOfUnsecuredLines', 'age',
       'NumberOfTime30-59DaysPastDueNotWorse', 'DebtRatio', 'MonthlyIncome',
       'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
       'NumberRealEstateLoansOrLines', 'NumberOfTime60-89DaysPastDueNotWorse',
       'NumberOfDependents']].dropna()
test_x=testNotNan.values
#tsetiin gogdluudiig normalchlah
test_x=preprocessing.normalize(test_x)
test_x.shape
#%%
#random-oor a-iin utguuig avch w  husnegted hadgalah
w=nm.random.rand(10)


#%%
i=0
sum1=0
j=0
k=0
#mor bur deer bodoj gargasan lose-iig hadgalah husnegt 
a=nm.zeros(train_x.shape)
sumA=0
#iteration bur deer omnoh gargasn a-gaa ashiglaj yvna
for i in range(iteration):
    print(i)
    #train_x -iin hemjeeger davtana "train_x-d NA utga bhgui bgaa"
    for j in range(len(train_x)):
        #10 baganatai
        for k in  range(10):
            sum1=0
            #bagana buriin utgiig a-giin hargalzah utgaar urjuulj tuhain bagana dahi ogogdluudiig hargalzah a-gaar upjuulsen utguudiin niilber
            for m in range(10):
                sum1=w[m]*train_x[j][m]+sum1
            #niilberees ulamjlal avch lose-oo olno
            l=2*(train_y[j]-sum1)*train_x[j][k]
            #olson lose-uudaa husnegted hadgalna
            a[j][k] = l
    loss = nm.zeros(10)
    #1 iteration yvaj duusahad olson lose-uudiinhaa bagana tus bur deerh dundaj lose-iig bodno 
    loss = nm.sum(a,axis=0)/len(train_x)
    #bagana tus bur deerh dundaj lose-uud hervee 0-oos ih bol w- dahi hargalzah utgiig alhamaaraa nemegduulne 
    #herev baga bol w- dahi hargalzah utgiig alhmaaraa hopogduulna
    for j in range(10):
        if loss[j]>0:
            w[j]=w[j]+lr
        else :
            w[j]=w[j]-lr
        
w                

#%%
i=0
j=0
#testiin ogogdluud deer ajilsan utguudiig hadgalah husnegt
res=[]
sum2=0
#test_x-iin hemjeegeer davtana
for i in range(len(test_x)):
    sum2 = 0
    #bagana tus bureer guij w-iin hargalzah utgaaar urjuulne
    for j in range(10):
        sum2=(sum2+w[j]*test_x[i][j])
    #tuhain mopiin niilberiig  olj dundajiig avah
    sum2=sum2/10 
    #husnegted dundaj utguudiig hadgalna
    res.append(sum2)
    print(sum2)
    
#%%
#testiin ogogdloo unshih "Unnamed" baganatai ni unshih ene ni tuhain testiin ogodluudiin id 
test_1 = testdf[['Unnamed: 0', 'RevolvingUtilizationOfUnsecuredLines', 'age',
       'NumberOfTime30-59DaysPastDueNotWorse', 'DebtRatio', 'MonthlyIncome',
       'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
       'NumberRealEstateLoansOrLines', 'NumberOfTime60-89DaysPastDueNotWorse',
       'NumberOfDependents']]
#NA utguudiig ustgah
test_2 = test_1.dropna()
#NA aguulaagui husnegtees ogogdol tus buriin id-iig avna
id_test = test_2['Unnamed: 0'].values
#dropna hiisnii daraah test-iin ogogdliin hemjee
print(id_test.shape)
print(id_test)
#%%
#taniltiiin ur dung huvilah
j=0
#taniltiin ur dun testiin hariutai her zopuutei bgaag hadgalah husnegt
answers = nm.zeros(len(res))
#testiin ogodliin hariug unshih
sample=pd.read_csv("sampleEntry.csv")
#probability baganiig unshih
sample_res=sample['Probability'].values
#hargalzah id-iig unshih
id_sample = sample['Id'].values
sample.columns
#niit ogogdliin hemjeegeer davtah
for i in range(len(id_sample)):
    #hervee testiin gogdliin hariun dahi id ni dropna hiigdsen esehiig shalgaj herev dropna hiigdsen bol tuhain id-tai ogogdliig algasna
    #herev dropna hiigdeegui id-tai bol bodoj gargasn surgaltiin ur dun testiin ur dungees her zopuutei bgaag olj 0.03aas bga bol tanisan gej uzej answers husnegt ruu hadgalna
    if id_sample[i] == id_test[j]:
        if abs(sample_res[i] - res[j]) < 0.03:
            answers[j] = 1
        j = j + 1                                                                                        
#niit heden ogogdol tanisan gedgees taniltiin huiig todorhoilno
accuracy = sum(answers)/len(answers)
print(accuracy)



    

