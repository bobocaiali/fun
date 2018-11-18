#coding=utf-8
import threading
import time
import datetime
import sys
import os

class order_monitor:
	def __init__(self):
		pass
		self.lunch_start_monitor = None
		self.lunch_end_monitor = None
		self.supper_start_monitor = None
		self.supper_end_monitor = None
		self.snack_start_monitor = None
		self.snack_end_monitor = None

		self.lunch_start_cmd = '''
		curl 'https://oapi.dingtalk.com/robot/send?access_token=bd28df0a9acf84015847b1c1e2ead9fb58f48ddbc1aea6b8485ff73f2ef5f6eb' \
   		-H 'Content-Type: application/json' \
   		-d '
		  {"msgtype": "text", 
		    "text": {
		        "content": "该定午餐啦。"
		     },
		     "at": {
		         "isAtAll": true
		     }
		  }'
		'''

		self.lunch_end_cmd = '''
		curl 'https://oapi.dingtalk.com/robot/send?access_token=bd28df0a9acf84015847b1c1e2ead9fb58f48ddbc1aea6b8485ff73f2ef5f6eb' \
   		-H 'Content-Type: application/json' \
   		-d '
		  {"msgtype": "text", 
		    "text": {
		        "content": "午餐快结束预定了。快，还有救。"
		     },
		     "at": {
		         "isAtAll": true
		     }
		  }'
		'''

		self.supper_start_cmd = '''
		curl 'https://oapi.dingtalk.com/robot/send?access_token=bd28df0a9acf84015847b1c1e2ead9fb58f48ddbc1aea6b8485ff73f2ef5f6eb' \
   		-H 'Content-Type: application/json' \
   		-d '
		  {"msgtype": "text", 
		    "text": {
		        "content": "该定晚餐啦。"
		     },
		     "at": {
		         "isAtAll": true
		     }
		  }'
		'''

		self.supper_end_cmd = '''
		curl 'https://oapi.dingtalk.com/robot/send?access_token=bd28df0a9acf84015847b1c1e2ead9fb58f48ddbc1aea6b8485ff73f2ef5f6eb' \
   		-H 'Content-Type: application/json' \
   		-d '
		  {"msgtype": "text", 
		    "text": {
		        "content": "晚餐快结束预定了。快，定了吃完打球。"
		     },
		     "at": {
		         "isAtAll": true
		     }
		  }'
		'''

		self.snack_start_cmd = '''
		curl 'https://oapi.dingtalk.com/robot/send?access_token=bd28df0a9acf84015847b1c1e2ead9fb58f48ddbc1aea6b8485ff73f2ef5f6eb' \
   		-H 'Content-Type: application/json' \
   		-d '
		  {"msgtype": "text", 
		    "text": {
		        "content": "去拿夜宵啦。"
		     },
		     "at": {
		         "isAtAll": true
		     }
		  }'
		'''

		self.snack_end_cmd = '''
		curl 'https://oapi.dingtalk.com/robot/send?access_token=bd28df0a9acf84015847b1c1e2ead9fb58f48ddbc1aea6b8485ff73f2ef5f6eb' \
   		-H 'Content-Type: application/json' \
   		-d '
		  {"msgtype": "text", 
		    "text": {
		        "content": "夜宵快结束了。快，吃完走人。"
		     },
		     "at": {
		         "isAtAll": true
		     }
		  }'
		'''


	def order_lunch_start(self):
		pass
		print(self.lunch_start_cmd)
		os.system(self.lunch_start_cmd)

		self.lunch_start_monitor = threading.Timer(86400,self.order_lunch_start)
		self.lunch_start_monitor.start()

	def order_lunch_end(self):
		pass
		print(self.lunch_end_cmd)
		os.system(self.lunch_end_cmd)

		self.lunch_end_monitor = threading.Timer(86400,self.order_lunch_end)
		self.lunch_end_monitor.start()

	def order_supper_start(self):
		pass
		print(self.supper_start_cmd)
		os.system(self.supper_start_cmd)

		self.supper_start_monitor = threading.Timer(86400,self.order_supper_start)
		self.supper_start_monitor.start()

	def order_supper_end(self):
		pass
		print(self.supper_end_cmd)
		os.system(self.supper_end_cmd)

		self.supper_end_monitor = threading.Timer(86400,self.order_supper_end)
		self.supper_end_monitor.start()

	def order_snack_start(self):
		pass
		print(self.snack_start_cmd)
		os.system(self.snack_start_cmd)

		self.snack_start_monitor = threading.Timer(86400,self.order_snack_start)
		self.snack_start_monitor.start()

	def order_snack_end(self):
		pass
		print(self.snack_end_cmd)
		os.system(self.snack_end_cmd)

		self.snack_end_monitor = threading.Timer(86400,self.order_snack_end)
		self.snack_end_monitor.start()


	def start_monitor_process(self):
		pass
		now = datetime.datetime.now()
		lunch_start_time = datetime.datetime.strptime('10:00:00', '%H:%M:%S').replace(year=now.year,month=now.month,day=now.day)
		lunch_end_time = datetime.datetime.strptime('10:25:00', '%H:%M:%S').replace(year=now.year,month=now.month,day=now.day)
		supper_start_time = datetime.datetime.strptime('15:40:00', '%H:%M:%S').replace(year=now.year,month=now.month,day=now.day)
		supper_end_time = datetime.datetime.strptime('16:20:00', '%H:%M:%S').replace(year=now.year,month=now.month,day=now.day)
		snack_start_time = datetime.datetime.strptime('20:59:00', '%H:%M:%S').replace(year=now.year,month=now.month,day=now.day)
		snack_end_time = datetime.datetime.strptime('21:15:00', '%H:%M:%S').replace(year=now.year,month=now.month,day=now.day)

		if lunch_start_time < now:
			lunch_start_time = lunch_start_time + datetime.timedelta(days=1)
		time_to_lunch_start = int(round((lunch_start_time - datetime.datetime.now()).total_seconds()))

		if lunch_end_time < now:
			lunch_end_time = lunch_end_time + datetime.timedelta(days=1)
		time_to_lunch_end = int(round((lunch_end_time - datetime.datetime.now()).total_seconds()))

		if supper_start_time < now:
			supper_start_time = supper_start_time + datetime.timedelta(days=1)
		time_to_supper_start = int(round((supper_start_time - datetime.datetime.now()).total_seconds()))

		if supper_end_time < now:
			supper_end_time = supper_end_time + datetime.timedelta(days=1)
		time_to_supper_end = int(round((supper_end_time - datetime.datetime.now()).total_seconds()))

		if snack_start_time < now:
			snack_start_time = snack_start_time + datetime.timedelta(days=1)
		time_to_snack_start = int(round((snack_start_time - datetime.datetime.now()).total_seconds()))

		if snack_end_time < now:
			snack_end_time = snack_end_time + datetime.timedelta(days=1)
		time_to_snack_end = int(round((snack_end_time - datetime.datetime.now()).total_seconds()))

		self.lunch_start_monitor = threading.Timer(time_to_lunch_start,self.order_lunch_start)
		self.lunch_start_monitor.start()

		self.lunch_end_monitor = threading.Timer(time_to_lunch_end,self.order_lunch_end)
		self.lunch_end_monitor.start()

		self.supper_start_monitor = threading.Timer(time_to_supper_start,self.order_supper_start)
		self.supper_start_monitor.start()

		self.supper_end_monitor = threading.Timer(time_to_supper_end,self.order_supper_end)
		self.supper_end_monitor.start()

		self.snack_start_monitor = threading.Timer(time_to_snack_start,self.order_snack_start)
		self.snack_start_monitor.start()

		self.snack_end_monitor = threading.Timer(time_to_snack_end,self.order_snack_end)
		self.snack_end_monitor.start()



		# self.lunch_start_monitor = threading.Timer(1,self.order_lunch_start)
		# self.lunch_start_monitor.start()

		# self.lunch_end_monitor = threading.Timer(2,self.order_lunch_end)
		# self.lunch_end_monitor.start()

		# self.supper_start_monitor = threading.Timer(3,self.order_supper_start)
		# self.supper_start_monitor.start()

		# self.supper_end_monitor = threading.Timer(4,self.order_supper_end)
		# self.supper_end_monitor.start()

		# self.snack_start_monitor = threading.Timer(5,self.order_snack_start)
		# self.snack_start_monitor.start()

		# self.snack_end_monitor = threading.Timer(6,self.order_snack_end)
		# self.snack_end_monitor.start()



if __name__ == '__main__':
	meal_order_monitor = order_monitor()
	meal_order_monitor.start_monitor_process();
