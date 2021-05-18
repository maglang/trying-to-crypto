import streamlit as st
import pandas as pd
import numpy as np
import requests

st.sidebar.title("The Case for Cryptocurrency")
st.sidebar.write("""A source for cryptocurrency research.

I recently got into cryptocurrencies but there was simply too much information online. I created this page to compile analyses and resources. As usual, DYOR, but here is some research that I personally use to start you with your cryptocurrency journey.

Disclaimer: this is not financial advise.""")

st.sidebar.header("Dashboards")
st.sidebar.write("""Check out the following dashboards""")

option = st.sidebar.selectbox(
    'Select a dashboard here:',
     ('Stable-ish Coins', 'Potential Moons', 'Crypto Winter', 'Online Chatter', 'Sustainability', 
     'Crypto Language', 'Sources and Resources'))


st.sidebar.subheader("Contact me")
st.sidebar.write("Feel free to send me an e-mail if you have any comments/suggestions/violent reactions ;) at angelie.maglasang@gmail.com")
st.sidebar.write("T: @anj_maglasang")
st.sidebar.write("GitHub: maglang/")
st.sidebar.write("GitHub Repo for this page: maglang/trying-to-crypto")


st.title(option)
st.write()
if option == 'Stable-ish Coins':
    stableish_coin = st.selectbox("Select a coin here:", 
    ('BTC | Bitcoin', 'ETH | Ethereum', 'BNB | Binance Coin', 'DOGE | Dogecoin', 'ADA | Cardano', 'XRP | XRP', 
    'ICP | Internet Computer', 'BCH | Bitcoin Cash', 'UNI | Uniswap', 'LTC | Litecoin', 'LINK | Chainlink', 
    'XLM | Stellar', 'VET | VeChain', 'THETA | THETA', 'TRX | Tron', 'XMR | Monero'))

if option == 'Potential Moons':
    """
    Still building
    """

if option == 'Crypto Winter':
    """
    Still building
    """

if option == 'Online Chatter':
    st.write('Source: Stocktwits API')
    
    # st.beta_set_page_config(layout="wide")
    
    coin_list = ["BTC", "ETH"]
    tweet_coin = st.selectbox("Choose a coin from the drop down", options =  coin_list)
    
    if tweet_coin == 'BTC':
        r = requests.get('https://api.stocktwits.com/api/2/streams/symbol/BTC.json')
        
        data = r.json()

        for message in data['messages']:
            st.write(message['created_at'])
            st.write(message['user']['username'])
            st.image(message['user']['avatar_url'])
            st.write(message['body'])
            st.write("")
            st.write("")
    
    if tweet_coin == 'ETH':
        r = requests.get('https://api.stocktwits.com/api/2/streams/symbol/ETH.json')
        
        data = r.json()

        for message in data['messages']:
            st.write(message['created_at'])
            st.write(message['user']['username'])
            st.image(message['user']['avatar_url'])
            st.write(message['body'])
            st.write("")
            st.write("")
    
    
            
            



    


if option == 'Sustainability':
    """
    ## Why is sustainability an issue for Bitcoin?

    Bitcoin operates on a Proof-of-Work (PoW) protocol. To validate transactions and mine new coins on the blockchain,
    work has to be expended. In this case, work is solving a puzzle using computing power. Computing power uses energy. 
    Thus, the question on the sustainability of blockchain networks. 

    A 2019 [study](https://pubs.acs.org/doi/pdf/10.1021/acs.est.9b05687) by Köhler and Pizzol estimated that the Bitcoin network consumed __31.29 TWh
    of energy__. At face value, these numbers don't really mean much so let's take a look at other energy consumption metrics to understand the scale of
    Bitcoin's energy consumption.

    #### Table 1. Energy Consumption by Country, 2018 (unit: TWh)
    Source: [Global Energy Statistical Yearbook 2020](https://yearbook.enerdata.net/electricity/electricity-domestic-consumption-data.html)"""

    energy_cons_by_country_2018 = pd.DataFrame.from_dict(
        {"Country":["China", "United States", "India", "Japan", "Russia", "South Korea", "Canada", 
        "Brazil", "Germany", "France", "United Kingdom", "Italy"], 
        "Energy Consumption, 2018, in TWh":[6230, 3953, 1227, 960, 918, 560, 543, 528, 525, 441, 308, 303]}
    ).set_index('Country')
    bitcoin_expenditure = 31.29
    energy_cons_by_country_2018['% consumed by Bitcoin'] = (bitcoin_expenditure / energy_cons_by_country_2018["Energy Consumption, 2018, in TWh"]) * 100
    energy_cons_by_country_2018

    """
      
    Our first comparison is by country. Bitcoin consumed __10.3%__ of what United Kingdom consumed in terms of energy. More comparison is available in the table above. 

    ### Table 2. Energy Consumption per Capita, 2019 (kWh)
    Source: [Our World in Data](https://ourworldindata.org/energy#energy-country-profiles)
    """
    per_cap_energy_use = pd.read_csv('per-capita-energy-use.csv')
    per_cap_energy_use = per_cap_energy_use[per_cap_energy_use['Year'] == 2018].set_index('Entity')
    per_cap_energy_use = per_cap_energy_use[['Year', 'Energy consumption per capita (kWh)']]
    per_cap_energy_use = per_cap_energy_use.loc[["China", "United States", "India", "Japan", "Russia", "South Korea", "Canada", "Brazil", "Germany", "France", "United Kingdom", "Italy", "Philippines"]]
    per_cap_energy_use['Number of people'] = ((bitcoin_expenditure*100000000) / per_cap_energy_use["Energy consumption per capita (kWh)"])

    per_cap_energy_use
    """
    We could also look into individual consumption. Table 2 above tells us that it takes around 614,190 Filipinos a year to consume that much energy and 
    using our earlier comparison, almost 94,962 Britons.

    However, these are 2018 numbers. As of March 2021, the Cambridge Bitcoin Electricity Consumption Index estimates the annualised consumption of energy
    at __149.63 TWh__. In just three years, Bitcoin is potentially consuming __4.78x__ more energy. 
    Clearly, the Bitcoin blockchain will only increase in energy consumption
    the more that coins are mined and the more that transactions occur.

    On the other hand, there are a lot of arguments that defend Bitcoin. Such arguments include those that compare Bitcoin energy consumption with the investment of banks into 
    fossil fuels, or the energy consumption of minting new money. However, I think we should veer outside of those arguments. Bitcoin and blockchain technology, after all, are inevitable innovations
    and these have to be responsible and sustainable not in comparison to the old ways but to the new.

    The one productive argument I see for this is PoS or Proof-of-Stake, which we will talk about as an alternative to the Bitcoin network.
    """

    """
    ## What are the current alternatives?
    """

if option == 'Crypto Language':
    """
    This is a WIP list of phrases and words commonly used in the cryptocurrency markets.
    ### 1. DYOR
    #### Do your own research
    The decentralized currency world is not regulated by any entity. There are many upsides to this, but there too are downsides.
    For instance, you can fall victim to some scams or false information. Without a regulatory entity, these scammers can't be punished.
    Thus, the community always reminds you to do your own research and not to trust anyone online.

    ### 2. FOMO
    #### Fear of missing out
    This is that feeling you get when you failed to buy a coin/asset and it sky rockets. "I could've earned this much." I feel it too. Still, don't buy. Wait for a dip, 
    unless you're DCA-ing.

    ### 3. FUD
    #### Fear, uncertainty, doubt
    The cryptocurrency markets are very volatile. Thus, an abbreviation was borne out of the need to describe what individuals 
    (well, mostly newcomers) feel during a dip. The usual advice is, don't check the prices! They will recover. They usually do. That is,
    unless you bought into a shitcoin then that's unknown territory.

    ### 4. MOON
    I believe this word was borrowed from r/wallstreetbets. It means that a certain crypto asset (also applicable to stocks) jumps
    in price within a very short period of time. The community will say "to the moon", along with this emoji 🚀, in the hopes that it continues to rise.
    
    ### 5. HODL
    #### Holding on for dear life
    This is a long term investment strategy. No matter what happens to the price, HODL! Individuals who HODL have the strongest of wills
    because they won't sell even if the asset's price has dipped (it'll go up... just wait for it) or is at an all time high (it'll go up, need I say more?).

    ### 6. DCA
    #### Dollar Cost Averaging
    This is also a long term investment strategy. Dollar cost averaging means that you regularly invest a constant amount of money into an asset, regardless of the price.
    This is in comparison to lump-sum investing, where you add big amounts of money when the price dips. In DCA, you don't really care if the prices dip or skyrocket, 
    you just invest. 

    ### 7. TAYOR
    #### Trade At Your Own Risk
    Again, the cryptocurrency markets are volatile.

    ### 8. Whale
    Some individual/entity who holds a huge amount of crypto assets. They have the potential to affect prices when they sell. Since crypto assets are public, 
    these transactions/wallets are public. Thus, whales can be tracked.

    ### 9. DeFi
    #### Decentralized Finance
    These are the platforms or applications for doing your usual financial transactions, but made unusual due to its use of blockchain technology and smart contracts. 
    (Usual meaning centralized finance, which uses banks and balance sheets and bankers and etc.)  
    That's the gist but it's a bit more complicated than that. You should read more about it [here](https://www.investopedia.com/decentralized-finance-defi-5113835).   
    """

if option == 'Sources and Resources':
    """
    ## Resources
    1. University of California, Berkeley: [Bitcoin and Cryptocurrencies](https://www.edx.org/course/bitcoin-and-cryptocurrencies?index=product&queryID=8e3e96d14c3b179e0621f9d90bfd438f&position=1)  
    
    This is an online course that I took on edX. The lectures are pretty straightforward so this is a good start.
    You'll learn a lot about the history of Bitcoin and blockchain technology, as well as Ethereum.


    Special thanks to my friends Noelle Manahan and Fritzy Yanez for joining me on my cryptocurrency journey.
    """
