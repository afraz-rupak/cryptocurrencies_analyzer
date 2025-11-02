import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Crypto Investing Analyzer",
    page_icon="💰",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# API Base URLs for different cryptocurrencies
API_ENDPOINTS = {
    'Bitcoin': 'https://crypto-investing.onrender.com/predict/bitcoin',
    'Ethereum': 'https://cryptocurrency-fastapi-11.onrender.com/predict/ETH',
    'XRP': None,  # To be added
    'Solana': None  # To be added
}

# Cryptocurrency logo local paths
CRYPTO_LOGOS = {
    'Bitcoin': 'icon/bitcoin.png',
    'Ethereum': 'icon/ethereum.png',
    'XRP': 'icon/xrp.png',
    'Solana': 'icon/solana.png'
}

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Bitcoin'


def fetch_historical_data(crypto_name):
    """Fetch historical price data for a cryptocurrency from Kraken API"""
    try:
        # Map cryptocurrency names to Kraken trading pairs
        pair_mapping = {
            'Bitcoin': 'XBTUSD',
            'Ethereum': 'ETHUSD',
            'XRP': 'XRPUSD',
            'Solana': 'SOLUSD'
        }
        
        pair = pair_mapping.get(crypto_name, 'XBTUSD')
        
        # Fetch OHLC data from Kraken API
        # interval=1440 means daily candles (1440 minutes = 24 hours)
        kraken_url = f"https://api.kraken.com/0/public/OHLC?pair={pair}&interval=1440"
        response = requests.get(kraken_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('error') and len(data['error']) > 0:
                raise Exception(f"Kraken API error: {data['error']}")
            
            # Extract the OHLC data
            result = data.get('result', {})
            # Get the first key (which is the pair name, might be slightly different)
            pair_key = [k for k in result.keys() if k != 'last'][0]
            ohlc_data = result[pair_key]
            
            # Convert to DataFrame
            # OHLC format: [time, open, high, low, close, vwap, volume, count]
            df = pd.DataFrame(ohlc_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'vwap', 'volume', 'count'])
            
            # Convert timestamp to datetime
            df['Date'] = pd.to_datetime(df['timestamp'], unit='s')
            
            # Convert price columns to float
            df['Price'] = df['close'].astype(float)
            df['High'] = df['high'].astype(float)
            df['Low'] = df['low'].astype(float)
            df['Open'] = df['open'].astype(float)
            
            # Get last 30 days of data
            df = df.tail(30)
            
            return df[['Date', 'Price', 'High', 'Low', 'Open']]
        else:
            raise Exception(f"Failed to fetch data from Kraken API: {response.status_code}")
    
    except Exception as e:
        st.error(f"Error fetching historical data: {str(e)}")
        # Return empty DataFrame on error
        return pd.DataFrame(columns=['Date', 'Price', 'High', 'Low', 'Open'])


def predict_next_day_price(crypto_name):
    """Call the API to predict next day's price"""
    try:
        # Adjust the endpoint based on your API structure
        response = requests.get(API_ENDPOINTS[crypto_name], timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": f"API returned status code {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def create_price_chart(df, crypto_name):
    """Create an interactive candlestick chart using Plotly"""
    fig = go.Figure()
    
    # Add candlestick chart
    fig.add_trace(go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Price'],
        name='OHLC',
        increasing_line_color='#26a69a',
        decreasing_line_color='#ef5350'
    ))
    
    fig.update_layout(
        title=f'{crypto_name} Price History (Last 30 Days)',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        hovermode='x unified',
        template='plotly_white',
        height=500,
        xaxis_rangeslider_visible=False
    )
    
    return fig


def show_crypto_page(crypto_name):
    """Display cryptocurrency page with chart and prediction button"""
    # Display cryptocurrency logo and title in parallel
    col1, col2 = st.columns([1, 10])
    with col1:
        st.image(CRYPTO_LOGOS[crypto_name], width=60)
    with col2:
        st.title(f"{crypto_name} Analysis")
    
    # Fetch and display historical data
    st.subheader("Price History")
    with st.spinner('Loading price data...'):
        df = fetch_historical_data(crypto_name)
        
        # Display the chart
        fig = create_price_chart(df, crypto_name)
        st.plotly_chart(fig, use_container_width=True)
    
    # Display current price info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Price", f"${df['Price'].iloc[-1]:,.2f}")
    with col2:
        price_change = df['Price'].iloc[-1] - df['Price'].iloc[-2]
        price_change_pct = (price_change / df['Price'].iloc[-2]) * 100
        st.metric("24h Change", f"${price_change:,.2f}", f"{price_change_pct:.2f}%")
    with col3:
        st.metric("30-Day High", f"${df['Price'].max():,.2f}")
    
    # Prediction section
    st.subheader("Price Prediction")
    st.write("Click the button below to predict the next day's HIGH price using our AI model.")
    
    if st.button(f"Predict Next Day's Price for {crypto_name}", key=f"predict_{crypto_name}"):
        # Check if API endpoint is available
        if API_ENDPOINTS[crypto_name] is None:
            st.warning(f"Prediction API for {crypto_name} is not yet available. Coming soon!")
            return
        
        with st.spinner('Fetching prediction...'):
            result = predict_next_day_price(crypto_name)
            
            if 'error' in result:
                st.error(f"Error: {result['error']}")
                st.info("The API might be warming up or the endpoint needs to be configured. Please try again in a moment.")
            else:
                st.success("Prediction retrieved successfully!")
                
                # Display prediction results in a nice layout
                st.markdown("### Prediction Results")
                
                # Handle different API response formats
                # Bitcoin API format: detailed with prediction.predicted_high_price
                # Ethereum API format: simple with predicted_high_tomorrow
                
                if 'prediction' in result:
                    # Bitcoin API format (detailed)
                    prediction_data = result.get('prediction', {})
                    current_data = result.get('current_data', {})
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        predicted_high = prediction_data.get('predicted_high_price')
                        if predicted_high:
                            st.metric(
                                "Predicted HIGH Price",
                                f"${predicted_high:,.2f}",
                                delta=prediction_data.get('predicted_change_from_close', 'N/A')
                            )
                    
                    with col2:
                        current_close = current_data.get('current_close_price')
                        if current_close:
                            st.metric("Current Close Price", f"${current_close:,.2f}")
                    
                    with col3:
                        predicted_return = prediction_data.get('predicted_return_pct')
                        if predicted_return:
                            st.metric("Predicted Return", f"{predicted_return:.4f}%")
                    
                    # Additional information
                    st.markdown("---")
                    col4, col5 = st.columns(2)
                    
                    with col4:
                        st.markdown("**Prediction Details**")
                        if 'prediction_date' in prediction_data:
                            st.write(f"**Prediction Date:** {prediction_data['prediction_date']}")
                        if 'current_date' in current_data:
                            st.write(f"**Current Date:** {current_data['current_date']}")
                        current_high = current_data.get('current_high_price')
                        if current_high:
                            st.write(f"**Current HIGH:** ${current_high:,.2f}")
                    
                    with col5:
                        st.markdown("**Model Information**")
                        model_info = result.get('model_info', {})
                        if model_info:
                            st.write(f"**Model:** {model_info.get('model_type', 'N/A')}")
                            st.write(f"**Features Used:** {model_info.get('features_used', 'N/A')}")
                            st.write(f"**Data Source:** {model_info.get('data_source', 'N/A')}")
                
                elif 'predicted_high_tomorrow' in result:
                    # Ethereum API format (simple)
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        predicted_price_str = result.get('predicted_high_tomorrow', '')
                        # Remove $ sign and convert to float
                        predicted_price = float(predicted_price_str.replace('$', '').replace(',', ''))
                        st.metric(
                            "Predicted HIGH Price (Tomorrow)",
                            f"${predicted_price:,.2f}"
                        )
                    
                    with col2:
                        if 'timestamp' in result:
                            st.write(f"**Timestamp:** {result['timestamp']}")
                        st.write(f"**Token:** {result.get('token', crypto_name)}")
                    
                    # Calculate potential change from current price
                    if len(df) > 0:
                        current_price = df['Price'].iloc[-1]
                        price_diff = predicted_price - current_price
                        price_diff_pct = (price_diff / current_price) * 100
                        
                        st.markdown("---")
                        col3, col4 = st.columns(2)
                        with col3:
                            st.metric("Current Price", f"${current_price:,.2f}")
                        with col4:
                            st.metric("Expected Change", f"${price_diff:,.2f}", f"{price_diff_pct:.2f}%")
                
                else:
                    # Unknown format - display raw JSON
                    st.json(result)


def show_about_page():
    """Display About page"""
    st.title("About Crypto Investing Analyzer")
    
    st.markdown("""
    ## Welcome to Crypto Investing Analyzer!
    
    This application helps you analyze and predict cryptocurrency prices using advanced AI models.
    
    ### Features:
    - **Historical Price Charts**: View 30-day price history for major cryptocurrencies
    - **AI-Powered Predictions**: Get next-day HIGH price predictions
    - **Real-time Data**: Access up-to-date market information
    
    ### Supported Cryptocurrencies:
    - **Bitcoin (BTC)**: The first and most valuable cryptocurrency
    - **Ethereum (ETH)**: Leading smart contract platform
    - **XRP**: Fast and efficient digital payment network
    - **Solana (SOL)**: High-performance blockchain platform
    
    ### How to Use:
    1. Select a cryptocurrency from the navigation menu
    2. View the historical price chart
    3. Click the prediction button to get next-day price forecast
    
    ### API Information:
    - **API Endpoint**: `https://crypto-investing.onrender.com/`
    - **Predictions**: Based on machine learning models trained on historical data
    
    ### Project Information:
    - **GitHub**: [afraz-rupak/Crypto_Investing](https://github.com/afraz-rupak/Crypto_Investing)
    - **License**: MIT License
    
    ---
    
    **Disclaimer**: This tool is for educational purposes only. Cryptocurrency investments carry risk. 
    Always do your own research before making investment decisions.
    """)


# Main App
def main():
    # Navigation bar
    st.sidebar.title("Navigation")
    st.sidebar.markdown("---")
    
    # Navigation buttons with icons
    col1, col2 = st.sidebar.columns([1, 4])
    with col1:
        st.image(CRYPTO_LOGOS['Bitcoin'], width=30)
    with col2:
        if st.button("Bitcoin", use_container_width=True, key="btn_bitcoin"):
            st.session_state.page = 'Bitcoin'
    
    col1, col2 = st.sidebar.columns([1, 4])
    with col1:
        st.image(CRYPTO_LOGOS['Ethereum'], width=30)
    with col2:
        if st.button("Ethereum", use_container_width=True, key="btn_ethereum"):
            st.session_state.page = 'Ethereum'
    
    col1, col2 = st.sidebar.columns([1, 4])
    with col1:
        st.image(CRYPTO_LOGOS['XRP'], width=30)
    with col2:
        if st.button("XRP", use_container_width=True, key="btn_xrp"):
            st.session_state.page = 'XRP'
    
    col1, col2 = st.sidebar.columns([1, 4])
    with col1:
        st.image(CRYPTO_LOGOS['Solana'], width=30)
    with col2:
        if st.button("Solana", use_container_width=True, key="btn_solana"):
            st.session_state.page = 'Solana'
    
    st.sidebar.markdown("---")
    
    if st.sidebar.button("About", use_container_width=True):
        st.session_state.page = 'About'
    
    # Display selected page
    if st.session_state.page == 'About':
        show_about_page()
    else:
        show_crypto_page(st.session_state.page)


if __name__ == "__main__":
    main()
