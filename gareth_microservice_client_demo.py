import requests


def get_filtered_data(state):
    # Server URL
    url = f'http://127.0.0.1:5001/filter/{state}'
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: Invalid state abbreviation")

if __name__ == '__main__':
    # Example call
    state = input("Enter the state abbreviation (e.g., CA, NY): ")
    get_filtered_data(state)
