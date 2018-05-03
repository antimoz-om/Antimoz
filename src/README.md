# Main src folder

## The stack

+ Divolte - Clickstream data anlytics provider
+ Hadoop
+ Kafka -  Real time streaming data handling platform

This project is setup such that the divolte container will collect data from within the test page and send the data to the other docker containers. To find out more go [here](https://medium.com/transparent-analytics)

To launch run

    docker-compose build && docker-compose up