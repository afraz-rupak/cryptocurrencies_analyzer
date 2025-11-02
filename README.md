# Cryptocurrency Price Analyzer & Predictor

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

A comprehensive Streamlit web application for analyzing cryptocurrency prices and predicting next-day HIGH prices using advanced machine learning models. View real-time historical data with interactive candlestick charts and get AI-powered price predictions for Bitcoin, Ethereum, XRP, and Solana.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🚀 Features

- **📊 Real-Time Price Charts**: Interactive candlestick charts with 30-day historical OHLC (Open, High, Low, Close) data from Kraken API
- **🔮 AI Price Predictions**: Machine learning-powered predictions for next-day HIGH prices
- **💰 Multi-Cryptocurrency Support**: Bitcoin (BTC), Ethereum (ETH), XRP, and Solana (SOL)
- **📈 Price Metrics**: Current price, 24-hour change, 30-day high, and predicted returns
- **🎨 Professional UI**: Clean, intuitive interface with cryptocurrency logos and icons
- **⚡ Fast & Responsive**: Built with Streamlit for smooth, real-time updates

## 🖼️ Screenshots

The app features:
- Navigation sidebar with cryptocurrency icons
- Interactive candlestick price charts
- Current price metrics and statistics
- AI-powered prediction interface
- Detailed prediction results with model information

## 🛠️ Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/afraz-rupak/cryptocurrencies_analyzer.git
   cd cryptocurrencies_analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   The app will automatically open at `http://localhost:8501`

## 📦 Dependencies

- **streamlit** - Web application framework
- **requests** - HTTP library for API calls
- **pandas** - Data manipulation and analysis
- **plotly** - Interactive visualization library
- **python-dotenv** - Environment variable management

## 🎯 How to Use

1. **Select a Cryptocurrency**: Click on Bitcoin, Ethereum, XRP, or Solana in the sidebar navigation
2. **View Historical Data**: Explore the interactive candlestick chart showing 30 days of price history
3. **Check Current Metrics**: View current price, 24-hour change, and 30-day high
4. **Get Predictions**: Click the "Predict Next Day's Price" button to get AI-powered forecasts
5. **Analyze Results**: Review predicted HIGH price, expected change, and model information

## 🔌 API Integrations

### Price Data (Kraken API)
- **Endpoint**: `https://api.kraken.com/0/public/OHLC`
- **Purpose**: Fetches real-time OHLC data for all cryptocurrencies
- **Data**: 30-day historical prices with daily intervals

### Prediction APIs

#### Bitcoin
- **API**: `https://crypto-investing.onrender.com/`
- **Endpoint**: `/predict/bitcoin`
- **Model**: RandomForest (Return-Based)
- **Features**: 31 engineered features
- **Response**: Detailed prediction with current data and model information
- **Repository**: [Crypto_Investing](https://github.com/afraz-rupak/Crypto_Investing)

#### Ethereum
- **API**: `https://cryptocurrency-fastapi-11.onrender.com/`
- **Endpoint**: `/predict/ETH`
- **Response**: Simple format with predicted HIGH price and timestamp
- **Repository**: [cryptocurrency_fastAPI](https://github.com/disha193/cryptocurrency_fastAPI)

#### Solana
- **API**: `https://solana-forecast-api.onrender.com/`
- **Status**: Advanced API requiring feature engineering (Coming Soon)
- **Repository**: [solana-forecast-api](https://github.com/saifrahmania/solana-forecast-api)

#### XRP
- **Status**: API integration pending

## 📊 Technical Details

### Data Sources
- **Historical Prices**: Kraken Exchange API
- **Price Predictions**: Multiple machine learning models (RandomForest, ElasticNet)
- **Prediction Features**: Technical indicators (SMA, EMA, RSI, volatility, lagged values)

### Visualization
- **Chart Type**: Candlestick charts with Plotly
- **Colors**: Green for price increases, red for decreases
- **Interactivity**: Hover tooltips, zoom, pan capabilities

### Prediction Display
- **Bitcoin**: Shows predicted HIGH price, current close price, predicted return %, prediction date, model type, and features used
- **Ethereum**: Shows predicted HIGH price, timestamp, expected change from current price
- **Error Handling**: Graceful fallback messages for API unavailability

## 📁 Project Structure

```
├── app.py                 <- Main Streamlit application
├── icon/                  <- Cryptocurrency logo images
│   ├── bitcoin.png
│   ├── ethereum.png
│   ├── solana.png
│   └── xrp.png
├── requirements.txt       <- Python dependencies
├── LICENSE               <- MIT License
├── README.md             <- This file
├── Makefile              <- Convenience commands
├── pyproject.toml        <- Project configuration
└── cryptocurrencies_analyzer/  <- Source code package
    ├── __init__.py
    ├── config.py
    ├── dataset.py
    ├── features.py
    ├── modeling/
    └── plots.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

**AT3-group-18**

### API Contributors
- **Bitcoin API**: [Crypto_Investing](https://github.com/afraz-rupak/Crypto_Investing)
- **Ethereum API**: [cryptocurrency_fastAPI](https://github.com/disha193/cryptocurrency_fastAPI)
- **Solana API**: [solana-forecast-api](https://github.com/saifrahmania/solana-forecast-api)

## ⚠️ Disclaimer

**Important**: This tool is for educational and informational purposes only. Cryptocurrency investments carry significant risk. The predictions provided by this application should NOT be used as financial advice. Always do your own research (DYOR) and consult with financial professionals before making investment decisions.

## 🔮 Future Enhancements

- [ ] Add XRP prediction API integration
- [ ] Complete Solana prediction integration with feature engineering
- [ ] Add more technical indicators to charts (Bollinger Bands, MACD, Volume)
- [ ] Implement price alerts and notifications
- [ ] Add historical prediction accuracy tracking
- [ ] Support for more cryptocurrencies (Cardano, Polygon, etc.)
- [ ] Export prediction results to CSV/PDF
- [ ] Dark mode theme option
- [ ] Multi-day prediction forecasts

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review API documentation for endpoint details

## 🙏 Acknowledgments

- [Kraken Exchange](https://www.kraken.com/) for providing free public API access
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Plotly](https://plotly.com/) for interactive visualization capabilities
- [CryptoLogos](https://cryptologos.cc/) for cryptocurrency logos

---

**Made with ❤️ for the crypto community**

