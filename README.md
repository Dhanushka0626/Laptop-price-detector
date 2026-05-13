# Laptop Price Detector 💻

A machine learning-powered web application that predicts laptop prices based on hardware specifications and features. Built with Python and Streamlit, this project uses a trained ML model to estimate laptop prices in LKR (Sri Lankan Rupees).

## 🌐 Live Demo

Try the application here: [Laptop Price Detector App](https://laptop-price-detector-iudgptnsrniq9clkbrssfv.streamlit.app/)

## 📋 Features

- **Real-time Price Prediction**: Get instant price estimates based on laptop specifications
- **Comprehensive Input Options**:
  - RAM (1-128 GB)
  - Weight (0.5-10 Kg)
  - Touchscreen capability
  - IPS display support
  - Laptop brand (Acer, Apple, Asus, Dell, HP, Lenovo, MSI, Toshiba, Other)
  - Laptop type (2-in-1 Convertible, Gaming, Netbook, Notebook, Ultrabook, Workstation)
  - Operating System (Linux, Mac, Windows, Other)
  - Processor type (AMD, Intel Core i3/i5/i7, Other)
  - GPU type (AMD, Intel, NVIDIA)

## 🛠️ Technologies Used

- **Python** - Programming language
- **Streamlit** - Web framework for ML applications
- **scikit-learn** - Machine learning library
- **NumPy** - Numerical computing
- **Pickle** - Model serialization

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Dhanushka0626/Laptop-price-detector.git
cd Laptop-price-detector
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### How to Use
1. Enter or select the laptop specifications:
   - Adjust RAM and Weight using number inputs
   - Toggle Touchscreen and IPS options
   - Select Company, Type, OS, CPU, and GPU from dropdowns
2. Click the **"Predict Price"** button
3. View the estimated laptop price in LKR

## 📁 Project Structure

```
Laptop-price-detector/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── model/
│   └── predictor.pickle   # Pre-trained ML model
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── .gitignore           # Git ignore rules
└── .gitattributes       # Git attributes
```

## 💡 How It Works

1. **Feature Engineering**: The app converts categorical inputs (company, type, OS, CPU, GPU) into one-hot encoded features
2. **Model Prediction**: The trained scikit-learn model processes all features to generate predictions
3. **Price Conversion**: The raw prediction is scaled by 380 to convert to LKR
4. **User-Friendly Output**: Results are displayed with formatted currency notation

## 📊 Input Features

The model considers the following features:
- RAM (continuous)
- Weight (continuous)
- Touchscreen (binary)
- IPS Display (binary)
- Company (categorical - 9 options)
- Type (categorical - 6 options)
- Operating System (categorical - 4 options)
- CPU (categorical - 5 options)
- GPU (categorical - 3 options)

## 📝 Model Details

- **Algorithm**: Regression model trained using scikit-learn
- **Output**: Price prediction in normalized units (scaled to LKR by factor of 380)
- **Format**: Serialized using pickle for efficient loading

## ⚙️ Requirements

See `requirements.txt` for full list:
- streamlit
- numpy
- scikit-learn==1.7.2

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Dhanushka0626**
- GitHub: [@Dhanushka0626](https://github.com/Dhanushka0626)

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📧 Support

For issues or questions about the project, please open an issue on the [GitHub Issues](https://github.com/Dhanushka0626/Laptop-price-detector/issues) page.

---

**Note**: This project uses data from laptop specifications to predict prices in the Sri Lankan market. Predictions are estimates and may vary based on market conditions.
