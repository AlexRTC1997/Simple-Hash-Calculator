from tkinter import *
from tkinter.filedialog import askopenfilename

from md4 import md4
from md5 import md5
from sha1 import sha1
from sha256 import sha256

from utils import read_file

# === ROOT ===
root = Tk()
root.geometry('600x220')
root.title('Simple Hash Calculator')

# === FRAME ===
values_frame = Frame(root, pady=20)
buttons_frame = Frame(root)

# === PLAIN TEXT LABEL ===
plain_text_label = Label(
    values_frame,
    text='Plain Text: ',
    font=('JetBrains Mono', 10, 'bold'),
    padx=7,
    compound='top'
)

plain_text_label.pack(side=LEFT)

# === PLAIN TEXT INPUT ===
plain_text_entry = Entry(
    values_frame,
    font=('JetBrains Mono', 10),
    state=NORMAL,
    width=50,
)

plain_text_entry.pack()


# === DISPLAY RESULTS ===
def display_result(hash_name):
    if plain_text_entry.get():
        plain_text = plain_text_entry.get().encode('UTF-8')
    else:
        plain_text = read_file(filename).encode('UTF-8')
        plain_text_entry.insert(END, plain_text)

    if hash_name == 'MD4':
        hash_result_label.config(text=md4(plain_text))
    elif hash_name == 'MD5':
        hash_result_label.config(text=md5(plain_text))
    elif hash_name == 'SHA-1':
        hash_result_label.config(text=sha1(plain_text.decode('ascii')))
    elif hash_name == 'SHA-256':
        hash_result_label.config(text=sha256(plain_text))


# === BUTTONS ===
md4_button = Button(
    buttons_frame,
    text='MD4',
    command=lambda: display_result('MD4'),
    font=('JetBrains Mono', 10, 'bold'),
    compound='right',
    state=ACTIVE,
    cursor='hand1'
)

md5_button = Button(
    buttons_frame,
    text='MD5',
    command=lambda: display_result('MD5'),
    font=('JetBrains Mono', 10, 'bold'),
    compound='right',
    state=ACTIVE,
    cursor='hand1'
)

sha1_button = Button(
    buttons_frame,
    text='SHA-1',
    command=lambda: display_result('SHA-1'),
    font=('JetBrains Mono', 10, 'bold'),
    compound='right',
    state=ACTIVE,
    cursor='hand1'
)

sha256_button = Button(
    buttons_frame,
    text='SHA-256',
    command=lambda: display_result('SHA-256'),
    font=('JetBrains Mono', 10, 'bold'),
    compound='right',
    state=ACTIVE,
    cursor='hand1'
)

# === DISPLAY ELEMENTS ===
md4_button.pack(side=LEFT)
md5_button.pack(side=LEFT)
sha1_button.pack(side=LEFT)
sha256_button.pack(side=LEFT)

values_frame.pack()
buttons_frame.pack()

# === OUTPUT LABEL ===
hash_result_label = Label(
    root,
    text='Output will be here...',
    font=('JetBrains Mono', 10),
    padx=7,
    pady=7,
    compound='top',
)

hash_result_label.pack(pady=20)

# === FILE BUTTON ===
filename = ''


def open_file_chooser():
    try:
        global filename
        filename = askopenfilename()

        if filename:
            plain_text = read_file(filename).encode('UTF-8')
            plain_text_entry.insert(END, plain_text)
    except TclError:
        pass


open_file = Button(
    root,
    cursor='hand1',
    font=('JetBrains Mono', 10, 'bold'),
    text="Open File",
    command=open_file_chooser)
open_file.pack()

# === DISPLAY MAIN WINDOW ===
root.resizable(False, False)
root.mainloop()
