import requests
import time

LOG_FILE = "/data/log.txt"

while True:
	try:
	    response = requests.get("http://producer:5000/data")
	    data = response.json()
	    print(f"Data recieved: {data}")
	    with open(LOG_FILE, "a") as file:
	         file.write(str(data) + "\n")
	    print("Data written:", data)
	except Exception as e:
	    print ("Error fetching data:" , e)
	time.sleep(5)
