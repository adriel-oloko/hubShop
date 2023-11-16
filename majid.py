import hashlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


host="localhost"
sql_user="root"
sql_pass="zxcvb"
dbase = "cdf"

confirm = '''
<div style="background-color: #fff6d4; width: 98%; margin: auto; border-radius: 8px;"><div style="background-color: #ffea99; width: 100%; margin: auto;"><img src="https://cdf-community.com/images/logo.png" alt="" style="width: 100%;"></div><div style="width: 85%; margin: auto; text-align: left;"><h3 style="color: #feaf26;">Forgot your password?</h3><p style="font-family: monospace; font-size: 10px;">Hey, we received a request to reset your password.</p>
<p style="font-family: monospace; font-size: 10px;">We can get you a new one</p><button style="background-color: #feaf26; text-align: center; padding: 10px; border: none; border-radius: 8px; color: white; font-weight: 700; font-size: 10px;">RESET MY PASSWORD</button><p style="font-family: monospace; font-size: 10px;">Did not request a password reset? You can ignore this message.</p>
            <br /><br />
        </div>
    </div>
'''
#TEMPLATE_PATH.append('./cdf-community.com/user/')

def mail_sender(sender, password, receiver, subject, content):
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender
	message['To'] = receiver
	message['Subject'] = subject

	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender, 'qsciapovrxxbzkcb')#password)

	part2 = MIMEText(content, 'html')

	message.attach(part2)
	text = message.as_string()

	session.sendmail(sender, receiver, text)
	session.quit()
	print('Mail Sent')

mail_sender('services.hubshop@gmail.com', 'egobkrjrnzsjoaaq', 'adrielloks@gmail.com', '#ui##mkk', confirm)
