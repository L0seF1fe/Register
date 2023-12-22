import time
print(" ")
print(" ")
print(" ")
print(r"          /$$$$$$            /$$                       /$$     /$$           /$$")
print(r"         /$$__  $$          | $$                      | $$    |__/          | $$")
print(r"        | $$  \__/  /$$$$$$ | $$  /$$$$$$   /$$$$$$$ /$$$$$$   /$$  /$$$$$$ | $$")
print(r"        | $$       /$$__  $$| $$ /$$__  $$ /$$_____/|_  $$_/  | $$ |____  $$| $$")
print(r"        | $$      | $$$$$$$$| $$| $$$$$$$$|  $$$$$$   | $$    | $$  /$$$$$$$| $$")
print(r"        | $$    $$| $$_____/| $$| $$_____/ \____  $$  | $$ /$$| $$ /$$__  $$| $$")
print(r"        |  $$$$$$/|  $$$$$$$| $$|  $$$$$$$ /$$$$$$$/  |  $$$$/| $$|  $$$$$$$| $$")
print(r"         \______/  \_______/|__/ \_______/|_______/    \___/  |__/ \_______/|__/)")
Login = str(input("Enter your Nickname: "))
Password = int(input("Enter your Password: "))
File_location = r"C:\Users\User\Desktop\Register\Register-and-Login\NamePassword.txt"
class Pattern_Register:
    Login: list
    Password: list
    File_location = str

    def __init__(self, Login: str, Password: int, File_location: str):
        self.Login = Login
        self.Password = Password
        self.File_location = File_location

    def entering_data(self, Login: str, Password: int, File_location: str):
        try:
            with open(self.File_location, 'a') as data_file:
                data_file.write(f"{self.Login}:{self.Password}\n")
                data_file.close()
        except Exception:
            print("Аккаунт не Зарегистрироване по неизвестной ошибке")
            time.sleep(5)
            quit()
        print("Аккаунт успешно создан")
        time.sleep(5)
        quit()

Register = Pattern_Register(Login, Password, File_location)
Register.entering_data(Login, Password, File_location)