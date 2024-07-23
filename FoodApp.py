from models.User import User
from models.UserManager import UserManager
from controller.MainMenu import MainMenu


class LoginSystem:
    def Login(self):
        Mail = input("enter yor mail: ")
        Password = input("enter your password: ")
        user=UserManager.FindUser(Mail,Password)

        if user is not None:
            print("successfully logined")



           
        else:
            print("invalid email or pass ...retry")



    def Register(self):
        Name=input("enter your name: ")
        Mobile=int(input("enter your mobile: "))
        Mail=input("enter yor mail: ")
        Password=input("enter your password: ")

        user=User(Name,Mobile,Mail,Password)
        UserManager.AddUser(user)

    def Guest(self):
        pass

    def Exit(self):
        print("thank you!!")
        exit()


    def validate(self,option):
        getattr(self,option)()



class FoodApp:
    loginOptions = {1:"Login",2:"Register",3:"Guest",4:"Exit"}
    @staticmethod
    def init():
        print("Welcome to the FoodApp!!:)")
        menu = MainMenu()
        menu.Start()


        # loginSystem=LoginSystem()
        #
        # while True:
        #     for option in FoodApp.loginOptions:
        #        print(f"{option}.{FoodApp.loginOptions[option]}",end=" ")
        #     print()
        #     try:
        #         choice=int(input("Enter your Choice: "))
        #         loginSystem.validate(FoodApp.loginOptions[choice])
        #     except (ValueError,KeyError):
        #         print("invalid choice")



