import smtplib
import ssl
import csv
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

context = ssl.create_default_context()

class SendEmail():

	def __init__(self,smtp_server,port,email,password):
		
		self.smtp_server = smtp_server
		self.port = port
		self.email = email
		self.password = password

	def send(self,content_path , email_path):
		
		with smtplib.SMTP_SSL(self.smtp_server,self.port, context=context) as server:
			server.login(self.email,self.password)
			with open(content_path,'r') as message_content:
				content = json.load(message_content)
				message = MIMEMultipart("alternative")
				message["Subject"] = content['subject']
				message["From"] = self.email
				message.attach(MIMEText(content['content']['text'],"text"))
				message.attach(MIMEText(content['content']['html'],"html"))

				with open(email_path,'r') as emails:
					csv_data = csv.reader(emails)
					next(csv_data)
					for line in csv_data:
						name = line[0]
						rec_email = line[1]
						message["To"] = rec_email
						server.sendmail(self.email,rec_email, message.as_string())
						print('email send sucessfully to {} ({})'.format(name,rec_email))

    	