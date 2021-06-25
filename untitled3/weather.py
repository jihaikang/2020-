from tkinter import *
import requests
import json



class Weather:
    def _init_(self):
        self.root = Tk()
        self.root.geometry("500*300")
        self.root.wm_title("Weather Teller")
        self.label = Label(self.root,text = "city")
        self.label.pack()
        self.entrytext = StringVar()
        Entry(self.root,textvariable = self.entrytext).pack()
        self.buttontext = StringVar()
        self.buttontext.set('Tell me')
        Button(self.root,textvariable = self.buttontext,command =self.click).pack()
        self.label = Label(self.root,text = "")
        self.label.pack()
        self.root.mainloop()

    def click(self):
        input = str(self.entrytext.get())
        location = str(input)
        r = requests.get('***api.openweathermap/data/2.5/weather?q=' + location + '&APPID = c8b38acfc161132a0da1574bc472e74e')
        j = json.loads(r.text)
        temperature = str(j['main']['temp']- 273) + 'C'
        result = temperature
        self.label.configure(text = result)



def main():
    Weather()


if __name__ == '__main__':
    main()