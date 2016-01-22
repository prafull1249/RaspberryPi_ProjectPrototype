import pika 
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='queue1')
channel.basic_publish(exchange='',routing_key='hello',body='Hello World')
print('sent hello world')
connection.close()

