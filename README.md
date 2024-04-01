# Stock-Prediction-using-Time-Series-Forecasting-and-NLP-Techniques
CS3244 project, together with Alfred, Zhi Min and Xuan Le.

Explanation:
raw-input: all the files that are scraped, including missing dates
output_csv: all the intermediate and final files being generated
code:
1. date-mapping: close market dates mapping
2. scrape-code: scraping blogs and news code
3. missing-date-finder: EDA checks for final missing dates, missing-date-ascending sort the missing dates and find-missing-dates find the missing dates
4. merging-blog-news: merge missing dates, original and blog
5. final-input: final inputs

first, we find missing dates from original dates and merge them together, then we use dateMapping to clean close market and extract price, finally we data clean them in final input folder.

****due to the rearrangement of files, the file path may not direct you to the correct folders but effort has been made, just double check when running the code.
