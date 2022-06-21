from aiokafka import AIOKafkaProducer
from aiokafka.helpers import create_ssl_context
import asyncio

async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers='enhanced-kitten-9929-eu1-kafka.upstash.io:9092',
        ssl_context=create_ssl_context(),
        sasl_mechanism='SCRAM-SHA-256',
        security_protocol='SASL_SSL',
        sasl_plain_username='<USERNAME AS STRING>',
        sasl_plain_password='<PASSWORD AS STRING>'
        )
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait("test", b"Super message")
        print("message sent")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

asyncio.run(send_one())