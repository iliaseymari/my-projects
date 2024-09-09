import requests
import streamlit as st

user_input = st.text_input("what product do you want: ")

if user_input != '':
    api = f'https://api.torob.com/v4/base-product/search/?category=&sort=popularity&q={user_input}&page=0&size=24&source=next'

    url = requests.get(api)

    x = url.json()

    for i in x['results']:
        names = i['name1']
        price = i['price']
        image = i['image_url']
        col1, col2 = st.columns(2)
        f = str(int(price / 60000))
        with col1:
            st.image(image)
        with col2:
            st.subheader(names)
            st.write(f, '$')

#In this app you can search on pruduct and this app shows a photo and price of that product 
#but you shouldn't run the project you should open the terminal and cd to your files, you put this project on that.
#after write "streamlit run web_scraping" in the treminal after project opens a web page after you can search, Thank you for taking the time to read this text🙏
        
