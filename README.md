# csv_parser

This microservice parses a local CSV file and returns relevant data in CSV format based on the passed U.S. state abbreviation.

Uses HTTP for communication.

---------------------------------------------

Server:

Import Flask and requests from flask

Import pandas

Server URL: http://127.0.0.1:5001/filter/{state} (*state being the parameter passed in)

data = pandas.read_csv('ProjectDirectory/data.csv') (*Have the CSV file in the same directory as the project. Replace 'data' with filename)

---------------------------------------------

To Request:

Enter a state in abbreviated form into the server URL where is has 'state'

response = requests.get(URL)

---------------------------------------------

To Receive:

Print or save the response

print(response.text)

![UML Diagram](https://github.com/user-attachments/assets/a507806f-c945-4647-a45a-82802917e4b1)
