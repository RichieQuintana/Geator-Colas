import pika

def send_message(message):
    # Conectar a RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar una cola
    channel.queue_declare(queue='email_queue')

    # Enviar el mensaje
    channel.basic_publish(exchange='', routing_key='email_queue', body=message)
    print(f" [x] Sent '{message}'")

    # Cerrar la conexión
    connection.close()

if __name__ == "__main__":
    send_message('Hola, este es un mensaje de prueba para enviar por correo electrónico.')