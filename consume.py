import pika
import json

def on_message(channel, method_frame, header_frame, body):
    message = json.loads(body)
    # Perform your action here
    print("Received message:", message)

    # Acknowledge the message
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

def main():
    # RabbitMQ server connection parameters
    credentials = pika.PlainCredentials('username', 'password')
    parameters = pika.ConnectionParameters('your.rabbitmq.server', 5672, '/', credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Set up the queue
    queue_name = 'your_queue_name'
    channel.queue_declare(queue=queue_name, durable=True)

    # Consume messages
    channel.basic_consume(queue=queue_name, on_message_callback=on_message)

    print("Waiting for messages. To exit press CTRL+C")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()

if __name__ == '__main__':
    main()
