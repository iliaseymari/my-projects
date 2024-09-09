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
        
