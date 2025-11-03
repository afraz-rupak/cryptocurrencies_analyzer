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
- **🔄 Automatic Data Fetching**: All prediction APIs automatically fetch latest market data
- **📊 Multiple Display Formats**: Each cryptocurrency shows predictions in its optimal format

## 🖼️ App Interface

The app features:
- **Sidebar Navigation**: Cryptocurrency icons with buttons for easy switching
- **Interactive Candlestick Charts**: 30-day price history with zoom and pan capabilities
- **Current Price Dashboard**: Real-time metrics (current price, 24h change, 30-day high)
- **AI Prediction Panel**: One-click prediction interface with detailed results
- **Multiple Data Views**: Tailored display for each cryptocurrency's API format

## 🛠️ Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager
- Internet connection for API calls

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

- **streamlit** - Web application framework for creating interactive dashboards
- **requests** - HTTP library for API calls to prediction and market data services
- **pandas** - Data manipulation and analysis for OHLC data processing
- **plotly** - Interactive visualization library for candlestick charts
- **python-dotenv** - Environment variable management for configuration

Install all dependencies with:
```bash
pip install streamlit requests pandas plotly python-dotenv
```

## 🎯 How to Use

1. **Select a Cryptocurrency**: Click on Bitcoin, Ethereum, XRP, or Solana in the sidebar navigation
2. **View Historical Data**: Explore the interactive candlestick chart showing 30 days of price history
   - Hover over candles to see exact OHLC values
   - Zoom in/out using the chart controls
   - Pan across different date ranges
3. **Check Current Metrics**: View current price, 24-hour change percentage, and 30-day high
4. **Get AI Predictions**: Click the "Predict Next Day's Price" button to get forecasts
5. **Analyze Results**: Review predicted HIGH price, expected change, model information, and log returns

## 🔌 API Integrations

### Market Data - Kraken Exchange API
- **Base URL**: `https://api.kraken.com/0/public/`
- **Endpoint**: `/OHLC?pair={PAIR}&interval=1440`
- **Purpose**: Fetches real-time OHLC (Open, High, Low, Close) data for all cryptocurrencies
- **Data**: 30-day historical prices with daily intervals (1440 minutes)
- **Supported Pairs**: XBTUSD (Bitcoin), ETHUSD (Ethereum), XRPUSD (XRP), SOLUSD (Solana)
- **Documentation**: [Kraken API Docs](https://docs.kraken.com/api/docs/rest-api/get-ohlc-data/)

### Prediction APIs

#### 🟠 Bitcoin (BTC)
- **API URL**: `https://crypto-investing.onrender.com/`
- **Prediction Endpoint**: `https://crypto-investing.onrender.com/predict/bitcoin`
- **Method**: GET
- **Model**: RandomForest (Return-Based)
- **Features**: 31 engineered features including:
  - Lagged high prices (1, 2, 3, 5, 7 days)
  - Lagged close prices (1, 2, 3, 5, 7 days)
  - Lagged returns (1, 2, 3, 5, 7 days)
  - Simple Moving Averages (SMA 7, 14, 30)
  - Exponential Moving Averages (EMA 7, 14, 30)
  - Standard deviations (7, 14, 30 days)
  - RSI (14-period)
  - Price-to-SMA ratios
  - Volatility measures
  - Date features (day of week, month)
- **Response Format**: Detailed prediction with current data and model information
- **Metrics**: Test R² = 0.815, RMSE = 1785.70
- **Data Source**: Yahoo Finance (BTC-USD)
- **GitHub Repository**: [Crypto_Investing](https://github.com/afraz-rupak/Crypto_Investing)

#### 🔵 Ethereum (ETH)
- **API URL**: `https://cryptocurrency-fastapi-11.onrender.com/`
- **Prediction Endpoint**: `https://cryptocurrency-fastapi-11.onrender.com/predict/ETH`
- **Method**: GET
- **Health Check**: `https://cryptocurrency-fastapi-11.onrender.com/health/`
- **Response Format**: Simple format with predicted HIGH price and timestamp
- **Output**: Predicted high price for tomorrow (formatted as currency string)
- **GitHub Repository**: [cryptocurrency_fastAPI](https://github.com/disha193/cryptocurrency_fastAPI)

#### 🔷 XRP (Ripple)
- **API URL**: `https://ripple-predict-api.onrender.com/`
- **Prediction Endpoint**: `https://ripple-predict-api.onrender.com/predict/XRP`
- **Method**: GET
- **Health Check**: `https://ripple-predict-api.onrender.com/health`
- **Response Format**: Detailed format with log returns and dual predictions (today + tomorrow)
- **Features**:
  - Last known price with timestamp
  - Predicted HIGH for today and tomorrow
  - Log-relative returns for today and tomorrow
  - Date information (today, tomorrow)
- **Output**: Price predictions with percentage change calculations
- **GitHub Repository**: [Ripple-Predict-API](https://github.com/benedict-brunker/Ripple-Predict-API)

#### 🟣 Solana (SOL)
- **API URL**: `https://solana-forecast-api-1.onrender.com/`
- **Prediction Endpoint**: `https://solana-forecast-api-1.onrender.com/predict/simple`
- **Method**: GET
- **Health Check**: `https://solana-forecast-api-1.onrender.com/health`
- **Models Available**: 5 models (random_forest, gradient_boosting, xgboost, lightgbm, best)
- **Best Model**: Gradient Boosting (RMSE: 5.61, R²: 0.96)
- **Features**: 49 automatically calculated features including:
  - OHLC data and derived metrics
  - Lagged values (1, 2, 3, 7 days)
  - Moving averages (7, 14, 30-day periods)
  - Standard deviations
  - Technical indicators (RSI, momentum)
  - Date features
- **Response Format**: Similar to XRP with log returns and dual predictions
- **Note**: Uses `/predict/simple` endpoint for automatic feature calculation
- **GitHub Repository**: [solana-forecast-api](https://github.com/saifrahmania/solana-forecast-api)

## 📊 Technical Details

### Data Processing
- **Historical Prices**: Fetched from Kraken Exchange API with 1-day intervals
- **Price Predictions**: Multiple machine learning models (RandomForest, Gradient Boosting, XGBoost, LightGBM, ElasticNet)
- **Feature Engineering**: Automated calculation of technical indicators and lagged values
- **Prediction Target**: Next-day HIGH price (most relevant for traders)

### Visualization
- **Chart Type**: Interactive candlestick charts powered by Plotly
- **Color Scheme**: 
  - Green (`#26a69a`) for price increases (bullish candles)
  - Red (`#ef5350`) for price decreases (bearish candles)
- **Interactivity**: 
  - Hover tooltips showing OHLC values
  - Zoom and pan controls
  - Responsive design for all screen sizes

### Prediction Display Formats

#### Bitcoin Format (Detailed)
- Predicted HIGH price with delta from close
- Current close price
- Predicted return percentage
- Prediction date and current date
- Current HIGH price
- Model type, features used, and data source

#### Ethereum Format (Simple)
- Predicted HIGH price for tomorrow
- Timestamp of prediction
- Token identifier
- Expected change from current price (calculated)
- Percentage change

#### XRP & Solana Format (Rich)
- Predicted HIGH price for tomorrow
- Last known price
- Predicted HIGH for today (comparison)
- Prediction timeline (dates and timestamps)
- Log returns (today and tomorrow)
- Expected percentage change

### Error Handling
- **Timeout Management**: 60-second timeout for sleeping APIs (Render free tier)
- **Connection Errors**: Clear error messages with retry suggestions
- **API Unavailability**: Graceful fallback with user-friendly messages
- **Data Validation**: Handles multiple API response formats automatically

## 📁 Project Structure

```
cryptocurrencies_analyzer/
├── app.py                      <- Main Streamlit application (400+ lines)
├── icon/                       <- Cryptocurrency logo images (PNG format)
│   ├── bitcoin.png            <- Bitcoin logo
│   ├── ethereum.png           <- Ethereum logo
│   ├── solana.png             <- Solana logo
│   └── xrp.png                <- XRP/Ripple logo
├── requirements.txt            <- Python dependencies
├── LICENSE                     <- MIT License
├── README.md                   <- This comprehensive documentation
├── Makefile                    <- Convenience commands (format, lint, etc.)
├── pyproject.toml             <- Project configuration and metadata
├── setup.cfg                  <- Configuration for flake8
├── data/                      <- Data directory (gitignored)
│   ├── external/              <- Third-party data sources
│   ├── interim/               <- Intermediate transformed data
│   ├── processed/             <- Final canonical datasets
│   └── raw/                   <- Original immutable data
├── docs/                      <- Documentation (MkDocs)
├── models/                    <- Trained models, predictions, summaries
├── notebooks/                 <- Jupyter notebooks for analysis
├── references/                <- Data dictionaries and manuals
├── reports/                   <- Generated analysis (HTML, PDF, LaTeX)
│   └── figures/               <- Graphics and figures for reports
└── cryptocurrencies_analyzer/ <- Source code package
    ├── __init__.py            <- Makes it a Python module
    ├── config.py              <- Configuration variables
    ├── dataset.py             <- Data download/generation scripts
    ├── features.py            <- Feature engineering code
    ├── modeling/              <- Model training and inference
    │   ├── __init__.py
    │   ├── predict.py         <- Model inference code
    │   └── train.py           <- Model training code
    └── plots.py               <- Visualization code
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the project** on GitHub
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Make your changes** with clear, descriptive commits
4. **Write or update tests** if applicable
5. **Update documentation** (README, docstrings, comments)
6. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
7. **Push to the branch** (`git push origin feature/AmazingFeature`)
8. **Open a Pull Request** with a clear description of your changes

### Development Guidelines
- Follow PEP 8 style guidelines for Python code
- Use type hints where appropriate
- Add docstrings to functions and classes
- Test your changes locally before submitting
- Keep commits atomic and well-documented

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for full details.

**MIT License Summary:**
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ⚠️ No warranty provided
- ⚠️ No liability accepted

Copyright (c) 2025, AT3-group-18

## 👥 Team & Contributors

**Project Team:** AT3-group-18

### API Development Contributors
- **Bitcoin API**: [afraz-rupak](https://github.com/afraz-rupak) - [Crypto_Investing](https://github.com/afraz-rupak/Crypto_Investing)
- **Ethereum API**: [disha193](https://github.com/disha193) - [cryptocurrency_fastAPI](https://github.com/disha193/cryptocurrency_fastAPI)
- **XRP API**: [benedict-brunker](https://github.com/benedict-brunker) - [Ripple-Predict-API](https://github.com/benedict-brunker/Ripple-Predict-API)
- **Solana API**: [saifrahmania](https://github.com/saifrahmania) - [solana-forecast-api](https://github.com/saifrahmania/solana-forecast-api)

## ⚠️ Important Disclaimer

**PLEASE READ CAREFULLY:**

This tool is for **educational and informational purposes only**. The predictions provided by this application are generated by machine learning models and should **NOT** be used as financial advice or as the sole basis for making investment decisions.

**Key Points:**
- 📉 **Cryptocurrency investments carry significant risk** - you can lose all invested capital
- 🤖 **ML predictions are not guarantees** - past performance doesn't predict future results
- 💡 **Always DYOR** (Do Your Own Research) before investing
- 👨‍💼 **Consult financial professionals** for investment advice
- ⚖️ **No liability** - developers and contributors are not responsible for financial losses
- 🔮 **Predictions can be wrong** - use them as one data point among many
- 📊 **Market volatility** - crypto markets are highly volatile and unpredictable

**By using this application, you acknowledge that:**
1. You understand the risks of cryptocurrency trading
2. You will not rely solely on these predictions for investment decisions
3. You accept full responsibility for your investment choices
4. The developers provide no warranty or guarantee of accuracy

## 🔮 Future Enhancements

### Planned Features
- [ ] 📊 Add more technical indicators to charts (Bollinger Bands, MACD, Volume overlays)
- [ ] 🔔 Implement price alerts and email/SMS notifications
- [ ] 📈 Add historical prediction accuracy tracking and performance metrics
- [ ] 🪙 Support for more cryptocurrencies (Cardano, Polygon, BNB, etc.)
- [ ] 📥 Export prediction results to CSV/PDF/Excel formats
- [ ] 🌙 Dark mode theme option with toggle
- [ ] 📅 Multi-day prediction forecasts (3-day, 7-day, 30-day)
- [ ] 📱 Mobile-responsive improvements
- [ ] 🔄 Real-time WebSocket price updates
- [ ] 📊 Portfolio tracking and analysis features
- [ ] 🤖 Model comparison views (side-by-side predictions)
- [ ] 📈 Sentiment analysis integration (Twitter, Reddit)
- [ ] 💹 Trading simulation / paper trading mode

### Technical Improvements
- [ ] Add caching for API responses
- [ ] Implement rate limiting for API calls
- [ ] Add unit tests and integration tests
- [ ] Set up CI/CD pipeline
- [ ] Dockerize the application
- [ ] Add database for storing historical predictions
- [ ] Implement user authentication and personalization
- [ ] Add API key management for users

## 📞 Support & Contact

### Getting Help
- **GitHub Issues**: [Open an issue](https://github.com/afraz-rupak/cryptocurrencies_analyzer/issues) for bugs or feature requests
- **Documentation**: Check the README and code comments
- **API Documentation**: Review individual API repositories for endpoint details

### Reporting Issues
When reporting bugs, please include:
1. Description of the issue
2. Steps to reproduce
3. Expected vs actual behavior
4. Screenshots (if applicable)
5. Browser and OS information
6. Error messages or console logs

### Feature Requests
We welcome feature suggestions! Please:
1. Check existing issues first
2. Provide clear use case description
3. Explain expected benefits
4. Include mockups/wireframes if applicable

## 🙏 Acknowledgments

### Technologies
- [Streamlit](https://streamlit.io/) - Amazing framework for building data apps
- [Plotly](https://plotly.com/) - Powerful interactive visualization library
- [Pandas](https://pandas.pydata.org/) - Essential data manipulation tool
- [Kraken Exchange](https://www.kraken.com/) - Free public API for market data
- [FastAPI](https://fastapi.tiangolo.com/) - Used by prediction API services

### Data & Icons
- [CryptoLogos](https://cryptologos.cc/) - High-quality cryptocurrency logos
- [Kraken API](https://docs.kraken.com/api/) - Reliable OHLC market data
- [Yahoo Finance](https://finance.yahoo.com/) - Historical price data (via APIs)

### Inspiration & Resources
- [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) - Project structure template
- Cryptocurrency trading communities for feedback and testing
- Open-source contributors who provided API services

---

## 🚀 Quick Start Commands

```bash
# Clone and setup
git clone https://github.com/afraz-rupak/cryptocurrencies_analyzer.git
cd cryptocurrencies_analyzer
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Development commands
make format          # Format code with ruff
make lint           # Lint code with ruff
make clean          # Remove compiled Python files

# API health checks (optional)
curl https://crypto-investing.onrender.com/health/
curl https://cryptocurrency-fastapi-11.onrender.com/health/
curl https://ripple-predict-api.onrender.com/health
curl https://solana-forecast-api-1.onrender.com/health
```

---

**Made with ❤️ by AT3-group-18 for the crypto community**

**⭐ If you find this project useful, please consider giving it a star on GitHub!**

---

*Last Updated: November 3, 2025*
*Version: 1.0.0*

