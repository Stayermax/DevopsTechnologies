from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import logging
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

    def create_session(self):
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

    def run_set_of_queries_without_output(self, set_of_queries: list):
        self.create_session()
        try:
            for query in set_of_queries:
                self.session.query(text(query))
            self.commit()
        except Exception as e:
            logging.error(e)
        finally:
            self.close_session()

    def run_set_of_queries_with_output(self, set_of_queries: list):
        self.create_session()
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