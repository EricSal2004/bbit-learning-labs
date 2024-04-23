import pika # type: ignore
import producer.producer_interface as p

class mqProducer(p):
    def __init__(self, routing_key: str, exchange_name: str):
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:

        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        connection = pika.BlockingConnection(parameters=con_params)
        # Establish Channel
        channel = connection.channel()
        # Create the exchange if not already present
        exchange = channel.exchange_declare(exchange="Exchange Name")

    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        self.channel.basic_publish(
        exchange="Exchange Name",
        routing_key="Routing Key",
        body="Message",
        )
        # Close Channel
        self.channel.close()
        self.connection.close()
        # Close Connection
    
       




    