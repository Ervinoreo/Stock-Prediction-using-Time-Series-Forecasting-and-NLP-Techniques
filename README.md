# Stock-Prediction-using-Time-Series-Forecasting-and-NLP-Techniques
CS3244 project, together with Alfred, Zhi Min and Xuan Le.

Pipelines:
1. merge_data_1.ipynb -> merged_tesla_headlines.csv
2. find_missings.ipynb use merged_tesla_headlines.csv and stock_price.csv -> missing_date.csv and missing_dates_from_here.csv
3. missing_date_ascending.ipynb use tesla_google_missing_date_raw.csv -> tesla_google_missing_date_ascending.csv
4. merge_data_2.ipynb use tesla_google_missing_date_ascending.csv and missing_dates_from_here.csv -> tesla_no_perc_no_combined.csv
5. intermediate.ipynb use tesla_no_perc_no_combined.csv -> tesla_final.csv
6. WordEmbedding.ipynb use tesla_final.csv -> Word_Embedding.csv
