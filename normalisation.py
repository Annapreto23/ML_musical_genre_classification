import pandas as pd
from sklearn.preprocessing import StandardScaler

#Renvoie le DataFrame normalisé

X_train = pd.read_csv('data/all.csv') 
X_train = X_train.drop(['genre', 'mode', 'key', 'time_signature'], axis = 1)
standard_scaler = StandardScaler() 
standard_scaler.fit(X_train)   #On scale sur entrainement dataset


def normalisation(DF):
    
    #print(standard_scaler.mean_)
    cols = DF.columns
    
    DF = standard_scaler.transform(DF) #Normalisation par meme paramètre que dataset entrainement
    
    DF = pd.DataFrame(DF,columns=cols)
    
    return DF