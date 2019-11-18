import time
import requests
import csv
from datetime import datetime

#
link = 'https://desafioperformance.b2w.io/bairros'

# Status code lists 
list_codes_2xx = [200,201,203,204,205,206,207,208,226]
list_codes_4xx = [400,401,402,403,404,405,406,407,408,
			      409,410,411,412,413,414,415,416,417,
			      418,421,422,423,424,426,428,429,431,
			      451]
list_codes_5xx = [500,501,502, 503,504,505,506,507,508,
                  510,511] 


def write_file(t, qtt_2xx, qtt_4xx, qtt_5xx):
	with open('output.csv', mode='a') as csvFile:
		writer = csv.writer(csvFile,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

		print("DENTRO DA FUNCAO")
		print("Quantity 2XX ", qtt_2xx)
		print("Quantity 4XX ", qtt_4xx)
		print("Quantity 5XX ", qtt_5xx)


		writer.writerow([t,qtt_2xx,qtt_4xx,qtt_5xx])

	csvFile.close()


if __name__ == '__main__':

	while True: 
		
		timestamp = datetime.timestamp(datetime.now())
		begin_time = time.time()
		end_time = begin_time + 60

		qtt_2xx = 0
		qtt_4xx = 0
		qtt_5xx = 0


		while time.time() < end_time:

			print("GET Request...")

			try:
				status_code = requests.get(link).status_code

				print("Status code: ")
				print(status_code)		
			except requests.ConnectionError as e:
				print("Connection Error")

			found = False

			i = 0
			while( (not found) and i < len(list_codes_2xx)):
				if status_code == list_codes_2xx[i]:
					found = True
					qtt_2xx = qtt_2xx + 1
				i = i + 1


			i = 0
			while( (not found) and i < len(list_codes_4xx)):
				if status_code == list_codes_4xx[i]:
					found = True
					qtt_4xx = qtt_4xx + 1 
				i = i + 1


			i = 0
			while( (not found) and i < len(list_codes_5xx)):
				if status_code == list_codes_5xx[i]:
					found = True
					qtt_5xx = qtt_5xx + 1
				i = i + 1

			time.sleep(2)


		write_file(timestamp,qtt_2xx,qtt_4xx,qtt_5xx)

		
	print("Shutting down...")