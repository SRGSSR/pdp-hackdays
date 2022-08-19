# pdp-hackdays

Example code for accessing PDP API and PDP Kafka streams. 

## GraphQL API

### Prerequisites

- Python 3.x
- pip3
- https://kafka.apache.org/downloads

### Installation steps

``` python
pip3 install -r requirements.txt
```

### Run example

``` python
python3 __main__.py
```

## Kafka

### Prerequisites

- https://kafka.apache.org/downloads

### Example Consumer

Note: kafka-console-consumer.sh runs without Avro schema deserialisation. For deserialising Avro messages use Avro deserialiser https://stackoverflow.com/questions/49927747/how-to-pass-parameters-for-a-specific-schema-registry-when-using-kafka-avro-cons

```
./kafka-console-consumer.sh --bootstrap-server kafka.pdp.production.srgssr.ch:9095 --consumer.config ./kafka.consumer.properties --topic t-ebucore-programme-v14
```

### Schema Registry

- User: admin
- Password: Pdp-Test1

### Available Topics

- t-ebucore-programme-v14
- t-ebucore-document-v14
- t-ebucore-items-v14
