import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.text('testing')

DATA_URL =('dataset.csv')

@st.cache_data  
def load_data():
    data = pd.read_csv(DATA_URL)
    return data


data = load_data()
data.columns = data.columns.str.replace(' ', '_')
st.subheader('Raw data')
st.dataframe(data)



# Example: calculate and print the mean of a numerical column 
mean_value = data['Lower_Pay_Band_Bound'].mean() 
st.write(f"The mean value of the lower pay limit is: {mean_value}")


# Example: plotting a bar chart using matplotlib


average_income_by_year = data.groupby('Data_Year')['Lower_Pay_Band_Bound'].mean().reset_index()

fig, ax = plt.subplots()
ax.bar(average_income_by_year['Data_Year'], average_income_by_year['Lower_Pay_Band_Bound'])


st.pyplot(fig)
st.write("Value counts in 'Race' column:", data['Race'].value_counts())



data['Upper_Pay_Band_Bound'] = data['Upper_Pay_Band_Bound'] > 100000  #pick a different threshold.. I'm not sure about this

# Group by ethnicity and calculate the sum (because True is treated as 1 and False as 0 when summing)
ethnicity_count_upper = data[data['Upper_Pay_Band_Bound'] == True]['Race'].value_counts()

# Calculate percentages
ethnicity_percentage_upper = (ethnicity_count_upper / data['Race'].value_counts()) * 100

# Handling NaN values
ethnicity_percentage_upper = ethnicity_percentage_upper.fillna(0)

# Visualization
plt.figure(figsize=(10, 6))
plt.pie(ethnicity_percentage_upper, labels = ethnicity_percentage_upper.index, autopct='%1.1f%%', startangle=140)
plt.title("Percentage of Each Ethnicity in the Upper Pay Band")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the plot in Streamlit
st.pyplot(plt)