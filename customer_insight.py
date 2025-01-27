import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


st.set_page_config(layout="wide")

def app():
    st.header("Customer Insight")
    st.subheader("General Customer Data")
    st.write('<p style="font-size:20px;">Let us first take a look at the top ten customers and what their top products were.</p>', unsafe_allow_html=True)

    data = pd.read_csv('cleaned_data.csv').drop(columns={'Unnamed: 0'})

    def insight(data):

        col1, col2 = st.columns(2)
        revs = data.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)
        revenue_per_customer = data[data['CustomerID'].isin(list(revs.index))]

        with col1: 
            # Total Revenue for Top 10 Customers
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            revs.plot(kind='bar', color='#96c0b7', ax = ax1)
            ax1.bar_label(ax1.containers[0], fmt='%.0f', label_type='edge')
            plt.title('Total Revenue for Top 10 Customers',fontsize=20, fontfamily='serif')
            plt.xlabel('Customer ID',fontsize=15, fontfamily='serif')
            plt.ylabel('Revenue',fontsize=15, fontfamily='serif')
            st.pyplot(fig1)
        with col2:
            # Top 10 Products Bought by Top Customers
            fig2, ax2 = plt.subplots(figsize=(10, 5.7))
            customer_prods = revenue_per_customer.groupby('Description')['InvoiceNo'].count().sort_values(ascending=False).head(10)
            customer_prods.plot(kind='bar', color='#96c0b7', ax = ax2)
            ax2.bar_label(ax2.containers[0], fmt='%.0f', label_type='edge')
            plt.title('Top 10 Products Bought by Top Customers',fontsize=20, fontfamily='serif')
            plt.xlabel('Product',fontsize=15, fontfamily='serif')
            plt.ylabel('Count',fontsize=15, fontfamily='serif')
            st.pyplot(fig2)

        st.write('<p style="font-size:20px;">Now, let us look at the frequency of purchases and average order value for the top 10 customers.</p>', unsafe_allow_html=True)


        col1, col2 = st.columns(2)

        with col1: 
            # Frequency of Purchases for Top 10 Customers
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            frequency_per_customer = revenue_per_customer.groupby('CustomerID')['InvoiceNo'].nunique().sort_values(ascending=False).head(10)
            frequency_per_customer.plot(kind='bar', color='#96c0b7', ax = ax1)
            ax1.bar_label(ax1.containers[0], fmt='%.0f', label_type='edge')
            plt.title('Frequency of Purchases for Top 10 Customers',fontsize=20, fontfamily='serif')
            plt.xlabel('Customer ID',fontsize=15, fontfamily='serif')
            plt.ylabel('Count',fontsize=15, fontfamily='serif')
            st.pyplot(fig1)
        with col2:
            revs = data.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)
            # Average Order Value (AOV) for Top 10 Customers
            revenue_per_cust = revenue_per_customer.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False)
            frequency_per_customer = revenue_per_customer.groupby('CustomerID')['InvoiceNo'].nunique().sort_values(ascending=False)
            aov_per_customer = revenue_per_cust / frequency_per_customer
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            aov = aov_per_customer.sort_values(ascending=False).head(10)
            aov.plot(kind='bar', color='#96c0b7', ax = ax2)
            ax2.bar_label(ax2.containers[0], fmt='%.0f', label_type='edge')
            plt.title('Average Order Value (AOV) for Top 10 Customers',fontsize=20, fontfamily='serif')
            plt.xlabel('Customer ID',fontsize=15, fontfamily='serif')
            plt.ylabel('Average',fontsize=15, fontfamily='serif')
            st.pyplot(fig2)

        
        st.subheader("Statistical Analysis")

        st.write('<p style="font-size:20px;">This script performs customer-level analysis using transactional data. It aggregates customer purchase history, calculates key metrics (e.g., purchase frequency, total quantity, and total revenue), and builds a linear regression model to explore how purchase frequency and total quantity contribute to total revenue. By evaluating the model performance (R-squared and coefficients), we gain insights into customer behavior and can use the findings to inform business strategies such as targeted marketing, demand forecasting, and revenue optimization.</p>', unsafe_allow_html=True)


        # Create customer-level data
        customer_data = data.groupby('CustomerID').agg({
            'InvoiceNo': 'nunique',  # Number of unique purchases
            'Quantity': 'sum',       # Total quantity purchased
            'TotalPrice': 'sum',     # Total revenue
        }).reset_index()

        # Regression: Total revenue vs. purchase frequency and total quantity
        X = customer_data[['InvoiceNo', 'Quantity']]
        y = customer_data['TotalPrice']

        # Train-test split and regression
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        st.write("R-Score: ", r2_score(y_test, y_pred))
        st.write("Coefficients:", model.coef_[0],model.coef_[1] )

        st.write("""
        An R-squared of 0.778 means that 77.8% of the variation in TotalPrice is explained by InvoiceNo and Quantity. 
        This suggests that these predictors are effective in explaining customer spending.
        """)

        # Encouraging Repeat Purchases section
        st.write('<p style="font-size:25px;"><b>Encourage Repeat Purchases</b></p>', unsafe_allow_html=True)
        st.write('<p style="font-size:20px;"><b>Why?</b></p>', unsafe_allow_html=True)
        st.write("""
        The coefficient for InvoiceNo (45.27) shows that each additional purchase has a larger impact on total revenue than increasing Quantity (1.63).
        """)
        st.write('<p style="font-size:25px;"><b>How to Implement?</b></p>', unsafe_allow_html=True)
        st.write("""
        - Offer loyalty programs where customers earn rewards or discounts after a certain number of purchases.
        - Use personalized email campaigns with product recommendations or discounts.
        - Introduce limited-time offers to encourage urgency for repeat purchases.
        """)

        # Optimizing Quantity-Based Offers section
        st.write('<p style="font-size:25px;"><b>Optimize Quantity-Based Offers</b></p>', unsafe_allow_html=True)
        st.write('<p style="font-size:20px;"><b>Why?</b></p>', unsafe_allow_html=True)
        st.write("""
        Increasing Quantity has a smaller impact, but it still contributes positively to revenue.
        """)
        st.write('<p style="font-size:25px;"><b>How to Implement?</b></p>', unsafe_allow_html=True)
        st.write("""
        - Create bundle deals (e.g., "Buy 2, Get 1 Free").
        - Offer volume-based discounts (e.g., "10% off when you buy 5+ items").
        - Use cross-selling strategies by recommending related items to increase transaction size.
        """)

        st.subheader("Customer Segmentation")
        # Aggregating customer metrics for clustering
        customer_features = data.groupby('CustomerID').agg({
            'TotalPrice': ['sum', 'mean'],      # Total and Average Purchase
            'InvoiceNo': 'count',              # Frequency of Purchases
            'Returned': 'sum',                 # Total Returns
            'Region': 'first'                  # Retain region for reference
        }).reset_index()

        # Flatten column names
        customer_features.columns = ['CustomerID', 'Total_Purchase', 'Avg_Purchase', 'Frequency', 'Returns', 'Region']

        # Fill any missing values (e.g., Returns may have NaN for customers without returns)
        customer_features.fillna(0, inplace=True)

        # Normalize the numerical features
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(customer_features[['Total_Purchase', 'Avg_Purchase', 'Frequency', 'Returns']])

        # Perform K-Means Clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        customer_features['Cluster'] = kmeans.fit_predict(scaled_features)

        # Visualize Clusters using Pairplot
        cluster_graphs = sns.pairplot(customer_features, vars=['Total_Purchase', 'Avg_Purchase', 'Frequency'], hue='Cluster', palette='Set2')
        st.pyplot(cluster_graphs)

        # Analyze Each Cluster
        cluster_analysis = customer_features.groupby('Cluster').agg({
            'Total_Purchase': ['mean', 'sum'],
            'Avg_Purchase': 'mean',
            'Frequency': 'mean',
            'Returns': 'mean',
            'CustomerID': 'count'
        }).reset_index()

        # Rename columns for readability
        cluster_analysis.columns = ['Cluster', 'Avg_Total_Purchase', 'Total_Purchase', 'Avg_Purchase', 'Avg_Frequency', 'Avg_Returns', 'Customer_Count']
        st.write(cluster_analysis)

        st.write('<p style="font-size:25px;"><b>Cluster 0: Regular Shoppers</b></p>', unsafe_allow_html=True)
        st.write("""
        - These customers make frequent, smaller purchases, contributing steadily to overall revenue.
        - They have occasional returns but represent the majority of the customer base.
        - Marketing efforts should focus on **upselling** or **cross-selling** to increase their purchase value.""")

        # Cluster 1: High-Value Buyers
        st.write('<p style="font-size:25px;"><b>Cluster 1: High-Value Buyers</b></p>', unsafe_allow_html=True)
        st.write("""
        - A small group of customers with **high spending per purchase** and extremely frequent transactions.
        - Likely wholesale or bulk buyers, with a higher rate of returns.
        - Retention strategies and **personalized offers** could help maintain loyalty and maximize revenue.""")

        # Cluster 2: Moderate Spenders
        st.write('<p style="font-size:25px;"><b>Cluster 2: Moderate Spenders</b></p>', unsafe_allow_html=True)
        st.write("""
        - Customers who make **infrequent transactions** but spend significantly when they shop.
        - They contribute moderately to overall revenue and rarely return items.
        - Focus on campaigns to **increase shopping frequency** and drive engagement.""")
    
    insight(data)

        
