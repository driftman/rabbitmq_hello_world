import pika
connection_credentials = pika.PlainCredentials("guest", "guest")
connection_params = pika.ConnectionParameters("localhost")
connection_broker = pika.BlockingConnection(connection_params)
channel = connection_broker.channel()
channel.exchange_declare(exchange="hello-exchange", passive=False, durable=True, auto_delete=False, type="direct")
channel.queue_declare(queue="hello-queue")
channel.queue_bind(queue="hello-queue", exchange="hello-exchange", routing_key="hola")
def msg_consumer(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if body == "quit":
        channel.basic_cancel(consumer_tag="hello-consumer")
        channel.stop_consuming()
    else:
        print body
    return
channel.basic_consume(msg_consumer, queue="hello-queue", consumer_tag="hello-consumer")
channel.start_consuming()
