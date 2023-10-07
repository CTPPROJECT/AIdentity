### Import libraries

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import plotly_express as px
import mpld3
import streamlit.components.v1 as components

### Define functions

# Function for the Statistics Synopsis
def stats(dataframe):
    st.header('Data Statistics')
    st.write(dataframe.describe())

# Function for the Header Analysis
def data_header(dataframe):
    st.header('Data Header')
    st.write(dataframe.head())

# Functions for the individual interactive graphics
def interactive_bar(dataframe):
    x_axis_val = st.selectbox('Select X-Axis Value', options=df.columns)
    y_axis_val = st.selectbox('Select Y-Axis Value', options=df.columns)
    #col = st.color_picker('Pick a color')

    plot = px.bar(dataframe, x = x_axis_val, y = y_axis_val)
    #plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)

###def plot(dataframe):
    ###fig, ax = plt.subplots(1, 1)
    ###ax.scatter(x=df['Year'], y=df['RS'])
    ###ax.set_xlabel('Year')
    ###ax.set_ylabel('RS')
    ###st.pyplot(fig)

def interactive_scatter(dataframe):
    x_axis_val = st.selectbox('Select X-Axis Value', options=df.columns)
    y_axis_val = st.selectbox('Select Y-Axis Value', options=df.columns)
    #col = st.color_picker('Pick a color')

    plot = px.scatter(dataframe, x = x_axis_val, y = y_axis_val)
    #plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)

def interactive_area(dataframe):
    x_axis_val = st.selectbox('Select X-Axis Value', options=df.columns)
    y_axis_val = st.selectbox('Select Y-Axis Value', options=df.columns)
    #col = st.color_picker('Pick a color')

    plot = px.area(dataframe, x = x_axis_val, y = y_axis_val)
    #plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)

def interactive_line(dataframe):
    x_axis_val = st.selectbox('Select X-Axis Value', options=df.columns)
    y_axis_val = st.selectbox('Select Y-Axis Value', options=df.columns)
    #col = st.color_picker('Pick a color')

    plot = px.line(dataframe, x = x_axis_val, y = y_axis_val)
    #plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)

### Title for the page
st.markdown('''# :rainbow[Visualize Your Data]''')
multi = '''The point of this dashboard is to build something that can easily:

-Take in different datasets

-Give initial insights through statistical breakdowns and header visualization

-Lets you play around with a variety of simple visualizations'''
st.markdown(multi)

### Establishing a sidebar for page navigation
st.sidebar.title('Navigation')
uploaded_file = st.sidebar.file_uploader('Upload your file here')

### Creating the individual page names and locations
options = st.sidebar.radio('Pages',
options=['Home',
'Data Statistics',
'Data Header',
'Interactive Area',
'Interactive Bar',
'Interactive Line',
'Interactive Scatter'])

### Create a place to upload a file
if uploaded_file:
    df = pd.read_csv(uploaded_file)

### Determines what happens when you click over to a page from sidebar
if options == 'Data Statistics':
    stats(df)
elif options == 'Data Header':
    data_header(df)
elif options == 'Interactive Scatter':
    interactive_scatter(df)
elif options == 'Interactive Area':
    interactive_area(df)
elif options == 'Interactive Bar':
    interactive_bar(df)
elif options == 'Interactive Line':
    interactive_line(df)