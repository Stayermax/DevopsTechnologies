from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import logging
import pandas as pd
from utils.text_colors import bcolors

class PostgresConnector:
    def __init__(self, db_details):
        print(db_details)
        self.host = db_details['host']
        self.port = db_details['port']
        self.username = db_details['username']
        self.password = db_details['password']
        self.dbname = db_details['dbname']
        self.engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(
            self.username, self.password, self.host, self.port, self.dbname
        ))
        self.SessionMaker = sessionmaker(bind=self.engine)
        self.session = self.SessionMaker()
        self.base = declarative_base()

    def start_session(self):
        self.session = self.SessionMaker()
        return self.session

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def close_session(self):
        self.session.close()

    def run_get_query(self, query: str):
        res = self.engine.execute(query).mappings().all()
        return res

    def run_query_without_output(self, query: str):
        self.engine.execute(query)

    def run_list_of_queries_without_output(self, set_of_queries: list[str]):
        self.start_session()
        try:
            for query in set_of_queries:
                self.session.query(text(query))
            self.commit()
        except Exception as e:
            logging.error(e)
        finally:
            self.close_session()

    def run_list_of_queries_with_output(self, set_of_queries: list[str]):
        self.start_session()
        res = None
        try:
            res = []
            for query in set_of_queries:
                res.append(self.session.execute(text(query)).mappings().all())
            self.commit()
        except Exception as e:
            logging.error(e)
        finally:
            self.close_session()
            return res

    def insert_df_to_table(self, df: pd.DataFrame, table_name: str):
        df.to_sql(table_name, self.engine, index=False, if_exists='replace')
        logging.info(f"Dataframe was inserted into database with name '{table_name}'")


    def append_df_to_table(self, df: pd.DataFrame, table_name: str):
        df.to_sql(table_name, self.engine, index=False, if_exists='append')
        logging.info(f"Dataframe was appended to table '{table_name}'")
    def insert_dict_into_table(self, dictionary: dict, table_name: str):
        keys = dictionary.keys()
        values = [f"'{str(dictionary[key])}'" for key in dictionary.keys()]
        query = f"INSERT INTO {table_name} ({', '.join(keys)}) VALUES ({', '.join(values)});"
        self.engine.execute(query)
        logging.info(f"Dictionary was inserted into table '{table_name}'")

    def insert_list_of_dicts_into_table(self, list_of_dicts: list[dict], table_name: str):
        self.start_session()
        try:
            for dictionary in list_of_dicts:
                keys = dictionary.keys()
                values = [f"'{str(dictionary[key])}'" for key in dictionary.keys()]
                query = f"INSERT INTO {table_name} ({', '.join(keys)}) VALUES ({', '.join(values)});"
                logging.info(f"Executing query: {query}")
                self.session.execute(query)
            self.session.commit()
            logging.info(f"List of dictionaries was inserted into table '{table_name}'")
        except Exception as e:
            logging.error(e)
        finally:
            self.close_session()

    def delete_table(self, table_name: str):
        query = f"DROP TABLE {table_name}"
        self.engine.execute(query)
        logging.info(f"Table '{table_name}' was dropped")

