# Investment strategy testing and benchmarking using data science techniques


### Project Motivation

Warren Buffett won a 10 year bet that the hedge fund industry will not be able to outperform the passive indexing, given the high fee charged by the hedge fund. Warren won bet 2 years early. But why the well funded and more resourceful hedge fund not able to bit a supposed less intelligent way of investing, e.g., passive investing?

This project utilizes supervised machine learning techniques to analyze various macro indicators, including economic indicators, asset prices, option market, and investor sentiments to attend to predict the market price movement. And attempt to replicate the process of investment strategy, attempt to beat the market.

### Document Summary

- capstone project report.pdf/docs: summary of the findings
- capstone_project.ipynb: the main codes and project workflow of the complete report

The supplemental code file is in common directory. The data files in data dir. These directory structure needs to be maintanined as in the zip file for notebook to execute properly.

```
│  capstone project report.docx   : Readable format of the report
│  capstone project report.pdf    : Readable format of the report
│  capstone_project.html          : HTML version of the Notebook
│  capstone_project.ipynb         : Jupyter Notebook of the data analysis
│  proposal.pdf                   : Proposal of the project
│  README.md                      : Introduction of the project
│
├─common                        
│      stockhistory.py            : Code that organizes the stock price history
│
└─data
    │  leius.json                 : Data file of the Leading Economic Indicators
    │  margindebt-data-finra.csv  : Data file of the margin debt usage
    │
    ├─pcratio_data    
    │      totalpc_my.csv         : Data file of CBOE Volume Total Put/Call Ratio
    │
    ├─sentiment_data
    │      naaim_chart_data.csv   : Data file of investor sentiment from NAAIM
    │      sentiment.xls          : Data file of investor sentiment from AAII
    │
    └─yahoo_data
            SPY.csv               : Data file of daily trading of SPY ETF
            TB3MS.csv             : Data file of daily 3-Month Treasury Interest Rate
            TEDRATE.csv           : Data file of Interest Rate spread
            ^GSPC.csv             : Data file of daily trading of S&P 500 Index
            ^TNX.csv              : Data file of daily 10-year Treasury Interest Rate
```

### Result Summary

1. SVM perform the best, Decision Tree give just as good result as SVM. Naive Bayes can be a bit unpredictable and have wider score variations.
2. SVM, and Decision Tree comes close, but not able to, beat the passive strategy. The score of passive strategy is indicated by dash lines in above graph.
3. Since Decision Tree is a good enough model, we take advantage of it being able to provide the feature weight analysis, and look at the contribution to the weights  from the three categories. Leading Economic Indicator has majority of the weight, with Treasury Interest Rate not far behind. Sentiment data contribute to some but far less weight in this analysis.
4. Decision Tree is interesting in that it has huge difference between the score of training data and testing data. Overfitting occur very often for this model.

### Acknowledgements

The research is not possible without the generous publications made available by the following organizations:

- Yahoo Finance: provides Financial market data and some of the macro economic data
- Conference Board: provides Economic indicator data
- Federal Reserve Bank of St. Louis: provides Treasury interest rate data
Market sentiment data, are gathered from
- Chicago Board Options Exchange: provides market sentiment data in Put/Call Ratio
- American Association of Individual Investors: provides investor sentiment survey result
- National Association of Active Investment Managers: provides investor sentiment survey result
- Financial Industry Regulatory Authority, Inc.: provides margin debt information
