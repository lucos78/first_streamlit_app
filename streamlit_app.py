import streamlit

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

#pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruits_selected]
#display table
streamlit.dataframe(fruit_to_show)

#New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like infotmation about ?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)
import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) #just writes data to the screen

#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

#snowflake data
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT FRUIT_NAME FROM FRUIT_LOAD_LIST")
df = pandas.DataFrame(
    my_cur,
    columns=('col %d' %i for i in range(20)))
streamlit.dataframe(df)
