
# CS3244 Project Stock 

Topic: Stock Prediction Using Time Series Forecasting And NLP Techniques

Together with Alfred, Zhi Min and Xuan Le.

Welcome to our Stock Prediction project! This system leverages machine learning and NLP to predict TESLA stock price based on Tesla news headline and Tesla blog news!

## Overview

This project attemps to propose a basic architecture using ensemble method **stacking** to predict stock price using textual input together with lagged prices. Comparisons with baseline model across performance are also conducted.

### Project Pipeline

1. **Initial merging**
   - **Folder**: `1. first-merge`
   - **main code**:  `merge_data_1.ipynb`
   - **Input csv**: `raw_input`
   - **Output csv**: `merged_tesla_headlines.csv`
   - **Aim**: Merge google news data together with blog news scraped to form our initial dataset.

2. **Find Missing Dates**
   - **Folder**: `2. find-missings`
   - **main code**:  `find_missings.ipynb`
   - **Input csv**: `merged_tesla_headlines.csv` `stock_price.csv`(containing TESLA stock price closing price and date)
   - **Output csv**: `missing_dates_from_here.csv` (`missing_date.csv` is an EDA result from `missing_dates_from_here.csv`)
   - **Aim**: Trim the initial dataset to only contain the dates when TESLA is listed, then map the dates that aren't in stock_price.csv to its nearest dates which are in stock_price.csv.

3. **Sort And Filter Missing Dates**
   - **Folder**: `3. missings-filter-sort`
   - **main code**:  `missing_date_ascending.ipynb`
   - **Input csv**: `tesla_google_missing_date_raw.csv`(scraped after identifying missing dates from last step)
   - **Output csv**: `tesla_google_missing_date_ascending.csv` 
   - **Aim**: To first sort the csv according to dates and filter until only 3 of the headlines are left for each date. 

4. **Second Merging**
   - **Folder**: `4. second-merge`
   - **main code**:  `merge_data_2.ipynb`
   - **Input csv**: `tesla_google_missing_date_ascending.csv` `missing_dates_from_here.csv`
   - **Output csv**:  `tesla_no_perc_no_combined.csv`
   - **Aim**: Incorporate missing dates and perform date mapping again.

5. **Merging Headlines and Descriptions**
   - **Folder**: `5. cleaning`
   - **main code**:  `intermediate.ipynb`
   - **Input csv**: `tesla_no_perc_no_combined.csv`
   - **Output csv**:  `tesla_final.csv`
   - **Aim**: Group the csv by dates, and join headlines and descriptions columns so 1 date has only 1 text input. Create one column for label, instead of closing price we compute percentage change of stock price(daily basis) for label as it is more stationary.

6. **TFIDF computing**
   - **Folder**: `6. tfidf`
   - **main code**:  `WordEmbedding.ipynb`
   - **Input csv**: `tesla_final.csv`
   - **Output csv**:  `Word_Embedding.csv`
   - **Aim**: Turn the merged textual input to a word vector for model input after stop word removal, lemmatisation and symbol removing.

## Data Scraping

- **Folder**: `scrape_code`
- **Skill**: Selenium

## Getting Started

To run any part of this pipeline, follow these steps:

1. **Fork the Repository**:
    Fork this repository to your local machine, then clone it to get started. Use the following command in your terminal:

    ```bash
    git clone https://github.com/yourusername/yourrepositoryname.git
    ```

    Replace `https://github.com/yourusername/yourrepositoryname.git` with the actual URL of your repository.

2. **Run the Notebooks**:
    Open the notebooks using Google Colab(Preferable as this is what the author used) or Jupyter Notebook or JupyterLab:

    ```bash
    jupyter notebook
    ```

    Navigate to the respective notebook file (`.ipynb`) you wish to run and follow the instructions within.

3. **Data Files**:
    Ensure you have the necessary data files(.csv) downloaded from each folder and placed in your local drive. Then, import them into your colab by cd into your own local drive to access the csv needed in colab.


