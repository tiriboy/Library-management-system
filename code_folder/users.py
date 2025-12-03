import random

class User:
    def __init__(self, user_name, full_name, phone_number,email):
        self.id = random.randint(100000, 999999)
        self.user_name = user_name
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email

    def get_info(self):
        return f"{self.id},{self.user_name},{self.full_name},{self.phone_number},{self.email}"

    def update_info(self,user_name=None,full_name=None,phone_number=None,email=None):
        updated=False
        if user_name:
            self.user_name = user_name
            updated = True
        if full_name:
            self.full_name = full_name
            updated = True
        if phone_number:
            self.phone_number = phone_number
            updated = True
        if email:
            self.email = email
            updated = True  
        if updated:
            print("Info updated succesfully")
            print(f"New info - > Username:{self.user_name} Full Name:{self.full_name} Phone Number:{self.phone_number} Email:{self.email}")
        else:
            print("No updates were made.")                     



    def __str__(self):
        return f"{self.id:<15} {self.user_name:<30} {self.full_name:<30} {self.phone_number:<25} {self.email:<30}"
    
    def __eq__(self,other):
        return self.id == other.id

def create_user(username, full_name, phone_number,email):
    return User(username, full_name, phone_number,email)

def delete_user(user_list, user):
    for u in user_list:
        if u == user:
            user_list.remove(u)
            return f"User : {u.user_name} has been deleted."
  
def list_users(user_list):
    for user in user_list:
        print(user)  
