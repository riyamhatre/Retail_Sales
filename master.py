import streamlit as st
import pandas as pd 
import numpy as np

import home
import time_sales
import external_factors
import summary
import store_performance
import customer_insight

PAGES = {
    "Home": home,
    "Sales Trend Over Time": time_sales,
	"Customer Insights": customer_insight,
    "Store Performance": store_performance,
    "External Factors": external_factors, 
    "Summary": summary
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()