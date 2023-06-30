from sqlalchemy import create_engine
import logging

class DBAccess():

    def connect_database():
        logging.info("start Database Access.")
        conn = None

        try:
            engine = create_engine('postgresql://postgres:postgres@host.docker.internal:5437/Incident_DB')
            conn = engine.connect()
            print("successfulAccess.")
        except Exception as err:
            logging.error("--- Failed Database Access ---")
            logging.error(err)
            print("--- Failed Database Access ---")
            print(err)
        finally:
            print("successful Database Access.")
            
        return conn

    def close_connect_database(conn):
        logging.info("close Database Access.")

        try:
            conn.close()
            print("successfulClose.")
        except Exception as err:
            logging.error("--- Failed Database Close ---")
            logging.error(err)
            print("--- Failed Database Close ---")
            print(err)
        finally:
            print("successful Database Close.")
            