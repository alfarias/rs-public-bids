import pandas as pd

def clean_text(df, feature: str):
    '''
    Description:
        Clean text applying lower case, strip white spaces and removing
        unwanted characters.
    Parameters:
        df: dataframe
            The dataset with the text feature.
        fearure: string
            The Text feature/column to clean.
    Return:
        Cleaned text.
    '''
    df[feature] = df[feature].str.lower()
    df[feature] = df[feature].str.strip()
    df[feature] = df[feature].str.replace(r'\d+', '')
    df[feature] = df[feature].str.replace(r'[^\w\s]', '')
    df[feature] = df[feature].str.findall(r'\w{2,}').str.join(' ')
    return df