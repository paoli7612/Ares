import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_confirm(to, experiment_id):
    msg = MIMEMultipart()
    msg['From'] = 'permessi@fedro.tech'
    msg['To'] = to
    msg['Subject'] = "PROVA"
    body = f"""
    <html>
        <body>
            <h1>Experiment completed! :D</h1>
            <p>See the report <a href="ares.com/report/{experiment_id}">hier</a></p>
        </body>
    </html>
    """
    msg.attach(MIMEText(body, 'html'))
    with smtplib.SMTP('smtp.hostinger.com', 587) as server:
        server.starttls()
        server.login('permessi@fedro.tech', 'Redebu$01')
        server.send_message(msg)
