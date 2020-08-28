import pandas as pd
import os

def build_features(dataset: str, data_path: str, cols: list, values: list):
    '''
    Description:
        Function to build the required fields to public bids analysis.
    Parameters:
        dataset: string 
            A string with the dataset name.
        data_path: string
            The data path on the development environment.
        cols: list
            The required columns (features) to the new dataset.
    Return:
        A list with the built datasets.
    '''
    datasets = []
    # Iterate to get on multiple folders
    for idx in values:
        data = pd.read_csv(data_path+os.sep+'external'+
                            os.sep+str(idx)+os.sep+dataset,
                            usecols=cols
                                    )
        data.drop_duplicates(inplace=True)
        # For processing "licitacao.csv"
        # Filter by Buy (COM)
        if dataset == 'licitacao.csv':
            data.query('TP_OBJETO == "COM"', inplace=True)
            data.drop(['TP_OBJETO'], axis=1, inplace=True)
            datasets.append(data)
        # For processing "item.csv"
        elif dataset == 'item.csv':
            data['ANO_LICITACAO'] = idx
            datasets.append(data)
        else:
            pass

    return datasets