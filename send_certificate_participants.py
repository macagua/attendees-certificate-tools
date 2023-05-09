"""Send via email the certificate for every participants."""
import os
import smtplib

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


GMAIL_USERNAME = 'CHANGE_ME@gmail.com'
# get the password in the gmail (manage your google account, click on the avatar on the right)
# then go to security (right) and app password (center)
# insert the password and then choose mail and this computer and then generate
# copy the password generated here
GMAIL_PASSWORD = 'CHANGE_ME'
# put your email here
EMAIL_FROM = 'Scrum LATAM Comunidad <scrums.latam+eventos@gmail.com>'
# put the email of the receiver here
EMAIL_TO = 'noreply@mail.com'
# put your email body here
EMAIL_BODY = '''Hola, Estimado(a)<br/>
<br/>
Como <font color="#DB360D"><b>Scrum LATAM Comunidad</b></font> estamos felices y agradecemos que nos hayas acompañado en la celebración de nuestro <b>3er Aniversario</b> porque tu participación es muy importante para nosotros y sabemos lo valioso que es tu tiempo de aprendizaje, adjunto encontrarás el certificado de participación como asistente.
<br/>
<br/>
La educación nos motiva para trascender y en este maravilloso mundo de la <b>agilidad</b> nosotros te ayudamos a mejorar cada día, sigue acompañándonos para que crezcamos juntos.
<br/>
<br/>
Mucho éxito, somos y seguimos siendo <font color="#DB360D"><b>Scrum LATAM Comunidad</b></font>.
<br/>
<br/>
Para seguir aprendiendo 📚 y creciendo 🚀 síguenos en nuestras redes sociales.
<br/>
👉 Calendario de actividades: https://bit.ly/EventosScrumLatam
<br/>
👉 Telegram: https://t.me/+LXuWe0Rd69FjZTBh
<br/>
👉 Instagram: https://bit.ly/3Bvsdq3
<br/>
👉 Youtube: https://bit.ly/3QX9zNH
<br/>
--
<br/>
Cordialmente,
<br/>
<br/>
Equipo de Scrum LATAM Comunidad
'''


def send_message(username, password, email_from, email_to, email_body):
    """Send a email with a attachment file using Gmail SMTP.

    Args:
        username (str): Gmail username
        password (str): Gmail password
        email_from (str): Email from
        email_to (str): Email to
        email_body (str): Email Body
    """

    # List to store files
    files = []
    dir_path = os.path.dirname(
        os.path.abspath(__file__)
    ) + os.sep + "certificates" + os.sep + "participants" + os.sep

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            files.append(dir_path + path)

    for file_name in files:
        # Open the file in binary
        pdf_file = open(file_name, 'rb')
        email_to = file_name.split("/")[-1].replace('.pdf', '')

        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = email_from
        message['To'] = email_to
        message['Subject'] = "[Scrum LATAM Comunidad] Certificado de Participación"
        message.attach(MIMEText(email_body, 'html'))

        # Read pdf name for attachment file
        attachment = MIMEApplication(pdf_file.read(),_subtype="pdf")

        # Add header with pdf name
        attachment.add_header('Content-Disposition', 'attachment', filename='ParticipantCertificate.pdf')
        message.attach(attachment)

        # Use Gmail with port
        session = smtplib.SMTP('smtp.gmail.com:587')

        # Enable security
        session.ehlo()
        session.starttls()
        session.ehlo()

        # Login with mail_id and password
        session.login(username, password)

        # Send mail
        session.sendmail(email_from, email_to, message.as_string())

        # Quit session
        session.quit()
        print('Email sent successfully to {}'.format(email_to))


if __name__ == '__main__':
    """Start the main module"""
    send_message(
        GMAIL_USERNAME,
        GMAIL_PASSWORD,
        EMAIL_FROM,
        EMAIL_TO,
        EMAIL_BODY
    )
