from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

def open_main_window():
    landing_page.destroy()  # Menutup jendela landing page
    show_main_window()  # Memunculkan jendela utama

def show_main_window():
    hunians = []
    hunians.append(Apartemen("Nelly Joy", 3, 3,"Kampung Durian Runtuh", r'assets\apart.jpg'))
    hunians.append(Rumah("Sekar MK", 5, 2, "Kampung Kelapa Tumbang", r'assets\rumah1.jpg'))
    hunians.append(Indekos("Bp. Romi", "Cahya", "Kampung Kelapa Tumbang", r'assets\kosan.jpg'))
    hunians.append(Rumah("Satria", 1, 4, "Kampung Kelapa Tumbang", r'assets\rumah2.jpg'))

    root = Tk()
    root.title("Praktikum DPBO Python")

    def details(index):
        top = Toplevel()
        top.title("Detail " + hunians[index].get_jenis())
        # tampilkan image
        img_detail = ImageTk.PhotoImage((Image.open(hunians[index].get_foto())).resize((300, 200)))
        image_label = Label(top)
        image_label.image = img_detail
        image_label.configure(image=img_detail)
        image_label.pack()
        
        d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
        d_frame.pack(padx=10, pady=10)

        d_summary = Label(d_frame, text="Summary: " +"\n" +hunians[index].get_summary() + hunians[index].get_detail(), anchor="w").grid(row=0, column=0, sticky="w")

    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type_label = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type_label.grid(row=index, column=1)

        if h.get_jenis() != "Indekos":
            name_label = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name_label.grid(row=index, column=2)
        else:
            name_label = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name_label.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

    root.mainloop()

# Landing Page
landing_page = Tk()
landing_page.title("Welcome")
landing_page.iconbitmap(r'assets\halal.ico')
my_img=ImageTk.PhotoImage(Image.open(r'assets\wellcome_jat.jpg'))
my_label=Label(image=my_img)
my_label.pack()
welcome_label = Label(landing_page, text="Welcome to LP 9 DPBO Python GUI")
welcome_label.pack(padx=50, pady=50)
start_button = Button(landing_page, text="Start", command=open_main_window)
start_button.pack()


landing_page.mainloop()
