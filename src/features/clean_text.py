import pandas as pd

def clean_text(df, feature: str):
    df[feature] = df[feature].str.lower()
    df[feature] = df[feature].str.strip()
    df[feature] = df[feature].str.replace(r'\d+', '')
    df[feature] = df[feature].str.replace(r'[^\w\s]', '')
    df[feature] = df[feature].str.findall(r'\w{2,}').str.join(' ')
    return df