# Homeprice_Prediction_ML_Model

# Predicting Home Prices

This repository contains a Python script for predicting home prices using linear regression. The script uses the pandas library to read in a CSV file containing home prices and areas, and the scikit-learn library to build a linear regression model.

## Requirements

To run the script, you will need to have the following libraries installed:

- pandas
- numpy
- scikit-learn

You can install these libraries using pip by running the following command:

```
pip install pandas numpy scikit-learn
```
  
## Usage

To use the script, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal window and navigate to the directory containing the script.
3. Run the script using the following command:

```
python predict_homeprice.py
```

This will train a linear regression model on the data in homeprices.csv, and use it to predict the price of a home with an area of 5000 square feet.

The trained model will be saved to a file called model_predict_homeprice using the joblib library. You can load the model using the following code:

```
import joblib
ml = joblib.load('model_predict_homeprice')
```

You can then use the loaded model to make predictions using the same code as in the script:

```
print(ml.predict([[5000]]))
```
