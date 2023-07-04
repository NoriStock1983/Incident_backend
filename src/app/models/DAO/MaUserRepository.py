
import logging
from typing import List
from app.commons.dbaccess import DBAccess
from app.models.DTO.ma_user_model import MA_USERBase
from sqlalchemy.sql import text

class MaUserRepository():
    # ma userの内容を全権取得する。
    def select_all_mauser():
        logging.info("Start select_all_mauser.")

        # DBへのアクセス
        con = DBAccess.connect_database()
        
        # List型の変数を定義する。MA＿USERのテーブルから取得したデータを格納する。
        all_mauser = List[MA_USERBase]
        # Listを初期化する。
        all_mauser = []

        # MaCodeテーブルから全権取得するQueryを作成する。
        query = text("SELECT * FROM MA_USER")
        print(query)
        logging.info(query.text)

        try:
            rows = con.execute(query)
            for row in rows:
                all_mauser.append(row)
            
        except Exception as err:
            logging.error("Error: ", err)

        finally:
            logging.info("Close DB Access.")
            DBAccess.close_connect_database(con)
            logging.info("End select_all_mauser.")

        return all_mauser
    
    # MA_CODEの内容をIDで取得する。
    def select_by_mauser_cd(usercd: str):
        logging.info("Start select_all_macode.")
        # DBへのアクセス
        con = DBAccess.connect_database()
        # 取得したデータを格納する変数を定義する。
        macode = List[MA_USERBase]
        macode = []


        query = text("SELECT * FROM MA_CODE WHERE code_1 = :codecd")
        logging.info(query.text)

        try:
            rows = con.execute(query, usercd=usercd)

            for row in rows:
                macode.append(row)
            
        except Exception as err:
            logging.error("Error: ", err)

        finally:
            logging.info("Close DB Access.")
            DBAccess.close_connect_database(con)
            logging.info("End select_all_macode.")
        
        return macode
        