import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_ViewVehEnter,count_vehicles,show_vehicles,read_record_count,read_amount,faculty_not,Student_not



def readvehicles():
    result=view_ViewVehEnter()
    df=pd.DataFrame(result,columns=['Date','Type','OwnerType','VehicleNumber','ParkingID','ID','Name','Contact'])
    with st.expander("View all vehicle details"):
        st.dataframe(df)

def read_no_vehicles():
    result=count_vehicles()
    df=pd.DataFrame(result,columns=['Vehicle Count'])
    with st.expander("All the vehicles inside"):
        st.dataframe(df)

def read_parkinglots():
    result=show_vehicles()
    df=pd.DataFrame(result,columns=['Parking ID','Status'])
    with st.expander("Status of the Parking slots"):
        st.dataframe(df)

def readamnt():
    result=read_amount()
    df=pd.DataFrame(result,columns=['VehicleNumber','Amount'])
    with st.expander("Amount per vehicle"):
        st.dataframe(df)

def read_records_count():
    result=read_record_count()
    df=pd.DataFrame(result,columns=['Total records','Owner Type','Date'])
    with st.expander("Number of records per teacher and student"):
        st.dataframe(df)

def read_notF():
    result=faculty_not()
    df=pd.DataFrame(result,columns=['Contact','ID','Name'])
    with st.expander("Faculty that havent used parking"):
        st.dataframe(df)

def read_notS():
    result=Student_not()
    df=pd.DataFrame(result,columns=['Contact','ID','Name','Semester'])
    with st.expander("Student that havent used parking"):
        st.dataframe(df)
# def read():
#     result = view_all_data()
#     # st.write(result)
#     df = pd.DataFrame(result, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
#     with st.expander("View all Dealers"):
#         st.dataframe(df)
#     with st.expander("Dealer Location"):
#         task_df = df['Dealer City'].value_counts().to_frame()
#         task_df = task_df.reset_index()
#         st.dataframe(task_df)
#         p1 = px.pie(task_df, names='index', values='Dealer City')
#         st.plotly_chart(p1)
        