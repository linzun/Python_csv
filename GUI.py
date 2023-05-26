# -*- coding = utf-8 -*-
# @Time :  2023/4/14/0014 
# @Author : HeyBro
# @File : GUI.py
# @Software : PyCharm


import tkinter as tk
from tkinter import filedialog


class MyWindow:

    def __init__(self, master):
        self.master = master
        master.title("全自动数据处理Ver1.0")
        master.geometry('800x300')

        # Creating the folder selection button
        self.folder_button = tk.Button(master, text="选择文件夹", command=self.select_folder)
        self.folder_button.pack()

        # Creating the four input fields
        tk.Label(master, text="高斯模糊指数（0-2，推荐0.7-1.5）：").pack()
        self.input_field_1 = tk.Entry(master)
        self.input_field_1.pack()

        tk.Label(master, text="最小值范围（推荐0.21）：").pack()
        self.input_field_2 = tk.Entry(master)
        self.input_field_2.pack()

        tk.Label(master, text="最大值范围（推荐0.98）：").pack()
        self.input_field_3 = tk.Entry(master)
        self.input_field_3.pack()

        tk.Label(master, text="Input Field 4:").pack()
        self.input_field_4 = tk.Entry(master)
        self.input_field_4.pack()

        # Creating the confirm execution button and exit button
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack(side=tk.RIGHT, padx=10, pady=10)


        self.confirm_button = tk.Button(master, text="Confirm", command=self.confirm)
        self.confirm_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def select_folder(self):
        # Function to open a folder selection dialog box
        folder_path = filedialog.askdirectory()
        return folder_path

    def confirm(self):
        # Function to execute the confirmed action
        input_1 = self.input_field_1.get()
        input_2 = self.input_field_2.get()
        input_3 = self.input_field_3.get()
        input_4 = self.input_field_4.get()
        a = input_1
        b = input_2
        c = input_3
        d = input_4
        return a,b,c,d

# Creating the main window
root = tk.Tk()
my_window = MyWindow(root)
root.mainloop()
