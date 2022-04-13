import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

#pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruits_selected]
#display table
streamlit.dataframe(fruit_to_show)

#import requests
#create the repeatable code block (called a fonction)
def get_fruityvice_data(this_fruit_choise)
    fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choise)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like infotmation about ?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(this_fruit_choise)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error
  
#stop le chargement de la page
streamlit.stop()


#import snowflake.connector
#snowflake data
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add ?', 'Jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)

#This will no work...
my_cur.execute("insert into fruit_load_list values ('from streamlist')")
