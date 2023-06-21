import streamlit as st
from create import create_enter
from database import create_table_vehicleEnter
from read import read_no_vehicles,readamnt
# def main():
#     #elif choice=="Security Guard Login":
#     form = st.form(key='my_form')
#     username = form.text_input(label='Enter Username')
#     password = form.text_input(label='Enter Password',type='password')
#     submit_button = form.form_submit_button(label='Submit')
#     if username=='security' and password=='guard123':
#         main2()
def main2():
    st.title("PESU PARKING SECURITY GUARD")
    menu2 = ["Vehicle ENTER", "Vehicle COUNT","Vehicle Parking Fee"]
    choice = st.sidebar.selectbox("Menu", menu2)

    
    if choice == "Vehicle ENTER":
        create_table_vehicleEnter()
        st.subheader("Enter Details:")
        create_enter()

    elif choice == "Vehicle COUNT":
        #create_table_vehicleExit()
        read_no_vehicles()
        # st.subheader("Enter Details:")
        #create_exit()

    elif choice == "Vehicle Parking Fee":
        st.subheader("Amount per vehicle")
        readamnt()
# if __name__ == '__main__':
#     main()