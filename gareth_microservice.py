from flask import Flask, request
import pandas

app = Flask(__name__)

# Load data from a local CSV file
data = pandas.read_csv('/Users/henry/Documents/Henry’s_Mac_Pro/CS 361/A7/median_home_prices.csv')

# List of valid US state abbreviations
valid_states = {
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
}

@app.route('/filter/<state>', methods=['GET'])
def filter_data(state):
    # Uppercase state to allow input flexibility
    state = state.upper()

    # Verify that the state is a valid US state abbreviation
    if state not in valid_states:
        return

    # Filter data by state
    filtered_df = data[data['State'] == state]

    # Convert filtered data to CSV format
    csv_data = filtered_df.to_csv(index=False)

    return csv_data

if __name__ == '__main__':
    # URL = http://127.0.0.1:5001/filter/{state}
    app.run(debug=True, port=5001)
