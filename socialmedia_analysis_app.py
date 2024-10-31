import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data for handset manufacturers and top handsets
handsets_data = {
    'Handset Manufacturer': ['Apple', 'Samsung', 'Huawei', 'Xiaomi', 'Nokia'],
    'Total Handsets': [50, 75, 30, 40, 20],
    'Average Data Usage (GB)': [15, 20, 10, 12, 5],
    'Customer Satisfaction (%)': [90, 85, 75, 80, 65]
}
handsets_df = pd.DataFrame(handsets_data)

# Sample data for general activity (as provided)
data = {
    'Column Name': [
        'Social Media DL (Bytes)', 'Social Media UL (Bytes)', 'Netflix DL (Bytes)', 
        'Netflix UL (Bytes)', 'Google DL (Bytes)', 'Google UL (Bytes)', 
        'Email DL (Bytes)', 'Email UL (Bytes)', 'Gaming DL (Bytes)', 'Gaming UL (Bytes)',
        'Youtube DL (Bytes)', 'Youtube UL (Bytes)', 'Total DL (Bytes)', 'Total UL (Bytes)'
    ],
    'Sum (Bytes)': [
        2.693001e+11, 4.939298e+09, 1.744039e+12, 1.650274e+12, 8.626186e+11,
        3.084833e+11, 2.687611e+11, 7.010648e+10, 6.330713e+13, 1.243268e+12,
        1.745123e+12, 1.651423e+12, 6.8196969155275e+13, 6.168222065022292e+12
    ]
}
sums_df = pd.DataFrame(data)

# Session data
total_duration_ms = 15691365831902.0
total_duration_hr = total_duration_ms / 3600000
total_entries = 150001

# Streamlit App with Multiple Pages
st.title("TellCo Telecom Data Analysis Dashboard")

# Page Navigation
page = st.sidebar.selectbox("Select Page", ["Customer Insights", "Growth Opportunities", "Handset Overview", "Handset Analysis"])

# Page 1: Customer Insights
if page == "Customer Insights":
    st.header("Customer Activity Overview")

    # Displaying key metrics
    st.write(f"**Total Number of Entries in Dataset**: {total_entries}")
    st.write(f"**Total Session Duration (hours)**: {total_duration_hr:.2f}")
    st.write(f"**Total Downlink Data (Bytes)**: {data['Sum (Bytes)'][12]:.2e}")
    st.write(f"**Total Uplink Data (Bytes)**: {data['Sum (Bytes)'][13]:.2e}")
    
    # Visualization
    st.subheader("Data Volume by Service Type")
    plt.figure(figsize=(10, 8))
    plt.barh(sums_df['Column Name'], sums_df['Sum (Bytes)'], color='skyblue')
    plt.xlabel('Sum (Bytes)')
    plt.title('Data Volume for Various Services')

    # Adding text labels for clarity in the plot
    for index, value in enumerate(sums_df['Sum (Bytes)']):
        plt.text(value, index, f'{value:.2e}', va='center', ha='left', fontsize=8,
                 color='red' if 'Total' in sums_df['Column Name'][index] else 'black')

    plt.grid(axis='x')
    st.pyplot(plt)

    # Insights Summary
    st.write("""### Key Insights:
    - **High Downlink Usage in Gaming and Streaming Services**: Reflects a primarily consumer-driven user base, especially among younger demographics.
    - **Predominant Consumer Role**: Low uplink (UL) data suggests that customers engage more in content consumption rather than creation.
    - **Social Media Engagement**: Indicates active online engagement, providing an opportunity to capitalize on entertainment-focused and social plans.
    """)

# Page 2: Growth Opportunities
elif page == "Growth Opportunities":
    st.header("Strategic Growth Opportunities for TellCo")

    # Growth Strategy Insights
    st.write("""### Potential Growth and Strategic Opportunities
    Based on the analysis of TellCo’s customer usage data, the following growth strategies are recommended to leverage the current market demands and expand the business:

    1. **Targeted Youth and Gaming Plans**: Given the high data consumption in gaming, especially downlink, creating targeted data packages for younger demographics focused on gaming and streaming services could increase customer acquisition and retention.
    
    2. **Partnerships with Streaming Services**: Significant usage of Netflix and YouTube highlights potential for bundled offerings with popular streaming services. This could include subscription bundles or data packages tailored for heavy streaming users.

    3. **Expand Business Plans**: The relatively low data usage in productivity (e.g., email) services suggests room to grow in business-focused data plans. Developing business-friendly packages with priority connectivity and higher uplink capacity could attract professional users.

    4. **Enhancing Social Media Plans**: High social media usage indicates potential for specialized data plans focused on social platforms. Plans emphasizing unlimited social media access or data bonuses for social engagement could resonate with the existing user base.

    5. **Customer Retention Strategies**: Given the high total session duration and user engagement, loyalty programs or tiered subscription plans could be introduced to retain high-usage customers.
    
    ### Recommendation for TellCo Buyer
    Based on the analysis, TellCo demonstrates strong growth potential within a consumer-driven audience, especially in entertainment and social media sectors. However, to attract a diverse range of users, particularly in business sectors, new data packages may be needed. If the buyer’s objective aligns with expanding TellCo’s consumer base in entertainment and social media, this acquisition is promising. If the buyer’s focus includes business and productivity, strategic development will be essential.
    """)

# Page 3: Handset Overview
elif page == "Handset Overview":
    st.header("Top Handsets Used by Customers")
    
    # Sample data for handsets and manufacturers
    handset_data = {
        'Handset': [
            'Huawei B528S-23A', 'Apple iPhone 6S (A1688)', 'Apple iPhone 6 (A1586)',
            'Apple iPhone 7 (A1778)', 'Apple iPhone Se (A1723)', 'Apple iPhone 8 (A1905)',
            'Apple iPhone Xr (A2105)', 'Samsung Galaxy S8 (Sm-G950F)', 
            'Apple iPhone X (A1901)', 'Samsung Galaxy A5 (Sm-A520F)'
        ],
        'Usage Count': [
            19752, 9419, 9023, 6326, 5187, 4993, 4568, 4520, 3813, 3724
        ]
    }

    manufacturer_data = {
        'Manufacturer': ['Apple', 'Samsung', 'Huawei'],
        'Total Handsets': [59565, 40839, 34423]
    }

    # Create DataFrames
    handset_df = pd.DataFrame(handset_data)
    manufacturer_df = pd.DataFrame(manufacturer_data)

    # Handset usage bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(handset_df['Handset'], handset_df['Usage Count'], color='lightblue')
    plt.xlabel('Usage Count')
    plt.title('Top 10 Handsets Used by Customers')
    st.pyplot(plt)

    # Display manufacturer data
    st.subheader("Total Handsets by Manufacturer")
    plt.figure(figsize=(8, 5))
    plt.bar(manufacturer_df['Manufacturer'], manufacturer_df['Total Handsets'], color='salmon')
    plt.ylabel('Total Handsets')
    plt.title('Handsets by Manufacturer')
    st.pyplot(plt)

    # Display top handsets from the top manufacturers
    st.subheader("Top 5 Handsets from Top Manufacturers")
    st.write(handset_df.head(5))

# Page 4: Handset Analysis
elif page == "Handset Analysis":
    st.header("Handset and Manufacturer Analysis")
    
    # Insights
    st.write("""### Interpretation:
    1. **Dominance of Major Brands**: Apple leads significantly in total handsets, followed by Samsung and Huawei.
    2. **Top Handset Usage**: The Huawei B528S-23A is the most used device, indicating a strong market presence.
    3. **Smartphone Preferences**: Users prefer brands that offer high-quality applications and services, particularly from Apple.

    ### Recommendations:
    1. **Targeted Advertising Partnerships**: Collaborate with Apple and Samsung for joint promotions.
    2. **Promote Device-Specific Offers**: Create campaigns for specific handsets to incentivize upgrades.
    3. **Focus on Loyalty Programs**: Implement programs rewarding high data usage, especially for iPhone users.
    4. **Utilize User Insights**: Conduct surveys to refine service offerings based on user preferences.
    5. **Monitor Emerging Trends**: Stay updated on new models and adapt marketing strategies accordingly.
    """)

# Footer
st.sidebar.write("**TellCo Analysis Report**")
st.sidebar.write("Provide insights to determine acquisition worthiness.")
