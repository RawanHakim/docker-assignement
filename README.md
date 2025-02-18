# docker-assignement
This demonstrates a simple producer consumerusing docker compose. The producer generates data and sends it to a specified endpoint, while the consumerretrieves this data and logs it to a file
both services are connected to the same docker network allowing themto communicate

producer: fetches data continously from an endpointannd writes it in a log file.
consumer: reads data from producer's log file and process it.
to build producer run the command : docker-compose up -d
to build consumer run the command : docker-compose logs -f consumer
