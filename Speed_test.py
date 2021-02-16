import tkinter as tk
import speedtest
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import time


def convert(in_bit):
    in_mbps = in_bit // 1000000
    return in_mbps


def find_speed():
    try:
        t1 = time.time()
        main_button.config(text='Testing...')
        messagebox.showinfo('TESTING', 'Please Wait.....Your Results Will Pop Up')
        global st, message
        download_raw = st.download()
        upload_raw = st.upload()
        download_speed = convert(download_raw)
        upload_speed = convert(upload_raw)
        if download_speed > 30.0:
            message = 'Good Speed,You can use multiple devices streaming HD videos'
        elif download_speed > 15.0:
            message = 'Medium Speed,You can stream HD videos on a device'
        elif download_speed > 10.0:
            message = 'Low Speed, Sites May Take a While to Load'
        t2 = time.time()
        messagebox.showinfo("SPEED", f'DOWNLOAD SPEED : {download_speed} Mbps\n'
                                     f'UPLOAD SPEED : {upload_speed} Mbps\n\n'
                                     f'{message}\n\n'
                                     f'Time Taken = {t2 - t1} Seconds')

        main_button.configure(text="TEST AGAIN")

    except():
        messagebox.showerror("ERROR", "Unexpected Error occurred.Please Check if you are Connected to Internet!")


def find_ping():
    try:
        t1 = time.time()
        global st, message_ping
        ping_button.configure(text="TESTING")
        servernames = []
        st.get_servers(servernames)
        ping = st.results.ping
        t2 = time.time()
        Time = t2 - t1
        if ping < 35:
            message_ping = "Low ping! Expect No Lag"
        elif 70 > ping > 36:
            message_ping = 'Medium ping Expect Little Lag'
        elif ping > 100:
            message_ping = "High ping! Expect Lot Of Lag"
        if Time > 1 or Time < 1:
            messagebox.showinfo("PING", f'YOUR PING : {ping}\n\n'
                                        f'{message_ping}\n\n'
                                        f'Time Taken = {Time} Seconds')
        elif Time == 1:
            messagebox.showinfo("PING", f'YOUR PING : {ping}\n\n'
                                        f'{message_ping}\n\n'
                                        f'Time Taken = {Time} Seconds')
        ping_button.configure(text="TEST AGAIN")
    except():
        messagebox.showerror("ERROR", "Unexpected Error occurred.Please Check if you are Connected to Internet!")


def over():
    exit()


st = speedtest.Speedtest()
root = tk.Tk()
# main window
root.title("INTERNET SPEED TEST")
root.iconbitmap(r'speed_rnH_icon.ico')
root.geometry('400x400')
root.resizable('false','false')

Img = ImageTk.PhotoImage(Image.open("LOGODARKSMALL1.png"))
img_label = tk.Label(root, image=Img)
img_label.pack()

# find speed button
main_button = tk.Button(root, text="Test Speed", command=find_speed, width=15, height=5, borderwidth=5, relief=SOLID)
main_button.pack(side=LEFT)

# ping button
ping_button = tk.Button(root, text='Find Ping', command=find_ping, width=15, height=5, borderwidth=5, relief=SOLID)
ping_button.place(relx=0.5, rely=0.88, anchor=CENTER)

# exit button
exit_Button = tk.Button(text='EXIT', command=over, width=15, height=5, borderwidth=5, relief=SOLID)
exit_Button.pack(side=RIGHT)

root.mainloop()

