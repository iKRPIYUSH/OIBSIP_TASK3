# BMI Calculator
import sqlite3
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BmiCalculator: 
    def _init(self, master):
         self.master = master
         self.master.title("Body Mass Index(BMI) Calculator")
         self.master.geometry("450x400")

         #Variables for user's input
         self.weight_entry_var = tk.DoubleVari()
         self.height_entry_var = tk.DoubleVari()
         self.result_var = tk.StringVari()

         # Creating and placing widgets
         self.create_gui_elements()

         # Setting up SQLite database
         self.database_connection = sqlite3.connect("Bmi_Data.db")
         self.create_database_table()

    def create_gui_elements(self):
        # Labels
         ttk.Label(self.master, text = "weight (Kg):").grid(row = 0, column = 0, padx  = 6, pady = 8)
         ttk.Label(self.master, text = "height (m):").grid(row = 1, column = 0, padx = 6, pady = 8)
         ttk.Label(self.master, text = "BMI Final Value:").grid(row = 3, column = 0, padx = 6, pady = 8)

         # Data entry widgets
         ttk.Entry(self.master, textvariable = self.weight_entry_variable).grid(row = 0, column = 1, padx = 6, pady = 8)
         ttk.Entry(self.master, textvariable = self.height_entry_variable).grid(row = 1, column = 1, padx = 6, pady = 8)

         # Claculation button
         ttk.Button(self.master, text = "Claculate BMI", command = self.calculate_Bmi).grid(row = 2, column = 0, columnspan = 2, pady = 10)

         # Result label
        ttk.Label(self.master, textvariable= self.result_var).grid(row=3, column=1, padx=10, pady=10)

        # Save button
        ttk.Button(self.master, text="Save Data", command= self.save_data).grid(row=4, column=0, columnspan=2, pady=10)

        # View Data button
        ttk.Button(self.master, text="View Data", command= self.view_data).grid(row=5, column=0, columnspan=2, pady=10)
    
    def calculate_Bmi(self):
         try :
              weight = self.weight_entry_variable.get()
              height = self.height_entry_variable.get()

              if 
              weight <= 0 or height <= 0:
              raise ValueError("Weight and Height must be positive values")
         
         bmi = weight/(height ** 2)
         result_message = f"BMI : {bmi: .3f}, {self.categorize_bmi(bmi)}"
         self.result_variable.set(result_message)

        except ValueError as error_message :
        self.result_variable.set(result_message)

    def categorize_bmi(self, bmi):
         if bmi < 18.5:
              return "Underweight"
         elif 18.5 <= bmi < 24.9 :
              return "Normal Weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def create_database_table(self):
        cursor = self.database_connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS bmi_data (id INTEGER PRIMARY KEY AUTOINCREMENT, weight REAL, height REAL, bmi REAL)"
        self.database_connection.commit()

        except Exception as Error :
        print(f"Error saving data : {error}")

    def view_data(self) :
    cursor = self.database_connection.cursor()
    cursor.execute("SELECT weight, height, bmi from bmi_data")

    data = cursor.fetchall()

    if not data:
        print("!! NO DATA AVAILABLE.")
        return

    weights = [item[0] for item in data]
    heights = [item[1] for item in data]
    bmis = [item[2] for item in data]


    # Using Matplotlib for visualizing data 
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (6, 6))
    ax1.plot(weights, label = "Weight")
    ax1.plot(heights, label = "Height")
    ax1.set_ylabel("Value")
    ax1.legend()

    ax2.plot(bmis, color = "blue, label = "BMI")
    ax2.set_xlabel("Data Entry")
    ax2.set_ylabel("BMI")
    ax2.legend()

    plt.show()

def main():
    root = tk.Tk()
    app = BodyMassIndexCalculator(root)
    root.mainloop()

if _name_ == " _main_ " :
    main()




