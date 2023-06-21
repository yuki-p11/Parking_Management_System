# Importing pakages
import streamlit as st
import mysql.connector
from admin import main1 
from security import main2 
import base64
# from streamlit_extras.switch_page_button import switch_page
# from create import create
# from database import create_table
#from delete import delete
#from read import read
#from update import update

#mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
 #    #password="password"
# )
#c = mydb.cursor()

#c.execute("CREATE DATABASE ebike_1")


# def main1():
#     st.title("PESU PARKING SECURITY GUARD")
#     menu = ["Add", "View", "Edit", "Remove"]
#     choice = st.sidebar.selectbox("Menu", menu)

#     create_table()
#     if choice == "Add":
#         st.subheader("Enter Details:")
#         create()

    # elif choice == "View":
    #     st.subheader("View created tasks")
    #     read()

    # elif choice == "Edit":
    #     st.subheader("Update created tasks")
    #     update()

    # elif choice == "Remove":
    #     st.subheader("Delete created tasks")
    #     delete()

    # else:
    #     st.subheader("About tasks")




# st.sidebar.title('Navigation')
# selection = st.sidebar.radio("Go to", list(PAGES.keys()))
# page = PAGES[selection]
# page.app()


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/gif;base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('t.gif')


def main():
    st.title("PESU PARKING")
    navigate = ["Admin Login","Security Guard Login"]
    choice = st.sidebar.radio("User Login",navigate)
    if choice=="Admin Login":
        form = st.form(key='my_form')
        username = form.text_input(label='Enter Admin Username')
        password = form.text_input('Enter Admin Password',type='password')
        submit_button = form.form_submit_button(label='Submit')
        if username=='admin' and password=='admin123' :
                main1()
        else :
            st.error('Please enter a valid input',icon='🚨')
            


    elif choice=="Security Guard Login":
        form = st.form(key='my_form')
        username = form.text_input(label='Enter Username')
        password = form.text_input(label='Enter Password',type='password')
        submit_button = form.form_submit_button(label='Submit')
        if username=='security' and password=='guard123':
            main2()
        else:
            st.error('Please enter a valid input',icon='🚨')
            
            

if __name__ == '__main__':
    main()

# import admin
# import security
# import streamlit as st
# PAGES = {
#     "Admin": admin,
#     "Security": security
# }
# st.sidebar.title('Navigation')
# selection = st.sidebar.radio("Select", list(PAGES.keys()))
# page = PAGES[selection]
# page.main()