from typing import List
from app.commons.dbaccess import DBAccess
from sqlalchemy.sql import text


class AuthenticationRepositry():

    # ユーザ情報登録チェック
    def checkusercd(usercd:str):

        check_user = False
        con = DBAccess.connect_database()

        query = text("SELECT count(ID) FROM MA_USER WHERE usercd = :usercd")

        try:
            countuser = con.execute(query,**{"usercd": usercd}).scalar()

            if countuser != None and countuser != 0:
                check_user = True

        except Exception as err:
            print(err)

        finally:
            con.close()

        return check_user

    #PWの取得
    def get_hashpw(usercd:str):

        con = DBAccess.connect_database()

        query = text("SELECT password FROM MA_USER WHERE usercd = :usercd")

        try:
            hash_pw = con.execute(query,**{"usercd": usercd}).scalar()

        except Exception as err:
            print(err)
        
        finally:
            con.close()
            
        return hash_pw
