import csv
import glob
import pandas as pd
import sys

csv_files = glob.glob('*{}'.format('csv')) #list fichier csv dans dossier

def concatenate(concatenate = True): 
    print(csv_files)
    if concatenate == True : #Fusion
        df_csv_all = pd.DataFrame()
        for file in csv_files:
             
            df_file = pd.read_csv(file) #Clean tt les fichiers
 
            df_csv_all = pd.concat([df_csv_all,df_file], ignore_index = True)
        
        columns = ['type','id','uri','track_href','analysis_url','name', 'Unnamed: 0']
        
        for column in columns :

            try :
                df_csv_all = df_csv_all.drop([column],axis=1)
            except KeyError:
                pass
            
        df_csv_all.to_csv('all.csv',index=False)

    return 'concatenate success'