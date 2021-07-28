import numpy as np
import pandas as pd
import os

def transform(df):
    
    # mapping dictionaries
    required_map = { 
        'YES': 'YES',
        'NO': 'NO',
        'MISSING': 'YES' 
    }
    
    colname_map = {
        'generaltype': 'generalType', 
        'globalphredentitycode': 'fullAssetPath', 
        'standardfieldname': 'standardFieldName', 
        'phredentitycode': 'assetName'
    }
    
    # table transforming
    # splitting objectId into objectId and objectType
    df['objectId_old'] = df['objectId']
    df['objectType'] = df.loc[df['objectId'].isna() == False]['objectId'].apply(lambda x: x.split(':')[0])
    df.loc[df['objectId'].isna() == False, 'objectId'] = df[df['objectId'].isna() == False]['objectId'].apply(lambda x: x.split(':')[1])
    
    # adding new empty columns
    df['manuallyMapped'] = np.nan
    df['typeName'] = np.nan
    
    # mapping "required" field text to LoadBoy-compatible
    # replacing 'MISSING' with 'YES' and any other value with 'NO'
    df['required'] =  df['required'].map(required_map).fillna('NO')
    
    # standardizing column names
    df.rename(columns=colname_map, inplace=True)
    
    # reordering columns
    df = df[['location','controlProgram','name','type','path','deviceId','objectType','objectId',\
             'objectName','units','required','manuallyMapped','building', 'generalType', 'typeName',\
             'assetName', 'fullAssetPath', 'standardFieldName']]
    
    return(df)


if __name__ == '__main__':
    
    files = os.listdir('.')
    files = [file for file in files if 'US-MTV-' in file and '~' not in file]

    try:
        os.mkdir('./transformed')
    except FileExistsError: pass

    with open('./transformed/log.txt',"w+") as f:
        for file in files:
            df = pd.read_excel(f'./{file}')
            filename = file.replace('.xlsx', '')
            try:
                df = transform(df)
                f.write(f'{file} OK\n')
                print(f'{file} OK')
                df.to_excel(f'./transformed/{filename}_tf.xlsx', index=False)
            except Exception as e:
                f.write(f'{file} someting went wrong: {e}\n')
                print(f'{file} someting went wrong: {e}')
                pass