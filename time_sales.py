import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def app():
    st.write('<p style="font-size:33px;"><b>Sales Trend Over Time</b></p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px;">As already mentioned, this data is only for one store based in the United Kingdom. The store owners need to determine the behavior of the sales over time for each location and figure out a solution that is location-based.</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px;">Pick a region that you are interested in studying. Subsequently, pick a country in that region to observe! Hover over the data points to see the actual values!</p>', unsafe_allow_html=True)
    df = pd.read_csv('cleaned_data.csv').drop(columns={'Unnamed: 0'})

    
    def graphs(countries):
        data = df[df['Country'].isin(countries)]
        # Monthly Revenue
        data['MonthYear'] = pd.to_datetime(data['InvoiceDate']).dt.to_period('M')
        monthly_revenue = data.groupby('MonthYear')['TotalPrice'].sum()

        # Plotly figure
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=monthly_revenue.index.astype(str),  # Convert PeriodIndex to string for x-axis labels
            y=monthly_revenue.values,
            mode='lines+markers',
            line=dict(color='#96c0b7'),
            marker=dict(symbol='circle'),
            text=monthly_revenue.values,  # Set the label text for each data point
            hoverinfo='text',  # This will show the 'text' when hovering
        ))

        # Customize the layout
        fig.update_layout(
            title='Monthly Revenue Trend (Dec 2010-Dec 2011)',
            title_font=dict(size=20, family='serif', color='black'),  # Title font properties
            xaxis_title='Month-Year',
            xaxis_title_font=dict(size=15, family='serif', color='black'),  # X-axis title font properties
            yaxis_title='Total Revenue',
            yaxis_title_font=dict(size=15, family='serif', color='black'),  # Y-axis title font properties
            xaxis_tickangle=-45,  # Rotate x-axis labels for better visibility
            template='plotly_white',  # Optional: sets a white background
        )

        st.write('<p style="font-size:15px;"Here, we have the sales trend over time. Observe which months have more sales or less sales. This could be due to various reasons, such as holidays or weather conditions, which we will look into closely later.</p>', unsafe_allow_html=True)
        st.plotly_chart(fig)
        st.write('<p style="font-size:20px;">Now, let us see if the customers purchase more on weekends or weekdays or certain times of the day.</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)

        with col1: 
            # Sales by Day of Week
            sales_by_day = data.groupby('DayofWeek')['TotalPrice'].sum()
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            sales_by_day = sales_by_day.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
            sales_by_day.plot(kind='bar', color='#96c0b7', ax = ax1)
            ax1.bar_label(ax1.containers[0], fmt='%.0f', label_type='edge')
            plt.xticks(rotation=45, ha='right')
            plt.title('Revenue by Day of Week',fontsize=20, fontfamily='serif')
            plt.xlabel('Day of Week',fontsize=15, fontfamily='serif')
            plt.ylabel('Revenue',fontsize=15, fontfamily='serif')
            st.pyplot(fig1)

        with col2: 
            # Sales by Hour
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            data['Hour'] = pd.to_datetime(data['InvoiceDate']).dt.hour
            sales_by_hour = data.groupby('Hour')['TotalPrice'].sum()
            sales_by_hour.plot(kind='bar', color='#96c0b7', ax = ax2)
            ax2.bar_label(ax2.containers[0], fmt='%.0f', label_type='edge')
            plt.title('Revenue by Hour of Day',fontsize=20, fontfamily='serif')
            plt.xticks(rotation=45, ha='right')
            plt.xlabel('Hour',fontsize=15, fontfamily='serif')
            plt.ylabel('Revenue',fontsize=15, fontfamily='serif')
        
            st.pyplot(fig2)
        st.write('<p style="font-size:20px;">The insight gained from these graphs can help this store determine which time periods have high and low performance. To increase performance during those time periods, the store could work to increase advertisements or the frequency of sales to encourage the customers to make more purchases during these times. </p>', unsafe_allow_html=True)
        
    

    # Region filtering
    region = st.multiselect('Please select a region to filter the data.', ["All", 'Western Europe', 'Northern Europe', 'Eastern Europe', 
                                             'Southern Europe', 'Middle East', 'East Asia', 'Southeast Asia', 
                                             'Oceania', 'North America', 'South America', 'Other'])

    # Drop Down to Choose Country
    if len(region) >= 1:
        if "All" in region:
            graphs(list(df['Country'].unique()))  # Pass all countries if "All" is selected
        else:
            dataset = df[df['Region'].isin(region)]  # Filter dataset by selected regions
            countries = st.selectbox('Select a Country', ['All'] + list(dataset['Country'].unique()))  # Select countries
            if countries:
                if countries == "All":
                    graphs(list(dataset['Country'].unique()))  # Pass all countries if "All" is selected
                else:
                    graphs([countries])  # Pass the selected countries if "All" is not selected
