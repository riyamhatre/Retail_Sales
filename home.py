import pandas as pd
import numpy as np
import math
import streamlit as st


def app():
    st.write('<p style="font-size:33px;"><b>Retail Sales!</b></p>', unsafe_allow_html=True)

    st.write("""The dataset being used is the UCI Repository Online Retail dataset, 
             which contains transactional data for a UK-based, non-store online retailer. 
             The dataset spans transactions that occurred between December 2010 and December 2011. 
             The company primarily sells unique all-occasion gifts, with a significant portion of 
             its customers being wholesalers. This dataset includes information on customer 
             purchases, product details, transaction dates, and sales values, offering valuable 
             insights into sales trends, customer behavior, and purchasing patterns. It serves as a 
             rich resource for analyzing various aspects of retail sales and customer segmentation.""")
    
    st.write("""Using this dataset, I will analyze sales trends and perform customer segmentation to identify distinct purchasing 
             patterns and target key customer groups effectively. By leveraging advanced analytics techniques, 
             I will uncover drivers of high sales and pinpoint low-performing categories, providing actionable 
             insights for improvement. Incorporating external factors such as holidays, weather, and location 
             demographics into my analysis will offer a comprehensive understanding of their impact on sales,
              enabling me to make data-informed decisions. Additionally, I will provide tailored suggestions to 
             enhance sales performance and optimize product placements, ensuring businesses can adapt strategies 
             to maximize revenue and meet customer demands efficiently.""")

    

    st.write("""
The main questions I aim to answer in this analysis revolve around understanding sales performance and customer behavior in-depth. 
I will explore the following key points:
""")

    # Bullet points for main questions
    st.markdown("""
    - **What are the primary factors influencing sales?**  
    - **How do customer demographics and behaviors vary across different locations?**  
    - **How do external factors, such as weather and holidays, impact sales?**  
    """)

    # KPI explanation
    st.write("""
    To guide this analysis, I will track and analyze the following key performance indicators (KPIs):
    - **Revenue Growth**  
    - **Sales by Location**  
    - **Customer Retention Rates**  
    - **Impact of Holidays**
    """)

    st.write('These KPIs will help derive actionable insights and ensure our strategy aligns with business objectives.')
