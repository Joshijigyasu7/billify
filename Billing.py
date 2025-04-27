#billing software
import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

items=[]
def data_add():
    name=entry2.get()
    price=entry3.get()
    if not name or not price:
        messagebox.showerror("error","Please Fill both the feilds")
        return
    try:
        price=float(price)
    except ValueError:
        messagebox.showerror("Error","Please Enter a valid number")
        return
    items.append((name,price))
    update()

    entry2.delete(0,tk.END)
    entry3.delete(0,tk.END)

def update():
    text_area.delete(1.0,tk.END)
    total=0
    for idx,(name,price) in enumerate(items,1):
        text_area.insert(tk.END,f"{idx}.{name}=₹{price}\n")
        total+=price
    
    pricel.config(text=f"Total --> ₹{total} ")

    
def pdf_gen():
    c=canvas.Canvas(f"{entry_name.get()}.pdf",A4)
    width, height = c._pagesize
    vert=height-40
    c.setFont("Helvetica-Bold", 16)
    c.drawString(width/2,vert,"Monthly Bill")
    vert-=20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40,vert,f"Bill For: {entry_name.get()}")
    vert-=20
    total=0
    for idx,(name,price) in enumerate(items,1):
       
        c.drawString(40,vert,f"{idx}.{name}-₹{price}")
        vert-=15
        total+=price
    c.drawString(40,vert,f"Total Payable amount-₹{total}")
    c.save()


root=tk.Tk()
root.title("Billify: Your Daily Billing Partner")
root.geometry("600x550")

tk.Label(root,text="Enter the Buyer name",font=("Arial",16)).pack(pady=10)
entry_name=tk.Entry(root,width=20,font=("Arial",14))
entry_name.pack(pady=10)

frame=tk.Frame(root)
frame.pack(pady=10)
tk.Label(frame,text="iteam name:",font=("Arial",14)).grid(row=0, column=0, padx=5)
entry2=tk.Entry(frame,width=10,font=("Arial",14))
entry2.grid(row=0, column=1, padx=5)
tk.Label(frame,text="iteam price:",font=("Arial",14)).grid(row=0, column=2, padx=5)
entry3=tk.Entry(frame,width=10,font=("Arial",14))
entry3.grid(row=0, column=3, padx=5)
button_add=tk.Button(root,text="Add data",command=data_add,bg="blue",font=("Arial",14))
button_add.pack(pady=10)
text_area=tk.Text(root,width=50,height=10,font=("Arial",12))
text_area.pack(pady=10)

pricel=tk.Label(root,text="Total --> ₹0.00 ",font=("Arial",16))
pricel.pack(pady=10)
button_gen=tk.Button(root,text="generate pdf",command=pdf_gen,bg="green",font=("Arial",14))
button_gen.pack(pady=10)
tk.mainloop()
