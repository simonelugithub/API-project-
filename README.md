# Data Project with Python and R
#contributors: Simone Lu, Lorenzo Antolini, Marco Pisano.

**TASK 1 Data collection**
**PYTHON**
 In this task we retrieved different pages from the API response from https://api.magicthegathering.io/v1/cards in json format. We retrieved more pages in order to have more rows in our dataset (TOTAL = 700)t. All the pages we retrieved, are normalized and merged into a unique dataset. Than we write that dataset into a csv file.

# TASK 2 Data Manipulation and Data Visualizations

**Python**
#DATA MANIPOLATION
 We observed that the dataset had some ambiguities:
 1) some columns had list of values, exemple ---> [{es1, es2, es.3}] as variable. We transorm them into a more managble format.
 2) we dropped all the columns that we consider not necessary for our analysis.
 3) We manipolate the column type value in order to extract only the "creature" from the cards dataframe

#DATA VISUALIZATION
 We use crature dataframe to plot and count different variables distribution such as the rarity, mana colour, type and subtypes of the cards.
 Than we saved the figure.
 
**R**
  In the task two we retrieved the dataset from the repository of our colleagues. the dataset is about a stock price historical information from binance.com. At first glance, the dataset seeems really well done. However, For the Data visualizations, we plot 4 graphs, namely: a barplot, boxplot,a line and a scatterplot.
  Then for the data manipulation, we used some basic commands of the tidyverse library like select,filter and summarise.

