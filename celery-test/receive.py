
import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='queue1')
channel.basic_publish(exchange='',routing_key='queue1',body='Hello World')
def callback(ch, method, properties, body):
	print(" [x] Received %r" % body)
channel.basic_consume(callback,queue='queue1',no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

