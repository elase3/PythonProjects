from tkinter import *
from pytube import *
from tkinter import font
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

root = Tk()
root.geometry('600x400+400+100')
root.resizable(0, 0)
root.title('YouTube Downloader')
root.configure(bg='#252525')
root.iconbitmap('Youtube Icon (PNG240p) - Vector69Com.ico')



lbl = Label(root, text='Paste Link Here:', fg='lightgrey', bg='#252525', font='arial 14 bold')
lbl.place(relx=.5, anchor=CENTER, y=90)

def downloader():
    if link.get() == '':
        messagebox.showerror('Error', 'Please Enter The Link')
        com1.set('')
    else:
        try:
            if com1.get() == 'Video':
                url = YouTube(str(link.get()))
                lbl['text'] = "Video Downloading......"
                download_dir = filedialog.askdirectory(initialdir='path')
                download_me.set(download_dir)
                folder = download_me.get()

                lbl2 = Label(root, fg='grey', bg='#252525', wraplength=500,
                      text=url.title + ', ' + '\n\nWe Hope You Enjoy Our Program',
                      font='arial 15')
                lbl2.place(relx=.5, anchor=CENTER, y=250)
                url.streams.filter(file_extension='mp4')
                stream = url.streams.get_highest_resolution()
                stream.download(folder)
                messagebox.showinfo('Complete', 'Video Downloaded Successful')
                lbl['text'] = ""
                lbl['text'] = "Paste Link Here:"
                link.set('')
                com1.set('')
                lbl2['text'] = ""

            elif com1.get() == 'Audio':
                url = YouTube(str(link.get()))
                lbl['text'] = "Audio Downloading......"
                download_dir = filedialog.askdirectory(initialdir='path')
                download_me.set(download_dir)
                folder = download_me.get()
                lbl2 = Label(root, fg='grey', bg='#252525', wraplength=500,
                      text=url.title + ', ' + '\n\nWe Hope You Enjoy Our Program',
                      font='arial 15')
                lbl2.place(relx=.5, anchor=CENTER, y=250)

                url.streams.filter(only_audio=True)
                stream = url.streams.get_by_itag(251)
                stream.download(folder)
                messagebox.showinfo('Complete', 'Audio Downloaded Successful')
                lbl['text'] = ""
                lbl['text'] = "Paste Link Here:"
                link.set('')
                com1.set('')
                lbl2['text'] = ""

            elif link.get() == link.get() and (com1.get() != 'Video' or com1.get() != 'Audio'):
                messagebox.showinfo('Category', 'Please Choose Video Or Audio To Download')
        except:
            root.update_idletasks()
            messagebox.showerror('Error', 'Invalid link , Please Enter Correct Link')
            lbl['text'] = ""
            lbl['text'] = "Paste Link Here:"
            link.set('')
            com1.set('')


my_image = Image.open("photo1.png")
resized = my_image.resize((70, 70), Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)

my_image = ImageTk.PhotoImage(file="photo1.png")
#my_label = Label(root, image=new_pic, border=0)
#my_label.place(x=483, y=300)

def web_browser():
    webbrowser.open_new("https://www.youtube.com/")

btn2= Button(root,image=new_pic, border=0,relief='flat',bg='#252525',command=web_browser)
btn2.place(x=483, y=298)

ourfont = font.Font(family='Bahnschrift Light Condensed', size=11)

introlable = Label(root, text='Welcome To Youtube Video Downloader', width=37,
                   font=('chiller', 24, 'italic bold'), fg='#FF0000', bg='#252525')
introlable.place(relx=.5, anchor=CENTER, y=35)

link = StringVar()
download_me = StringVar()

Entry(root, insertbackground='white', selectbackground='yellow', selectforeground='black', relief=SUNKEN,
      highlightthickness=0.5, highlightbackground="lightgrey", highlightcolor="grey",
      width=90, background='#252525', foreground='lightgrey', borderwidth=2,
      textvariable=link).place(relx=.5, anchor=CENTER, y=120, height=30)


com1 = ttk.Combobox(root, values=('Video', 'Audio'), width=7, font='arial', state='readonly')
com1.place(x=120, y=340)

#btn1 = Button(root, text='Press To Download', font='arial 15 bold ', fg='white', activeforeground='red', bg='#1877f2'
 #             , padx=2, cursor="spider", command=downloader)
#btn1.place(relx=.5, anchor=CENTER, y=170)


lablmade = ttk.Label(root, text='PROGRAMMED BY ALADDIN', foreground='#a3a3a3', background='#252525', font=ourfont)
lablmade.place(x=450, y=360)

lablmade1 = Label(root, text='Video or Audio :', fg='gold1', bg='#252525', font='arial 10 bold')
lablmade1.place(x=10, y=340)


def bttn(text,bactivcol,factivecol):
    def on_entera(e):
        myButton1['background'] = '#2851A3'
        myButton1['foreground'] = 'white'

    def on_leavea(e):
        myButton1['background'] = '#1764e1'
        myButton1['foreground'] = 'white'

    myButton1 = Button(root, text=text,
                       width=18,
                       fg='white',
                       font='arial 15 bold ',
                       border=0,
                       bg='#1764e1',
                       activeforeground=factivecol,
                       activebackground= bactivcol,
                       command=downloader)

    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(relx=.5, anchor=CENTER, y=170)


bttn('Press To Download','#606770','white')

root.mainloop()
