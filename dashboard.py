import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="World Bank Data Dashboard for key Macroeconomic Indicators",
    layout="wide",
    page_icon="🌍"
)

# --- Data Loading (from the cleaned file) ---
@st.cache_data
def get_cleaned_data():
    """
    Loads the pre-cleaned data from the pickle file.
    """
    try:
        data = pd.read_pickle("cleaned_data.pkl")
        return data
    except FileNotFoundError:
        st.error("Cleaned data file not found. Please run data_cleaner.py first.")
        st.stop()

data = get_cleaned_data()

# --- Sidebar for User Controls ---
st.sidebar.header("Dashboard Filters ⚙️")

try:
    all_countries = sorted(data.columns.get_level_values(1).unique().tolist())
except IndexError:
    all_countries = []

if not all_countries:
    st.warning("No data found in the cleaned file. Please run data_cleaner.py and check your data.")
    st.stop()

selected_country = st.sidebar.selectbox("Select a Country:", options=all_countries, index=all_countries.index('India') if 'India' in all_countries else 0)

# The corrected code for the multiselect widget
default_compare = [c for c in ['United States', 'China'] if c != selected_country]
compare_countries = st.sidebar.multiselect("Compare with:", options=[c for c in all_countries if c != selected_country], default=default_compare)

# New: Indicator selector for comparison chart
all_indicators = data.columns.get_level_values(0).unique().tolist()
selected_indicator_comp = st.sidebar.selectbox("Select Indicator to Compare:", options=all_indicators, index=all_indicators.index('GDP Growth (%)'))

min_year = int(data.index.min()) if not data.empty else 1960
max_year = int(data.index.max()) if not data.empty else 2024
selected_year_range = st.sidebar.slider(
    "Select Year Range:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

filtered_data = data.loc[selected_year_range[0]:selected_year_range[1]]

# --- Main Dashboard Layout ---
st.title(f"🌍 Economic Dashboard for {selected_country}")
st.markdown("### Powered by World Bank Data")

## 1. Macroeconomic Overview
st.subheader("1. Macroeconomic Overview")
col1, col2, col3 = st.columns(3)

# Extract data for the selected country
country_data = filtered_data.loc[:, pd.IndexSlice[:, selected_country]]
country_data.columns = country_data.columns.droplevel(1)

with col1:
    latest_gdp_growth = country_data['GDP Growth (%)'].iloc[-1] if not country_data.empty else 0
    st.metric("Latest GDP Growth", f"{latest_gdp_growth:.2f}%")

with col2:
    latest_exports = country_data['Exports (USD)'].iloc[-1] / 1e9 if not country_data.empty else 0
    st.metric("Latest Exports", f"${latest_exports:.2f}B")

with col3:
    latest_imports = country_data['Imports (USD)'].iloc[-1] / 1e9 if not country_data.empty else 0
    st.metric("Latest Imports", f"${latest_imports:.2f}B")

st.markdown("---")

fig_gdp = px.line(
    country_data,
    x=country_data.index,
    y='GDP Growth (%)',
    title=f"Real GDP Growth for {selected_country} Over Time",
    template="plotly_white"
)
st.plotly_chart(fig_gdp, use_container_width=True)

# New: Export button for single country data
st.download_button(
    label=f"Export Data for {selected_country}",
    data=country_data.to_csv().encode('utf-8'),
    file_name=f"{selected_country}_all_data.csv",
    mime="text/csv",
)

# New: Multi-country comparison chart
if compare_countries:
    st.subheader(f"{selected_indicator_comp} Comparison: {selected_country} vs. Others")
    
    # Extract data for the selected indicator and countries
    comparison_data = filtered_data.loc[:, pd.IndexSlice[selected_indicator_comp, [selected_country] + compare_countries]]
    comparison_data.columns = comparison_data.columns.droplevel(0)
    
    fig_comp = px.line(
        comparison_data,
        x=comparison_data.index,
        y=comparison_data.columns,
        title=f"{selected_indicator_comp} Over Time",
        template="plotly_white"
    )
    st.plotly_chart(fig_comp, use_container_width=True)
    
    # Export button for comparison data
    st.download_button(
        label=f"Export {selected_indicator_comp} Data",
        data=comparison_data.to_csv().encode('utf-8'),
        file_name=f"{selected_indicator_comp.replace(' (%)', '').replace(' ', '_')}_comparison_data.csv",
        mime="text/csv",
    )

# New: Choropleth Map
st.markdown("---")
st.subheader("World Map: GDP Growth by Country")
map_year = st.selectbox("Select Year for Map:", options=filtered_data.index.unique(), index=len(filtered_data.index)-1)
map_data = filtered_data.loc[map_year, 'GDP Growth (%)'].T.reset_index()
map_data.columns = ['country', 'GDP Growth (%)']

fig_map = px.choropleth(
    map_data,
    locations='country',
    locationmode='country names',
    color='GDP Growth (%)',
    hover_name='country',
    color_continuous_scale=px.colors.sequential.Plasma,
    title=f'GDP Growth (Annual %) in {map_year}'
)
st.plotly_chart(fig_map, use_container_width=True)

# New: Export option for all filtered data
st.markdown("---")
st.subheader("Export All Filtered Data")

# New selectbox for choosing which indicator to export
export_indicator = st.selectbox("Select Indicator to Export All Countries for:", options=all_indicators)

# Corrected code for creating the export DataFrame
export_data_df = filtered_data.loc[:, pd.IndexSlice[export_indicator, :]]
export_data_df = export_data_df.T.reset_index(names=['Indicator', 'Country Name'])

# The download button
st.download_button(
    label=f"Download {export_indicator} Data for All Countries",
    data=export_data_df.to_csv().encode('utf-8'),
    file_name=f"{export_indicator.replace(' (%)', '').replace(' ', '_')}_all_countries.csv",
    mime="text/csv",
)

## 2. Trade and External Sector
st.subheader("2. Trade and External Sector")

trade_df = country_data[['Exports (USD)', 'Imports (USD)']]
fig_trade = px.bar(
    trade_df,
    x=trade_df.index,
    y=['Exports (USD)', 'Imports (USD)'],
    title=f"Exports vs. Imports for {selected_country}",
    barmode='group',
    labels={"value": "Amount (in US Dollars)", "variable": "Trade Component"},
    template="plotly_white"
)
st.plotly_chart(fig_trade, use_container_width=True)

trade_balance_df = pd.DataFrame(country_data['Exports (USD)'] - country_data['Imports (USD)'], columns=['Trade Balance (USD)'])
fig_balance = px.line(
    trade_balance_df,
    x=trade_balance_df.index,
    y='Trade Balance (USD)',
    title=f"Trade Balance for {selected_country}",
    template="plotly_white"
)
st.plotly_chart(fig_balance, use_container_width=True)

## 3. Sectoral Analysis
st.subheader("3. Sectoral Contribution to GDP")
selected_year_sector = st.selectbox(
    "Select a Year to view Sectoral Contribution:",
    options=country_data.index.unique(),
    index=len(country_data.index) - 1
)

sector_data = country_data.loc[selected_year_sector, ['Agriculture (%)', 'Industry (%)', 'Services (%)']]
sectoral_contributions = pd.DataFrame(sector_data).reset_index()
sectoral_contributions.columns = ['Sector', 'Contribution (%)']

fig_pie = px.pie(
    sectoral_contributions,
    names='Sector',
    values='Contribution (%)',
    title=f"GDP Contribution by Sector in {selected_year_sector} for {selected_country}",
    template="plotly_white"
)
st.plotly_chart(fig_pie, use_container_width=True)

# --- About and Data Source ---
st.sidebar.markdown("---")

# New text explaining how missing values are handled
st.sidebar.info("Missing data points are handled by showing the last known value. This is done to provide a complete time-series visualization. ")

st.sidebar.info(
    "This dashboard uses data from **World Bank Open Data**."
    "\n\nUse the filters to explore economic trends for different countries."
)