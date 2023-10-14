from tkinter import Tk, messagebox, Label, Frame, Button, Entry, StringVar
from tkinter.ttk import Combobox



LABELS = (("site", (0,0)),("new pwd",(1,0)), ("find", (4,0)), ("top empty label", (0,3)), ("bottom empty label", (1,3)))

ENTRIES = (("site_entry",(0,1)), ("user_pwd",(1,1)), ("random_pwd",(2,1)), ("found",(5,1)))


BUTTONS = (("generate", (2,0)), ("copy",(2,2)),("save",(3,1)), ("find",(4,2)), ("copy2",(5,2)))
BUTTONS_POSITIONS = ((2,0),(2,2),(3,1))

TEXT = "Password must contain at least 8 to 20 characters,including at least one uppercase letter, one lowercase letter, one number, and one special character."
               


class PwdManagerGui:

    def __init__(self) -> None:
        
        self.root = Tk()
        self.root.geometry("550x300")       
        self.root.resizable(False, False)
        
        self.frame = Frame(self.root)
        self.frame.configure(pady= 20, padx = 15)
        
        self.labels = {}
        self.entries = {}
        self.buttons = {}
        self.combo = Combobox(self.frame)
        
        self.frame.pack(anchor="nw")
        
        self.gui_init()
        self.style()
        self.entries_control()
        
        self.root.mainloop()
        
    
       
    def gui_init(self):
        
        for widget_list in (LABELS, ENTRIES, BUTTONS):

            for widget_position in widget_list:

                widget, position = widget_position
                row_axis, col_axis = position

                if widget_list == LABELS:

                    self.labels[widget]= Label(self.frame, pady=10,)
                    self.labels[widget].configure( text = widget)
                    self.labels[widget].grid(row = row_axis, column = col_axis)

                elif widget_list == ENTRIES:

                    self.entries[widget] = Entry(self.frame)
                    self.entries[widget].grid(row = row_axis, column = col_axis)
                
                else:

                    self.buttons[widget] = Button(self.frame, pady=10, text = widget.replace("2",""))
                    self.buttons[widget].grid(row = row_axis, column = col_axis)

        
                   

        self.combo.grid(row=4, column= 1)            

    def entries_get(self):

        entries ={"site" : self.entries["site_entry"].get(),
                 "user" : self.entries["user_pwd"].get(),
                 "random": self.entries["random_pwd"].get()}

        return entries

    
    def entries_control(self):
    
        def focus_out_entry_controller(event):

            entry = self.entries_get()

            if event.widget == self.entries["site_entry"]:
                if not entry["site"]:
                    self.labels["top empty label"].configure(text= "you must fill this field")
                else:
                    self.labels["top empty label"].configure(text= "")
            
            elif event.widget == self.entries["user_pwd"]:
                if not entry["user"]:
                    self.labels["bottom empty label"].configure(text= "choose a password")
                else:
                    self.labels["bottom empty label"].configure(text= "")
            else:
                if not entry["user"] and not entry["random_pwd"]:  
                    self.labels["bottom empty label"].configure(text= "choose a password")
                else:
                    self.labels["bottom empty label"].configure(text= "")   


        self.entries["site_entry"].bind("<FocusOut>",focus_out_entry_controller)
        self.entries["user_pwd"].bind("<FocusOut>",focus_out_entry_controller)
        self.entries["random_pwd"].bind("<FocusOut>",focus_out_entry_controller)
    
    
    
    
    def style(self):            
        
        self.labels["top empty label"].configure(text = "")
        self.labels["bottom empty label"].configure(text = "")    

        self.entries["site_entry"].focus_set()
        self.entries["random_pwd"].configure( state = "readonly")
        self.entries["found"].configure(state = "readonly")            
            


       

            






        
