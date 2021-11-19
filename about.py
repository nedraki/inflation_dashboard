message_users = str(
"""
Data experiment to track real inflation rates in countries where statistics are unreliable or no official data is published. The objective is to measure the exchange rate of a given fiat currency against a cripto-currency and calculate the implicit exchange rate relative to the USD. 

The project could be helpful to identify country's inflation under the assumption that a ***constant increase on the exchange rate is an early indicator of inflation***, this is specially true for the countries that heavily rely on foreign exports billed on USD or any other reserve currency. 

Similar strategies have been followed by the [Troubled currencies](https://sites.krieger.jhu.edu/iae/research-programs/troubled-currencies-project/) project at Johns Hopkins University.

Additionally, the Big-Mac Index is studied by exploring the dataset published by The Economist.

## Inspiration
 
This dashboard is inspired by a challenged proposed by Balaji Srinivasan on his [newsletter](https://1729.com/inflation). 

***"...when inflation is happening, there is often a push to censor discussion of inflation itself, under the grounds that discussing the problem actually causes it in the first place. That is exactly what happened in Argentina and Venezuela over the last decade."*** 

***"If inflation is a government-caused problem, we can't necessarily rely on government statistics like the CPI to diagnose it or remediate it. Indeed, in places with high inflation, censorship and denial is the rule rather than the exception."***

I was born and raised in Venezuela, a beautiful country witch today is sadly facing a chapter of hyperinflation, ramping corruption, and lack of rule of law. The challenge presented by Balaji it's for me intellectually inspiring but also an opportunity to demonstrate how tech can contribute to strengthen democracies


No matter how accurate the metrics can be, there's no words to explain with precision the significant damage that wrong economic policies can make on people's lives.


## Methodology

- Obtain exchange rate of a given local currency (FIAT) against a cripto-currency (BTC).
- Obtain exchange rate USD vs BTC.
- The exchange rates are obtain from a peer to peer platform where both parties agree on the exchange rate before closing a transaction. This represents a real time, free market where agreement among parties is achieved without governmental restrictions or regulations.
- The implicit exchange rate local currency vs USD is calculated on a daily basics.

## About the data:

- Exchange rates are obtained from daily transactions on localbitcoins.com
- [Mapping of country currency code](https://gist.github.com/marcusbaguley/304261)
- [The Economist Big Mac Index](link)

## Extra comments and things to do:

The project is on an initial stage and the published version is a first draft.

- Data related to Venezuela is not yet published on the Dashboard due to discrepancies on data entries caused probably by confusion caused during the last "currency reconversion" on October 2021.

- The data should be registered on a blockchain to make the dashboard decentralized and censorship resistance.

- I need to learn coding for blockchain applications. Advice, cool tutorials, mentors and volunteers are welcome

- The dashboard is currently depending of an API, to guarantee long term access to information, it would be ideal to:
    - Close partnership with API owner
    - Connect with extra data sources to make the system redundant

- Currently the dashboard keeps track of the exchange rates of local currencies vs the USD. The values are positive to evaluate real exchange rate, for example the value for Argentina is significantly different than the official one published by the government. In the cases of countries relying on foreign exports or with a significant external debt denominated on USD, the increase on exchange rate is an early indication of inflation.
- Due to the comparisons are done against the USD, currently there's no direct way to measure real devaluation or appreciation on the USD. This could be solved by measuring a basket of products in the USA as proposed originally by Srinivasan.

- ***"The US dollar accounts for about 60% of the global reserves" (Ray Dalio)***
- ***"The beauty of our model is that the entire world uses the US dollar as its stable currency as its ultimate stable coin. And so every time we print a dollar, 70 cents of that dilution, that inflation goes overseas..." Naval Ravikant***

- Maybe a rough measure of the real  monetary inflation in the USA could be calculated by evaluating the performance of those economies around the globe with reserves on USD. (To be tested)

- The draft code should be refactored to OOP and some calculations could be done more efficiently.
""")