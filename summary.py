import streamlit as st
import pandas as pd
import numpy as np

def app():
	st.write('<p style="font-size:33px;"><b>Project Findings and Recommendations</b></p>', unsafe_allow_html=True)

	# Key Findings Section
	st.subheader("Key Findings")
	st.markdown(
		"""
		1. **Time Periods as Predictors of Revenue**  
		- Factors like month, day of the week, and hour of the day significantly predict revenue trends.  
		- Variations across countries highlight the importance of understanding local shopping behaviors, such as weekday vs. weekend patterns and holiday shopping.  
		- **Recommendation**: Use time-based insights to optimize store hours, inventory, and marketing campaigns, such as launching promotions during holidays or peak hours.

		2. **United Kingdom Dominance**  
		- The UK leads in revenue and product sales due to strong brand loyalty and a local presence.  
		- This success provides an opportunity to replicate effective strategies in other regions.  
		- **Recommendation**: Analyze the UK market deeply to identify practices like loyalty incentives and premium positioning, and adapt these strategies globally.

		3. **Product Performance Insights**  
		- **Top Products by Revenue**: High-value products drive profitability and present opportunities for upselling or premium bundling.  
		- **Top Products by Volume**: Frequently sold items reflect price sensitivity and demand patterns, ideal for driving traffic and bundling with higher-margin items.  
		- **Bottom Products**: Underperforming products may point to pricing, marketing, or appeal issues.  
		- **Recommendations**:  
			- Promote high-revenue products through premium campaigns.  
			- Use high-volume items as entry points and bundle them with profitable products.  
			- Reassess or enhance underperforming items to meet customer needs better.

		4. **Customer Behavior and Revenue Drivers**  
		- **Customer Segments**:  
			- *Budget-Conscious Regular Shoppers*: Frequent buyers of lower-cost items, contributing to volume.  
			- *High-Value Buyers*: Smaller group with significant impact on revenue.  
			- *Occasional Buyers*: Less frequent shoppers who still add value to sales.  
		- **Key Insight**: Each additional purchase has a larger impact on total revenue than increasing the quantity per transaction, but both contribute positively.  
		- **Recommendations**:  
			- Encourage repeat purchases through loyalty programs and personalized offers.  
			- Upsell high-value products to occasional and high-spending buyers.

		5. **Holiday and Non-Holiday Trends**  
		- Holidays lead to significant revenue spikes, while non-holiday periods show consistent patterns tied to routines.  
		- **Recommendations**:  
			- Launch holiday-specific campaigns with curated bundles or discounts.  
			- Target key non-holiday periods to sustain consistent revenue.
		"""
	)


	# Closing Summary
	st.subheader("Conclusion")
	st.markdown(
		"""
		By integrating insights from time-based trends, product performance, and customer behavior, businesses can refine global and regional strategies.  
		- **Focus on high-value customers** to maximize revenue.  
		- **Leverage time-based insights** to optimize sales during peak periods.  
		- **Address underperforming products** to free up resources for higher-impact opportunities.  

		A data-driven approach ensures sustainable growth and a competitive edge in a dynamic market.
		"""
	)
