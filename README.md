# Group 2 Foreign Exchange Analysis Project

## Overview 
Between 2004 and 2024, the U.S. Presidential General Elections have influenced USD foreign exchange rates with major currencies like EUR, JPY, and CNY. Our research will indicate exchange rate volatility 15 days before the election and 15 days after the election reflecting market uncertainty. 

## Objectives
This project examines the relationship between the U.S. Presidential General Elections and exchange rate dynamics by analyzing:
- The behavior of exchange rates across three key periods: pre-election, election, and post-election phases.
- The identification of election cycle phases that demonstrate the most significant and consistent exchange rate fluctuations.
- Historical patterns across multiple election cycles, including potential correlations between exchange rate movements and the winning party (Republican vs Democratic).

## Team Members
1. [Matt Le](https://github.com/mattledevs) - Missouri
2. [Patrick McCourt](https://github.com/patrickjm7) - Utah
3. [Spencer Gerritsen](https://github.com/sppencerr) - Utah
4. [Ingrid Blankevoort](https://github.com/AIBC2024) - Utah
5. [Vijay Srinivasula](https://github.com/vijaysrini-1982) - Arizona
6. Yves Mugaba - Oregon

## Prerequisites
- For Source 1: Download the Exchange Rate API key
- [Read API doc](https://www.exchangerate-api.com/docs/overview)
- Use Jupyter Notebook
- Store the csv file in /Resources/ folder
- Foreign currency data collection: USD/EUR (Euro), USD/JPY (Japanese Yen), USD/CNY (Chinese Yuan)
- For Source 2: Get familiarize with the Exchange Rate data from the Federal Reserve website

## Activities
1. Use Prophet model to predict the seasonal trend, show the plot, and qualitative analysis
2. Exploration of the data:
Years, month, week, day (For example: US election cycle 2024, 2020, 2016, 2012, 2008 and 2004)
3. Comparing data during the U.S. Presidential General Election cycles. For example, if the election day is on November 2, we'll look for data starting at 15 days prior the election day till 15 days after the election (that means between Oct 18 - November 17).
4. This project provides a small calculator to convert USD/EUR, USD/JPY, USD/CNY in 2024.
5. [Google Slides Presentation](https://docs.google.com/presentation/d/1-d574a8OJdIFsXGoa078BxuTmT_EhNgnVtsYezYIVM4/edit?usp=sharing)

## References
- Source 1 [Exchange rate API](https://app.exchangerate-api.com/sign-up)
- Source 2 [Federal Reserve Resource](https://www.federalreserve.gov/data.htm) with [Scrape HTML table for each country](https://www.federalreserve.gov/releases/h10/hist/)
