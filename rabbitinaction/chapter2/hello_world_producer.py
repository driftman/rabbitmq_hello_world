import pika, sys
credentials = pika.PlainCredentials("guest", "guest")
connection_params = pika.ConnectionParameters()
connection_broker = pika.BlockingConnection(connection_params)
channel = connection_broker.channel()
channel.exchange_declare(exchange="hello-exchange", type="direct", passive=False, durable=True, auto_delete=False)
msg = sys.argv[1]
msg_properties = pika.BasicProperties()
msg_properties.content_type = "text/plain"
msg_properties.persistent = True
channel.basic_publish(exchange="hello-exchange", body=msg, properties=msg_properties, routing_key="hola")

