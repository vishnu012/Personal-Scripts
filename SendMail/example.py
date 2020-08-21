from sendemail import SendEmail 

#gmail service as example

s = SendEmail("smtp.gmail.com",465,email,password)

s.send('content.json','emails.csv')