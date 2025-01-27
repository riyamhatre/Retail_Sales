import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
from scipy.stats import ttest_ind
import plotly.graph_objects as go

def app():
    st.write('<p style="font-size:33px;"><b>External Factors</b></p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px;">Let us look at some holiday data!</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px;">The holiday names for specific dates were scraped from timeanddate.com and only the prominent holidays were included in the dataset.</p>', unsafe_allow_html=True)


    data = pd.read_csv('cleaned_data.csv').drop(columns={'Unnamed: 0'})

    col1, col2 = st.columns(2)
    with col1: 

        month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
        data['Month'] = pd.Categorical(data['Month'], categories=month_order, ordered=True)

        # Group by Holiday and Month and count entries
        holidays_grouped = data.groupby(["Holiday", "Month"])['InvoiceNo'].count().sort_values(ascending=False).to_frame().reset_index()

        # Take the top 10 holidays and pivot the data
        pivot_data = holidays_grouped[:10].pivot(index='Month', columns='Holiday', values='InvoiceNo').fillna(0)

        # Sort the pivoted data by the order of months
        pivot_data = pivot_data.reindex(month_order, axis=0)

        # Plot the stacked bar chart
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        pivot_data.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='GnBu', ax=ax1)

        # Customize the chart
        plt.title('Total Entries per Holiday by Month', fontsize=20, fontfamily='serif')
        plt.xlabel('Holiday Month', fontsize=15, fontfamily='serif')
        plt.ylabel('Total Entries', fontsize=15, fontfamily='serif')
        plt.tight_layout()

        st.pyplot(fig1)
    with col2:
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        # Convert 'Day' to a categorical type with a defined order
        data['DayofWeek'] = pd.Categorical(data['DayofWeek'], categories=day_order, ordered=True)

        # Group by Holiday and Month and count entries
        holidays_grouped = data.groupby(["Holiday", "DayofWeek"])['InvoiceNo'].count().sort_values(ascending=False).to_frame().reset_index()

        # Take the top 10 holidays and pivot the data
        pivot_data = holidays_grouped[:10].pivot(index='DayofWeek', columns='Holiday', values='InvoiceNo').fillna(0)

        # Sort the pivoted data by the order of months
        pivot_data = pivot_data.reindex(day_order, axis=0)

        # Plot the stacked bar chart
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        pivot_data.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='GnBu', ax=ax2)

        # Customize the chart
        plt.title('Total Entries per Holiday by Day', fontsize=20, fontfamily='serif')
        plt.xlabel('Holiday Month', fontsize=15, fontfamily='serif')
        plt.ylabel('Total Entries', fontsize=15, fontfamily='serif')
        plt.tight_layout()
        st.pyplot(fig2)

    col1, col2 = st.columns(2)
    with col1: 
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        data['is_Holiday'] = np.where(data['Holiday'].isna(), 0, 1)

    # Step 2: Analyze Sales by Specific Holidays
        holiday_sales_by_type = data.groupby('Holiday')['TotalPrice'].sum().sort_values(ascending=False)
        # Visualize Sales by Specific Holidays
        colors = sns.color_palette("crest", n_colors=len(holiday_sales_by_type))
        sns.barplot(x=holiday_sales_by_type.index, y=holiday_sales_by_type.values, ax= ax1, palette=colors)
        plt.title("Average Sales by Holiday",fontsize=20, fontfamily='serif')
        plt.xlabel("Holiday",fontsize=15, fontfamily='serif')
        plt.ylabel("Average Sales",fontsize=15, fontfamily='serif')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig1)
    with col2: 
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=data, x='is_Holiday', y='TotalPrice', ax = ax2)
        plt.title('Revenue Distribution: Holidays vs Non-Holidays',fontsize=20, fontfamily='serif')
        plt.xlabel('Is Holiday',fontsize=15, fontfamily='serif')
        plt.ylabel('Revenue',fontsize=15, fontfamily='serif')
        st.pyplot(fig2)


    st.write('<p style="font-size:20px;">Let us see some statistics to determine if holidays affect revenue and number of product purchases.</p>', unsafe_allow_html=True)

    st.write('<p style="font-size:20px;"><b>1. Does the presence of a holiday affect revenue?</b></p>', unsafe_allow_html=True)

    holiday_revenue = data[data['Holiday'].isna() == True]['TotalPrice']
    non_holiday_revenue = data[data['Holiday'].isna() == False]['TotalPrice']

    t_stat, p_value = ttest_ind(holiday_revenue, non_holiday_revenue)

    st.write("t-statistic:", t_stat)
    st.write("p-value:", p_value)
    
    st.write('<p style="font-size:18px;">The p-value suggests no statistically significant difference between the revenue on holidays and non-holidays. In practical terms, this means that whether it is a holiday or not does not have a meaningful impact on the revenue in your dataset. The negative t-statistic further indicates that the mean revenue on holidays might be slightly lower than on non-holidays, but the difference is so small that it islikely due to random variation in the data.</p>', unsafe_allow_html=True)

    st.write('<p style="font-size:20px;"><b>2. Does the presence of a holiday affect number of products purchased?</b></p>', unsafe_allow_html=True)
    holiday_quantity = data[data['Holiday'].isna() == True]['Quantity']
    non_holiday_quantity = data[data['Holiday'].isna() == False]['Quantity']

    t_stat, p_value = ttest_ind(holiday_quantity, non_holiday_quantity)

    st.write("t-statistic:", t_stat)
    st.write("p-value:", p_value)
    st.write('<p style="font-size:18px;">The result suggests that holidays have a positive impact on quantity, and this effect is statistically significant. Businesses likely experience a noticeable increase in purchase frequency on holidays compared to regular days.</p>', unsafe_allow_html=True)
