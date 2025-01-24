# Questions to address 
## 1. how do exchange rates behave before, during, and after elections? ( in a 30 day period 10/18 - 11/18 )
### variable name election_window = october 15th to november 15th load exchange rate data, add election year and column to categorize pre-election

## 2. is there any signficant difference in volatility during the election period compared to non-election periods

## 3. which phase of the election cycle shows the most consistent change in exchange rates

## 4. are there consistent trends acrsoss multilple election cycles for USD/other currency



# Notebook 1: data preperation
## objective load, clean and prepare dataset for analysis
### Steps: load exchange rate data for USD/JPY, add election window columns (1 for within, 0 for outside the window), create the phase column to categorize pre-election, election day, and post-election data.

# Notebook 2: Behavior Analysis
## Examine the behavior of exchange rates before, during, and after elections.
### Steps: Plot time series data for exchange rates with election windows highlighted, Calculate average exchange rates for each phase (Pre-Election, Election Day, Post-Election), Compare means to see if there's a trend.

# Notebook 3: Multi-Cycle Trend analysis
## Objective: Determine if volatility is higher during election cycles
### Steps: Calculate daily returns (percentage change) for exchange rates, Compute standard deviation of returns during election and non-election periods, Use boxplots or histograms to visualize the difference in volatility.

# Notebook 4: Multi-Cycle Trend analysis
## Objective: Analyze trends across multiple election cycles.
### Steps:  Compare trends for multiple election years (e.g., 2012, 2016, 2020, 2024), Identify patterns in exchange rates and volatility over cycles.

# Notebook 5: Summary and Visualizations 
## Objective: Summarize findings with clear visualizations and explanations.
### Steps: Combine insights from previous notebooks, Create summary plots showing trends, volatility, and patterns, Write a summary of findings and implications.
