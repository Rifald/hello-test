import os
import tkinter as tk
import requests
import git

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
with open(dir_path+'\\version.txt') as f:
    currentVersion = f.read()
import requests
r = requests.get('https://raw.githubusercontent.com/Rifald/hello-test/main/version.txt')
data = r.text

def hello ():  
    label1 = tk.Label(root, text= 'Hello World! ' +currentVersion+ '\n' + check, fg='blue', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)

if (data == currentVersion):
    check =  "App is up to date!"
    root= tk.Tk()


    canvas1 = tk.Canvas(root, width = 300, height = 300)
    canvas1.pack()
        
    button1 = tk.Button(text='Click Me', command=hello, bg='brown',fg='white')
    canvas1.create_window(150, 150, window=button1)

    root.mainloop()
else:
    os.rename(dir_path+"\\hello_test.exe",dir_path+"\\hello_test.exe.tmp")
    # Instantiate repo object
    r = requests.get('https://github.com/Rifald/hello-test/raw/main/hello_test.exe', allow_redirects=True).content
    open(dir_path+'\\hello_test.exe', 'wb').write(r)


