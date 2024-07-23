from FoodApp import User

class UserManager:
    __Users=[]

    @classmethod
    def AddUser(cls,user):
        if isinstance(user,User):
            cls.__Users.append(user)
            print("you have been successfully registered")
        else:
            print("invalid user")

    @classmethod
    def FindUser(cls,mail,password):
        for user in cls.__Users:
          if user.Mail==mail and user.Password==password:
              return user


