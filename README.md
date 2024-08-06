# csv_parser

This microservice parses a local CSV file and returns relevant data in CSV format based on the passed U.S. state abbreviation.

Uses HTTP for communication.


Import Flask and requests from flask
Import pandas

Server URL: http://127.0.0.1:5001/filter/{state} (state being the parameter passed in)

To Request:
Enter a state in abbreviated form into the server URL where is has 'state'

response = requests.get(URL)

To Receive:
Print or save the response
print(response.text)
