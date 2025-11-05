# class Calculator:

#     def __init__(self, id, manf_date):
#         self.id = id
#         self.manf_date = manf_date
#         print("These are the details.")
    
#     def describe(self):
#         print(self.id, self.manf_date)

# calc1 = Calculator(1, "2025-10-25")
# calc2 = Calculator(2, "2025-10-25")

# calc1.describe()
# calc2.describe()

# --------------------------------------------

# Operator Overloading

class Marks:

    def __init__(self, sc_marks, so_marks, math_marks):
        self.sc_marks = sc_marks
        self.so_marks = so_marks
        self.math_marks = math_marks
    
    def __add__(self, other):
        print(self.sc_marks + other.sc_marks)
        print(self.so_marks + other.so_marks)
        print(self.math_marks + other.math_marks)

marks1 = Marks(25, 55, 68)
marks2 = Marks(88, 96, 32)

total_marks = marks1 + marks2
print(total_marks)

