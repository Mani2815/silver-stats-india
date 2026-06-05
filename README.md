# Silver Price Calculator & Silver Sales Analysis Dashboard

This is a Streamlit-based web application that provides a comprehensive interface for calculating silver costs and analyzing silver market data in India.

## Live Demo
Check out the live application here: [Live Demo](https://mani2815-2547261-cia1-cia1-h5togh.streamlit.app/)

## Features

The application is divided into two main tabs:

### 1. Silver Price Calculator
- **Cost Calculation**: Allows users to calculate the total cost of silver by inputting the weight (in Grams or Kilograms), the current price per gram, and selecting the desired currency (INR or USD).
- **Historical Price Trends**: Displays an interactive line chart (powered by Altair) showing historical silver prices.
- **Filtering**: Users can filter the historical price data by predefined price ranges (e.g., ≤ ₹20,000, ₹20,000 - ₹30,000, ≥ ₹30,000) to analyze specific market conditions.

### 2. Silver Sales Dashboard
- **Geospatial Analysis**: Features a choropleth map of India (using GeoPandas and Matplotlib) that visualizes state-wise silver purchases, making it easy to identify regions with the highest demand.
- **Top Performers**: Includes a bar chart highlighting the top 5 states with the highest silver purchases.
- **Raw Data Access**: Provides a detailed data table of silver purchases across all states for deeper inspection.

## Project Structure

- `cia1.py`: The main Streamlit application code.
- `historical_silver_price.csv`: Dataset containing historical silver prices over time.
- `state_wise_silver_purchased_kg.csv`: Dataset containing the volume of silver purchased (in kg) across different Indian states.
- `india_state_geo.json`: GeoJSON file used to render the geographical map of India.
- `requirements.txt`: List of Python dependencies required to run the application.

## Installation & Usage

To run this application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mani2815/silver-stats-india.git
   cd silver-stats-india
   ```

2. **Install the required dependencies:**
   Make sure you have Python installed. Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application:**
   ```bash
   streamlit run main.py
   ```

4. **Access the app:**
   Open your web browser and navigate to `http://localhost:8501` (or the URL provided in your terminal).

## Technologies Used
- **[Streamlit](https://streamlit.io/)**: For building the interactive web interface.
- **[Pandas](https://pandas.pydata.org/)**: For data manipulation and analysis.
- **[Altair](https://altair-viz.github.io/)**: For creating interactive charts.
- **[GeoPandas](https://geopandas.org/)**: For spatial operations and processing GeoJSON data.
- **[Matplotlib](https://matplotlib.org/)**: For plotting the choropleth map.
