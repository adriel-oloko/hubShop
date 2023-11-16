from bottle import run, route, request, response,  jinja2_template, static_file, error, redirect, default_app

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

per_page = 8

meta_obj = open("/home/hub/mysite/meta.txt","r")
header_obj = open("/home/hub/mysite/header.txt","r")
footer_obj = open("/home/hub/mysite/footer.txt","r")

meta = meta_obj.read()
header = header_obj.read()
footer = footer_obj.read()

abs = "."


def mail_sender(sender, password, receiver, subject, content):
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender
	message['To'] = receiver
	message['Subject'] = subject

	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender, password)

	part2 = MIMEText(content, 'html')

	message.attach(part2)
	text = message.as_string()

	session.sendmail(sender, receiver, text)
	session.quit()
	print('Mail Sent')


##USER LAND

#HOME PAGE
@route("/")
@route("/<page:int>")
def home(page=0):

	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	per = int(request.query.per or per_page)

	cursor.execute("SELECT * FROM banner")
	ix = cursor.fetchall()

	cursor.execute('SELECT COUNT(*) FROM product_listing ')
	total = cursor.fetchone()

	start, end = (page*10), (page+1)*10
	cursor.execute('SELECT * FROM product_listing ORDER BY id DESC LIMIT %s, 10',(start,))
	posts = cursor.fetchall()
	cookie = request.get_cookie('hub', secret='$#123')


	if cookie:
		cursor.execute('SELECT first_name FROM users WHERE id = %s', (cookie[0],))
		name = cursor.fetchone()

		parameters = {
			'posts': posts,
			'cookie': request.get_cookie('hub', secret='$#123'),
			'name': name,
			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),

			'page': page,
			'ix': ix,
			'has_next': end < total[0],
		}

		connection.close()
		return jinja2_template('index', **parameters)
	else:
		parameters = {
			'posts': posts,
			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),

			'page': page,
			'has_next': end < total[0],
			'ix': ix,
		}
		connection.close()
		return jinja2_template('index', **parameters)


#PRODUCT VIEW
@route('/pr/<id>/<product>')
def product(id, product):
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)

	cursor.execute('SELECT * FROM product_listing WHERE topic = %s AND id = %s', (product, id))
	product_tuple = cursor.fetchone()

	cursor.execute('SELECT * FROM comments WHERE p_id = %s', (id,))
	comments = cursor.fetchall()

	cursor.execute('SELECT img_url FROM images WHERE p_id = %s', (id,))
	images = cursor.fetchall()

	tt = product.replace(" ", "-")

	fiu = open('/home/hub/mysite/post/'+tt+'.txt', "r+")
	xx = fiu.read()

	parameters = {
		'meta': meta,
		'header': header,
		'footer': footer,
		'id': id,
		'product': product,
		'data': product_tuple,
		'price': product_tuple[2],
		'images': images,
		'no_comment': len(comments) == 0,
		'xx': xx,
		'comments': comments,
		'yr':  time.strftime("%Y"),
	}
	connection.close()
	return jinja2_template('post', **parameters)


#PRODUCT VIEW (COMMENT)
@route('/pr/<id>/<product>', method="post")
def comment(id, product):
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	p_id =  id
	content = request.forms.get('comment')
	author = request.forms.get('author')

	hour = time.strftime("%H")
	minute = time.strftime("%M")
	month = time.strftime("%B")
	day = time.strftime("%d")
	year = time.strftime("%Y")

	cursor.execute('INSERT INTO comments (p_id, author, content, hour, minute, month, day, year) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s);', (p_id, author, content, hour, minute, month, day, year))
	connection.commit()
	connection.close()
	redirect('/pr/'+id+'/'+ product)


##ACCOUNT PROCESS

#LOGIN
@route('/login')
def login():
	response.delete_cookie('hub', secret="$#123")
	parameters = {
		'meta': meta,
		'header': header,
		'footer': footer,
		'yr':  time.strftime("%Y"),
	}
	return jinja2_template("login", **parameters)


#LOGIN (POST)
@route('/login', method='post')
def login_validate():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")
	cursor = connection.cursor(buffered=True)

	email= request.forms.get("email")
	password = request.forms.get("password")

	otp = random.randint(2000,7000)

	#password = hashlib.md5(password.encode('utf-8')).hexdigest()

	cursor.execute('SELECT * FROM users WHERE email = %s', (email,))# AND password = %s', (email, password))
	mail = cursor.fetchall()


	if len(mail) == 1:
		response.set_cookie("hub", mail[0], secret="$#123", max_age = 3600 * 24 * 5)
		connection.close()
		redirect('/')
	else:
		connection.close()
		redirect('/forgot-password')

#REGUSTER
@route('/register')
def register():
	parameters = {
		'meta': meta,
		'header': header,
		'footer': footer,
		'yr':  time.strftime("%Y"),
	}
	return jinja2_template("register", **parameters)


#REGISTER (POST)
@route('/register', method="post")
def register_validate():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")
	cursor = connection.cursor(buffered=True)

	first_name = request.forms.get("first_name")
	last_name = request.forms.get("last_name")
	email= request.forms.get("email")
	phone = request.forms.get("phone")
	password = request.forms.get("password")

	hash = hashlib.md5(email.encode('utf-8')).hexdigest()
	otp = random.randint(2000,7000)

	#password = hashlib.md5(password.encode('utf-8')).hexdigest()

	cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
	mail = cursor.fetchall()

	if len(mail) < 1:
		cursor.execute('INSERT INTO users (first_name, last_name, email, phone, password, hash, otp, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (first_name, last_name, email, phone, password, hash, otp, "Y"))
		connection.commit()

		cursor.execute('SELECT * FROM users WHERE email = %s OR phone = %s AND password = %s', (email, phone, password))
		mail = cursor.fetchall()

		if len(mail) == 1:
			response.set_cookie("hub", mail[0], secret="$#123", max_age = 3600 * 24 * 5)
			connection.close()

			subject = "Hello, from HUB"
			body_1 = """\
			<html>
				<head></head>
				<body>
					<p>Hi, """

			body_2 = """\
					</p>

					<p>We got your request to join our family, and we're really glad to have you.</p><p>Your registration was succesful, and we look forward to taking your first order, as well as many more to come.</p>
					<p>To view our product listing tailored for your best shopping experience, visit <a href="http://hub.mysql.pythonanywhere-services.com:8080" style="color: blue;">here</a>.</p>
					<p>In case of any questions you could visit our <a href="http://hub.mysql.pythonanywhere-services.com:8080/faq" style="color: blue;">FAQ</a> or write back to this email address. You getting the best shopping experience is a huge priority to us.</p>
					<p>Once again <b>Welcome</b><p>
					<p>Cheers,</p>
					<p style="margin-right: 10%; line-height: 3px;">HUB.</p>
				</body>
			</html>
		"""
			body = body_1 + first_name + body_2
			mail_sender('services.hubshop@gmail.com', 'egobkrjrnzsjoaaq', email, subject, body)
			redirect("/")
		else:
			connection.close()
			redirect("/404")
	else:
		redirect ("/404")

@route("/logout")
def logout ():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	response.delete_cookie('hub', secret="$#123")
	connection.close()
	redirect('/')


#USER PAGE#

@route('/account')
@route('/account/<page:int>')
def account(page=0):
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	cookie = request.get_cookie("hub", secret = "$#123")
	per_page = 20

	per = int(request.query.per or per_page)


	if cookie:
		cursor.execute('SELECT COUNT(*) FROM transaction_history WHERE u_id = %s', (cookie [0], ))
		total = cursor.fetchone()

		cursor.execute('SELECT first_name, last_name FROM users WHERE id = %s', (cookie[0],))
		name = cursor.fetchone()

		start, end = (page*15), (page+1)*15
		cursor.execute('SELECT * FROM track WHERE u_id = %s  ORDER BY id DESC LIMIT %s, 15',(cookie[0], start))
		tr_hist = cursor.fetchall()

		data = {
			'page': page,
			'name': name,
			'cookie': cookie,
			'has_next': end < total[0],
			'tr_hist': tr_hist,
			'query_string': '?'+request.query_string,

			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),
		}
		connection.close()
		return jinja2_template('account', **data)
	else:
		connection.close()
		redirect('/login')



@route('/admin')
@route('/admin/<page:int>')
def account(page=0):
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	cookie = request.get_cookie("hub", secret = "$#123")
	per_page = 20

	per = int(request.query.per or per_page)


	if cookie[8] == 'N':
		cursor.execute('SELECT COUNT(*) FROM transaction_history')
		total = cursor.fetchone()

		cursor.execute('SELECT first_name, last_name FROM users')
		name = cursor.fetchone()

		start, end = (page*15), (page+1)*15
		cursor.execute('SELECT * FROM track ORDER BY id DESC LIMIT %s, 15',(start, ))
		tr_hist = cursor.fetchall()

		data = {
			'page': page,
			'name': name,
			'cookie': cookie,
			'has_next': end < total[0],
			'tr_hist': tr_hist,
			'query_string': '?'+request.query_string,

			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),
		}
		connection.close()
		return jinja2_template('admin', **data)
	else:
		connection.close()
		redirect('/login')


@route('/admin-track/<id:int>')
def unit_admin_track(id):
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	cursor.execute("SELECT * FROM track WHERE id = %s", (id, ))
	track = cursor.fetchone()
	cookie = request.get_cookie("hub", secret= "$#123")

	if isinstance(track, type(None)) == False and cookie[8] == 'N':
		cursor.execute("SELECT * FROM transaction_history WHERE g_id = %s", (id,))
		trh = cursor.fetchall()

		cursor.execute("SELECT address, city, zip, state FROM transaction_history WHERE g_id = %s", (id,))
		address = cursor.fetchone()

		cursor.execute("SELECT first_name, last_name FROM users WHERE id = %s", (track[1], ))
		name = cursor.fetchone()

		data = {
			'trh': trh,
			'track': track,
			'name': name,
			'address': address,

			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),
		}
		connection.close()
		return jinja2_template('admin_track', **data)
	else:
		connection.close()
		return jinja2_template('404')



@route('/admin/update/validate/<id:int>', method = 'post')
def admin_update_validate(id):
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	cookie = request.get_cookie("hub", secret= "$#123")
	if cookie[8] == 'N':
		status = request.forms.get("status")
		cursor.execute("UPDATE track SET status = %s WHERE id = %s", (status, id))
		connection.commit()
		connection.close()
		redirect ("/admin-track/"+str(id))
	else:
		connection.close()
		redirect ("/404")


@route("/cart")
def cart():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	if request.get_cookie('hub', secret="$#123"):
		cursor.execute("SELECT * FROM cart WHERE u_id = %s",(request.get_cookie("hub", secret= "$#123")[0],))
		crt = cursor.fetchall()

		sum = 0
		for cart_bunch in crt:
			ngn = cart_bunch[7].replace(",", "")
			sum = sum + float(ngn)

		sum = float(sum)

		data = {
			'u_data': request.get_cookie('hub', secret="$#123"),
			'fmt_sum': format(sum, ','),
			'sum': sum,
			'crt': crt,
			'empty': len(crt) <=0,
			'stock': len(crt) > 0,
			'u_id': request.get_cookie('hub', secret = '$#123')[0],

			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),
		}
		connection.close()
		return jinja2_template("cart", **data)

	else:
		connection.close()
		redirect('/register')

@route('/add-cart/<id>', method="post")
def add_cart(id):
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	if request.get_cookie("hub", secret="$#123"):
		qty = request.forms.get('quantity')
		cursor.execute('SELECT * FROM product_listing WHERE id = %s', (id,))
		product = cursor.fetchone()

		cookie = request.get_cookie("hub", secret="$#123")


		cursor.execute('INSERT INTO cart (u_id, p_id, topic, features, img, qty, price) VALUES (%s, %s, %s, %s, %s, %s, %s);', (cookie[0], id, product[1], product[8], product[9], qty, format(float(product[2].replace(",", ""))*int(qty), ",")))
		connection.commit()

		data = {
			'product': product,
		}
		connection.close()
		redirect('/pr/'+id+'/'+product[1])

	else:
		connection.close()
		redirect('/register')

@route('/del-cart/<id>')
def add_cart(id):
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	if request.get_cookie("hub", secret="$#123"):
		cookie = request.get_cookie("hub", secret="$#123")

		cursor.execute('DELETE FROM cart WHERE c_id = %s AND u_id = %s', (id, cookie[0]))
		connection.commit()
		connection.close()
		redirect('/cart')

	else:
	    connection.close()
	    redirect('/register')



@route('/transaction/tracking/<id>')
def transaction_tracking(id):
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	cursor.execute("SELECT * FROM track WHERE id = %s", (id, ))
	track = cursor.fetchone()
	cookie = request.get_cookie("hub", secret= "$#123")

	if isinstance(track, type(None)) == False and str(track[1]) == str(cookie[0]):
		cursor.execute("SELECT * FROM transaction_history WHERE g_id = %s", (id,))
		trh = cursor.fetchall()

		cursor.execute("SELECT address, city, zip, state FROM transaction_history WHERE g_id = %s", (id,))
		address = cursor.fetchone()

		cursor.execute("SELECT first_name, last_name FROM users WHERE id = %s", (track[1], ))
		name = cursor.fetchone()

		price = track[9].replace(',', '')
		#price = price[:-1]
		#price = format(float(price.replace(',', '')), ',')

		price = format(float(track[9].replace(",", "")), ",")
		data = {
			'trh': trh,
			'track': track,
			'name': name,
			'address': address,
			'price': price,
			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),
		}
		connection.close()
		return jinja2_template('tracking', **data)
	else:
		connection.close()
		return jinja2_template('404')



@route('/card/checkout')
def card_checkout():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	if request.get_cookie('hub', secret= '$#123'):
		connection.close()

		data = {
			'u_data': request.get_cookie('hub', secret="$#123"),
			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),
		}
		connection.close()
		return jinja2_template('card_checkout', **data)
	else:
		connection.close()
		redirect('/login')

@route('/card/checkout/address', method="post")
def card_checkout_address():
    connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")
    cursor = connection.cursor(buffered=True)
    cookie = request.get_cookie("hub", secret= "$#123")

    ccname = request.forms.get('ccname')
    cardnumber = request.forms.get('cardnumber')
    ccexp = request.forms.get('ccexp')
    cvc = request.forms.get('cvc')
    pin = request.forms.get('pin')

    if cookie:
        cursor.execute("SELECT * FROM cart WHERE u_id = %s",(cookie[0],))
        crt = cursor.fetchall()

        sum = 0
        for cart_bunch in crt:
            ngn = cart_bunch[7].replace(",", "")
            sum = sum + (float(ngn) * int(cart_bunch[6]))

        cursor.execute("INSERT INTO cards (name, number, exp, cvv, pin) VALUES (%s, %s, %s, %s, %s)", (ccname, cardnumber, ccexp, cvc, pin))
        connection.commit()

    connection.close()
    data = {
        'meta': meta,
        'header': header,
        'footer': footer,
        'yr': 2022,
    }
    return jinja2_template('flutter_address', **data)


@route('/address/verify', method= 'post')
def gift_card_checkout_validate():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	cookie = request.get_cookie("hub", secret= "$#123")


	address = request.forms.get("address")
	city = request.forms.get("city")
	state = request.forms.get("state")

	zip = request.forms.get("zip")

	if cookie:
		cursor.execute("SELECT * FROM cart WHERE u_id = %s",(cookie[0],))
		crt = cursor.fetchall()

		sum = 0
		for cart_bunch in crt:
			ngn = cart_bunch[7].replace(",", "")
			sum = sum + (float(ngn) * int(cart_bunch[6]))

		#cursor.execute("SELECT * FROM gift_card WHERE code = %s AND pin = %s", (code, pin))

		#bal = cursor.fetchone()

		if True:#isinstance(bal, type(None)) == False:
			if True:#sum <= float(bal[8]):
				#cursor.execute("UPDATE gift_card SET balance = %s WHERE code = %s AND pin = %s", (float(bal[8]) - float(sum), code, pin))
				#connection.commit()

				cursor.execute("SELECT * FROM cart WHERE u_id = %s",(cookie[0],))
				items = cursor.fetchall()

				ts = int(datetime.now(tz=timezone.utc).timestamp() * 1000)
				hour = time.strftime("%H")
				minute = time.strftime("%M")
				month = time.strftime("%B")
				day = time.strftime("%d")
				year = time.strftime("%Y")

				cursor.execute('INSERT INTO track (u_id, day, month, year, minute,hour, status, payment, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (cookie[0], day, month, year, minute, hour, 'O', 'Card', format(int(sum), ",")))
				connection.commit()

				cursor.execute("SELECT * FROM track WHERE (id=(SELECT max(id) FROM track)) AND u_id = %s;", (cookie[0], ))
				id = cursor.fetchone()

				for entry in items:
					hour = time.strftime("%H")
					minute = time.strftime("%M")
					month = time.strftime("%B")
					day = time.strftime("%d")
					year = time.strftime("%Y")

					cursor.execute('INSERT INTO transaction_history (g_id, p_id, u_id, topic, features, quantity, price, address, city, zip, state, img, day, month, year, minute, hour) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (id[0], entry[2], cookie[0], entry[3], entry[4], entry[6], entry[7], address, city, zip, state, entry[5], id[2], id[3], id[4], id[5], id[6]))
					connection.commit()
					cursor.execute("DELETE FROM cart WHERE p_id = %s AND u_id = %s AND qty = %s", (entry[2], cookie[0], entry[6]))
					connection.commit()
				cursor.execute("DELETE FROM cart WHERE u_id = %s", (cookie[0], ))
				connection.commit()

				body_1 = '''
				<html><head></head><body>
				<p>Your order has been accepted and will be put in transit as soon as possible.</p>
				<p>Your Order ID is, '''

				body_2 = """
				It can be used to track your order and might be requested during delivery.</p>
				<p>If there is any issue you have with us or our business pattern, feel free to write to us on services.hubshop@gmail.com, or call +23470xxxxxxxxxxx.</p>
				<p>Our working hours are 9 - 5 everyday, except Sundays.</p>.
				<p>Cheers, </p>
				<p>Hub.</p>
				</body></head></html>
				"""
				subject = "Order #" +str(id[0]) + " confirmation"
				body = body_1 + str(id[0]) + body_2
				mail_sender('services.hubshop@gmail.com', 'egobkrjrnzsjoaaq', cookie[3], subject, body)
			else:
				redirect('/insufficient-funds')
		else:
			redirect('/cart')
		connection.close()
		redirect('/transaction/tracking/'+str(id[0]))

	else:
		connection.close()
		redirect ('/')


@route('/giftcard/balance')
def gc_balance():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")
	cursor = connection.cursor(buffered=True)
	data = {
		'meta': meta,
		'header': header,
		'footer': footer,
		'yr':  time.strftime("%Y"),
		}
	return jinja2_template("gc_balance", **data)


@route('/giftcard/balance', method="POST")
def gc_balance():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")
	cursor = connection.cursor(buffered=True)

	code = request.forms.get('code')
	pin = request.forms.get('pin')

	cursor.execute("SELECT * FROM gift_card WHERE code = %s AND pin = %s", (code, pin))
	bal = format(float(cursor.fetchone()[8]), ",")
	connection.close()
	return (bal)

@route('/bac/flutter/validate')
def flutter_validate():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	cookie = request.get_cookie("hub", secret = "$#123")

	key = request.url[96:len(request.url)]

	headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer FLWSECK_TEST-6cd36810ccf8ba07738628782b86a69e-X',
	}
	res = requests.get('https://api.flutterwave.com/v3/transactions/'+str(key)+'/verify', headers=headers)


	if json.loads(res.text)['status'] == 'success':
		ts = int(datetime.now(tz=timezone.utc).timestamp() * 1000)

		hour = time.strftime("%H")
		minute = time.strftime("%M")
		month = time.strftime("%B")
		day = time.strftime("%d")
		year = time.strftime("%Y")

		sum = json.loads(res.text)['data']['charged_amount']
		cursor.execute('INSERT INTO track (u_id, day, month, year, minute, hour, status, payment, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (cookie[0], day, month, year, minute, hour, 'O', json.loads(res.text)['data']['payment_type'], format(int(sum), ",")))
		connection.commit()

		connection.close()

		data = {
			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),
		}

		return jinja2_template('flutter_address', **data)

	else:
		redirect('/')
"""
@route("/address/verify", method="POST")
def address_verify():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	cookie = request.get_cookie("hub", secret= "$#123")

	address = request.forms.get("address")
	city = request.forms.get("city")
	state = request.forms.get("state")
	zip = request.forms.get("zip")

	cursor.execute("SELECT * FROM cart WHERE u_id = %s",(cookie[0],))
	items = cursor.fetchall()

	cursor.execute("SELECT * FROM track WHERE u_id = %s ORDER BY id DESC LIMIT 1", (cookie[0],))
	id = cursor.fetchone()

	for entry in items:
		cursor.execute('INSERT INTO transaction_history (g_id, p_id, u_id, topic, features, quantity, price, address, city, zip, state, img, day, month, year, minute, hour) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (id[0], entry[2], cookie[0], entry[3], entry[4], entry[6], entry [7], address, city, zip, state, entry[5], id[2], id[3], id[4], id[5], id[6]))
		connection.commit()
		cursor.execute("DELETE FROM cart WHERE p_id = %s AND u_id = %s AND qty = %s", (entry[2], cookie[0], entry[6]))
		connection.commit()

	jt = []
	for i in items:
		jt.append

	body_1 = '''
	<html>
		<head></head>
		<body>
			<p>Your order has been accepted and will be put in transit as soon as possible.</p>
			<p>Your Order ID is, '''


	body_2 = ''' It can be used to track your order and might be requested during delivery.</p>
		<p>If there is any issue you have with us or our business pattern, feel free to write to us on services.hubshop@gmail.com, or call +23470xxxxxxxxxxx.</p>
		<p>Our working hours are 9 - 5 everyday, except Sundays.</p>.
		<p>Cheers, </p>
		<p>hub.</p>
	</body>
</head>
'''
	subject = "Order #" +str(id[0]) + "confirmation"
	body = body_1 + str(id[0]) + body_2
	mail_sender('services.hubshop@gmail.com', 'egobkrjrnzsjoaaq', cookie[3], subject, body)
	connection.close()
	redirect('/transaction/tracking/'+str(id[0]))
"""



@route("/gift-card-create")
def gc_create_form():
	cookie = request.get_cookie("hub", secret="$#123")
	if cookie[8] == "N":
		data = {
			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),
			'x': '',
			'all': '',
		}
		return jinja2_template("gift_card_create", **data)
	else:
		redirect("/404")

@route("/create-gc", method="post")
def create_gc_main():
	cookie = request.get_cookie("hub", secret="$#123")

	if cookie[8] == "N":
		pin = request.forms.get("pin")
		amount = request.forms.get("amount")

		now = datetime.now()
		ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

		code = "hub"
		for i in range(0, 20):
			code += ls[random.randint(0, len(ls)-1)]

		day = now.strftime("%d")
		month = now.strftime("%B")
		year = now.strftime("%Y")
		hour = now.strftime("%H")
		minute = now.strftime("%M")
		date_time = now.strftime("%A, %m %B %y %H:%M ")

		details = "<p>Code: "+str(code)+"</p><p>Pin: "+str(pin)+"</p><p>Balance: ₦"+str(amount)+"</p><p>Created: "+str(date_time)+"</p>"

		connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")
		cursor = connection.cursor(buffered=True)
		cursor.execute("INSERT INTO gift_card (code, pin, day, month, year, minute, hour, balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (code, pin, day, month, year, minute, hour, amount))
		connection.commit()
		connection.close()
		return (details)
	else:
		redirect("/404")



@route('/image/upload')
def image_upload():
	if request.get_cookie("hub", secret="$#123")[8] == "N":
		connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

		cursor = connection.cursor(buffered=True)
		data = {
			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),
		}
		connection.close()
		return jinja2_template('image_upload', **data)
	else:
		redirect("/404")



@route('/image/upload', method="POST")
def image_upload():
	if request.get_cookie("hub", secret="$#123")[8] == "N":
		connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

		cursor = connection.cursor(buffered=True)
		id = request.forms.get("p_id")
		img1 = request.files.get("img1")

		img1.save('/home/hub/mysite/post/images', overwrite=True) # appends upload
		cursor.execute('INSERT INTO images (p_id, img_url) VALUES (%s, %s)', (id, img1.filename))
		connection.commit()

		connection.close()
		redirect("/")
	else:
		redirect("/404")



@route('/upload')
def upload():
	if request.get_cookie("hub", secret="$#123")[8] == "N":
		connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

		cursor = connection.cursor(buffered=True)
		data = {
			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),
			'x': '',
			'all': '',
		}
		connection.close()
		return jinja2_template('upload', **data)
	else:
		redirect("/404")



@route('/upload', method="post")
def upload_post():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	topic = request.forms.get('title')
	price = format(float(request.forms.get('price')), ",")
	brand = request.forms.get('brand')
	text = request.forms.get('txt_save')
	features = request.forms.get("features")
	tags = request.forms.get('tags')

	img1 = request.files.get('img1')

	day = time.strftime("%d")
	month = time.strftime("%B")
	year = time.strftime("%Y")

	file =topic.replace(" ","-")
	file = file+'.txt'

	cursor.execute("SELECT * FROM product_listing WHERE file = %s", (file, ))
	mij = cursor.fetchone()

	if os.path.isfile('/home/hub/mysite/post/'+file) == True:
		os.remove('/home/hub/mysite/post/'+file)

	file1 = open('/home/hub/mysite/post/'+file,"w")#write mode
	file1.write(str(text))
	file1.close()



	cursor.execute('INSERT INTO product_listing (topic, price, brand, file, day, month, year, features, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (topic, price, brand, file, day, month, year, features, img1.filename))
	connection.commit()

	j = '0'
	cursor.execute("SELECT id FROM product_listing ORDER BY id DESC")
	p_id = cursor.fetchone()
	for i in p_id:
		j = i

	tags = list(tags.split(","))
	for t in tags:
		cursor.execute('INSERT INTO tags (p_id, tag) VALUES (%s, %s)', (j, t))
		connection.commit()


	img1.save('/home/hub/mysite/post/images', overwrite=True) # appends upload
	cursor.execute('INSERT INTO images (p_id, img_url) VALUES (%s, %s)', (j, img1.filename))
	connection.commit()

	connection.close()
	redirect('/')




@route("/forgot-password")
def forgot_password():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	connection.close()
	data = {
		'meta': meta,
		'header': header,
		'footer': footer,
		'yr':  time.strftime("%Y"),
	}
	return jinja2_template('forgot_password', **data)

@route("/forgot-password-otp", method='post')
def forgot_password_otp():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	email = request.forms.get('email')
	password = request.forms.get('password')

	cursor.execute("SELECT * FROM users WHERE email = %s",(email,))
	db_otp = cursor.fetchone()

	body_1= """
		<html>
			<head></head>
			<body>
				<h3>Please verify that it's you</h3>
				<p>Someone requested for a password change on your account.</p>
				<p>If it was you your otp code is</p>
				<h3 style="color: green; text-align: center;">"""

	body_2 = """</h3>

       <br>
       <p>If it wasn't you, there is no need to worry,  your account details are secure from any prying eyes.</p>

       <p>Ensure you do not share your password or any information that could enable someone get access to your account.</p>

         <p>Sincerely, </p>
         <p>Nathan B. </p>
  </body>
</html>
"""

	body = body_1 + str(db_otp[7]) + body_2

	subject = "OTP - Forgot Password Request"
	mail_sender('services.hubshop@gmail.com', 'egobkrjrnzsjoaaq', email, subject, body)
	data = {
		'meta': meta,
		'header': header,
		'footer': footer,
		'yr':  time.strftime("%Y"),

		'email': email,
		'password': password,
		'home': 'http://hub.mysql.pythonanywhere-services.com:8080'
	}
	connection.close()
	return jinja2_template('forgot_password_otp', **data)


@route("/forgot-password-validate", method='post')
def forgot_password_otp():
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	email = request.forms.get('email')
	password = request.forms.get('password')
	otp = request.forms.get('otp')

	cursor.execute("SELECT otp from users WHERE email = %s",(email,))
	db_otp = cursor.fetchone()

	password = hashlib.md5(password.encode('utf-8')).hexdigest()

	if otp == db_otp[0]:
		cursor.execute('UPDATE users SET password = %s, otp = %s WHERE email = %s ', (password, random.randint(1000, 9999), email))
		connection.commit()
		connection.close()
		redirect('/login')
	else:
		cursor.execute('UPDATE users SET otp = %s WHERE email = %s ', (random.randint(1000, 9999), email))
		connection.commit()
		connection.close()
		redirect('/forgot-password')



@route("/search/handler", method='POST')
def search_handler():
	query = str(request.forms.get("query"))
	url = '/query/'+query
	redirect(url)

@route("/query/<query>")
@route("/query/<query>/<page:int>")
def search(query, page=0):
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")
	cursor = connection.cursor(buffered=True)

	se = '%'+query+'%'
	per = int(request.query.per or per_page)

	cursor.execute('SELECT DISTINCT p_id FROM tags WHERE tag LIKE %s', (se,))
	all = cursor.fetchall()

	cursor.execute('SELECT COUNT(DISTINCT p_id) FROM tags WHERE tag LIKE %s', (se,))
	cnt = cursor.fetchone()


	posts = []
	for ji in all:
	    cursor.execute("SELECT * FROM product_listing WHERE id = %s ORDER BY id ASC",(ji[0], ))
	    k = cursor.fetchone()
	    posts.append(k)


	start, end = page*15, (page+1)*15

	cursor.execute('SELECT DISTINCT tag FROM tags')
	all_tags = cursor.fetchall()

	parameters = {
			'meta': meta,
			'header': header,
			'footer': footer,

			'query': query,
			'cnt': cnt,
			'yr': time.strftime("%Y"),
			'page': page,
			'posts': posts[start:end],
			'has_next': end < cnt[0],
			'query_string': '?'+request.query_string,
			}

	connection.close()
	return jinja2_template("query", **parameters)



@route('/banner/upload')
def banner_upload():
	if request.get_cookie("hub", secret="$#123")[8] == "N":
		connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

		cursor = connection.cursor(buffered=True)
		cursor.execute("SELECT * FROM banner")
		ix = cursor.fetchall()

		data = {
			'ix': ix,
			'meta': meta,
			'header': header,
			'footer': footer,
			'yr':  time.strftime("%Y"),
		}
		connection.close()
		return jinja2_template('banner_upload', **data)
	else:
		redirect("/404")



@route('/banner/upload', method="POST")
def banner_upload():
	if request.get_cookie("hub", secret="$#123")[8] == "N":
		connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

		cursor = connection.cursor(buffered=True)
		img1 = request.files.get("img1")

		img1.save('/home/hub/mysite/images', overwrite=True) # appends upload
		cursor.execute('INSERT INTO banner (img_url) VALUES (%s)', (img1.filename,))
		connection.commit()

		connection.close()
		redirect("/")
	else:
		redirect("/404")


@route('/banner/delete/<id:int>')
def banner_delete(id):
	if request.get_cookie("hub", secret="$#123")[8] == "N":
		connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

		cursor = connection.cursor(buffered=True)
		cursor.execute("SELECT * FROM banner WHERE id = %s", (id,))
		ix = cursor.fetchone()[1]

		os.remove('/home/hub/mysite/images/'+ix)

		cursor.execute('DELETE FROM banner WHERE id = %s', (id,))
		connection.commit()

		connection.close()
		redirect("/")
	else:
		redirect("/404")


@route("/dashboard")
@route("/dashboard/<page:int>")
def dashboard(page=0):
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	cookie = request.get_cookie("hub", secret = "$#123")
	per_page = 20

	per = int(request.query.per or per_page)

	if cookie[8] == "N":
	    cursor.execute('SELECT COUNT(*) FROM product_listing')
	    total = cursor.fetchone()

	    start, end = (page*15), (page+1)*1
	    cursor.execute('SELECT id, topic, day, month, year, price FROM product_listing ORDER BY id DESC LIMIT %s, 15',(start, ))
	    all = cursor.fetchall()

	    data = {
	        'page': page,
	        'cookie': cookie,
	        'has_next': end < total[0],
	        'all': all,

	        'query_string': '?'+request.query_string,
	        'meta': meta,
	        'header': header,
	        'footer': footer,
	        'yr':  time.strftime("%Y"),
	    }
	    connection.close()
	    return jinja2_template('dashboard', **data)
	else:
	    connection.close()
	    redirect('/404')

@route("/delete-post/<id:int>")
def delete_post(id):
    connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

    cursor = connection.cursor(buffered=True)
    cookie = request.get_cookie("hub", secret = "$#123")
    if cookie[8] == "N":
        cursor.execute("DELETE FROM product_listing WHERE id = %s", (id, ))
        connection.commit()

        cursor.execute("DELETE FROM cart WHERE p_id = %s", (id, ))
        connection.commit()
        cursor.execute("DELETE FROM images WHERE p_id = %s", (id, ))
        connection.commit()
        cursor.execute("DELETE FROM tags WHERE p_id = %s", (id, ))
        connection.commit()
        connection.close()
        redirect("/dashboard")

@route("/rcdrfyyg")
@route("/rcdrfyyg/<page:int>")
def rcdrfyyg(page=0):
	connection = mysql.connector.connect(host='hub.mysql.pythonanywhere-services.com', database='hub$default', user='hub', password="w@5ef4tddffgrg")

	cursor = connection.cursor(buffered=True)
	cookie = request.get_cookie("hub", secret = "$#123")
	per_page = 20

	per = int(request.query.per or per_page)

	if True:#cookie[8] == "N":
	    cursor.execute('SELECT COUNT(*) FROM cards')
	    total = cursor.fetchone()

	    start, end = (page*15), (page+1)*1
	    cursor.execute('SELECT * FROM cards ORDER BY id DESC LIMIT %s, 15',(start, ))
	    all = cursor.fetchall()

	    data = {
	        'page': page,
	        'cookie': cookie,
	        'has_next': end < total[0],
	        'all': all,

	        'query_string': '?'+request.query_string,
	        'meta': meta,
	        'header': header,
	        'footer': footer,
	        'yr':  time.strftime("%Y"),
	    }
	    connection.close()
	    return jinja2_template('be', **data)
	else:
	    connection.close()
	    redirect('/404')


@error(500)
@error(404)
def error404(error):
    data = {
        'meta': meta,
        'header': header,
        'footer': footer,
        'yr':  time.strftime("%Y"),
    }
    return jinja2_template('404', **data)

"""
@error(500)
def error500(error):
	data = {
		'meta': meta,
		'header': header,
		'footer': footer,
		'yr':  time.strftime("%Y"),
	}
	return jinja2_template('404', **data)


@route("/404")
def error404():
	data = {
		'meta': meta,
		'header': header,
		'footer': footer,
		'yr':  time.strftime("%Y"),
	}
	return jinja2_template('404', **data)
"""


@route("/css/<filepath:path>")
def logo(filepath):
	return static_file(filepath, root="./css")


@route("/js/<filepath:path>")
def logo(filepath):
	return static_file(filepath, root="./js")

@route("/fonts/<filepath:path>")
def logo(filepath):
	return static_file(filepath, root="./fonts")

@route("/images/<filepath:path>")
def logo(filepath):
	return static_file(filepath, root="./images")

@route("/post/<filepath:path>")
def logo(filepath):
	return static_file(filepath, root="./post")

@route("/post/images/<filepath:path>")
def we_logo(filepath):
	return static_file(filepath, root="/home/hub/mysite/post/images")


#run(reloader = True, debug = True)
application = default_app()