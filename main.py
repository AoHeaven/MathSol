import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import math
 
CONST_COLOR_WHITE = "#ffffff"
CONST_COLOR_BLACK = "#000000"
CONST_COLOR_ORANGE = "#ffa602"
CONST_COLOR_GREEN = "#00c000"
CONST_COLOR_BLUE = "#4da1e6"
CONST_COLOR_GREY = "#e6e6e6"
CONST_COLOR_RED = "#e7616e"
 
class CreateWindow():
    def __init__(self, title, width, height):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.resizable(False, False)
 
        pos_x = self.window.winfo_screenwidth()
        pos_y = self.window.winfo_screenheight()
        pos_x = pos_x // 2
        pos_y = pos_y // 2
        pos_x = pos_x - (width // 2)
        pos_y = pos_y - (height // 2)
 
        self.window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
 
        # Список з індексами створених віджетів
        self.list_btn = []
        self.list_cbox = []
        self.list_entry = []
        self.list_img = []
        self.list_lbl = []
        self.list_lfrm = []


    # Загальні методи
    def statusbar_config(self):
        if self.window.title() == "Площа трикутника - MathSol":
            self.list_lbl[6].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Площа прямокутника - MathSol":
            self.list_lbl[3].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Площа квадрата - MathSol":
            self.list_lbl[2].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Площа паралелограма - MathSol":
            self.list_lbl[4].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Площа ромба - MathSol":
            self.list_lbl[3].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Площа трапеції - MathSol":
            self.list_lbl[4].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Площа круга - MathSol":
            self.list_lbl[2].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Площа еліпса - MathSol":
            self.list_lbl[2].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Об'єм куба - MathSol":
            self.list_lbl[1].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Об'єм призми - MathSol":
            self.list_lbl[2].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Об'єм паралелепіпеда - MathSol":
            self.list_lbl[4].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Об'єм піраміди - MathSol":
            self.list_lbl[2].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Об'єм правильного тетраедра - MathSol":
            self.list_lbl[1].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Об'єм циліндра - MathSol":
            self.list_lbl[3].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Об'єм конуса - MathSol":
            self.list_lbl[3].config(text="", background=CONST_COLOR_GREY)
        elif self.window.title() == "Об'єм кулі - MathSol":
            self.list_lbl[1].config(text="", background=CONST_COLOR_GREY)

    def math_calc(self):
        if self.window.title() == "Площа трикутника - MathSol":
            if self.list_cbox[0].current() == 0 and self.list_cbox[1].current() == 0:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[6].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[6].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    # Звичайний трикутник - за стороною і висотою
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_result = 1 / 2 * float(num_one) * float(num_two)
                    self.list_lbl[6].config(text="Відповідь: {} сантиметрів (квадратних).".format(num_result), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 0 and self.list_cbox[1].current() == 1:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "" or self.list_entry[2].get() == "":
                    self.list_lbl[6].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0" or self.list_entry[2].get() == "0":
                    self.list_lbl[6].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                try:
                    # Звичайний трикутник - за трьома сторонами
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()
                    num_three = self.list_entry[2].get()

                    num_one = float(num_one)
                    num_two = float(num_two)
                    num_three = float(num_three)

                    num_four = 1/2*(num_one+num_two+num_three)
                    num_five = num_four-num_one
                    num_six = num_four-num_two
                    num_seven = num_four-num_three

                    num_result = math.sqrt(num_four*num_five*num_six*num_seven)
                except ValueError:
                    self.list_lbl[6].config(text="Трикутника з такими параметрами не існує.", background=CONST_COLOR_RED)
                else:
                    self.list_lbl[6].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 4)), background=CONST_COLOR_BLUE) 
            elif self.list_cbox[0].current() == 0 and self.list_cbox[1].current() == 2:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "" or self.list_entry[2].get() == "":
                    self.list_lbl[6].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0" or self.list_entry[2].get() == "0":
                    self.list_lbl[6].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    # Звичайний трикутник - за двома сторонами і кутом між ними
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()
                    num_three = self.list_entry[2].get()

                    num_one = float(num_one)
                    num_two = float(num_two)
                    num_three = float(num_three)

                    num_three = math.sin(math.radians(num_three))
                    num_three = round(num_three, 8)

                    num_result = 1/2*num_one*num_two*num_three
                    self.list_lbl[6].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 2)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 0 and self.list_cbox[1].current() == 3:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "" or self.list_entry[2].get() == "" or self.list_entry[3].get() == "":
                    self.list_lbl[6].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0" or self.list_entry[2].get() == "0" or self.list_entry[3].get() == "0":
                    self.list_lbl[6].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    # Звичайний трикутник - за трьома сторонами і радіусом ОПИСАНОГО кола
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()
                    num_three = self.list_entry[2].get()
                    num_four = self.list_entry[3].get()

                    num_one = float(num_one)
                    num_two = float(num_two)
                    num_three = float(num_three)
                    num_four = float(num_four)

                    num_result = (num_one*num_two*num_three)/(4*num_four)
                    self.list_lbl[6].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 2)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 0 and self.list_cbox[1].current() == 4:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "" or self.list_entry[2].get() == "" or self.list_entry[3].get() == "":
                    self.list_lbl[6].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0" or self.list_entry[2].get() == "0" or self.list_entry[3].get() == "0":
                    self.list_lbl[6].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    # Звичайний трикутник - за трьома сторонами і радіусом ВПИСАНОГО кола
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()
                    num_three = self.list_entry[2].get()
                    num_four = self.list_entry[3].get()

                    num_one = float(num_one)
                    num_two = float(num_two)
                    num_three = float(num_three)
                    num_four = float(num_four)

                    num_result = 1/2*(num_one+num_two+num_three)*num_four
                    self.list_lbl[6].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 2)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 1 and self.list_cbox[1].current() == 0:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[6].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[6].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    # Прямокутний трикутник - формула площі прямокутного трикутника
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_result = 1/2*num_one*num_two
                    self.list_lbl[6].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 2)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 2 and self.list_cbox[1].current() == 0:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[6].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[6].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    # Рівнобедрений трикутник - за основою та бічною стороною
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_result = 1/2*num_two*math.sqrt((num_one+1/2*num_two)*(num_one-1/2*num_two))
                    self.list_lbl[6].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 2)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 2 and self.list_cbox[1].current() == 1:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[6].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[6].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    # Рівнобедрений трикутник - за двома бічними сторонами та кутом між ними
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_two = math.sin(math.radians(num_two))
                    num_two = round(num_two, 3)

                    num_result = 1/2*num_one**2*num_two
                    self.list_lbl[6].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 4)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 2 and self.list_cbox[1].current() == 2:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "" or self.list_entry[2].get() == "":
                    self.list_lbl[6].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0" or self.list_entry[2].get() == "0":
                    self.list_lbl[6].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    # Рівнобедрений трикутник - за основою, бічною стороною та кутом при вершині
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()
                    num_three = self.list_entry[2].get()

                    num_one = float(num_one)
                    num_two = float(num_two)
                    num_three = float(num_three)

                    num_three = math.sin(math.radians(num_three))
                    num_three = round(num_three, 3)

                    num_result = 1/2*num_one*num_two*num_three
                    self.list_lbl[6].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 4)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 3 and self.list_cbox[1].current() == 0:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[6].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[6].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    # Рівносторонній трикутник - через сторону та висоту
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_result = 1/2*num_one*num_two
                    self.list_lbl[6].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 4)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 3 and self.list_cbox[1].current() == 1:
                if self.list_entry[0].get() == "":
                    self.list_lbl[6].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0":
                    self.list_lbl[6].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    # Рівносторонній трикутник - через висоту
                    num_one = self.list_entry[0].get()

                    num_one = float(num_one)

                    num_result = (math.sqrt(3)/4)*num_one**2
                    self.list_lbl[6].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 4)), background=CONST_COLOR_BLUE)
        elif self.window.title() == "Площа прямокутника - MathSol":
            if self.list_cbox[0].current() == 0:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[3].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[3].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_result = num_one*num_two
                    self.list_lbl[3].config(text="Відповідь: {} сантиметрів".format(round(num_result, 3)))
            elif self.list_cbox[0].current() == 1:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[3].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[3].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_two = math.sin(math.radians(num_two))
                    num_two = round(num_two, 4)

                    num_result = 1/2*num_one**2*num_two
                    self.list_lbl[3].config(text="Відповідь: {} сантиметрів".format(round(num_result, 3)))

            self.list_lbl[3].config(background=CONST_COLOR_BLUE)
        elif self.window.title() == "Площа квадрата - MathSol":
            if self.list_cbox[0].current() == 0:
                if self.list_entry[0].get() == "":
                    self.list_lbl[2].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0":
                    self.list_lbl[2].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()

                    num_one = float(num_one)

                    num_result = num_one**2
                    self.list_lbl[2].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 1:
                if self.list_entry[0].get() == "":
                    self.list_lbl[2].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0":
                    self.list_lbl[2].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()

                    num_one = float(num_one)

                    num_result = 1/2*num_one**2

                    self.list_lbl[2].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
        elif self.window.title() == "Площа паралелограма - MathSol":
            if self.list_cbox[0].current() == 0:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[4].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[4].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_result = num_one*num_two
                    self.list_lbl[4].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
            if self.list_cbox[0].current() == 1:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "" or self.list_entry[2].get() == "":
                    self.list_lbl[4].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0" or self.list_entry[2].get() == "0":
                    self.list_lbl[4].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()
                    num_three = self.list_entry[2].get()

                    num_one = float(num_one)
                    num_two = float(num_two)
                    num_three = float(num_three)

                    num_three = math.sin(math.radians(num_three))
                    num_three = round(num_three, 3)

                    num_result = num_one*num_two*num_three
                    self.list_lbl[4].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 2:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "" or self.list_entry[2].get() == "":
                    self.list_lbl[4].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0" or self.list_entry[2].get() == "0":
                    self.list_lbl[4].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()
                    num_three = self.list_entry[2].get()

                    num_one = float(num_one)
                    num_two = float(num_two)
                    num_three = float(num_three)

                    num_three = math.sin(math.radians(num_three))
                    num_three = round(num_three, 3)

                    num_result = 1/2*num_one*num_two*num_three

                    self.list_lbl[4].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
        elif self.window.title() == "Площа ромба - MathSol":
            if self.list_cbox[0].current() == 0:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[3].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[3].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_result = num_one*num_two
                    self.list_lbl[3].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 3)))
            elif self.list_cbox[0].current() == 1:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[3].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[3].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_two = math.sin(math.radians(num_two))
                    num_two = round(num_two, 3)

                    num_result = num_one**2*num_two
                    self.list_lbl[3].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 3)))
            elif self.list_cbox[0].current() == 2:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[3].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[3].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_result = 1/2*num_one*num_two
                    self.list_lbl[3].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 3)))

            self.list_lbl[3].config(background=CONST_COLOR_BLUE)
        elif self.window.title() == "Площа трапеції - MathSol":
            if self.list_cbox[0].current() == 0:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "" or self.list_entry[2].get() == "":
                    self.list_lbl[4].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0" or self.list_entry[2].get() == "0":
                    self.list_lbl[4].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()
                    num_three = self.list_entry[2].get()

                    num_one = float(num_one)
                    num_two = float(num_two)
                    num_three = float(num_three)

                    num_result = 1/2*(num_one+num_two)*num_three
                    self.list_lbl[4].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 3)))

            self.list_lbl[4].config(background=CONST_COLOR_BLUE)
        elif self.window.title() == "Площа круга - MathSol":
            if self.list_cbox[0].current() == 0:
                if self.list_entry[0].get() == "":
                    self.list_lbl[2].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0":
                    self.list_lbl[2].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()

                    num_one = float(num_one)

                    num_result = math.pi*num_one**2
                    self.list_lbl[2].config(text="Відповідь: {} сантиметрів (квадратних). ".format(round(num_result, 3)))
            elif self.list_cbox[0].current() == 1:
                if self.list_entry[0].get() == "":
                    self.list_lbl[2].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0":
                    self.list_lbl[2].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()

                    num_one = float(num_one)

                    num_result = 1/4*math.pi*num_one**2
                    self.list_lbl[2].config(text="Відповідь: {} сантиметрів (квадратних).".format(round(num_result, 3)))

            self.list_lbl[2].config(background=CONST_COLOR_BLUE)
        elif self.window.title() == "Площа еліпса - MathSol":
            if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                self.list_lbl[2].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
            elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                self.list_lbl[2].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
            else:
                num_one = self.list_entry[0].get()
                num_two = self.list_entry[1].get()

                num_one = float(num_one)
                num_two = float(num_two)

                num_result = math.pi*num_one*num_two
                self.list_lbl[2].config(text="Відповідь: {} сантиметрів".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
        elif self.window.title() == "Об'єм куба - MathSol":
            if self.list_entry[0].get() == "":
                self.list_lbl[1].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
            elif self.list_entry[0].get() == "0":
                self.list_lbl[1].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
            else:
                num_one = self.list_entry[0].get()

                num_one = float(num_one)

                num_result = num_one**3
                self.list_lbl[1].config(text="Відповідь: {} сантиметрів (кубічних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
        elif self.window.title() == "Об'єм призми - MathSol":
            if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                self.list_lbl[2].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
            elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                self.list_lbl[2].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
            else:
                num_one = self.list_entry[0].get()
                num_two = self.list_entry[1].get()

                num_one = float(num_one)
                num_two = float(num_two)

                num_result = num_one*num_two

                self.list_lbl[2].config(text="Відповідь: {} сантиметрів (кубічних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
        elif self.window.title() == "Об'єм паралелепіпеда - MathSol":
            if self.list_cbox[0].current() == 0:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[4].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[4].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_result = num_one*num_two
                    self.list_lbl[4].config(text="Відповідь: {} сантиметрів (кубічних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 1:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "" or self.list_entry[2].get() == "":
                    self.list_lbl[4].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0" or self.list_entry[2].get() == "0":
                    self.list_lbl[4].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()
                    num_three = self.list_entry[2].get()

                    num_one = float(num_one)
                    num_two = float(num_two)
                    num_three = float(num_three)

                    num_result = num_one*num_two*num_three
                    self.list_lbl[4].config(text="Відповідь: {} сантиметрів (кубічних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
        elif self.window.title() == "Об'єм піраміди - MathSol":
            if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                self.list_lbl[2].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
            elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                self.list_lbl[2].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
            else:
                num_one = self.list_entry[0].get()
                num_two = self.list_entry[1].get()

                num_one = float(num_one)
                num_two = float(num_two)

                num_result = 1/3*(num_one*num_two)

                self.list_lbl[2].config(text="Відповідь: {} сантиметрів (кубічних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
        elif self.window.title() == "Об'єм правильного тетраедра - MathSol":
            if self.list_entry[0].get() == "":
                self.list_lbl[1].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
            elif self.list_entry[0].get() == "0":
                self.list_lbl[1].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
            else:
                num_one = self.list_entry[0].get()

                num_one = float(num_one)

                num_result = (num_one**3*math.sqrt(2))/12

                self.list_lbl[1].config(text="Відповідь: {} сантиметрів (кубічних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
        elif self.window.title() == "Об'єм циліндра - MathSol":
            if self.list_cbox[0].current() == 0:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[3].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[3].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_result = math.pi*num_one**2*num_two
                    self.list_lbl[3].config(text="Відповідь: {} сантиметрів (кубічних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 1:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[3].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[3].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_result = num_one*num_two

                    self.list_lbl[3].config(text="Відповідь: {} сантиметрів (кубічних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
        elif self.window.title() == "Об'єм конуса - MathSol":
            if self.list_cbox[0].current() == 0:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[3].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[3].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_result = 1/3*math.pi*num_one**2*num_two
                    self.list_lbl[3].config(text="Відповідь: {} сантиметрів (кубічних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
            elif self.list_cbox[0].current() == 1:
                if self.list_entry[0].get() == "" or self.list_entry[1].get() == "":
                    self.list_lbl[3].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
                elif self.list_entry[0].get() == "0" or self.list_entry[1].get() == "0":
                    self.list_lbl[3].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
                else:
                    num_one = self.list_entry[0].get()
                    num_two = self.list_entry[1].get()

                    num_one = float(num_one)
                    num_two = float(num_two)

                    num_result = 1/3*num_one*num_two
                    self.list_lbl[3].config(text="Відповідь: {} сантиметрів (кубічних).".format(round(num_result, 3)), background=CONST_COLOR_BLUE)
        elif self.window.title() == "Об'єм кулі - MathSol":
            if self.list_entry[0].get() == "":
                self.list_lbl[1].config(text="Заповніть пусті поля", background=CONST_COLOR_ORANGE)
            elif self.list_entry[0].get() == "0":
                self.list_lbl[1].config(text="Одне з чисел не може дорівнювати 0", background=CONST_COLOR_ORANGE)
            else:
                num_one = self.list_entry[0].get()

                num_one = float(num_one)

                num_result = 4/3*math.pi*num_one**3
                self.list_lbl[1].config(text="Відповідь: {} сантиметрів".format(round(num_result, 3)), background=CONST_COLOR_BLUE)

    
    # Методи створення віджетів
    def btn_create(self, text, pos_x, pos_y, width, height):
        self.button = tk.Button(self.window, text=text)
        self.button.place(x=pos_x, y=pos_y, width=width, height=height)
        self.list_btn.append(self.button)

    def cbox_create(self, values, pos_x, pos_y, width, state):
        self.cbbox = ttk.Combobox(self.window, values=values, state=state)
        self.cbbox.place(x=pos_x, y=pos_y, width=width)
        self.list_cbox.append(self.cbbox)

    def entry_create(self, pos_x, pos_y, width):
        self.entry = tk.Entry(self.window)
        self.entry.place(x=pos_x, y=pos_y, width=width)
        self.list_entry.append(self.entry)

    def lbl_create(self, text, pos_x, pos_y, width, anchor, background):
        self.lbl = tk.Label(self.window, text=text, anchor=anchor, background=background)
        self.lbl.place(x=pos_x, y=pos_y, width=width)
        self.list_lbl.append(self.lbl)

    def lfrm_create(self, text, pos_x, pos_y, width, height):
        self.lfrm = tk.LabelFrame(self.window, text=text)
        self.lfrm.place(x=pos_x, y=pos_y, width=width, height=height)
        self.list_lfrm.append(self.lfrm)


    # Методи вікна
    def win_config(self, background):
        self.window.config(background=background)

    def win_hide(self):
        self.window.withdraw()

    def win_show(self):
        self.window.deiconify()

    def win_focus_set(self):
        self.window.focus_force()


    # Методи віджета ComboBox
    def cbox_event_triangle(self, event):
        triangle_type_formula_1 = ["За стороною і висотою",
                                    "За трьома сторонами",
                                    "За двома сторонами і кутом між ними",
                                    "За трьома сторонами і радіусом ОПИСАНОГО кола",
                                    "За трьома сторонами і радіусом ВПИСАНОГО кола"]

        triangle_type_formula_2 = ["Формула площі прямокутного трикутника"]

        triangle_type_formula_3 = ["За основою та бічною стороною",
                              "За двома бічними сторонами та кутом між ними",
                              "За основою, бічною стороною та кутом при вершині"]

        triangle_type_formula_4 = ["Через сторону та висоту", "Через сторону"]
                                    
        if self.list_cbox[0].current() == 0:
            self.list_cbox[1].config(values=triangle_type_formula_1)
        elif self.list_cbox[0].current() == 1:
            self.list_cbox[1].config(values=triangle_type_formula_2)
        elif self.list_cbox[0].current() == 2:
            self.list_cbox[1].config(values=triangle_type_formula_3)
        elif self.list_cbox[0].current() == 3:
            self.list_cbox[1].config(values=triangle_type_formula_4)

        # Label & Entry 1
        self.list_lbl[2].config(text="")
        self.list_entry[0].place_forget()
        self.list_entry[0].delete(0, tk.END)
        
        # Label & Entry 2
        self.list_lbl[3].config(text="")
        self.list_entry[1].place_forget()
        self.list_entry[1].delete(0, tk.END)

        # Label & Entry 3
        self.list_lbl[4].config(text="")
        self.list_entry[2].place_forget()
        self.list_entry[2].delete(0, tk.END)

        # Label & Entry 4
        self.list_lbl[5].config(text="")
        self.list_entry[3].place_forget()
        self.list_entry[3].delete(0, tk.END)

        # Кнопка "Обчислити"
        self.list_btn[0].place_forget()

        # Кнопка "Очистити поля"
        self.list_btn[1].place_forget()

        # Status bar
        self.list_cbox[1].set("")
        self.list_lbl[6].config(text="Оберіть формулу", background=CONST_COLOR_ORANGE)


    def cbox_action(self):
            self.list_cbox[0].bind('<<ComboboxSelected>>', self.cbox_mode_change)

    def cbox_event(self, event):
        if self.window.title() == "Площа трикутника - MathSol":
            # Status bar
            if self.list_cbox[1].current() >= 0:
                self.list_lbl[6].config(background=CONST_COLOR_GREEN, text="Формула вибрана")

                # Кнопка "Обчислити"
                self.list_btn[0].place(x=25, y=335, width=450, height=25)

                # Кнопка "Очистити поля"
                self.list_btn[1].place(x=25, y=415, width=120, height=25)

            if self.list_cbox[0].current() == 0 and self.list_cbox[1].current() == 0:
                # Звичайний трикутник - за стороною і висотою
                # Label & Entry 1
                self.list_lbl[2].config(text="Довжина сторони (см)")
                self.list_entry[0].place(x=278, y=135, width=202)
                
                # Label & Entry 2
                self.list_lbl[3].config(text="Висота (см)")
                self.list_entry[1].place(x=278, y=185, width=202)

                # Label & Entry 3
                self.list_lbl[4].config(text="")
                self.list_entry[2].place_forget()

                # Label & Entry 4
                self.list_lbl[5].config(text="")
                self.list_entry[3].place_forget()
            elif self.list_cbox[0].current() == 0 and self.list_cbox[1].current() == 1:
                # Звичайний трикутник - за трьома сторонами
                # Label & Entry 1
                self.list_lbl[2].config(text="Довжина 1-ї сторони (см)")
                self.list_entry[0].place(x=278, y=135, width=202)

                # Label & Entry 2
                self.list_lbl[3].config(text="Довжина 2-ї сторони (см)")
                self.list_entry[1].place(x=278, y=185, width=202)

                # Label & Entry 3
                self.list_lbl[4].config(text="Довжина 3-ї сторони (см)")
                self.list_entry[2].place(x=278, y=235, width=202)

                # Label & Entry 4
                self.list_lbl[5].config(text="")
                self.list_entry[3].place_forget()
            elif self.list_cbox[0].current() == 0 and self.list_cbox[1].current() == 2:
                # Звичайний трикутник - за двома сторонами і кутом між ними
                # Label & Entry 1
                self.list_lbl[2].config(text="Довжина 1-ї сторони (см)")
                self.list_entry[0].place(x=278, y=135, width=202)

                # Label & Entry 2
                self.list_lbl[3].config(text="Довжина 2-ї сторони (см)")
                self.list_entry[1].place(x=278, y=185, width=202)
                
                # Label & Entry 3
                self.list_lbl[4].config(text="Кут (у градусах)")
                self.list_entry[2].place(x=278, y=235, width=202)

                # Label & Entry 4
                self.list_lbl[5].config(text="")
                self.list_entry[3].place_forget()
            elif self.list_cbox[0].current() == 0 and self.list_cbox[1].current() == 3:
                # Звичайний трикутник - за трьома сторонами і радіусом ОПИСАНОГО кола
                # Label & Entry 1
                self.list_lbl[2].config(text="Довжина 1-ї сторони (см)")
                self.list_entry[0].place(x=278, y=135, width=202)

                # Label & Entry 2
                self.list_lbl[3].config(text="Довжина 2-ї сторони (см)")
                self.list_entry[1].place(x=278, y=185, width=202)

                # Label & Entry 3
                self.list_lbl[4].config(text="Довжина 3-ї сторони (см)")
                self.list_entry[2].place(x=278, y=235, width=202)

                # Label & Entry 4
                self.list_lbl[5].config(text="Радіус ОПИСАНОГО кола (у градусах)")
                self.list_entry[3].place(x=278, y=285, width=202)
            elif self.list_cbox[0].current() == 0 and self.list_cbox[1].current() == 4:
                # Звичайний трикутник - за трьома сторонами і радіусом ВПИСАНОГО кола
                # Label & Entry 1
                self.list_lbl[2].config(text="Довжина 1-ї сторони (см)")
                self.list_entry[0].place(x=278, y=135, width=202)

                # Label & Entry 2
                self.list_lbl[3].config(text="Довжина 2-ї сторони (см)")
                self.list_entry[1].place(x=278, y=185, width=202)

                # Label & Entry 3
                self.list_lbl[4].config(text="Довжина 3-ї сторони (см)")
                self.list_entry[2].place(x=278, y=235, width=202)
                
                # Label & Entry 4
                self.list_lbl[5].config(text="Радіус ВПИСАНОГО кола (у градусах)")
                self.list_entry[3].place(x=278, y=285, width=202)
            elif self.list_cbox[0].current() == 1 and self.list_cbox[1].current() == 0:
                # Прямокутний трикутник - формула площі прямокутного трикутника
                # Label & Entry 1
                self.list_lbl[2].config(text="Довжина 1-го катета (см)")
                self.list_entry[0].place(x=278, y=135, width=202)

                # Label & Entry 2
                self.list_lbl[3].config(text="Довжина 2-го катета (см)")
                self.list_entry[1].place(x=278, y=185, width=202)

                # Label & Entry 3
                self.list_lbl[4].config(text="")
                self.list_entry[2].place_forget()

                # Label & Entry 4
                self.list_lbl[5].config(text="")
                self.list_entry[3].place_forget()
            elif self.list_cbox[0].current() == 2 and self.list_cbox[1].current() == 0:
                # Рівнобедрений трикутник - за основою та бічною стороною
                # Label & Entry 1
                self.list_lbl[2].config(text="Довжина бічної сторони (см)")
                self.list_entry[0].place(x=278, y=135, width=202)

                # Label & Entry 2
                self.list_lbl[3].config(text="Довжина основи (см)")
                self.list_entry[1].place(x=278, y=185, width=202)

                #Label & Entry 3
                self.list_lbl[4].config(text="")
                self.list_entry[2].place_forget()

                #Label & Entry 4
                self.list_lbl[5].config(text="")
                self.list_entry[3].place_forget()
            elif self.list_cbox[0].current() == 2 and self.list_cbox[1].current() == 1:
                # Рівнобедрений трикутник - за двома бічними сторонами та кутом між ними
                # Label & Entry 1
                self.list_lbl[2].config(text="Довжина бічної сторони (см)")
                self.list_entry[0].place(x=278, y=135, width=202)

                # Label & Entry 2
                self.list_lbl[3].config(text="Кут (у градусах)")
                self.list_entry[1].place(x=278, y=185, width=202)

                #Label & Entry 3
                self.list_lbl[4].config(text="")
                self.list_entry[2].place_forget()

                #Label & Entry 4
                self.list_lbl[5].config(text="")
                self.list_entry[3].place_forget() 
            elif self.list_cbox[0].current() == 2 and self.list_cbox[1].current() == 2:
                # Рівнобедрений трикутник - за основою, бічною стороною та кутом при вершині
                # Label & Entry 1
                self.list_lbl[2].config(text="Довжина бічної сторони (см)")
                self.list_entry[0].place(x=278, y=135, width=202)

                # Label & Entry 2
                self.list_lbl[3].config(text="Довжина основи (см)")
                self.list_entry[1].place(x=278, y=185, width=202)

                #Label & Entry 3
                self.list_lbl[4].config(text="Кут (у градусах)")
                self.list_entry[2].place(x=278, y=235, width=202)

                #Label & Entry 4
                self.list_lbl[5].config(text="")
                self.list_entry[3].place_forget()  
            elif self.list_cbox[0].current() == 3 and self.list_cbox[1].current() == 0:
                # Рівносторонній трикутник - через сторону та висоту
                # Label & Entry 1
                self.list_lbl[2].config(text="Довжина сторони (см)")
                self.list_entry[0].place(x=278, y=135, width=202)

                # Label & Entry 2
                self.list_lbl[3].config(text="Висота (см)")
                self.list_entry[1].place(x=278, y=185, width=202)

                #Label & Entry 3
                self.list_lbl[4].config(text="")
                self.list_entry[2].place_forget()

                #Label & Entry 4
                self.list_lbl[5].config(text="")
                self.list_entry[3].place_forget()
            elif self.list_cbox[0].current() == 3 and self.list_cbox[1].current() == 1:
                # Рівносторонній трикутник - через висоту
                # Label & Entry 1
                self.list_lbl[2].config(text="Довжина сторони (у см)")
                self.list_entry[0].place(x=278, y=135, width=202)

                # Label & Entry 2
                self.list_lbl[3].config(text="")
                self.list_entry[1].place_forget()

                #Label & Entry 3
                self.list_lbl[4].config(text="")
                self.list_entry[2].place_forget()

                #Label & Entry 4
                self.list_lbl[5].config(text="")
                self.list_entry[3].place_forget()
        elif self.window.title() == "Площа прямокутника - MathSol":
            if self.list_cbox[0].current() == 0:
                self.list_lbl[1].config(text="Довжина сторони A (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Довжина сторони B (см)")
                self.list_entry[1].place(x=278, y=155, width=202)
            elif self.list_cbox[0].current() == 1:
                self.list_lbl[1].config(text="Довжина діагоналі (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Синус гострого кута (у градусах)")
                self.list_entry[1].place(x=278, y=155, width=202)

            self.list_btn[0].place(x=25, y=305, width=450, height=25)
            self.list_btn[1].place(x=25, y=385, width=120, height=25)
            self.list_lbl[3].config(text="Формула вибрана", background=CONST_COLOR_GREEN)
        if self.window.title() == "Площа квадрата - MathSol":
            if self.list_cbox[0].current() == 0:
                self.list_lbl[1].config(text="Довжина сторони (см)")
                self.list_entry[0].place(x=278, y=105, width=202)
            elif self.list_cbox[0].current() == 1:
                self.list_lbl[1].config(text="Довжина діагоналі (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

            self.list_btn[0].place(x=25, y=305, width=450, height=25)
            self.list_btn[1].place(x=25, y=385, width=120, height=25)
            self.list_lbl[2].config(text="Формула вибрана", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Площа паралелограма - MathSol":
            if self.list_cbox[0].current() == 0:
                self.list_lbl[1].config(text="Довжина сторони (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Висота (см)")
                self.list_entry[1].place(x=278, y=155, width=202)

                self.list_lbl[3].config(text="")
                self.list_entry[2].place_forget()
            elif self.list_cbox[0].current() == 1:
                self.list_lbl[1].config(text="Довжина 1-ї сторони (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Довжина 2-ї сторони (см)")
                self.list_entry[1].place(x=278, y=155, width=202)

                self.list_lbl[3].config(text="Кут (у градусах)")
                self.list_entry[2].place(x=278, y=205, width=202)
            elif self.list_cbox[0].current() == 2:
                self.list_lbl[1].config(text="Довжина 1-ї діагоналі (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Довжина 2-ї діагоналі (см)")
                self.list_entry[1].place(x=278, y=155, width=202)

                self.list_lbl[3].config(text="Кут (у градусах)")
                self.list_entry[2].place(x=278, y=205, width=202)
  
            self.list_btn[0].place(x=25, y=305, width=450, height=25)
            self.list_btn[1].place(x=25, y=385, width=120, height=25)

            self.list_lbl[4].config(text="Формула вибрана", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Площа ромба - MathSol":
            if self.list_cbox[0].current() == 0:
                self.list_lbl[1].config(text="Довжина сторони (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Довжина висоти (см)")
                self.list_entry[1].place(x=278, y=155, width=202)
            elif self.list_cbox[0].current() == 1:
                self.list_lbl[1].config(text="Довжина сторони (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Кут (у градусах)")
                self.list_entry[1].place(x=278, y=155, width=202)
            elif self.list_cbox[0].current() == 2:
                self.list_lbl[1].config(text="Довжина 1-ї діагоналі (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Довжина 2-ї діагоналі (см)")
                self.list_entry[1].place(x=278, y=155, width=202)

            self.list_btn[0].place(x=25, y=305, width=450, height=25)
            self.list_btn[1].place(x=25, y=385, width=120, height=25)

            self.list_lbl[3].config(text="Формула вибрана", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Площа трапеції - MathSol":
            if self.list_cbox[0].current() == 0:
                self.list_lbl[1].config(text="Довжина 1-ї основи (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Довжина 2-ї основи (см)")
                self.list_entry[1].place(x=278, y=155, width=202)

                self.list_lbl[3].config(text="Висота (см)")
                self.list_entry[2].place(x=278, y=205, width=202)

            self.list_btn[0].place(x=25, y=305, width=450, height=25)
            self.list_btn[1].place(x=25, y=385, width=120, height=25)

            self.list_lbl[4].config(text="Формула вибрана", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Площа круга - MathSol":
            if self.list_cbox[0].current() == 0:
                self.list_lbl[1].config(text="Радіус (см)")
                self.list_entry[0].place(x=278, y=105, width=202)
            elif self.list_cbox[0].current() == 1:
                self.list_lbl[1].config(text="Довжина діагоналі (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

            self.list_btn[0].place(x=25, y=305, width=450, height=25)
            self.list_btn[1].place(x=25, y=385, width=120, height=25)

            self.list_lbl[2].config(text="Формула вибрана", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Об'єм паралелепіпеда - MathSol":
            if self.list_cbox[0].current() == 0:
                self.list_lbl[1].config(text="Площа основи (см^2)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Висота (см)")
                self.list_entry[1].place(x=278, y=155, width=202)

                self.list_lbl[3].config(text="")
                self.list_entry[2].place_forget()
            if self.list_cbox[0].current() == 1:
                self.list_lbl[1].config(text="Довжина (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Ширина (см)")
                self.list_entry[1].place(x=278, y=155, width=202)

                self.list_lbl[3].config(text="Висота (см)")
                self.list_entry[2].place(x=278, y=205, width=202)

            self.list_btn[0].place(x=25, y=305, width=450, height=25)
            self.list_btn[1].place(x=25, y=385, width=120, height=25)

            self.list_lbl[4].config(text="Формула вибрана", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Об'єм циліндра - MathSol":
            if self.list_cbox[0].current() == 0:
                self.list_lbl[1].config(text="Радіус (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Висота (см)")
                self.list_entry[1].place(x=278, y=155, width=202)
            elif self.list_cbox[0].current() == 1:
                self.list_lbl[1].config(text="Площа основи (см^2)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Висота (см)")
                self.list_entry[1].place(x=278, y=155, width=202)

            self.list_btn[0].place(x=25, y=305, width=450, height=25)
            self.list_btn[1].place(x=25, y=385, width=120, height=25)

            self.list_lbl[3].config(text="Формула вибрана", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Об'єм конуса - MathSol":
            if self.list_cbox[0].current() == 0:
                self.list_lbl[1].config(text="Радіус (см)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Висота (см)")
                self.list_entry[1].place(x=278, y=155, width=202)
            elif self.list_cbox[0].current() == 1:
                self.list_lbl[1].config(text="Площа основи (см^2)")
                self.list_entry[0].place(x=278, y=105, width=202)

                self.list_lbl[2].config(text="Висота (см)")
                self.list_entry[1].place(x=278, y=155, width=202)

            self.list_btn[0].place(x=25, y=305, width=450, height=25)
            self.list_btn[1].place(x=25, y=385, width=120, height=25)

            self.list_lbl[3].config(text="Формула вибрана", background=CONST_COLOR_GREEN)
        self.window.after(2000, self.statusbar_config)


    def cbox_mode_change(self, event):
        if self.list_cbox[0].current() == 0:
            self.list_btn[0].config(text=figure_names[0])
            self.list_btn[1].config(text=figure_names[1])
            self.list_btn[2].config(text=figure_names[2])
            self.list_btn[3].config(text=figure_names[3])
            self.list_btn[4].config(text=figure_names[4])
            self.list_btn[5].config(text=figure_names[5])
            self.list_btn[6].config(text=figure_names[6])
            self.list_btn[7].config(text=figure_names[7])
        else:
            self.list_btn[0].config(text=figure_names[8])
            self.list_btn[1].config(text=figure_names[9])
            self.list_btn[2].config(text=figure_names[10])
            self.list_btn[3].config(text=figure_names[11])
            self.list_btn[4].config(text=figure_names[12])
            self.list_btn[5].config(text=figure_names[13])
            self.list_btn[6].config(text=figure_names[14])
            self.list_btn[7].config(text=figure_names[15])


    # Методи віджета LabelFrame
    def lfrm_config(self, background):
        if self.window.title() == "Площа еліпса - MathSol":
            self.list_lfrm[0].config(background=background)
            self.list_lfrm[1].config(background=background)
        elif self.window.title() == "Об'єм куба - MathSol":
            self.list_lfrm[0].config(background=background)
            self.list_lfrm[1].config(background=background)
        elif self.window.title() == "Об'єм призми - MathSol":
            self.list_lfrm[0].config(background=background)
            self.list_lfrm[1].config(background=background)
        elif self.window.title() == "Об'єм піраміди - MathSol":
            self.list_lfrm[0].config(background=background)
            self.list_lfrm[1].config(background=background)
        elif self.window.title() == "Об'єм правильного тетраедра - MathSol": 
            self.list_lfrm[0].config(background=background)
            self.list_lfrm[1].config(background=background)
        elif self.window.title() == "Об'єм кулі - MathSol": 
            self.list_lfrm[0].config(background=background)
            self.list_lfrm[1].config(background=background)
        elif self.window.title() == "Список формул - MathSol":
            self.list_lfrm[0].config(background=background)
            self.list_lfrm[1].config(background=background)
        else:
            self.list_lfrm[0].config(background=background)
            self.list_lfrm[1].config(background=background)
            self.list_lfrm[2].config(background=background)


    # Методи віджета Button
    def btn_actions(self):
        self.list_btn[0].config(command=self.btn_action_1)
        self.list_btn[1].config(command=self.btn_action_2)
        self.list_btn[2].config(command=self.btn_action_3)
        self.list_btn[3].config(command=self.btn_action_4)
        self.list_btn[4].config(command=self.btn_action_5)
        self.list_btn[5].config(command=self.btn_action_6)
        self.list_btn[6].config(command=self.btn_action_7)
        self.list_btn[7].config(command=self.btn_action_8)
        self.list_btn[11].config(command=window_main.btn_action_exit)

    def btn_clear_fields(self):
        if self.window.title() == "Площа трикутника - MathSol":
            self.list_entry[0].delete(0, tk.END)
            self.list_entry[1].delete(0, tk.END)
            self.list_entry[2].delete(0, tk.END)
            self.list_entry[3].delete(0, tk.END)

            self.list_lbl[6].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Площа прямокутника - MathSol":
            self.list_entry[0].delete(0, tk.END)
            self.list_entry[1].delete(0, tk.END)

            self.list_lbl[3].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Площа ромба - MathSol":
            self.list_entry[0].delete(0, tk.END)
            self.list_entry[1].delete(0, tk.END)

            self.list_lbl[3].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Площа квадрата - MathSol":
            self.list_entry[0].delete(0, tk.END)

            self.list_lbl[2].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Площа паралелограма - MathSol":
            self.list_entry[0].delete(0, tk.END)
            self.list_entry[1].delete(0, tk.END)
            self.list_entry[2].delete(0, tk.END)

            self.list_lbl[4].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Площа трапеції - MathSol":
            self.list_entry[0].delete(0, tk.END)
            self.list_entry[1].delete(0, tk.END)
            self.list_entry[2].delete(0, tk.END)

            self.list_lbl[4].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Площа круга - MathSol":
            self.list_entry[0].delete(0, tk.END)

            self.list_lbl[2].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Площа еліпса - MathSol":
            self.list_entry[0].delete(0, tk.END)
            self.list_entry[1].delete(0, tk.END)

            self.list_lbl[2].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Об'єм куба - MathSol":
            self.list_entry[0].delete(0, tk.END)

            self.list_lbl[1].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Об'єм призми - MathSol":
            self.list_entry[0].delete(0, tk.END)
            self.list_entry[1].delete(0, tk.END)

            self.list_lbl[2].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Об'єм паралелепіпеда - MathSol":
            self.list_entry[0].delete(0, tk.END)
            self.list_entry[1].delete(0, tk.END)
            self.list_entry[2].delete(0, tk.END)

            self.list_lbl[4].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Об'єм піраміди - MathSol":
            self.list_entry[0].delete(0, tk.END)
            self.list_entry[1].delete(0, tk.END)

            self.list_lbl[2].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Об'єм правильного тетраедра - MathSol":
            self.list_entry[0].delete(0, tk.END)

            self.list_lbl[1].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Об'єм циліндра - MathSol":
            self.list_entry[0].delete(0, tk.END)
            self.list_entry[1].delete(0, tk.END)

            self.list_lbl[3].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Об'єм конуса - MathSol":
            self.list_entry[0].delete(0, tk.END)
            self.list_entry[1].delete(0, tk.END)

            self.list_lbl[3].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        elif self.window.title() == "Об'єм кулі - MathSol":
            self.list_entry[0].delete(0, tk.END)

            self.list_lbl[1].config(text="Поля очищені", background=CONST_COLOR_GREEN)
        self.window.after(2000, self.statusbar_config)


    def btn_return(self):
        self.window.destroy()
        window_main.win_show()
        

    def btn_action_1(self):
        triangle_type = ["Звичайний прямокутник",
                        "Прямокутний прямокутник",
                        "Рівнобедрений прямокутник",
                        "Рівносторонній прямокутник"]
 
        if self.list_btn[0]['text'] == "Трикутник":
            window_main.win_hide()

            window_triangle = CreateWindow("Площа трикутника - MathSol", 500, 490)
            window_triangle.win_config(CONST_COLOR_WHITE)
 
            window_triangle.lfrm_create("Список формул", 10, 5, 480, 95)
            window_triangle.lfrm_create("Область розрахунку", 10, 110, 480, 270)
            window_triangle.lfrm_create("Область керування", 10, 390, 480, 65)
            window_triangle.lfrm_config(CONST_COLOR_WHITE)
 
            window_triangle.lbl_create("Тип", 15, 30, 128, tk.W, CONST_COLOR_WHITE)
            window_triangle.lbl_create("Формула", 15, 60, 128, tk.W, CONST_COLOR_WHITE)
 
            window_triangle.cbox_create(triangle_type, 163, 30, 317, "readonly")
            window_triangle.list_cbox[0].bind("<<ComboboxSelected>>", window_triangle.cbox_event_triangle)
            window_triangle.cbox_create("", 163, 60, 317, "readonly")
            window_triangle.list_cbox[1].bind("<<ComboboxSelected>>", window_triangle.cbox_event)
 
            # Label & Entry 1
            window_triangle.lbl_create("", 15, 135, 218, tk.W, CONST_COLOR_WHITE)
            window_triangle.entry_create(278, 135, 202)
            window_triangle.list_entry[0].place_forget()
 
            # Label & Entry 2
            window_triangle.lbl_create("", 15, 185, 218, tk.W, CONST_COLOR_WHITE)
            window_triangle.entry_create(278, 185, 202)
            window_triangle.list_entry[1].place_forget()

            # Label & Entry 3
            window_triangle.lbl_create("", 15, 235, 218, tk.W, CONST_COLOR_WHITE)
            window_triangle.entry_create(278, 235, 202)
            window_triangle.list_entry[2].place_forget()

            # Label & Entry 4
            window_triangle.lbl_create("", 15, 285, 218, tk.W, CONST_COLOR_WHITE)
            window_triangle.entry_create(278, 285, 202)
            window_triangle.list_entry[3].place_forget()
 
            window_triangle.btn_create("Обчислити", 25, 335, 450, 25)
            window_triangle.list_btn[0].config(command=window_triangle.math_calc)
            window_triangle.list_btn[0].place_forget()
 
            window_triangle.btn_create("Очистити поля", 25, 415, 120, 25)
            window_triangle.list_btn[1].config(command=window_triangle.btn_clear_fields)
            window_triangle.list_btn[1].place_forget()

            window_triangle.btn_create("Повернутися", 355, 415, 120, 25)
            window_triangle.list_btn[2].config(command=window_triangle.btn_return)
 
            window_triangle.lbl_create("", 0, 470, 500, tk.W, CONST_COLOR_WHITE)
            window_triangle.list_lbl[6].config(text="Оберіть тип трикутника", background=CONST_COLOR_ORANGE)

            window_triangle.protocol_delete_window()
            window_triangle.win_focus_set()
        elif self.list_btn[0]['text'] == "Куб":
            window_main.win_hide()

            window_cube = CreateWindow("Об'єм куба - MathSol", 500, 240)
            window_cube.win_config(CONST_COLOR_WHITE)

            window_cube.lfrm_create("Область розрахунку", 10, 5, 480, 120)
            window_cube.lfrm_create("Область керування", 10, 135, 480, 65)
            window_cube.lfrm_config(CONST_COLOR_WHITE)

            window_cube.lbl_create("Довжина сторони (у сантиметрах)", 15, 30, 218, tk.W, CONST_COLOR_WHITE)
            window_cube.entry_create(278, 30, 202)
 
            window_cube.btn_create("Обчислити", 25, 80, 450, 25)
            window_cube.list_btn[0].config(command=window_cube.math_calc)
 
            window_cube.btn_create("Очистити поля", 25, 160, 120, 25)
            window_cube.list_btn[1].config(command=window_cube.btn_clear_fields)

            window_cube.btn_create("Повернутися", 355, 160, 120, 25)
            window_cube.list_btn[2].config(command=window_cube.btn_return)
 
            window_cube.lbl_create("", 0, 220, 500, tk.W, CONST_COLOR_GREY)

            window_cube.protocol_delete_window()
            window_cube.win_focus_set()


    def btn_action_2(self):
        if self.list_btn[1]['text'] == "Прямокутник":
            window_main.win_hide()

            rectangle_formula = ["За двома сторонами (більшою та меншою)", "Через діагональ та синус гострого кута між діагоналями"]

            window_rectangle = CreateWindow("Площа прямокутника - MathSol", 500, 460)
            window_rectangle.win_config(CONST_COLOR_WHITE)
 
            window_rectangle.lfrm_create("Список формул", 10, 5, 480, 65)
            window_rectangle.lfrm_create("Область розрахунку", 10, 80, 480, 270)
            window_rectangle.lfrm_create("Область керування", 10, 360, 480, 65)
            window_rectangle.lfrm_config(CONST_COLOR_WHITE)
 
            window_rectangle.lbl_create("Формула", 15, 30, 128, tk.W, CONST_COLOR_WHITE)
 
            window_rectangle.cbox_create(rectangle_formula, 163, 30, 317, "readonly")
            window_rectangle.list_cbox[0].bind("<<ComboboxSelected>>", window_rectangle.cbox_event)
 
            # Label & Entry 1
            window_rectangle.lbl_create("", 15, 105, 218, tk.W, CONST_COLOR_WHITE)
            window_rectangle.entry_create(278, 105, 202)
            window_rectangle.list_entry[0].place_forget()
 
            # Label & Entry 2
            window_rectangle.lbl_create("", 15, 155, 218, tk.W, CONST_COLOR_WHITE)
            window_rectangle.entry_create(278, 155, 202)
            window_rectangle.list_entry[1].place_forget()
 
            window_rectangle.btn_create("Обчислити", 25, 305, 450, 25)
            window_rectangle.list_btn[0].config(command=window_rectangle.math_calc)
            window_rectangle.list_btn[0].place_forget()
 
            window_rectangle.btn_create("Очистити поля", 25, 385, 120, 25)
            window_rectangle.list_btn[1].config(command=window_rectangle.btn_clear_fields)
            window_rectangle.list_btn[1].place_forget()

            window_rectangle.btn_create("Повернутися", 355, 385, 120, 25)
            window_rectangle.list_btn[2].config(command=window_rectangle.btn_return)
 
            window_rectangle.lbl_create("", 0, 440, 500, tk.W, CONST_COLOR_WHITE)
            window_rectangle.list_lbl[3].config(text="Виберіть формулу", background=CONST_COLOR_ORANGE)

            window_rectangle.protocol_delete_window()
            window_rectangle.win_focus_set()
        elif self.list_btn[1]['text'] == "Призма":
            window_main.win_hide()

            window_prism = CreateWindow("Об'єм призми - MathSol", 500, 285)
            window_prism.win_config(CONST_COLOR_WHITE)

            window_prism.lfrm_create("Область розрахунку", 10, 5, 480, 170)
            window_prism.lfrm_create("Область керування", 10, 185, 480, 65)
            window_prism.lfrm_config(CONST_COLOR_WHITE)

            window_prism.lbl_create("Площа основи призми", 15, 30, 218, tk.W, CONST_COLOR_WHITE)
            window_prism.entry_create(278, 30, 202)

            window_prism.lbl_create("Висота", 15, 80, 218, tk.W, CONST_COLOR_WHITE)
            window_prism.entry_create(278, 80, 202)
 
            window_prism.btn_create("Обчислити", 25, 130, 450, 25)
            window_prism.list_btn[0].config(command=window_prism.math_calc)
 
            window_prism.btn_create("Очистити поля", 25, 210, 120, 25)
            window_prism.list_btn[1].config(command=window_prism.btn_clear_fields)

            window_prism.btn_create("Повернутися", 355, 210, 120, 25)
            window_prism.list_btn[2].config(command=window_prism.btn_return)
 
            window_prism.lbl_create("", 0, 265, 500, tk.W, CONST_COLOR_GREY)

            window_prism.protocol_delete_window()
            window_prism.win_focus_set()


    def btn_action_3(self):
        if self.list_btn[2]['text'] == "Квадрат":
            window_main.win_hide()

            square_formula = ["За довжиною сторони", "За довжиною діагоналі"]

            window_square = CreateWindow("Площа квадрата - MathSol", 500, 460)
            window_square.win_config(CONST_COLOR_WHITE)
 
            window_square.lfrm_create("Список формул", 10, 5, 480, 65)
            window_square.lfrm_create("Область розрахунку", 10, 80, 480, 270)
            window_square.lfrm_create("Область керування", 10, 360, 480, 65)
            window_square.lfrm_config(CONST_COLOR_WHITE)
 
            window_square.lbl_create("Формула", 15, 30, 128, tk.W, CONST_COLOR_WHITE)
 
            window_square.cbox_create(square_formula, 163, 30, 317, "readonly")
            window_square.list_cbox[0].bind("<<ComboboxSelected>>", window_square.cbox_event)
 
            window_square.lbl_create("", 15, 105, 218, tk.W, CONST_COLOR_WHITE)
            window_square.entry_create(278, 105, 202)
            window_square.list_entry[0].place_forget()
 
            window_square.btn_create("Обчислити", 25, 305, 450, 25)
            window_square.list_btn[0].config(command=window_square.math_calc)
            window_square.list_btn[0].place_forget()
 
            window_square.btn_create("Очистити поля", 25, 385, 120, 25)
            window_square.list_btn[1].config(command=window_square.btn_clear_fields)
            window_square.list_btn[1].place_forget()

            window_square.btn_create("Повернутися", 355, 385, 120, 25)
            window_square.list_btn[2].config(command=window_square.btn_return)
 
            window_square.lbl_create("", 0, 440, 500, tk.W, CONST_COLOR_WHITE)
            window_square.list_lbl[2].config(text="Виберіть формулу", background=CONST_COLOR_ORANGE)

            window_square.protocol_delete_window()
            window_square.win_focus_set()
        elif self.list_btn[2]['text'] == "Паралелепіпед":
            window_main.win_hide()

            parallelepiped_formula = ["Звичайний паралелепіпед", "Прямокутний паралелепіпед"]

            window_parallelepiped = CreateWindow("Об'єм паралелепіпеда - MathSol", 500, 460)
            window_parallelepiped.win_config(CONST_COLOR_WHITE)
 
            window_parallelepiped.lfrm_create("Список формул", 10, 5, 480, 65)
            window_parallelepiped.lfrm_create("Область розрахунку", 10, 80, 480, 270)
            window_parallelepiped.lfrm_create("Область керування", 10, 360, 480, 65)
            window_parallelepiped.lfrm_config(CONST_COLOR_WHITE)
 
            window_parallelepiped.lbl_create("Тип", 15, 30, 128, tk.W, CONST_COLOR_WHITE)
 
            window_parallelepiped.cbox_create(parallelepiped_formula, 163, 30, 317, "readonly")
            window_parallelepiped.list_cbox[0].bind("<<ComboboxSelected>>", window_parallelepiped.cbox_event)

            # Label & Entry 1
            window_parallelepiped.lbl_create("", 15, 105, 218, tk.W, CONST_COLOR_WHITE)
            window_parallelepiped.entry_create(278, 105, 202)
            window_parallelepiped.list_entry[0].place_forget()

            # Label & Entry 2
            window_parallelepiped.lbl_create("", 15, 155, 218, tk.W, CONST_COLOR_WHITE)
            window_parallelepiped.entry_create(278, 155, 202)
            window_parallelepiped.list_entry[1].place_forget()

            # Label & Entry 3
            window_parallelepiped.lbl_create("", 15, 205, 218, tk.W, CONST_COLOR_WHITE)
            window_parallelepiped.entry_create(278, 205, 202)
            window_parallelepiped.list_entry[2].place_forget()
 
            window_parallelepiped.btn_create("Обчислити", 25, 305, 450, 25)
            window_parallelepiped.list_btn[0].config(command=window_parallelepiped.math_calc)
            window_parallelepiped.list_btn[0].place_forget()
 
            window_parallelepiped.btn_create("Очистити поля", 25, 385, 120, 25)
            window_parallelepiped.list_btn[1].config(command=window_parallelepiped.btn_clear_fields)
            window_parallelepiped.list_btn[1].place_forget()

            window_parallelepiped.btn_create("Повернутися", 355, 385, 120, 25)
            window_parallelepiped.list_btn[2].config(command=window_parallelepiped.btn_return)
 
            window_parallelepiped.lbl_create("", 0, 440, 500, tk.W, CONST_COLOR_WHITE)
            window_parallelepiped.list_lbl[4].config(text="Виберіть формулу", background=CONST_COLOR_ORANGE)

            window_parallelepiped.protocol_delete_window()
            window_parallelepiped.win_focus_set()


    def btn_action_4(self):
        if self.list_btn[3]['text'] == "Паралелограм":
            window_main.win_hide()

            parallelogram_formula = ["За довжиною сторони і висоти", "За двома сторонами і кутом між ними", "За двома діагоналями і кутом між ними"]

            window_parallelogram = CreateWindow("Площа паралелограма - MathSol", 500, 460)
            window_parallelogram.win_config(CONST_COLOR_WHITE)
 
            window_parallelogram.lfrm_create("Список формул", 10, 5, 480, 65)
            window_parallelogram.lfrm_create("Область розрахунку", 10, 80, 480, 270)
            window_parallelogram.lfrm_create("Область керування", 10, 360, 480, 65)
            window_parallelogram.lfrm_config(CONST_COLOR_WHITE)
 
            window_parallelogram.lbl_create("Формула", 15, 30, 128, tk.W, CONST_COLOR_WHITE)
 
            window_parallelogram.cbox_create(parallelogram_formula, 163, 30, 317, "readonly")
            window_parallelogram.list_cbox[0].bind("<<ComboboxSelected>>", window_parallelogram.cbox_event)

            # Label & Entry 1
            window_parallelogram.lbl_create("", 15, 105, 218, tk.W, CONST_COLOR_WHITE)
            window_parallelogram.entry_create(278, 105, 202)
            window_parallelogram.list_entry[0].place_forget()

            # Label & Entry 2
            window_parallelogram.lbl_create("", 15, 155, 218, tk.W, CONST_COLOR_WHITE)
            window_parallelogram.entry_create(278, 155, 202)
            window_parallelogram.list_entry[1].place_forget()

            # Label & Entry 3
            window_parallelogram.lbl_create("", 15, 205, 218, tk.W, CONST_COLOR_WHITE)
            window_parallelogram.entry_create(278, 205, 202)
            window_parallelogram.list_entry[2].place_forget()
 
            window_parallelogram.btn_create("Обчислити", 25, 305, 450, 25)
            window_parallelogram.list_btn[0].config(command=window_parallelogram.math_calc)
            window_parallelogram.list_btn[0].place_forget()
 
            window_parallelogram.btn_create("Очистити поля", 25, 385, 120, 25)
            window_parallelogram.list_btn[1].config(command=window_parallelogram.btn_clear_fields)
            window_parallelogram.list_btn[1].place_forget()

            window_parallelogram.btn_create("Повернутися", 355, 385, 120, 25)
            window_parallelogram.list_btn[2].config(command=window_parallelogram.btn_return)
 
            window_parallelogram.lbl_create("", 0, 440, 500, tk.W, CONST_COLOR_WHITE)
            window_parallelogram.list_lbl[4].config(text="Виберіть формулу", background=CONST_COLOR_ORANGE)

            window_parallelogram.protocol_delete_window()
            window_parallelogram.win_focus_set()
        elif self.list_btn[3]['text'] == "Піраміда":
            window_main.win_hide()

            window_pyramid = CreateWindow("Об'єм піраміди - MathSol", 500, 285)
            window_pyramid.win_config(CONST_COLOR_WHITE)

            window_pyramid.lfrm_create("Область розрахунку", 10, 5, 480, 170)
            window_pyramid.lfrm_create("Область керування", 10, 185, 480, 65)
            window_pyramid.lfrm_config(CONST_COLOR_WHITE)

            window_pyramid.lbl_create("Площа основи піраміди", 15, 30, 218, tk.W, CONST_COLOR_WHITE)
            window_pyramid.entry_create(278, 30, 202)

            window_pyramid.lbl_create("Висота", 15, 80, 218, tk.W, CONST_COLOR_WHITE)
            window_pyramid.entry_create(278, 80, 202)
 
            window_pyramid.btn_create("Обчислити", 25, 130, 450, 25)
            window_pyramid.list_btn[0].config(command=window_pyramid.math_calc)
 
            window_pyramid.btn_create("Очистити поля", 25, 210, 120, 25)
            window_pyramid.list_btn[1].config(command=window_pyramid.btn_clear_fields)

            window_pyramid.btn_create("Повернутися", 355, 210, 120, 25)
            window_pyramid.list_btn[2].config(command=window_pyramid.btn_return)
 
            window_pyramid.lbl_create("", 0, 265, 500, tk.W, CONST_COLOR_GREY)

            window_pyramid.protocol_delete_window()
            window_pyramid.win_focus_set()

    def btn_action_5(self):
        if self.list_btn[4]['text'] == "Ромб":
            window_main.win_hide()

            rhombus_formula = ["За довжиною сторони і висоти", "За стороною і кутом", "За довжинами двох діагоналей"]

            window_rhombus = CreateWindow("Площа ромба - MathSol", 500, 460)
            window_rhombus.win_config(CONST_COLOR_WHITE)
 
            window_rhombus.lfrm_create("Список формул", 10, 5, 480, 65)
            window_rhombus.lfrm_create("Область розрахунку", 10, 80, 480, 270)
            window_rhombus.lfrm_create("Область керування", 10, 360, 480, 65)
            window_rhombus.lfrm_config(CONST_COLOR_WHITE)
 
            window_rhombus.lbl_create("Формула", 15, 30, 128, tk.W, CONST_COLOR_WHITE)
 
            window_rhombus.cbox_create(rhombus_formula, 163, 30, 317, "readonly")
            window_rhombus.list_cbox[0].bind("<<ComboboxSelected>>", window_rhombus.cbox_event)
 
            # Label & Entry 1
            window_rhombus.lbl_create("", 15, 105, 218, tk.W, CONST_COLOR_WHITE)
            window_rhombus.entry_create(278, 105, 202)
            window_rhombus.list_entry[0].place_forget()
 
            # Label & Entry 2
            window_rhombus.lbl_create("", 15, 155, 218, tk.W, CONST_COLOR_WHITE)
            window_rhombus.entry_create(278, 155, 202)
            window_rhombus.list_entry[1].place_forget()
 
            window_rhombus.btn_create("Обчислити", 25, 305, 450, 25)
            window_rhombus.list_btn[0].config(command=window_rhombus.math_calc)
            window_rhombus.list_btn[0].place_forget()
 
            window_rhombus.btn_create("Очистити поля", 25, 385, 120, 25)
            window_rhombus.list_btn[1].config(command=window_rhombus.btn_clear_fields)
            window_rhombus.list_btn[1].place_forget()

            window_rhombus.btn_create("Повернутися", 355, 385, 120, 25)
            window_rhombus.list_btn[2].config(command=window_rhombus.btn_return)
 
            window_rhombus.lbl_create("", 0, 440, 500, tk.W, CONST_COLOR_WHITE)
            window_rhombus.list_lbl[3].config(text="Виберіть формулу", background=CONST_COLOR_ORANGE)

            window_rhombus.protocol_delete_window()
            window_rhombus.win_focus_set()
        elif self.list_btn[4]['text'] == "Прав. тетраедр":
            window_main.win_hide()

            window_ctetrahedron = CreateWindow("Об'єм правильного тетраедра - MathSol", 500, 240)
            window_ctetrahedron.win_config(CONST_COLOR_WHITE)

            window_ctetrahedron.lfrm_create("Область розрахунку", 10, 5, 480, 120)
            window_ctetrahedron.lfrm_create("Область керування", 10, 135, 480, 65)
            window_ctetrahedron.lfrm_config(CONST_COLOR_WHITE)

            window_ctetrahedron.lbl_create("Довжина сторони", 15, 30, 218, tk.W, CONST_COLOR_WHITE)
            window_ctetrahedron.entry_create(278, 30, 202)
 
            window_ctetrahedron.btn_create("Обчислити", 25, 80, 450, 25)
            window_ctetrahedron.list_btn[0].config(command=window_ctetrahedron.math_calc)
 
            window_ctetrahedron.btn_create("Очистити поля", 25, 160, 120, 25)
            window_ctetrahedron.list_btn[1].config(command=window_ctetrahedron.btn_clear_fields)

            window_ctetrahedron.btn_create("Повернутися", 355, 160, 120, 25)
            window_ctetrahedron.list_btn[2].config(command=window_ctetrahedron.btn_return)
 
            window_ctetrahedron.lbl_create("", 0, 220, 500, tk.W, CONST_COLOR_GREY)

            window_ctetrahedron.protocol_delete_window()
            window_ctetrahedron.win_focus_set()


    def btn_action_6(self):
        if self.list_btn[5]['text'] == "Трапеція":
            window_main.win_hide()

            trapezium_formula = ["За довжиною основ і висоти"]

            window_trapezium = CreateWindow("Площа трапеції - MathSol", 500, 460)
            window_trapezium.win_config(CONST_COLOR_WHITE)
 
            window_trapezium.lfrm_create("Список формул", 10, 5, 480, 65)
            window_trapezium.lfrm_create("Область розрахунку", 10, 80, 480, 270)
            window_trapezium.lfrm_create("Область керування", 10, 360, 480, 65)
            window_trapezium.lfrm_config(CONST_COLOR_WHITE)
 
            window_trapezium.lbl_create("Формула", 15, 30, 128, tk.W, CONST_COLOR_WHITE)
 
            window_trapezium.cbox_create(trapezium_formula, 163, 30, 317, "readonly")
            window_trapezium.list_cbox[0].bind("<<ComboboxSelected>>", window_trapezium.cbox_event)

            # Label & Entry 1
            window_trapezium.lbl_create("", 15, 105, 218, tk.W, CONST_COLOR_WHITE)
            window_trapezium.entry_create(278, 105, 202)
            window_trapezium.list_entry[0].place_forget()

            # Label & Entry 2
            window_trapezium.lbl_create("", 15, 155, 218, tk.W, CONST_COLOR_WHITE)
            window_trapezium.entry_create(278, 155, 202)
            window_trapezium.list_entry[1].place_forget()

            # Label & Entry 3
            window_trapezium.lbl_create("", 15, 205, 218, tk.W, CONST_COLOR_WHITE)
            window_trapezium.entry_create(278, 205, 202)
            window_trapezium.list_entry[2].place_forget()
 
            window_trapezium.btn_create("Обчислити", 25, 305, 450, 25)
            window_trapezium.list_btn[0].config(command=window_trapezium.math_calc)
            window_trapezium.list_btn[0].place_forget()
 
            window_trapezium.btn_create("Очистити поля", 25, 385, 120, 25)
            window_trapezium.list_btn[1].config(command=window_trapezium.btn_clear_fields)
            window_trapezium.list_btn[1].place_forget()

            window_trapezium.btn_create("Повернутися", 355, 385, 120, 25)
            window_trapezium.list_btn[2].config(command=window_trapezium.btn_return)
 
            window_trapezium.lbl_create("", 0, 440, 500, tk.W, CONST_COLOR_WHITE)
            window_trapezium.list_lbl[4].config(text="Виберіть формулу", background=CONST_COLOR_ORANGE)

            window_trapezium.protocol_delete_window()
            window_trapezium.win_focus_set()
        elif self.list_btn[5]['text'] == "Циліндр":
            window_main.win_hide()

            cylinder_formula = ["Через радіус та висоту", "Через площу основи та висоту"]
            
            window_cylinder = CreateWindow("Об'єм циліндра - MathSol", 500, 460)
            window_cylinder.win_config(CONST_COLOR_WHITE)
 
            window_cylinder.lfrm_create("Список формул", 10, 5, 480, 65)
            window_cylinder.lfrm_create("Область розрахунку", 10, 80, 480, 270)
            window_cylinder.lfrm_create("Область керування", 10, 360, 480, 65)
            window_cylinder.lfrm_config(CONST_COLOR_WHITE)
 
            window_cylinder.lbl_create("Формула", 15, 30, 128, tk.W, CONST_COLOR_WHITE)
 
            window_cylinder.cbox_create(cylinder_formula, 163, 30, 317, "readonly")
            window_cylinder.list_cbox[0].bind("<<ComboboxSelected>>", window_cylinder.cbox_event)
 
            # Label & Entry 1
            window_cylinder.lbl_create("", 15, 105, 218, tk.W, CONST_COLOR_WHITE)
            window_cylinder.entry_create(278, 105, 202)
            window_cylinder.list_entry[0].place_forget()
 
            # Label & Entry 2
            window_cylinder.lbl_create("", 15, 155, 218, tk.W, CONST_COLOR_WHITE)
            window_cylinder.entry_create(278, 155, 202)
            window_cylinder.list_entry[1].place_forget()
 
            window_cylinder.btn_create("Обчислити", 25, 305, 450, 25)
            window_cylinder.list_btn[0].config(command=window_cylinder.math_calc)
            window_cylinder.list_btn[0].place_forget()
 
            window_cylinder.btn_create("Очистити поля", 25, 385, 120, 25)
            window_cylinder.list_btn[1].config(command=window_cylinder.btn_clear_fields)
            window_cylinder.list_btn[1].place_forget()

            window_cylinder.btn_create("Повернутися", 355, 385, 120, 25)
            window_cylinder.list_btn[2].config(command=window_cylinder.btn_return)
 
            window_cylinder.lbl_create("", 0, 440, 500, tk.W, CONST_COLOR_WHITE)
            window_cylinder.list_lbl[3].config(text="Виберіть формулу", background=CONST_COLOR_ORANGE)

            window_cylinder.protocol_delete_window()
            window_cylinder.win_focus_set()


    def btn_action_7(self):
        if self.list_btn[6]['text'] == "Круг":
            window_main.win_hide()

            circle_formula = ["Через радіус", "Через діаметр"]

            window_circle = CreateWindow("Площа круга - MathSol", 500, 460)
            window_circle.win_config(CONST_COLOR_WHITE)
 
            window_circle.lfrm_create("Список формул", 10, 5, 480, 65)
            window_circle.lfrm_create("Область розрахунку", 10, 80, 480, 270)
            window_circle.lfrm_create("Область керування", 10, 360, 480, 65)
            window_circle.lfrm_config(CONST_COLOR_WHITE)
 
            window_circle.lbl_create("Формула", 15, 30, 128, tk.W, CONST_COLOR_WHITE)
 
            window_circle.cbox_create(circle_formula, 163, 30, 317, "readonly")
            window_circle.list_cbox[0].bind("<<ComboboxSelected>>", window_circle.cbox_event)
 
            window_circle.lbl_create("", 15, 105, 218, tk.W, CONST_COLOR_WHITE)
            window_circle.entry_create(278, 105, 202)
            window_circle.list_entry[0].place_forget()
 
            window_circle.btn_create("Обчислити", 25, 305, 450, 25)
            window_circle.list_btn[0].config(command=window_circle.math_calc)
            window_circle.list_btn[0].place_forget()
 
            window_circle.btn_create("Очистити поля", 25, 385, 120, 25)
            window_circle.list_btn[1].config(command=window_circle.btn_clear_fields)
            window_circle.list_btn[1].place_forget()

            window_circle.btn_create("Повернутися", 355, 385, 120, 25)
            window_circle.list_btn[2].config(command=window_circle.btn_return)
 
            window_circle.lbl_create("", 0, 440, 500, tk.W, CONST_COLOR_WHITE)
            window_circle.list_lbl[2].config(text="Виберіть формулу", background=CONST_COLOR_ORANGE)

            window_circle.protocol_delete_window()
            window_circle.win_focus_set()
        elif self.list_btn[6]['text'] == "Конус":
            window_main.win_hide()

            cone_formula = ["Через радіус та висоту", "Через площу основи та висоту"]
            
            window_cone = CreateWindow("Об'єм конуса - MathSol", 500, 460)
            window_cone.win_config(CONST_COLOR_WHITE)
 
            window_cone.lfrm_create("Список формул", 10, 5, 480, 65)
            window_cone.lfrm_create("Область розрахунку", 10, 80, 480, 270)
            window_cone.lfrm_create("Область керування", 10, 360, 480, 65)
            window_cone.lfrm_config(CONST_COLOR_WHITE)
 
            window_cone.lbl_create("Формула", 15, 30, 128, tk.W, CONST_COLOR_WHITE)
 
            window_cone.cbox_create(cone_formula, 163, 30, 317, "readonly")
            window_cone.list_cbox[0].bind("<<ComboboxSelected>>", window_cone.cbox_event)
 
            # Label & Entry 1
            window_cone.lbl_create("", 15, 105, 218, tk.W, CONST_COLOR_WHITE)
            window_cone.entry_create(278, 105, 202)
            window_cone.list_entry[0].place_forget()
 
            # Label & Entry 2
            window_cone.lbl_create("", 15, 155, 218, tk.W, CONST_COLOR_WHITE)
            window_cone.entry_create(278, 155, 202)
            window_cone.list_entry[1].place_forget()
 
            window_cone.btn_create("Обчислити", 25, 305, 450, 25)
            window_cone.list_btn[0].config(command=window_cone.math_calc)
            window_cone.list_btn[0].place_forget()
 
            window_cone.btn_create("Очистити поля", 25, 385, 120, 25)
            window_cone.list_btn[1].config(command=window_cone.btn_clear_fields)
            window_cone.list_btn[1].place_forget()

            window_cone.btn_create("Повернутися", 355, 385, 120, 25)
            window_cone.list_btn[2].config(command=window_cone.btn_return)
 
            window_cone.lbl_create("", 0, 440, 500, tk.W, CONST_COLOR_WHITE)
            window_cone.list_lbl[3].config(text="Виберіть формулу", background=CONST_COLOR_ORANGE)

            window_cone.protocol_delete_window()
            window_cone.win_focus_set()


    def btn_action_8(self):
        if self.list_btn[7]['text'] == "Еліпс":
            window_main.win_hide()

            window_ellipse = CreateWindow("Площа еліпса - MathSol", 500, 285)
            window_ellipse.win_config(CONST_COLOR_WHITE)

            window_ellipse.lfrm_create("Область розрахунку", 10, 5, 480, 170)
            window_ellipse.lfrm_create("Область керування", 10, 185, 480, 65)
            window_ellipse.lfrm_config(CONST_COLOR_WHITE)
 
            window_ellipse.lbl_create("Довжина великої піввісі (у см)", 15, 30, 218, tk.W, CONST_COLOR_WHITE)
            window_ellipse.entry_create(278, 30, 202)
 
            window_ellipse.lbl_create("Довжина малої піввісі (у см)", 15, 80, 218, tk.W, CONST_COLOR_WHITE)
            window_ellipse.entry_create(278, 80, 202)
 
            window_ellipse.btn_create("Обчислити", 25, 130, 450, 25)
            window_ellipse.list_btn[0].config(command=window_ellipse.math_calc)
 
            window_ellipse.btn_create("Очистити поля", 25, 210, 120, 25)
            window_ellipse.list_btn[1].config(command=window_ellipse.btn_clear_fields)

            window_ellipse.btn_create("Повернутися", 355, 210, 120, 25)
            window_ellipse.list_btn[2].config(command=window_ellipse.btn_return)
 
            window_ellipse.lbl_create("", 0, 265, 500, tk.W, CONST_COLOR_WHITE)

            window_ellipse.protocol_delete_window()
            window_ellipse.win_focus_set()
        elif self.list_btn[7]['text'] == "Куля":
            window_main.win_hide()

            window_ball = CreateWindow("Об'єм кулі - MathSol", 500, 240)
            window_ball.win_config(CONST_COLOR_WHITE)

            window_ball.lfrm_create("Область розрахунку", 10, 5, 480, 120)
            window_ball.lfrm_create("Область керування", 10, 135, 480, 65)
            window_ball.lfrm_config(CONST_COLOR_WHITE)

            window_ball.lbl_create("Радіус", 15, 30, 218, tk.W, CONST_COLOR_WHITE)
            window_ball.entry_create(278, 30, 202)
 
            window_ball.btn_create("Обчислити", 25, 80, 450, 25)
            window_ball.list_btn[0].config(command=window_ball.math_calc)
 
            window_ball.btn_create("Очистити поля", 25, 160, 120, 25)
            window_ball.list_btn[1].config(command=window_ball.btn_clear_fields)

            window_ball.btn_create("Повернутися", 355, 160, 120, 25)
            window_ball.list_btn[2].config(command=window_ball.btn_return)
 
            window_ball.lbl_create("", 0, 220, 500, tk.W, CONST_COLOR_GREY)

            window_ball.protocol_delete_window()
            window_ball.win_focus_set()

    def destroy(self):
        self.window.destroy()

    def btn_action_exit(self):
        ask_exit = mb.askyesno("Вихід", "Ви дійсно бажаєте вийти з програми?")
        if ask_exit is True:
            window_main.destroy()
            self.window.destroy()  

    def mainloop(self):
        self.window.mainloop()

    def protocol_delete_window(self):
        self.window.protocol("WM_DELETE_WINDOW", self.btn_action_exit)


if __name__ == "__main__":
    figure_names = ["Трикутник", "Прямокутник",
                    "Квадрат", "Паралелограм",
                    "Ромб", "Трапеція",
                    "Круг", "Еліпс",
                    "Куб", "Призма",
                    "Паралелепіпед", "Піраміда",
                    "Прав. тетраедр", "Циліндр",
                    "Конус", "Куля"]
                        
    figure_coords = [30, 80, 130, 180, 230, 280, 330, 380]
    
    mode_list = ["Площа", "Об'єм"]
    
    settings_names = ["Допомога", "Список формул", "Налаштування", "Вихід"]
    
    settings_coords = [95, 145, 195, 245]
    
    # Створення головного вікна
    window_main = CreateWindow("Головне меню - MathSol", 390, 445)
    window_main.win_config("#ffffff")
    
    # Створення 3 фреймів із заголовками
    window_main.lfrm_create("Список фігур", 10, 5, 180, 430)
    window_main.lfrm_create("Режим", 200, 5, 180, 60)
    window_main.lfrm_create("Налаштування", 200, 70, 180, 365)
    window_main.lfrm_config(CONST_COLOR_WHITE)
    
    # Створення кнопок з назвами фігур
    for i, name in enumerate(figure_names):
        if i >= 8:
            break
    
        window_main.btn_create(figure_names[i], 20, figure_coords[i], 160, 40)
    
    # Створення кнопок для фрейму "Налаштування"
    for i, name in enumerate(settings_names):
        if i >= 4:
            break
    
        window_main.btn_create(settings_names[i], 210, settings_coords[i], 160, 40)
    window_main.btn_actions()

    window_main.list_btn[8].place_forget()
    window_main.list_btn[9].place_forget()
    window_main.list_btn[10].place_forget()
    window_main.list_btn[11].place(x=210, y=95)
    
    # Створення списку з режимами
    window_main.cbox_create(mode_list, 210, 30, 160, "readonly")
    window_main.list_cbox[0].current(0)
    window_main.list_cbox[0].bind('<<ComboboxSelected>>', window_main.cbox_mode_change)
    
    # Цикл роботи вікна
    window_main.protocol_delete_window()
    window_main.mainloop()