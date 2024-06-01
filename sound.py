import sounddevice
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
from tkinter.filedialog import askdirectory
add = ""

def file_path():
    global add
    add = askdirectory()
    print(add)
def save_file():
    global add
    try:
        time = int(sec.get())
        addr = add+"/"+"sound.wav"
        showinfo(title="start recording", message="Recording Started")
        recording = sounddevice.rec((time * 44100), samplerate=44100, channels=2)
        sounddevice.wait()
        write("sound.wav", 44100, recording)
        showinfo(title="End", message="Recording Stopped")
    except:
        showwarning(title="Time", message="Wrong Time Format")
def main_window():
    global sec
    win = Tk()
    win.geometry("500x600")
    win.resizable(False, False)
    win.title("CiperByte tech")
    win.config(bg="#87CEEB")

    img1 = PhotoImage(file="sound-1837425_1280.png")
    l1 = Label(win, image=img1)
    l1.place(x=50, y=20, height=200, width=400)

    sec = Entry(win, font=(20))
    sec.place(x=150, y=230, height=50, width=200)

    l2 = Label(win, text="Enter time in seconds", font=("Sans Serif", 15))
    l2.place(x=100, y=290, height=50, width=300)

    b = Button(win, text="Click here to choose path for your audio file", font=("Sans Serif", 15), command=file_path)
    b.place(x=50, y=350, height=50, width=400)
    #img2 = PhotoImage(file="podcast-7858222_1280.png")
    #start = Button(win, image=img2, command=save_file)
    b1 = Button(win, text="Click here to Start Recording", font=("Sans Serif", 15), command=save_file)
    b1.place(x=100, y=400, height=50, width=300)


    win.mainloop()

main_window()


