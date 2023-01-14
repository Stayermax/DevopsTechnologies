from connectors.postgres_connector import PostgresConnector
import yaml
if __name__ == '__main__':
    with open('configs/db_configs.yml', 'r') as file:
        db_configuration = yaml.safe_load(file)['twitter_db']
    pg_connector = PostgresConnector(db_configuration)