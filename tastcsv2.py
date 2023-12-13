
import tkinter as tk
import csv
from tkinter import messagebox, filedialog
# Load and convert the image


class BMIApp:
    def __init__(self, root):
        self.root = root 
        # ... (rest of your existing code)
        sex_label = tk.Label(root, text='เพศ(1or0)',fg="black",bg="pink")      #ส่วนกรอกเพศ
        sex_label.grid(row=0, column=0, padx=20, pady=10)

        self.sex_entry = tk.Entry(root,bg="lightgreen")
        self.sex_entry.grid(row=0, column=1, padx=10, pady=10)

        age_label = tk.Label(root, text='อายุ',fg="black",bg="pink")            #ส่วนกรอกอายุ
        age_label.grid(row=1, column=0, padx=10, pady=10)

        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        weight_label = tk.Label(root, text='น้ำหนัก(kg):',fg="black",bg="pink") #ส่วนกรอกน้ำหนัก
        weight_label.grid(row=2, column=0, padx=10, pady=10)

        self.weight_entry = tk.Entry(root)
        self.weight_entry.grid(row=2, column=1, padx=10, pady=10)

        height_label = tk.Label(root, text='ส่วนสูง(cm):',fg="black",bg="pink")
        height_label.grid(row=3, column=0, padx=10, pady=10)   #ส่วนกรอกส่วนสูง

        self.height_entry = tk.Entry(root)
        self.height_entry.grid(row=3, column=1, padx=10, pady=10)

        calculate_button = tk.Button(root, text='Calculate BMI', command=self.calculate_bmi, bg='red', fg='black')  # Set background color to blue and text color to white
        calculate_button.grid(row=4, column=0, columnspan=2, pady=10)


        self.bmi_label = tk.Label(root, text='BMI: ',fg="black",bg="pink")
        self.bmi_label.grid(row=5, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(root, text='')
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

        self.setup_csv_viewer_writer()

    def calculate_bmi(self):
      
        try:
            age = float(self.age_entry.get())
            sex = float(self.sex_entry.get())
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            bmi = weight / ((height / 100) ** 2)            
            self.bmi_label.config(text=f'BMI: {bmi:.2f}')
          
            if bmi < 18.5:
                self.result_label.config(text='ต่ำกว่าเกณฑ์')
                data_to_insert = f'{height},{weight},{age},{sex},ต่ำกว่าเกณฑ์\n'
                self.text_data.insert(tk.END, data_to_insert)
            elif 18.5 <= bmi < 24.9:
                self.result_label.config(text='ปกติ')
                data_to_insert = f'{height},{weight},{age},{sex},เกณฑ์ปกติ\n'
                self.text_data.insert(tk.END, data_to_insert)
            elif 25 <= bmi < 29.9:
                self.result_label.config(text='ท้วม')
                data_to_insert = f'{height},{weight},{age},{sex},ท้วม\n'
                self.text_data.insert(tk.END, data_to_insert)
            else:
                self.result_label.config(text='น้ำหนักเกิน')
                data_to_insert = f'{height},{weight},{age},{sex},น้ำหนักเกิน\n'
                self.text_data.insert(tk.END, data_to_insert)
  # Update Text Data with entered values
               

        except ValueError:
            messagebox.showerror('Error', 'กรุณาใส่ข้อมูล')

    def setup_csv_viewer_writer(self):
        self.btn_browse = tk.Button(self.root, text="เปิดตาราง", command=self.browse_file, bg='skyblue', fg='black')
        self.btn_browse.grid(row=7, column=0, pady=10)

        self.text_data = tk.Text(self.root, height=10, width=40)
        self.text_data.grid(row=8, column=0, pady=10)

        self.btn_write = tk.Button(self.root, text="บันทึก", command=self.write_csv, bg='skyblue', fg='black')
        self.btn_write.grid(row=9, column=0, pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.file_path = file_path
            self.read_csv()

    def read_csv(self):          #ส่วนอ่านไฟล์
        if hasattr(self, 'file_path'):
            with open(self.file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)

            text_content = "\n".join([",".join(row) for row in data])
            self.text_data.delete(1.0, tk.END)
            self.text_data.insert(tk.END, text_content)

    
    def write_csv(self):   #ส่วนเขียนไฟล์
        if hasattr(self, 'file_path'):
            with open(self.file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                data = [line.split(",") for line in self.text_data.get("1.0", tk.END).strip().split("\n")]
                writer.writerows(data)

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.geometry("700x600+650+100")
    root.configure(bg='#FFFFCC')  # เซ็ดสีพื่นหลัง
    root.mainloop()
