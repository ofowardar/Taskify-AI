import hashlib
import uuid
from utils.json_helper import read_json,write_json

USERS_FILE = "C:/Users/Ömer Faruk Özvardar/Desktop/Taskify/data/users.json"

class UserManager:
    def __init__(self):
        self.users = read_json(USERS_FILE)

    def hash_password(self,password:str) -> str:
        """
        Cyrpt the passwd
        """
        return hashlib.md5(password.encode()).hexdigest() #Returned hashed password.
    

    def register_user(self,username:str,password:str) -> dict:
        """
        Add user to application
        """
        for user in self.users:
            if user["username"] == username:
                return {"error":"Username Already Exists!!"}
        
        new_user = {
            'id':str(uuid.uuid4()),
            'username':username,
            'password_hash':self.hash_password(password=password)
        }
        
        self.users.append(new_user)
        write_json(USERS_FILE,self.users)

        return {'message':'User registered succesfully! ' + f" Welcome to the Taskify {username}"}
    
    def login_user(self, username: str, password: str) -> list:
        """
        Login user and return [is_logined, username]
        """
        hashed_password = self.hash_password(password)
    
        for user in self.users:
            if user["username"] == username:
                if user["password_hash"] == hashed_password:
                    # Login başarılı
                    return [True, username]
                else:
                    # Şifre yanlış
                    return [False, None]
        
        # Kullanıcı bulunamadı
        return [False, None]


