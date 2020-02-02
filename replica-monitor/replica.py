import logging

import mysql.connector
from configparser import ConfigParser

from tools.slack import Slack

config = ConfigParser()
config.read('./conf/setup.ini')

logging.basicConfig(filename='replica.log', filemode='a', format='%(asctime)s - %(message)s')

class MySQL(object):
	def __init__(self):
		try:
			self.db = mysql.connector.connect(
                                host=config['MYSQL']['mysql_host'],
                                user=config['MYSQL']['mysql_user'],
                                password=config['MYSQL']['mysql_password']
                        )
			query= 'SHOW SLAVE STATUS;'
			cursor = self.db.cursor()
			cursor.execute(query)
			self.replication_status_row = cursor.fetchall()[0]
			self.sql_running = self.replication_status_row[11]
			self.last_error_no = self.replication_status_row[18]
			self.last_error = self.replication_status_row[19]
			self.seconds_behind_master = self.replication_status_row[32]
			self.io_error = self.replication_status_row[35]
			self.slave_sql_running_state = self.replication_status_row[44]

		except mysql.connector.errors.ProgrammingError as e:
			 logging.error(e)

	def Main(self):
		try:
			if type(self.seconds_behind_master) == int:
				if self.seconds_behind_master > 300:
					s.Alert('Alert', 'Error', 
                                        'MySQL replica is behind Master server by ' + str(self.seconds_behind_master) + ' seconds',
                                        'High', '#FF0000')
			if type(self.seconds_behind_master) != int:
				logging.error('None integer value returend from seconds behind master')
			if self.sql_running == 'No':
				s.Alert('Alert', 'Error', 'Slave is not running', 'High', '#FF0000')
			if self.io_error != '':
				s.Alert('Alert', 'Error', self.io_error, 'High', '#FF0000')
		except Exception as e:
			logging.error(e)

s = Slack()
obj = MySQL()

if __name__=="__main__":
	obj.Main()
