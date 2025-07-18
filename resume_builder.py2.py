from tkinter import *
from tkinter import filedialog, messagebox
from fpdf import FPDF
from PIL import Image, ImageTk
import os

def generate_resume():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = text_address.get("1.0", END).strip()
    skills = text_skills.get("1.0", END).strip()
    education = text_education.get("1.0", END).strip()
    experience = text_experience.get("1.0", END).strip()

    # Validation
    if not name or not email or not phone:
        messagebox.showwarning("Validation Error", "Name, Email and Phone Number are required!")
        return

    # Let user choose file save location
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    pdf = FPDF()
    pdf.add_page()

    # Add profile picture if uploaded
    if profile_pic_path:
        pdf.image(profile_pic_path, x=160, y=10, w=30)

    pdf.set_font("Arial", 'B', 20)
    pdf.cell(0, 10, name, ln=True)

    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Email: {email}", ln=True)
    pdf.cell(0, 10, f"Phone: {phone}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Address", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, address)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Skills", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, skills)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Education", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, education)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Experience", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, experience)

    pdf.output(file_path)

    messagebox.showinfo("Success", f"Resume saved to:\n{file_path}")
    os.startfile(file_path)  # auto open

def upload_photo():
    global profile_pic_path
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if path:
        profile_pic_path = path
        img = Image.open(path)
        img = img.resize((80, 80))
        img = ImageTk.PhotoImage(img)
        photo_label.config(image=img)
        photo_label.image = img

# GUI Setup
root = Tk()
root.title("Resume Builder by Keepooo")
root.geometry("400x600")
root.configure(bg="white")

Label(root, text="Resume Builder", font=("Arial", 18, "bold"), bg="white").pack(pady=10)

Button(root, text="Upload Profile Photo", command=upload_photo).pack()
photo_label = Label(root, bg="white")
photo_label.pack(pady=5)

Label(root, text="Full Name", bg="white").pack()
entry_name = Entry(root, width=40)
entry_name.pack()

Label(root, text="Email", bg="white").pack()
entry_email = Entry(root, width=40)
entry_email.pack()

Label(root, text="Phone Number", bg="white").pack()
entry_phone = Entry(root, width=40)
entry_phone.pack()

Label(root, text="Address", bg="white").pack()
text_address = Text(root, width=30, height=2)
text_address.pack()

Label(root, text="Skills", bg="white").pack()
text_skills = Text(root, width=30, height=2)
text_skills.pack()

Label(root, text="Education", bg="white").pack()
text_education = Text(root, width=30, height=2)
text_education.pack()

Label(root, text="Experience", bg="white").pack()
text_experience = Text(root, width=30, height=2)
text_experience.pack()

Button(root, text="Generate Resume", command=generate_resume, bg="lightblue").pack(pady=10)

profile_pic_path = None  # initially no picture
root.mainloop()
