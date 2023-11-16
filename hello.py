import sqlite3

import mysql.connector
from mysql.connector import Error

import itertools
import statistics
from statistics import mode

import csv
import hashlib
import time
import random
import requests
import json
import os
from datetime import datetime, timezone

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")
cursor = connection.cursor(buffered=True)

for ui in range(0, 3656):
	ts = int(datetime.now(tz=timezone.utc).timestamp() * 1000)
	hour = time.strftime("%H")
	minute = time.strftime("%M")
	month = time.strftime("%B")
	day = time.strftime("%d")
	year = time.strftime("%Y")
	cursor.execute('INSERT INTO track (u_id, day, month, year, minute,hour, status, payment, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (0, day, month, year, minute, hour, 'O', 'Card', format(int(5000), ",")))

	print(ui)
	connection.commit()
connection.close()