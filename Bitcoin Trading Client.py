############################
#Computer Science Coursework
#Emmanuel Learmount
#19/11/2018
#FINAL COPY
############################

#Imports
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.dates as mdates
from matplotlib import pyplot as plt
from matplotlib import gridspec

import tkinter as tk
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from tkinter.colorchooser import askcolor

import urllib
import urllib.request
import json

import pandas as pd
import numpy as np

import datetime
import os
import time as t
from PIL import ImageTk, Image
import requests

global theme
global colour

theme = int(1)
matplotlib.use("TkAgg")
currency = 0
currency_string = "USD"
title = "0"
colour = "#338DFF"
graph_run = True

LARGE_FONT=("Bebas Neue", 25)
NORMAL_FONT=("Bahnschrift Condensed", 14)

LABEL_FONT = {'family' : 'Sans',
        'weight' : 'bold',
        'size'   : 9}

def retry_connection():
    app.destroy()
    establish_connection()

def establish_connection():
    global app
    try:   
            dataLinkCC = 'http://www.apilayer.net/api/live?access_key=a159b585fb8716f9d3ad837e18beeb10&format=1'
            CCdata = urllib.request.urlopen(dataLinkCC)
            CCdata = urllib.request.urlopen(dataLinkCC)
            CCdata = CCdata.read().decode("utf-8")
            CCdata = json.loads(CCdata)
            CCdata = pd.DataFrame(CCdata)
            CCdata = (CCdata.iloc[7])
            CCdata = (CCdata.iloc[5])
            CCdata = float(CCdata)
            app = Main()
            app.geometry("1180x670")
            ani = animation.FuncAnimation(f, animate, interval=10000)
            app.mainloop()
    except:
        app = Tk()
        app.geometry("1180x670")
        app.wm_title("No Connection")
        title = ttk.Label(app, text="No Connection", font=LARGE_FONT)
        title.place(x=500,y=200)
        no_connection = ttk.Label(app, text="We were unable to establish a connection between the API and the client. This may be due to lack of internet connection, depleated API requests or otherwise. Retry, or contact a client administrator.", font=NORMAL_FONT, wraplength=500, justify=CENTER)
        no_connection.place(x=330,y=250)
        retry = ttk.Button(app, text="Retry", command=retry_connection)
        retry.place(x=500,y=350)
        _exit = ttk.Button(app, text="Exit", command=exit)
        _exit.place(x=580,y=350)
        sys_limits = ttk.Label(app, text="*Due to API limitations connection will be lost if 1,000 currency conversion requests are exceeded each month. To prevent this, Either re-define the currency conversion API or wait until the requests reset at the beggining of each month.", font=NORMAL_FONT, wraplength=500)
        sys_limits.place(x=10,y=570)
        app.mainloop()
        

if not os.path.exists('Saved Graphs'):
    os.mkdir('Saved Graphs')

if not os.path.exists('Exported Data'):
    os.mkdir('Exported Data')

if not os.path.exists('Config'):
    os.mkdir('Config')

if not os.path.exists('Config\\BTC.ico'):
    try:
        img = urllib.request.urlretrieve('https://i.imgur.com/2Q7jO1Z.png',
                                    os.getcwd()+'\\Config\\BTC.png')
        filename = os.getcwd()+'\\Config\\BTC.png'
        img = Image.open(filename)
        img.save(os.getcwd()+'\\Config\\BTC.ico')
        os.remove(os.getcwd()+'\\Config\\BTC.png')
    except:
        pass

if not os.path.exists('Config\\help.ico'):
    try:
        img = urllib.request.urlretrieve('https://i.imgur.com/grQElfW.png',
                                    os.getcwd()+'\\Config\\help.png')
        filename = os.getcwd()+'\\Config\\help.png'
        img = Image.open(filename)
        img.save(os.getcwd()+'\\Config\\help.ico')
        os.remove(os.getcwd()+'\\Config\\help.png')
    except:
        pass


if not os.path.exists('Config\\settings.ico'):
    try:
        img = urllib.request.urlretrieve('https://i.imgur.com/t2coJPn.png',
                                    os.getcwd()+'\\Config\\settings.png')
        filename = os.getcwd()+'\\Config\\settings.png'
        img = Image.open(filename)
        img.save(os.getcwd()+'\\Config\\settings.ico')
        os.remove(os.getcwd()+'\\Config\\settings.png')
    except:
        pass

if not os.path.exists('Config\\bitcoin.png'):
    try:
        img = urllib.request.urlretrieve('https://i.imgur.com/RlwRLHC.png',
                                    os.getcwd()+'\\Config\\bitcoin.png')
        filename = os.getcwd()+'\\Config\\bitcoin.png'
    except:
        pass

if not os.path.exists('Config\\EULA.txt'):
    try:
        paste_data = 'https://pastebin.com/raw/jA869F2W'
        r = requests.get(paste_data)
        content = r.text
        content = str(content)
        open(os.getcwd()+"\\Config\\EULA.txt","w+").write(content)
    except:
        pass 

if not os.path.exists('Config\\about.txt'):
    try:
        paste_data = 'https://pastebin.com/raw/WBEASu2y'
        r = requests.get(paste_data)
        content = r.text
        content = str(content)
        open(os.getcwd()+"\\Config\\about.txt","w+").write(content)
    except:
        pass

if not os.path.exists('Config\\Position_Config.txt'):
    open(os.getcwd()+"\\Config\\Position_Config.txt","w+")

style.use("ggplot")
gs0 = gridspec.GridSpec(3, 3)
gs0.update(left=0.07, right=0.98, hspace=0.1)
gs1 = gridspec.GridSpec(3, 3)
gs1.update(left=0.07, right=1.4765, hspace=0.1)

f = plt.figure()
matplotlib.pyplot.subplots_adjust(left=0.12, bottom=0.14, right=0.90, top=0.91, wspace=0.20, hspace=0.20)
a = f.add_subplot(gs0[:-1, :])
b = f.add_subplot(gs1[-1, :-1])
a.xaxis.label.set_color('blue')
a.yaxis.label.set_color('blue')
a.set_facecolor('gainsboro')
b.set_facecolor('gainsboro')
      
def get_data():
    try:
        dataLinkBTC = 'https://api.btcmarkets.net/market/BTC/AUD/trades'
        dataLinkCC = 'http://www.apilayer.net/api/live?access_key=a159b585fb8716f9d3ad837e18beeb10&format=1'

        global CCdata
        global BTCdata
        
        CCdata = urllib.request.urlopen(dataLinkCC)
        CCdata = CCdata.read().decode("utf-8")
        CCdata = json.loads(CCdata)
        CCdata = pd.DataFrame(CCdata)
        CCdata = (CCdata.iloc[7])
        CCdata = (CCdata.iloc[5])
        CCdata = float(CCdata)

        BTCdata = urllib.request.urlopen(dataLinkBTC)
        BTCdata = BTCdata.read().decode("utf-8")
        BTCdata = json.loads(BTCdata)
        BTCdata = pd.DataFrame(BTCdata)
    except:
        establish_connection()

def pause_resume(run):
    global graph_run

    if run == "start":
        graph_run = True
    elif run == "stop":
        graph_run = False

def theme():
    theme = tk.Tk()
    theme.geometry('235x215')
    theme.wm_title("Themes")
    tk.Tk.iconbitmap(theme, (os.getcwd()+"\\Config\\settings.ico"))
    theme_label = ttk.Label(theme, text="Themes", font=LARGE_FONT)
    theme_label.place(x=10,y=5)
    theme_colour_button = ttk.Button(theme, text="Plot Colour", width=15, command=colour_setting)
    theme_colour_button.place(x=10,y=65)
    dark_theme_button = ttk.Button(theme, text="Dark Theme", width=15, command=dark_theme)
    dark_theme_button.place(x=10,y=105)
    light_theme_button = ttk.Button(theme, text="Light Theme", width=15, command=light_theme)
    light_theme_button.place(x=10,y=145)
    
def dark_theme():
    global theme
    theme = int(0)
    f.patch.set_facecolor('black')
    a.set_facecolor('xkcd:black')
    b.set_facecolor('xkcd:black')

    a.spines['bottom'].set_color('grey')
    a.spines['top'].set_color('grey')
    a.spines['left'].set_color('grey')
    a.spines['right'].set_color('grey')

    b.spines['bottom'].set_color('grey')
    b.spines['top'].set_color('grey')
    b.spines['left'].set_color('grey')
    b.spines['right'].set_color('grey')

def light_theme():
    global theme
    theme = int(1)
    f.patch.set_facecolor('white')
    a.set_facecolor('gainsboro')
    b.set_facecolor('gainsboro')

    a.spines['bottom'].set_color('white')
    a.spines['top'].set_color('white')
    a.spines['left'].set_color('white')
    a.spines['right'].set_color('white')

    b.spines['bottom'].set_color('white')
    b.spines['top'].set_color('white')
    b.spines['left'].set_color('white')
    b.spines['right'].set_color('white')

def colour_setting():
    global colour
    try:
        colour = askcolor()
        colour = colour[1]
        change_colour(colour)
    except:
        pass
    
def change_colour(colour):
    try:
        colour = colour[1]
    except:
        pass


def save():
    savename = str(datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S"))
    filedir = (os.getcwd()+"\\Saved Graphs\\")
    matplotlib.pyplot.savefig(filedir+savename+".png")

def save_as():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".png",
                                    initialdir = "/",
                                    title="Save File",
                                    filetypes=(('PNG (*.png)', '*.png'),
                                               ('JPEG (*.jpeg)', '*.jpeg'),
                                               ('GIFF (*.giff)', '*.giff'),
                                               ('TIFF (*.tiff)', '*.tiff'),
                                               ('All Files (*.*)', '*.*'),
                                               ))
    try:
        matplotlib.pyplot.savefig(file.name)
    except:
        pass

def export(file_extension):
    get_data()
    savename = str(datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S"))
    BTCdata["price"] = BTCdata["price"]/CCdata

    x = BTCdata
    filedir = os.getcwd()+'\\Exported Data\\'
    print(filedir+savename)
    np.savetxt(filedir+savename+file_extension, x, fmt='%10.5f')

def export_as():
    get_data()
    x = BTCdata
    file = filedialog.asksaveasfile(mode='w', defaultextension=".png",
                                    initialdir = "/",
                                    title="Export File",
                                    filetypes=(('Text Documents (*.txt)', '*.txt'),
                                               ('CSV (*.csv)', '*.csv'),
                                               ('XLS (*.xls)', '*.xls'),
                                               ))
    np.savetxt(file.name, x, fmt='%10.5f')

def about():    
    _about = open(os.getcwd()+"\\Config\\about.txt","r")
    _about = _about.read()
    about_box = tk.Tk()
    about_box.geometry("520x400")
    tk.Tk.iconbitmap(about_box, (os.getcwd()+"\\Config\\help.ico"))
    about_box.title("About")
    about_label = ttk.Label(about_box, text="About", font=LARGE_FONT)
    about_label_1 = ttk.Label(about_box, text=_about, font=NORMAL_FONT, wraplength=500)
    about_label.place(x=10,y=10)
    about_label_1.place(x=10,y=60)
       
def change_currency_USD():
    global currency
    global currency_string
    currency = 0
    currency_string = 'USD'
    return currency

def change_currency_GBP():
    global currency
    global currency_string
    currency = 49
    currency_string = 'GBP'
    return currency
    
def change_currency_CAD():
    global currency
    global currency_string
    currency = 27
    currency_string = 'CAD'
    return currency

def change_currency_AUD():
    global currency
    global currency_string
    currency = 7
    currency_string = 'AUD'
    return currency

def _Trade():
    trade = Trade()
    trade.geometry("520x400")

def write_prices():
    get_data()

    currentprice = float(BTCdata["price"][499]/CCdata)
    _positions = _positions_.split('\n')
    _position = {}
    new_positions = open(os.getcwd()+"\\Config\\Position_Config.txt", "a")
            
    for x in range(0, len(open(os.getcwd()+"\\Config\\Position_Config.txt").readlines())):   
        _position["string{0}".format(x)]= _positions[x].split(' ')                           
        del _position["string{0}".format(x)][2]                                              
        _position_profit_loss = (float(currentprice)*                                        
                                    float(_position["string{0}".format(x)][1])-
                                    float(_position["string{0}".format(x)][0]))
        _position["string{0}".format(x)].insert(2, _position_profit_loss)
        open(os.getcwd()+"\\Config\\Position_Config.txt", "w").close()
        joint = ''.join(str(_position["string{0}".format(x)]))
        joint = joint.replace(",","")
        joint = joint.replace("[","")
        joint = joint.replace("'","")
        joint = joint.replace("]","")
        new_positions.write(joint+"\n")


def animate(i):
    if graph_run:
        try:
            change_colour(colour)
            
            dataLinkBTC = 'https://api.btcmarkets.net/market/BTC/AUD/trades'
            dataLinkCC = 'http://www.apilayer.net/api/live?access_key=a159b585fb8716f9d3ad837e18beeb10&format=1'

            CCdata = urllib.request.urlopen(dataLinkCC)
            CCdata = CCdata.read().decode("utf-8")
            CCdata = json.loads(CCdata)
            CCdata = pd.DataFrame(CCdata)
            CCdata = (CCdata.iloc[7])
            CCdata = (CCdata.iloc[5])
            CCdata = float(CCdata)
            
            BTCdata = urllib.request.urlopen(dataLinkBTC)
            BTCdata = BTCdata.read().decode("utf-8")
            BTCdata = json.loads(BTCdata)
            BTCdata = pd.DataFrame(BTCdata)

            price = BTCdata['price']
            volume = BTCdata['amount']
            price = price/CCdata

            if currency == 0:
                price = price
            else:
                CCdata = urllib.request.urlopen(dataLinkCC)
                CCdata = CCdata.read().decode("utf-8")
                CCdata = json.loads(CCdata)
                CCdata = pd.DataFrame(CCdata)
                CCdata = (CCdata.iloc[currency])
                CCdata = (CCdata.iloc[5])
                CCdata = float(CCdata)
                price = price*CCdata
                
            priceDate = BTCdata['date'].astype("datetime64[s]")
            volumeDate = BTCdata['date'].astype("datetime64[s]")
            
            a.clear()
            b.clear()
            a.plot_date(priceDate, price, colour, label="Price")
            a.legend(bbox_to_anchor=(0, 1.02, 1, 1.02), loc=3, ncol=2, borderaxespad=0)

            title = "Bitcoin (BTC)\nLast Price: "+str(round(BTCdata["price"][499]/CCdata))

            if theme == int(0):
                a.set_title(title, color="grey")
            else:
                a.set_title(title, color="black")
                
            a.grid(color='gray', linestyle='--', linewidth=0.5)
            b.grid(color='gray', linestyle='--', linewidth=0.5)

            for label in a.xaxis.get_ticklabels():
                label.set_rotation(45)
                
            for label in b.xaxis.get_ticklabels():
                label.set_rotation(45)

            a.set_ylabel('Price ('+currency_string+')', color=colour, **LABEL_FONT)
            b.set_ylabel('Volume', color=colour, **LABEL_FONT)
            b.set_xlabel('Time', color=colour, **LABEL_FONT)
            a.set_xticklabels([])
            
            if BTCdata["price"][498]>BTCdata["price"][499]:
                print("")
            else:
                print("")
            
            b.plot_date(volumeDate, volume, colour, label="Volume")
        except:
            establish_connection()

class Trade(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, (os.getcwd()+"\\Config\\BTC.ico"))
        tk.Tk.wm_title(self, "Trade")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (OpenPosition, BuyBTC, CurrentPositions):        
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(BuyBTC)

        if os.stat(os.getcwd()+"\\Config\\Position_Config.txt").st_size == 0:
            self.show_frame(BuyBTC)
        else:
            self.show_frame(CurrentPositions)
            
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class CurrentPositions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global var
        global lines
        var = StringVar(self)
        var.set("1")
        lines = range(0, len(open(os.getcwd()+"\\Config\\Position_Config.txt").readlines())+1)
        
        def get_value():
            global var
            var = int(var.get())
            f = open(os.getcwd()+"\\Config\\Position_Config.txt").readlines()
            del f[var-1]
            sold = open(os.getcwd()+"\\Config\\Position_Config.txt", "w")

            for x in range(0, len(f)):
                sold.write(str(f[x]))

        def re_get_value():
            global re_var
            re_var = int(re_var.get())
            f = open(os.getcwd()+"\\Config\\Position_Config.txt").readlines()
            del f[re_var-1]
            sold = open(os.getcwd()+"\\Config\\Position_Config.txt", "w")

            for x in range(0, len(f)):
                sold.write(str(f[x]))
            
        label1 = ttk.Label(self)
        label1.place(x=5,y=5)
        
        self.txt = tk.Text(label1, borderwidth=3, relief="sunken", height=10, width=50)
        self.txt.config(font=("consolas", 10), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky='se', padx=2, pady=2)
        
        scrollb = tk.Scrollbar(label1, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set
        
        self.open_position_button = ttk.Button(self, text="Open Position", width=15, command=lambda:
                                               controller.show_frame(OpenPosition))
        self.open_position_button.place(x=405,y=35)

        self.close_position_button = ttk.Button(self, text="Close Position", width=15, command=get_value)
        self.close_position_button.place(x=405,y=65)
        self.close_position_num = ttk.OptionMenu(self, var, *lines)
        self.close_position_num.place(x=405,y=95)

        def clear():
            global re_var
            global _positions_
            re_var = StringVar(self)
            re_var.set("1")
            lines = range(0, len(open(os.getcwd()+"\\Config\\Position_Config.txt").readlines())+1)

            self.close_position_num.destroy()
            self.close_position_button.destroy()
            
            self.close_position_num = ttk.OptionMenu(self, re_var, *lines)
            self.close_position_num.place(x=405,y=95)
            
            self.close_position_button = ttk.Button(self, text="Close Position", width=15, command=re_get_value)
            self.close_position_button.place(x=405,y=65)
            
            label1 = ttk.Label(self)
            label1.place(x=5,y=5)
            
            _positions_ = open(os.getcwd()+"\\Config\\Position_Config.txt", "r")
            _positions_ = _positions_.read()
            self.txt.delete('1.0', END)
            self.txt.insert(1.0, _positions_)
            write_prices()
                        
        self.refresh_button = ttk.Button(self, text="Refresh", width=15, command=clear)
        self.refresh_button.place(x=405,y=5)
                
class BuyBTC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        position_label = ttk.Label(self, text="You have no open positions", font=NORMAL_FONT)
        position_label.place(x=180,y=170)
        open_position_button = ttk.Button(self, text="+", command=lambda: controller.show_frame(OpenPosition))
        open_position_button.place(x=220,y=200)

class OpenPosition(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_data()
        BTCdata["price"] = BTCdata["price"]/CCdata
        currentprice = float(BTCdata["price"][499])

        self.btc_label = ttk.Label(self, text="Bitcoin (BTC)", font=LARGE_FONT)
        self.price_label = ttk.Label(self, text=currentprice, font=LARGE_FONT)
        self.btc_label.place(x=190,y=20)
        self.price_label.place(x=150,y=60)
        self.separator = ttk.Separator(self).place(x=0, y=110, relwidth=1)

        self.quantity_amount = tk.Scale(self, from_=0.1, to=10, resolution=0.1, orient=HORIZONTAL, command=self.get_slider)
        self.quantity_amount.place(x=250,y=120)
        self.quantity_label = ttk.Label(self, text="Quantity:", font=NORMAL_FONT)
        self.quantity_label.place(x=170,y=133)

        self.take_profit_label = ttk.Label(self, text="Take Profit:", font=NORMAL_FONT)
        self.take_profit_label.place(x=170,y=196)
        self.take_profit_amount = ttk.Entry(self, width=10)
        self.take_profit_amount.place(x=285,y=200)

        self.stop_loss_label = ttk.Label(self, text="Stop Loss:", font=NORMAL_FONT)
        self.stop_loss_label.place(x=170,y=266)
        self.stop_loss_amount = ttk.Entry(self, width=10)
        self.stop_loss_amount.place(x=285,y=270)

        self.confirm_buy = ttk.Button(self, text="Confirm Purchase", command=lambda: [self.buy(),
                                                                                      controller.show_frame
                                                                                     (CurrentPositions)])
        self.confirm_buy.place(x=200,y=320)
            
    def update_price():
        get_data()
        BTCdata["price"] = BTCdata["price"]/CCdata
        self.currentprice = float(BTCdata["price"][499])
        price_label.config(text=self.currentprice)
        self.after(1000, update_price())

    def get_slider(self, args):
        self.quantity = float(self.quantity_amount.get())

    def buy(self):
        global currentprice
        get_data()
        BTCdata["price"] = BTCdata["price"]/CCdata
        self.currentprice = float(BTCdata["price"][499])
        buyprice = float(BTCdata["price"][499])
        buyprice = str(buyprice*self.quantity)
        buyprice = buyprice+" "+str(self.quantity)+" "+"0.0"+"\n"
        f = open(os.getcwd()+"\\Config\\Position_Config.txt","a")
        f.write(buyprice)
        f.close()
        try:
            for x in range(0, len(open(os.getcwd()+"\\Config\\Position_Config.txt").readlines())):
                _position["string{0}".format(x)]= _positions[x].split(' ')
                del _position["string{0}".format(x)][2]
                _position_profit_loss = (float(currentprice)*
                                         float(_position["string{0}".format(x)][1])-
                                         float(_position["string{0}".format(x)][0]))
                _position["string{0}".format(x)].insert(2, _position_profit_loss)
                open(os.getcwd()+"\\Config\\Position_Config.txt", "w").close()
                joint = ''.join(str(_position["string{0}".format(x)]))
                joint = joint.replace(",","")
                joint = joint.replace("[","")
                joint = joint.replace("'","")
                joint = joint.replace("]","")
                new_positions.write(joint+"\n")
        except:
            pass
        

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, (os.getcwd()+"\\Config\\BTC.ico"))
        tk.Tk.wm_title(self, "Bitcoin Trading Client")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu2 = tk.Menu(filemenu, tearoff=0)
        filemenu3 = tk.Menu(filemenu, tearoff=0)
        filemenu4 = tk.Menu(filemenu, tearoff=0)
        filemenu5 = tk.Menu(filemenu, tearoff=0)
        filemenu.add_command(label="Save", accelerator="Ctrl+S", command=lambda: save())
        filemenu.add_command(label="Save As...", accelerator="Ctrl+Shift+S", command=lambda: save_as())
        filemenu.add_separator()
        filemenu.add_cascade(label="Export     ", menu=filemenu2)
        filemenu.add_cascade(label="Export As...     ", command=lambda: export_as())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", accelerator="Ctrl+X", command=exit)
        menubar.add_cascade(label="File", menu=filemenu)

        filemenu2.add_command(label="Text File", command=lambda: export(".txt"))
        filemenu2.add_command(label="CSV File", command=lambda: export(".csv"))
        filemenu2.add_command(label="Excel Spreadsheet", command=lambda: export(".xls"))


        edit = tk.Menu(menubar, tearoff=0)
        edit.add_command(label="Themes", command=theme)
        menubar.add_cascade(label="Edit", menu=edit)

        trademenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Trade", menu=trademenu)
        trademenu.add_command(label="Buy/Sell", accelerator="Ctrl+B", command=lambda: _Trade())

        currencymenu = tk.Menu(menubar, tearoff=0)
        currencymenu.add_command(label="USD", command=change_currency_USD)
        currencymenu.add_command(label="GBP", command=change_currency_GBP)
        currencymenu.add_command(label="CAD", command=change_currency_CAD)
        currencymenu.add_command(label="AUD", command=change_currency_AUD)
        menubar.add_cascade(label="Currency", menu=currencymenu)

        menubar.add_cascade(label="Pause/Resume Client", menu=filemenu5)
        filemenu5.add_command(label="Pause", command=lambda: pause_resume('stop'))
        filemenu5.add_command(label="Resume", command=lambda: pause_resume('start'))

        menubar.add_cascade(label="Help", menu=filemenu4)
        filemenu4.add_command(label="About", command=lambda: about())

        tk.Tk.config(self, menu=menubar)

            
        for F in (StartPage, BTC_Page):        
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(StartPage)

        self.bind("<Control-s>", lambda e: save())
        self.bind("<Control-x>", lambda e: tk.Tk.destroy(self))
        self.bind("<Control-b>", lambda e: _Trade())
        self.bind("<Control-Shift-KeyPress-S>", lambda e: save_as())

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        _text = open(os.getcwd()+"\\Config\\EULA.txt","r")
        _text = _text.read()
        
        label1 = ttk.Label(self)
        title = ttk.Label(self, text="Bitcoin Trading Client", font=LARGE_FONT)
        title.place(x=12,y=25)
        label1.place(x=10,y=70)

        self.txt = tk.Text(label1, borderwidth=3, relief="sunken", height=30, width=50)
        self.txt.config(font=("consolas", 10), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky='se', padx=2, pady=2)
        self.txt.insert(1.0, _text)
        
        scrollb = tk.Scrollbar(label1, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

        agree = ttk.Button(self, text="Agree",
                            command=lambda: controller.show_frame(BTC_Page))
        agree.place(x=10,y=560)

        disagree = ttk.Button(self, text="Disagree",
                            command=exit)
        disagree.place(x=100,y=560)
        
        global bitcoin_img
        global bitcoin_img_1
        global bitcoin_label
        
        bitcoin_img = Image.open(os.getcwd()+'\\Config\\bitcoin.png')
        bitcoin_img = bitcoin_img.resize((742, 564), Image.ANTIALIAS)
        bitcoin_img_1 = ImageTk.PhotoImage(bitcoin_img, master=self)
        bitcoin_label = tk.Label(self, image=bitcoin_img_1)
        bitcoin_label.image = bitcoin_img
        bitcoin_label.place(x=440,y=50)

        eula = ttk.Label(self, text="*Agreement is confirmation that you have read and acknowledged the terms and conditions. Disagreeing will terminate the program.", font=NORMAL_FONT, wraplength='450')
        eula.place(x=15,y=600)    
        
class BTC_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self) 
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

establish_connection()
