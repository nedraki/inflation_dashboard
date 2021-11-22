# Inflation dashboard

Data experiment to track real inflation rates in countries where statistics are unreliable or no official data is published. The objective is to measure the exchange rate of a given fiat currency against a cripto-currency and calculate the implicit exchange rate relative to the USD. The objective is to measure the country's inflation under the assumption that a ***constant increase on the exchange rate is an early indicator of inflation***, this is specially true for the countries that heavily rely on foreign exports. 

Similar strategies have been followed by the [Troubled currencies](https://sites.krieger.jhu.edu/iae/research-programs/troubled-currencies-project/) project at Johns Hopkins University.

Additionally, the Big-Mac Index is studied by exploring the dataset published by The Economist.

## Methodology

- Obtain exchange rate of a given local currency (FIAT) against a cripto-currency (BTC).
- Obtain exchange rate USD vs BTC.
- The exchange rates are obtain from a peer to peer platform where both parties agree on the exchange rate before closing a transaction. This represents a real time, free market where agreement among parties is achieved without governmental restrictions or regulations.
- The implicit exchange rate local currency vs USD is calculated on a daily basics.

## About the data:

- Exchange rates are obtained from daily transactions on localbitcoins.com
- [Mapping of country currency code](https://gist.github.com/marcusbaguley/304261)
- [The Economist Big Mac Index](link)


### TO DO:

- Organize better the repo 
-All the countries on btc are not available on big mac
- Index related to EU zone have different names on each dataset
- Data of minimum wage by country and comparison against big mac could be good for comparisons,
example "the m.salary in Venezuela affords 0.25 big mac per month"
- Can I get an index to quantify how much does rely a country on foreign exports ?
- Can I get an index to quantify US inflation by looking at the behavior of all the countries relying on USD for their economy?


