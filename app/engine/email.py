import smtplib
from email.mime.text import MIMEText

def send_confirm(email):
    msg = MIMEText("Conferma")

    msg['Subject'] = 'Experiment finish successfully'
    msg['From'] = '280873@studenti.unimore.it'
    msg['To'] = email

    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login('tomaoli7612@gmail.com', 'ehehehe')
    smtp_server.send_message("esperimento completato")
    smtp_server.quit()