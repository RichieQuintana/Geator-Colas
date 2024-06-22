import pika
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Configura los detalles del correo electrónico
    from_email = 'holaquehace1209@gmail.com'
    from_password = 'vsss twnn gvbf xliy'

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Enviar el correo
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(" [x] Email sent successfully")
    except Exception as e:
        print(f" [x] Failed to send email: {e}")

def callback(ch, method, properties, body):
    message = body.decode()
    print(f" [x] Received {message}")

    # Enviar el mensaje por correo electrónico
    send_email("Nuevo mensaje de RabbitMQ", message, "destinatario@example.com")

def start_subscriber():
    # Conectar a RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar la cola
    channel.queue_declare(queue='email_queue')

    # Configurar el consumidor
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    start_subscriber()

