import time
import requests
import csv
from datetime import datetime


def write_file(t, qtt):
	print("Writing CSV file...")
	with open('output.csv', mode='a') as csvFile:
		writer = csv.writer(csvFile,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow([t,qtt[0],qtt[1],qtt[2]])

	csvFile.close()



def reboot_service():
	print("Rebooting service...")
	try:
		r = requests.put('https://desafioperformance.b2w.io/')
		print("Reboot status code: ")
		print(r.status_code)
	except requests.ConnectionError as e:
		print("Reboot Connection Error")



def add_status_code(status_code, qtt):
	# Status code lists 
	list_codes_2xx = [200,201,203,204,205,206,207,208,226]
	list_codes_4xx = [400,401,402,403,404,405,406,407,408,
				      409,410,411,412,413,414,415,416,417,
				      418,421,422,423,424,426,428,429,431,
				      451]
	list_codes_5xx = [500,501,502, 503,504,505,506,507,508,
	                  510,511] 

	found = False
	
	i = 0
	while( (not found) and i < len(list_codes_2xx)):
		if status_code == list_codes_2xx[i]:
			found = True
			qtt[0] = qtt[0] + 1
		i = i + 1


	i = 0
	while( (not found) and i < len(list_codes_4xx)):
		if status_code == list_codes_4xx[i]:
			found = True
			qtt[1] = qtt[1] + 1 
		i = i + 1


	i = 0
	while( (not found) and i < len(list_codes_5xx)):
		if status_code == list_codes_5xx[i]:
			found = True
			qtt[2] = qtt[2] + 1
		i = i + 1

	return qtt



if __name__ == '__main__':

	while True: 
		
		timestamp = datetime.timestamp(datetime.now())
		begin_time = time.time()
		end_time = begin_time + 60

		# Quantities vector: [quantity 2xx, quantity 4xx, quantity 5xx]
		qtt = [0,0,0]

		while time.time() < end_time:

			print("GET Request...")

			try:
				status_code = requests.get('https://desafioperformance.b2w.io/bairros').status_code

				print("Status code: ")
				print(status_code)		
			except requests.ConnectionError as e:
				print("Connection Error")

			
			add_status_code(status_code,qtt)
			time.sleep(2)

		write_file(timestamp,qtt)

		if(qtt[2] > qtt[0]):
			reboot_service

		
	print("Shutting down...")