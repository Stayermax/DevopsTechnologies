# DevopsTechnologies
Data Science + DevOps technologies I want to try out

## Idea

Something with tweets or reddit. 
For example we can try to find posts on reddit connected to tweets.

## Technologies list:
* Fast API
* Docker
* Kafka
* Spark
* Hadoop
* K8
* Airflow
* Postgres + PgAdmin 
* Jenkins
* Elastic search
* BigQuery
* Snowflake
* Bash

## Theoretical architecture

* Airflow creates docker containers in which we run code
* Streaming tweets using Kafka
* Streaming posts from reddit using Spark
* Use Hadoop for storing data id database on google servers.
* Use BigQuery to get data out of servers
* Fast API will be used to send requests to server with project to get posts on reddit similar to tweets.
* Hadoop to work with tweets database (maybe)
* Learn the bash to install everything automatically.
* I don't know a thing about Jenkins
* I don't know a thing about Elasticsearch

## Questions

* What is better: to use kubernetes with aws servers or my own server? Or maybe use my server as base that creates aws servers
* Maybe Ansible or Spinnaker will be used to deploy everything
