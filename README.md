# Anomaly Detection on Public Bids

## Objective

This work has as objetive make an analysis on the public bids of the Brazilian State Rio Grande do Sul.\
An Anomaly Detection Model is built to identify suspicious items bought on bids.\
The datasets contain text and numerical features about the bids description and items bought for the years of 2016 to 2019.\
For the analysis, the text features are analyzed for specific recurrent set of words, like items and public organ names, and for numerical features, the item costs.

## Project Structure

The Project needs the related datasets from Google Drive and must be stored on the folder `data/external` unzipped and with separated folders for each year, after, the implementation on the `notebooks` folder `bids_anomaly_detection..ipynb` will make all the work.\
On `configs` folder, there are txt files to set custom stopwords(as a list) and corrections on mispelled words (as dictionaries).\
The folder `reports/figures` has the plotted figures if they not show on the notebook, to show the dynamic plots on the notebook, mark it as trust.