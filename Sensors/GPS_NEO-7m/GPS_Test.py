import os
import time

aa = 0

while True:
	aa += 1
	try:
		data = os.system("cat /dev/ttyTHS1")
	except KeyboardInterrupt:
		break

	print("this time : ",aa)
	print(data)
	print("end data")
	time.sleep(10)

