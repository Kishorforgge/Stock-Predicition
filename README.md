# StockVision App - Stocks Predictor Using Keras

StockVision App is a machine learning-based project that leverages deep learning techniques in **Keras** to predict stock prices. It utilizes historical stock market data to make predictions and provide insights for better investment decisions. This project is designed to assist both beginners and experienced investors in understanding market trends and forecasting potential stock movements.

Additionally, the project has been deployed as a web application using **Streamlit**. You can access the deployed app [here](https://stock-vision-keras.streamlit.app/).

---

## Features
- **Data Preprocessing:** Handles missing values, normalization, and data transformation for model readiness.
- **Deep Learning Models:** Implements LSTM (Long Short-Term Memory) networks for time-series forecasting.
- **Visualization:** Provides insightful visualizations of stock trends and prediction results.
- **Customizable:** Allows users to adjust parameters like time steps, epochs, and batch size.
- **User-Friendly Interface:** Includes a simple script-based interface to run predictions.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kishorforgge/Stock-Predicition.git
   cd Stock-Predicition
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Prepare your data:
   - Obtain historical stock data (e.g., from Yahoo Finance).
   - Save the data as a CSV file and place it in the `data/` folder.

2. Run the training script:
   ```bash
   python train_model.py
   ```
   Adjust parameters like the number of epochs or batch size in the `config.py` file.

3. Predict future stock prices:
   ```bash
   python predict.py
   ```
   Results will be saved in the `output/` folder.

4. Visualize results:
   - Check the `output/` folder for graphs showing the comparison between actual and predicted prices.

---

## Project Structure

```
Stock-Predicition/
├── data/
│   └── stock_data.csv    # Sample stock data file
├── models/
│   └── lstm_model.h5     # Trained LSTM model
├── output/
│   └── predictions.csv  # Prediction results
├── utils/
│   └── preprocess.py    # Data preprocessing functions
├── train_model.py          # Training script
├── predict.py              # Prediction script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Requirements

- Python 3.8+
- Keras
- TensorFlow
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

To install dependencies, use:
```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## Acknowledgments

- Thanks to [Yahoo Finance](https://finance.yahoo.com/) for providing historical stock data.
- Inspired by various stock market prediction projects and tutorials.

---

## Contact

For questions or feedback, reach out to:
- **Email:** kishorforgge@gmail.com
- **GitHub:** [Kishorforgge](https://github.com/Kishorforgge)

---

Happy Predicting!

