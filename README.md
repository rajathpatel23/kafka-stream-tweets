### Kafka-stream-tweets
The repo provides as a starting point to stream tweet with kafka streaming


#### Requirement with python3.6
- Install kakfa on your system https://kafka.apache.org/downloads
- Configure kafka to start both the zookeeper and kafka
    ```shell script
    bin/zookeeper-server-start.sh config/zookeeper.properties
    bin/kafka-server-start.sh config/server.properties
    ``` 
- Create a topic in kafka to store the results of streaming twitter for example: MSDhoni
    ```shell script
    bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic msdhoni
    ```
- Install python library to start the streaming processes with python
    ```shell script
    pip install kafka-python
    pip install python-twitter
    pip install tweepy
    ``` 
- Set the environment variable from your twitter account authorize it to access twitter
    ```shell script
    export TWEET_ACCESS_TOKEN = <access token>
    export TWEET_ACCESS_SECRET = <access secret token>
    export TWEET_CONSUMER_KEY = <consumer key/ API key>
    export TWEET_CONSUMER_SECRET = <consumer secret / API access secret token >
    ```
- Run the starter file to collect your streaming data
    ```shell script
    python tweeter_starter.py
    ```
- View the streaming logs from kafka consumer
    ```shell script
    bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic msdhoni --from-beginning
    ```