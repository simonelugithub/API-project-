# **Data Project**

#contributors: Simone Lu, Lorenzo Antolini, Marco Pisano.
# TASK 1 Data collection**

**PYTHON**
 In this task, we retrieved different pages from the API response from https://api.magicthegathering.io/v1/cards in JSON format. We retrieved more pages to have more rows in our dataset (TOTAL = 700). All the pages we retrieved, are normalized and merged into a unique dataset. Then we write that dataset into a CSV file.

# TASK 2 Data Manipulation and Data Visualizations

**Python**
#DATA MANIPULATION
 We observed that the dataset had some ambiguities:
 1) some columns had list of values, example ---> [{es1, es2, es.3}] as variable. We transform them into a more "usable" format.
 2) we dropped all the columns that we consider not necessary for our analysis.
 3) We manipulate the column type value to extract only the "creature" from the card data frame

# DATA VISUALIZATION
 We use creature data frame to plot and count different variables distribution such as the rarity, mana colour, type and subtypes of the cards.
 Then we saved the figure.
 
**R**
  In task two we retrieved the dataset from the repository of our colleagues. the dataset is about a stock price historical information from binance.com. At first glance, the dataset seems well done. However, For the Data visualizations, we plot 4 graphs, namely: a barplot, boxplot, a line and a scatterplot.
  Then for the data manipulation, we used some basic commands of the tidyverse library like select, filter and summarise.

  


