import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def app():
    st.write('<p style="font-size:33px;"><b>Store Performance</b></p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px;">Analyzing the top ten countries by revenue and product provides valuable customer insights. Revenue leaders identify high-performing markets, guiding resource allocation and strategy. Examining countries by product highlights consumer preferences, revealing where specific offerings resonate. Together, these insights uncover opportunities for targeted marketing, product development, and expansion.</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px;"><b>Hover over a shaded country to see more stats!</b></p>', unsafe_allow_html=True)
    df = pd.read_csv('cleaned_data.csv').drop(columns={'Unnamed: 0'})

    def inside():
        country_sales = df.groupby('Country')['TotalPrice'].sum().reset_index()

        # choropleth map
        fig = px.choropleth(country_sales, 
                            locations='Country', 
                            locationmode='country names', 
                            color='TotalPrice', 
                            hover_name='Country',
                            color_continuous_scale='Bluyl', 
                            projection='natural earth', 
                            title='Sales by Country',
                            range_color=[0, country_sales['TotalPrice'].quantile(0.95)])  # Limit color range to 95th percentile
        fig.for_each_trace(lambda trace: trace.update(hovertemplate=trace.hovertemplate.replace('TotalPrice', 'Total Revenue')))
        fig.update_layout(
            coloraxis_colorbar=dict(title='Total Revenue'),
            title=dict(
            text='Revenue by Country',
            font=dict(size=20, color='black',family='serif')))

        st.plotly_chart(fig)

        col1, col2 = st.columns(2)

        with col1: 
            #Top 10 Countries by Revenue
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            revenue_by_country = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)
            revenue_by_country.plot(kind='bar', color='#96c0b7', ax = ax1)
            ax1.bar_label(ax1.containers[0], fmt='%.0f', label_type='edge')
            plt.title('Top 10 Countries by Revenue', fontsize=20, fontfamily='serif')
            plt.xlabel('Country', fontsize=15, fontfamily='serif')
            plt.ylabel('Revenue',fontsize=15, fontfamily='serif')
            plt.xticks(rotation=45)
            st.pyplot(fig1)

        with col2: 
            #Top 10 Countries by Number of Products Sold
            fig2, ax2 = plt.subplots(figsize=(10, 6.3))
            products_by_country = df.groupby('Country')['TotalPrice'].count().sort_values(ascending=False).head(10)
            products_by_country.plot(kind='bar', color='#96c0b7', ax = ax2)
            ax2.bar_label(ax2.containers[0], fmt='%.0f', label_type='edge')
            plt.title('Top 10 Countries by Number of Products Sold', fontsize=20, fontfamily='serif')
            plt.xlabel('Country', fontsize=15, fontfamily='serif')
            plt.ylabel('Count',fontsize=15, fontfamily='serif')
            plt.xticks(rotation=45)
            st.pyplot(fig2)
            
        st.write('<p style="font-size:20px;">The United Kingdom leads in both revenue and product sales, thanks to its strong local presence, brand recognition, and customer loyalty. Analyzing the UK’s success offers strategies that could be adapted for other regions, helping businesses replicate this success globally.</p>', unsafe_allow_html=True)

        st.write('<p style="font-size:20px;">Analyzing the top 10 products by sales and revenue reveals customer preferences, demand patterns, and high-value items. This dual perspective helps businesses refine strategies, optimize pricing, and tailor product offerings to local markets, ensuring greater customer satisfaction and financial success.</p>', unsafe_allow_html=True)
    
        st.write('<p style="font-size:20px;">Reviewing the bottom 10 products by sales and revenue helps identify underperforming items. Low sales may indicate poor demand or ineffective strategies, while low revenue highlights products with weak profit margins. Analyzing these trends allows businesses to make informed decisions about product adjustments and improve overall profitability.</p>', unsafe_allow_html=True)
    

        st.write('<p style="font-size:20px;">Now let us look into country-specific data!</p>', unsafe_allow_html=True)
    
    def products_loc_filter(countries):
        data = df[df['Country'].isin(countries)]

        # Top 10 Most Sold Products 
        col1, col2 = st.columns(2)
        with col1:
            prod = data[data["Quantity"] >=0]
            most_sold_products = prod.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            most_sold_products.plot(kind='bar', color='#96c0b7', ax = ax1)
            ax1.bar_label(ax1.containers[0], fmt='%.0f', label_type='edge')
            plt.title('Top 10 Most Sold Products', fontsize=20, fontfamily='serif')
            plt.xlabel('Product', fontsize=15, fontfamily='serif')
            plt.ylabel('Total Quantity Sold', fontsize=15, fontfamily='serif')
            st.pyplot(fig1)
        # Top 10 Least Sold Products 
        with col2: 
            prod = data[data["Quantity"] >=0]
            least_sold_products = prod.groupby('Description')['Quantity'].sum().sort_values().head(10)
            fig2, ax2 = plt.subplots(figsize=(10, 5.7))
            least_sold_products.plot(kind='bar', color='#96c0b7', ax = ax2)
            ax2.bar_label(ax2.containers[0], fmt='%.0f', label_type='edge')
            plt.title('Top 10 Least Sold Products', fontsize=20, fontfamily='serif')
            plt.xlabel('Product', fontsize=15, fontfamily='serif')
            plt.ylabel('Total Quantity Sold', fontsize=15, fontfamily='serif')
            st.pyplot(fig2)

        # Top 10 Products By Revenue 
        col1, col2 = st.columns(2)
        with col1: 
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            revenue_by_product = data.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)
            revenue_by_product.plot(kind='bar', color='#96c0b7', ax = ax1)
            ax1.bar_label(ax1.containers[0], fmt='%.0f', label_type='edge')
            plt.title('Top 10 Products by Revenue', fontsize=20, fontfamily='serif')
            plt.xlabel('Product', fontsize=15, fontfamily='serif')
            plt.ylabel('Revenue', fontsize=15, fontfamily='serif')
            st.pyplot(fig1)
        # Bottom 10 Products By Revenue 
        with col2:    
            fig2, ax2 = plt.subplots(figsize=(10, 5.7))
            temp_rev = data[data['TotalPrice'] >=0]
            revenue_by_product = temp_rev.groupby('Description')['TotalPrice'].sum().sort_values().head(10)
            revenue_by_product.plot(kind='bar', color='#96c0b7', ax = ax2)
            ax2.bar_label(ax2.containers[0],label_type='edge')
            plt.title('Bottom 10 Products by Revenue', fontsize=20, fontfamily='serif')
            plt.xlabel('Product', fontsize=15, fontfamily='serif')
            plt.ylabel('Revenue', fontsize=15, fontfamily='serif')
            st.pyplot(fig2)

        st.write('<p style="font-size:20px;">Now things get a little interesting! In the data, there are negative values for the unit price, which indicate that a customer returned the product. Let us see what the top to returned products are, shall we?</p>', unsafe_allow_html=True)
    
        # Most Returned
        returned = data[data['Returned'] == True]
        fig, ax = plt.subplots(figsize=(10, 4))
        returns =returned.groupby("Description")['InvoiceNo'].count().sort_values(ascending = False)[:10]
        returns.plot(kind='bar', color='#96c0b7', ax = ax)
        ax.bar_label(ax.containers[0], fmt='%.0f', label_type='edge')
        plt.title('Most Returned Products', fontsize=20, fontfamily='serif')
        plt.xlabel('Product', fontsize=15, fontfamily='serif')
        plt.ylabel('Count', fontsize=15, fontfamily='serif')
        st.pyplot(fig)

        st.write('<p style="font-size:20px;">Understanding which products were returned is essential for identifying potential issues that may be impacting customer satisfaction and operational efficiency. High return rates can signal problems such as poor product quality, misleading product descriptions, sizing or functionality issues, or unmet customer expectations. Analyzing returned products provides valuable insights into why customers are dissatisfied, enabling businesses to address these concerns proactively by improving product design, refining marketing materials, or enhancing quality control processes. Furthermore, tracking return patterns can highlight trends, such as specific categories or regions with high return rates, which may require targeted interventions. Minimizing returns not only reduces costs associated with reverse logistics and restocking but also builds customer trust and loyalty by demonstrating a commitment to delivering value and meeting expectations.</p>', unsafe_allow_html=True)
    
    # Drop Down to Choose Country
    if True: 
        inside()
    region = st.multiselect('Pick a Region', ["All", 'Western Europe', 'Northern Europe', 'Eastern Europe', 
                                             'Southern Europe', 'Middle East', 'East Asia', 'Southeast Asia', 
                                             'Oceania', 'North America', 'South America', 'Other'])
    if len(region) >= 1:
        if "All" in region:
            products_loc_filter(list(df['Country'].unique()))  # Pass all countries if "All" is selected
        else:
            dataset = df[df['Region'].isin(region)]  # Filter dataset by selected regions
            countries = st.selectbox('Select Countries', ['All'] + list(dataset['Country'].unique()))  # Select countries
            if countries:
                if countries == "All":
                    products_loc_filter(list(dataset['Country'].unique()))  # Pass all countries if "All" is selected
                else:
                    products_loc_filter([countries])  # Pass the selected countries if "All" is not selected
