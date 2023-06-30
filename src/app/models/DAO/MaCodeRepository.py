
from typing import List
from app.commons.dbaccess import DBAccess
from app.models.DTO.ma_code_model import MA_CODEBase
from sqlalchemy.sql import text
import logging

class MaCodeRepository():
    # MA_CODEの内容を全権取得する。
    def select_all_macode():
        logging.info("Start select_all_macode.")

        # DBへのアクセス
        con = DBAccess.connect_database()
        # List型の変数を定義する。MA＿CODEのテーブルから取得したデータを格納する。
        all_macode = List[MA_CODEBase]
        # Listを初期化する。
        all_macode = []
        
        # MaCodeテーブルから全権取得するQueryを作成する。
        query = text("SELECT * FROM MA_CODE")
        print(query)
        logging.info(query.text)

        try:
            rows = con.execute(query)
            for row in rows:
                all_macode.append(row)
            
        except Exception as err:
            logging.error("Error: ", err)

        finally:
            logging.info("Close DB Access.")
            DBAccess.close_connect_database(con)
            logging.info("End select_all_macode.")

        return all_macode
    

    # MA_CODEの内容をIDで取得する。
    def select_by_macode_id(id:int):
        logging.info("Start select_all_macode.")
        # DBへのアクセス
        con = DBAccess.connect_database()
        # 取得したデータを格納する変数を定義する。
        macode = List[MA_CODEBase]
        macode = []


        query = text("SELECT * FROM MA_CODE WHERE ID = :codeid")
        logging.info(query.text)

        try:
            rows = con.execute(query, codeid=id)

            for row in rows:
                macode.append(row)
            
        except Exception as err:
            logging.error("Error: ", err)

        finally:
            logging.info("Close DB Access.")
            DBAccess.close_connect_database(con)
            logging.info("End select_all_macode.")
        
        return macode
        

    # MA_CODEの内容をIDで取得する。
    def select_by_macode_cd(codecd: str):
        logging.info("Start select_all_macode.")
        # DBへのアクセス
        con = DBAccess.connect_database()
        # 取得したデータを格納する変数を定義する。
        macode = List[MA_CODEBase]
        macode = []


        query = text("SELECT * FROM MA_CODE WHERE code_1 = :codecd")
        logging.info(query.text)

        try:
            rows = con.execute(query, codecd=codecd)

            for row in rows:
                macode.append(row)
            
        except Exception as err:
            logging.error("Error: ", err)

        finally:
            logging.info("Close DB Access.")
            DBAccess.close_connect_database(con)
            logging.info("End select_all_macode.")
        
        return macode
        