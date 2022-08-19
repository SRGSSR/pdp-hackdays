# pdp-hackdays

Example code for accessing the PDP API. 

## GraphQL API

### Prerequisites

Python version 3.X and pip3 have to be installed

### Installation steps

``` python
pip3 install -r requirements.txt
```

### Run example

``` python
python3 __main__.py
```

## Kafka

### Example Consumer

Note: kafka-console-consumer.sh runs without Avro schema deserialisation. For deserialising Avro messages please contact us on the teams channel.

```
./kafka-console-consumer.sh --bootstrap-server kafka.pdp.production.srgssr.ch:9095 --consumer.config ./kafka.consumer.properties --topic t-ebucore-programme-v14
```

### Schema Registry

User: admin
Password: Pdp-Test1

### Available Topics

- t-ebucore-programme-v14
- t-ebucore-document-v14
- t-ebucore-items-v14
