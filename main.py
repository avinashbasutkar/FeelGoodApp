from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob, random
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen" 

    def forgot_password(self):
        self.manager.current = "forgot_password_screen"

    def about(self):
        self.manager.current = "about_screen"

    def home_page(self, username, password):
        with open(r"C:\Users\home\Desktop\Python\Mobile App\users.json") as file:
            users = json.load(file)
        
        if username in users and users[username]['password'] == password:
            self.manager.current = "home_page_screen"
        else:
            self.ids.incorrect_credentials.text = 'Incorrect username or password.'      

class ForgotPasswordScreen(Screen):
    def login(self):
        self.manager.current = "login_screen"

class AboutScreen(Screen):
    def login(self):
        self.manager.current = "login_screen"

class SignUpScreen(Screen):
    def login(self):
        self.manager.current = "login_screen"

    def add_user(self, username, password):
        with open(r"C:\Users\home\Desktop\Python\Mobile App\users.json") as file:
            users = json.load(file)
        
        users[username] = {'username': username, 'password': password,
            'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open(r"C:\Users\home\Desktop\Python\Mobile App\users.json", 'w') as file:
            json.dump(users, file)
        
        self.manager.current = "sign_up_successful_screen"

class SignUpSuccessFulScreen(Screen):
    def login(self):
        self.manager.current = "login_screen"

class HomePageScreen(Screen):
    def logout(self):
        self.manager.current = "login_screen"

    

    def getquote(self, feel):
        feel = feel.lower()
        glob_path = Path(r"C:\Users\home\Desktop\Python\Mobile App\Quotes")
        available_feelings = [Path(pp).stem for pp in glob_path.glob("**/*.txt")]
       
        #self.ids.welcome_user.text = f"Welcome, {username}! How are you feeling today?"

        if feel in available_feelings:
            with open(fr"C:\Users\home\Desktop\Python\Mobile App\Quotes\{feel}.txt", encoding = "utf-8") as file:
                quotes = file.readlines()
            
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try any of the following: 'Sad', 'Happy' or 'Unloved'"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass            

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()