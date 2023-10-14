import pandas as pd

class fileManager:
        
    def __init__(self) -> None:
        
        self.file_init()

    def file_init(self):
        self.pwd_list = pd.read_csv("pxds.txt", sep=" ", header= None)
        self.pwd_list.columns= ("Site", "Password")
        self.sites = list(self.pwd_list["Site"])
        self.pwd = list(self.pwd_list["Password"])
        
        
    def unique_site(self, site):
        
        self.file_init()
        return site not in self.sites

    def unique_password(self, password):

        self.file_init()
        return password not in self.pwd

            
        