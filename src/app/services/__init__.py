from passlib.context import CryptContext

pwd_context = CryptContext(schemas=["bcrypt"],deprecated="auto")
