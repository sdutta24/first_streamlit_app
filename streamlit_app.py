import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Zena\'s Amazing Athleisure Catalog')
streamlit.header('SweatSuit Collection')
streamlit.text('Buy one Get One offer')
#streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
#streamlit.text('🐔 Hard Boiled Free Range Eggs')
#streamlit.text('🥑🍞 Avocado Toast')
#streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
#my_data_row=my_cur.fetchone()
#my_data_rows=get_fruit_load_list()
#my_cnx.close()
# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()
#streamlit.dataframe(my_catalog)
df=pandas.DataFrame(my_catalog)
# temp write the dataframe to the page so I Can see what I am working with
streamlit.write(df)
# put the first column into a list
color_list=df[0].values.tolist()
print(color_list)
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Apple'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(fruits_to_show)
#streamlit.header("Fruityvice Fruit Advice!")
#def get_fruityvice_data(this_fruit_choice):
      #fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
      #streamlit.text(fruityvice_response.json())
      #fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
      #return fruityvice_normalized
      #streamlit.dataframe(fruityvice_normalized)
#try:
  #fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  #if not fruit_choice:
      #streamlit.error("Please select a fruit to get information")
  #else:
      #back_from_function=get_fruityvice_data(fruit_choice)
      #streamlit.dataframe(back_from_function)
#except URLError as e:
      #streamlit.error()
#streamlit.header("View our fruit list - Add your favourites! ")
#def get_fruit_load_list():
      #with my_cnx.cursor() as my_cur:
            #my_cur.execute("select * from fruit_load_list")
            #return my_cur.fetchall()
#if streamlit.button('Get Fruit List'):
      

#def insert_row_snowflake(new_fruit):
      #with my_cnx.cursor() as my_cur:
          #my_cur.execute("insert into fruit_load_list values('" + new_fruit + "')")
          #return "Thanks for adding " + new_fruit
#add_my_fruit = streamlit.text_input('What fruit would you like to add?')
#if streamlit.button("Add a fruit to the list: "):
      #my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
      #back_from_function=insert_row_snowflake(add_my_fruit)
      #streamlit.text(back_from_function)

#streamlit.write('Thanks for adding ', add_my_fruit)

#fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)
#streamlit.text("Thanks for adding " + add_my_fruit)
