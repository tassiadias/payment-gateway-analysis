from flask import Flask, render_template, request
import pandas as pd
import time

app = Flask(__name__)

# Function to load dataset based on the selected file name
def load_dataset(file_name):
    try:
        file_path = f"./{file_name}.csv"
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        return None

datasets = {
    1: "yearly_dataset_sample",
    2: "multiple_currencies_dataset_sample",
    3: "high_value_transactions_sample",
    4: "fraud_detection_sample",
    5: "emerging_markets_sample"
}

# Mock API to generate insights
def mock_api_call() -> dict:
    time.sleep(2)  # Simulate API delay
    return {
        "emerging_market": "Increase in digital transactions from Southeast Asia",
        "pricing_strategy": "Consider a tiered pricing model for high-frequency customers",
        "market_expansion": "Enter the Latin American market, focusing on digital wallets",
        "fraud_detection": "5% of transactions show unusual patterns, likely related to bot activity"
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    preview = None
    insights = None
    selected_dataset = None

    if request.method == 'POST':
        # Get the selected dataset from the form
        selected_dataset = int(request.form['dataset'])
        df = load_dataset(datasets[selected_dataset])

        # Check if user clicked "Preview" or "Analyze"
        if 'analyze' in request.form:
            # Call the mock API to get insights
            insights = mock_api_call()

        # Preview the dataset
        if df is not None:
            preview = df.head().to_html()
        else:
            preview = "Error loading dataset."

    return render_template('index.html', datasets=datasets, preview=preview, insights=insights, selected_dataset=selected_dataset)

if __name__ == "__main__":
    app.run(debug=True)
