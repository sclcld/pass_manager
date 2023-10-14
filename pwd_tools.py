import string
import random





class pwdTools:

    def __init__(self) -> None:
        
        self.pwd_init()


    def pwd_init(self):
        self.upper = [random.choice(string.ascii_uppercase) for x in range(random.randint(2,4))]
        self.lower = [random.choice(string.ascii_lowercase) for x in range(random.randint(2,4))]
        self.digits =[random.choice(string.digits) for x in range(random.randint(2,4))]
        self.punctuation =[random.choice(string.punctuation) for x in range(random.randint(4,6))]

        

    def generate(self):
        
        self.pwd_init()
        new_pwd = self.upper + self.lower + self.digits + self.punctuation
        new_pwd.extend(["-","-","-"])
        
        for x in range(6000):
            random.shuffle(new_pwd)
        return "".join(new_pwd)
    
    def validate(self, pwd):

        has_upper = any([letter in string.ascii_uppercase for letter in pwd])
        has_lower = any([letter in string.ascii_lowercase for letter in pwd])
        has_digits = any([letter in string.digits for letter in pwd])
        has_punct = any([letter in string.punctuation for letter in pwd])
        right_lenght = 8 <= len(pwd) <= 20
        is_valid = all((has_upper,has_lower,has_digits,has_punct,right_lenght))
        
        return is_valid


            

