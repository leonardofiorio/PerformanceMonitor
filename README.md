# PerformanceMonitor

This is an application implemented in Python to verify the service https://desafioperformance.b2w.io/bairros. 
The verification is done every 2 seconds and the returns are counted according to the classes 2XX, 4XX and 5XX. 
If the quantity of 5XX is greater than 2XX, the service is restarted.
The quantities 2XX, 4XX and 5XX are written to the output.csv file in the format: #timestamp,qtt_2XX,qtt_4XX,qtt_5XX


# Dependencies

* Docker

* Docker-compose

OBS:The dependencies installation process will be according to the operating system


# Run the PerformanceMonitor

* Install the dependencies

* Clone the repository

* Run in the terminal: **$ docker-compose up**
