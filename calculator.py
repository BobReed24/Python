import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import time

def windowed_calculator():
    import tkinter as tk
    from tkinter import ttk
    import math

    class TI84Calculator:
        def __init__(self, root):
            self.root = root
            self.root.title("TI-84 Plus Calculator")
            
            self.entry = tk.Entry(root, font=('Arial', 18), borderwidth=2, relief="solid")
            self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

            
            self.buttons = [
                ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
                ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
                ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
                ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
                ('sqrt', 5, 0), ('^', 5, 1), ('cos', 5, 2), ('sin', 5, 3),
                ('tan', 6, 0), ('log', 6, 1), ('exp', 6, 2), ('(', 6, 3),
                (')', 7, 0), ('pi', 7, 1), ('e', 7, 2), ('C', 7, 3)
            ]

            self.create_buttons()

        def create_buttons(self):
            for (text, row, column) in self.buttons:
                if text == "=":
                    btn = ttk.Button(self.root, text=text, command=self.calculate)
                elif text == "C":
                    btn = ttk.Button(self.root, text=text, command=self.clear)
                else:
                    btn = ttk.Button(self.root, text=text, command=lambda t=text: self.button_click(t))
                btn.grid(row=row + 1, column=column, sticky="nsew", ipadx=10, ipady=10)

            
            for i in range(8):
                self.root.grid_rowconfigure(i, weight=1)
                self.root.grid_columnconfigure(i, weight=1)

        def button_click(self, text):
            current = self.entry.get()
            if text == 'pi':
                self.entry.insert(tk.END, str(math.pi))
            elif text == 'e':
                self.entry.insert(tk.END, str(math.e))
            else:
                self.entry.insert(tk.END, text)

        def clear(self):
            self.entry.delete(0, tk.END)

        def calculate(self):
            try:
                expression = self.entry.get()
                expression = expression.replace('^', '**')
                expression = expression.replace('sqrt', 'math.sqrt')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('tan', 'math.tan')
                expression = expression.replace('log', 'math.log')
                expression = expression.replace('exp', 'math.exp')
                result = eval(expression, {"math": math})
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

    if __name__ == "__main__":
        root = tk.Tk()
        calculator = TI84Calculator(root)
        root.mainloop()

def round_result(result, decimal_places):
    return round(result, decimal_places)

def simplemath():
    print('Evaluated Math Calculator')
    try:
        res = eval(input(">: "))
        print(res)
    except (ValueError, NameError, SyntaxError, TypeError) as e:
        print(f"Err: {e}")

def area_of_shapes():
    print("Area of Shapes")
    while True:
        shape = input("Enter a shape (rectangle, triangle, circle) to calculate area (or 'exit' to quit): ").lower()
        if shape == 'exit':
            break
        unit = input("Enter the unit (cm, ft, yd): ")
        if shape == 'rectangle':
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            area = l * w
            print(f"Area of rectangle: {area} {unit}²")
        elif shape == 'triangle':
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            area = 0.5 * b * h
            print(f"Area of triangle: {area} {unit}²")
        elif shape == 'circle':
            r = float(input("Enter radius: "))
            area = np.pi * (r ** 2)
            print(f"Area of circle: {area} {unit}²")
        else:
            print("Invalid shape, please try again.")

def perimeter_and_circumference():
    print("Perimeter and Circumference")
    while True:
        shape = input("Enter a shape (rectangle, triangle, circle) to calculate perimeter/circumference (or 'exit' to quit): ").lower()
        if shape == 'exit':
            break
        unit = input("Enter the unit (cm, ft, yd): ")
        if shape == 'rectangle':
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            perimeter = 2 * (l + w)
            print(f"Perimeter of rectangle: {perimeter} {unit}")
        elif shape == 'triangle':
            a = float(input("Enter side a: "))
            b = float(input("Enter side b: "))
            c = float(input("Enter side c: "))
            perimeter = a + b + c
            print(f"Perimeter of triangle: {perimeter} {unit}")
        elif shape == 'circle':
            r = float(input("Enter radius: "))
            circumference = 2 * np.pi * r
            print(f"Circumference of circle: {circumference} {unit}")
        else:
            print("Invalid shape, please try again.")

def volume_of_solids():
    print("Volume of Solids")
    while True:
        solid = input("Enter a solid (cube, rectangular prism, cylinder) to calculate volume (or 'exit' to quit): ").lower()
        if solid == 'exit':
            break
        unit = input("Enter the unit (cm³, ft³, yd³): ")
        if solid == 'cube':
            s = float(input("Enter side length: "))
            volume = s ** 3
            print(f"Volume of cube: {volume} {unit}")
        elif solid == 'rectangular prism':
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            volume = l * w * h
            print(f"Volume of rectangular prism: {volume} {unit}")
        elif solid == 'cylinder':
            r = float(input("Enter radius: "))
            h = float(input("Enter height: "))
            volume = np.pi * (r ** 2) * h
            print(f"Volume of cylinder: {volume} {unit}")
        else:
            print("Invalid solid, please try again.")

def surface_area_of_solids():
    print("Surface Area of Solids")
    while True:
        solid = input("Enter a solid (cube, rectangular prism, sphere) to calculate surface area (or 'exit' to quit): ").lower()
        if solid == 'exit':
            break
        unit = input("Enter the unit (cm², ft², yd²): ")
        if solid == 'cube':
            s = float(input("Enter side length: "))
            surface_area = 6 * (s ** 2)
            print(f"Surface area of cube: {surface_area} {unit}")
        elif solid == 'rectangular prism':
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            surface_area = 2 * (l * w + l * h + w * h)
            print(f"Surface area of rectangular prism: {surface_area} {unit}")
        elif solid == 'sphere':
            r = float(input("Enter radius: "))
            surface_area = 4 * np.pi * (r ** 2)
            print(f"Surface area of sphere: {surface_area} {unit}")
        else:
            print("Invalid solid, please try again.")

def pythagorean_theorem():
    print("Pythagorean Theorem")
    while True:
        sides = input("Enter two sides of a right triangle (a, b) separated by space (or 'exit' to quit): ")
        if sides.lower() == 'exit':
            break
        try:
            a, b = map(float, sides.split())
            c = np.sqrt(a**2 + b**2)
            print(f"Hypotenuse (c) = {c}")
        except Exception as e:
            print(f"Error: {e}")

def similar_triangles():
    print("Similar Triangles")
    while True:
        sides = input("Enter corresponding sides of two triangles (a1, a2, b1, b2, c1, c2) separated by space (or 'exit' to quit): ")
        if sides.lower() == 'exit':
            break
        try:
            a1, a2, b1, b2, c1, c2 = map(float, sides.split())
            ratio1 = a1 / a2
            ratio2 = b1 / b2
            ratio3 = c1 / c2
            if np.isclose(ratio1, ratio2) and np.isclose(ratio2, ratio3):
                print("The triangles are similar.")
            else:
                print("The triangles are not similar.")
        except Exception as e:
            print(f"Error: {e}")

def complementary_angles():
    print("Complementary Angles")
    while True:
        angles = input("Enter two angles A and B separated by space (or 'exit' to quit): ")
        if angles.lower() == 'exit':
            break
        try:
            A, B = map(float, angles.split())
            if np.isclose(A + B, 90):
                print("The angles are complementary.")
            else:
                print("The angles are not complementary.")
        except Exception as e:
            print(f"Error: {e}")

def supplementary_angles():
    print("Supplementary Angles")
    while True:
        angles = input("Enter two angles A and B separated by space (or 'exit' to quit): ")
        if angles.lower() == 'exit':
            break
        try:
            A, B = map(float, angles.split())
            if np.isclose(A + B, 180):
                print("The angles are supplementary.")
            else:
                print("The angles are not supplementary.")
        except Exception as e:
            print(f"Error: {e}")

def distance_formula():
    print("Distance Formula")
    while True:
        points = input("Enter two points (x1, y1) and (x2, y2) separated by space (or 'exit' to quit): ")
        if points.lower() == 'exit':
            break
        try:
            x1, y1, x2, y2 = map(float, points.split())
            distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            print(f"Distance between points: {distance}")
        except Exception as e:
            print(f"Error: {e}")

def midpoint_formula():
    print("Midpoint Formula")
    while True:
        points = input("Enter two points (x1, y1) and (x2, y2) separated by space (or 'exit' to quit): ")
        if points.lower() == 'exit':
            break
        try:
            x1, y1, x2, y2 = map(float, points.split())
            midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
            print(f"Midpoint: {midpoint}")
        except Exception as e:
            print(f"Error: {e}")

def slope_formula():
    print("Slope Formula")
    while True:
        points = input("Enter two points (x1, y1) and (x2, y2) separated by space (or 'exit' to quit): ")
        if points.lower() == 'exit':
            break
        try:
            x1, y1, x2, y2 = map(float, points.split())
            slope = (y2 - y1) / (x2 - x1)
            print(f"Slope: {slope}")
        except Exception as e:
            print(f"Error: {e}")

def plot_equation(eq, variable, title):
    x_vals = np.linspace(-10, 10, 400)
    y_vals = [eq.subs(variable, x) for x in x_vals]
    plt.plot(x_vals, y_vals, label=str(eq))
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.title(title)
    plt.xlabel(str(variable))
    plt.ylabel('Value')
    plt.grid()
    plt.legend()
    plt.show()

def algebra_solver():
    print("Algebra Solver")
    history = []
    
    while True:
        print("\nOptions:")
        print("1. Solve an equation")
        print("2. Solve an inequality")
        print("3. Solve a system of equations")
        print("4. Factor a polynomial")
        print("5. Plot an equation")
        print("6. Simplify rational expressions")
        print("7. Calculate exponent and logarithm")
        print("8. Solve trigonometric equations")
        print("9. Calculate derivative")
        print("10. Calculate integral")
        print("11. Perform polynomial long division")
        print("12. Unit conversion")
        print("13. View history")
        print("14. Exit")
        
        choice = input("Select an option: ")
        if choice == '1':
            variable_to_solve = input("What variable do you want to solve for? (e.g., x, y): ").strip()
            equation = input("Enter an equation (e.g., 2*x + 3*y = 7): ")
            try:
                eq = sp.sympify(equation.replace('=', '-(') + ')')
                variable = sp.symbols(variable_to_solve)
                solution = sp.solve(eq, variable)
                history.append((equation, solution))
                print(f"Solution for {variable_to_solve}: {solution}")

                if isinstance(solution, list) and solution:
                    solution_expr = solution[0]
                    other_vars = [str(v) for v in solution_expr.free_symbols if str(v) != variable_to_solve]
                    
                    if other_vars:
                        values = {}
                        for var in other_vars:
                            value = float(input(f"Enter a value for {var}: "))
                            values[var] = value
                        numeric_result = solution_expr.subs(values)
                        print(f"Numeric result for {variable_to_solve} with provided values: {numeric_result}")
                else:
                    print("No solution found.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            variable_to_solve = input("What variable do you want to solve for? (e.g., x, y): ").strip()
            inequality = input("Enter an inequality (e.g., x + 2 > 5): ")
            try:
                ineq = sp.sympify(inequality)
                variable = sp.symbols(variable_to_solve)
                solution = sp.solve(ineq, variable)
                print(f"Solution for {variable_to_solve}: {solution}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            equations = []
            while True:
                equation = input("Enter an equation (or type 'done' to finish): ")
                if equation.lower() == 'done':
                    break
                equations.append(equation)

            try:
                eqs = [sp.sympify(eq.replace('=', '-(') + ')') for eq in equations]
                solution = sp.solve(eqs)
                print(f"Solution for the system of equations: {solution}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            polynomial = input("Enter a polynomial (e.g., x**2 + 3*x + 2): ")
            try:
                poly = sp.sympify(polynomial)
                factored_poly = sp.factor(poly)
                print(f"Factored form: {factored_poly}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            variable_to_plot = input("Enter the variable for plotting (e.g., x): ").strip()
            equation_to_plot = input("Enter the equation to plot (e.g., x**2 - 4): ")
            try:
                variable = sp.symbols(variable_to_plot)
                eq_to_plot = sp.sympify(equation_to_plot)
                plot_equation(eq_to_plot, variable, f"Plot of {equation_to_plot}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '6':
            rational_expression = input("Enter a rational expression (e.g., (x**2 - 1)/(x - 1)): ")
            try:
                expr = sp.sympify(rational_expression)
                simplified_expr = sp.simplify(expr)
                print(f"Simplified form: {simplified_expr}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '7':
            base = input("Enter the base (e.g., 2): ")
            exponent = input("Enter the exponent (e.g., 3): ")
            try:
                result = float(base) ** float(exponent)
                print(f"{base} raised to the power of {exponent} is: {result}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '8':
            variable_to_solve = input("What variable do you want to solve for? (e.g., x): ").strip()
            trigonometric_equation = input("Enter a trigonometric equation (e.g., sin(x) = 0.5): ")
            try:
                eq = sp.sympify(trigonometric_equation.replace('=', '-(') + ')')
                variable = sp.symbols(variable_to_solve)
                solution = sp.solve(eq, variable)
                print(f"Solution for {variable_to_solve}: {solution}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '9':
            variable = input("Enter the variable for differentiation (e.g., x): ").strip()
            function = input("Enter the function (e.g., x**2 + 3*x): ")
            try:
                var = sp.symbols(variable)
                func = sp.sympify(function)
                derivative = sp.diff(func, var)
                print(f"The derivative of {function} with respect to {variable} is: {derivative}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '10':
            variable = input("Enter the variable for integration (e.g., x): ").strip()
            function = input("Enter the function (e.g., x**2 + 3*x): ")
            try:
                var = sp.symbols(variable)
                func = sp.sympify(function)
                integral = sp.integrate(func, var)
                print(f"The indefinite integral of {function} with respect to {variable} is: {integral}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '11':
            dividend = input("Enter the dividend polynomial (e.g., x**3 + 2*x**2 + 3): ")
            divisor = input("Enter the divisor polynomial (e.g., x + 1): ")
            try:
                div = sp.sympify(dividend)
                divisor = sp.sympify(divisor)
                quotient, remainder = sp.div(div, divisor)
                print(f"Quotient: {quotient}, Remainder: {remainder}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '12':
            print("Unit Conversion Options: ")
            print("1. Length (cm to m)")
            print("2. Area (m² to km²)")
            choice = input("Select an option: ")
            if choice == '1':
                cm = float(input("Enter length in cm: "))
                m = cm / 100
                print(f"{cm} cm is {m} m")
            elif choice == '2':
                m2 = float(input("Enter area in m²: "))
                km2 = m2 / 1_000_000
                print(f"{m2} m² is {km2} km²")

        elif choice == '13':
            print("Calculation History:")
            for entry in history:
                print(f"{entry[0]} = {entry[1]}")

        elif choice == '14':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice, please try again.")

def main_menu():
    while True:
        print("Math Application")
        print('1. Simple Math')
        print("2. Windowed Calculator")
        print("3. Area of Shapes")
        print("4. Perimeter and Circumference")
        print("5. Volume of Solids")
        print("6. Surface Area of Solids")
        print("7. Pythagorean Theorem")
        print("8. Similar Triangles")
        print("9. Complementary Angles")
        print("10. Supplementary Angles")
        print("11. Distance Formula")
        print("12. Midpoint Formula")
        print("13. Slope Formula")
        print("14. Algebra Solver")
        print("15. Exit")
        
        choice = input("Select an option: ")
        if choice == '1':
            simplemath()
        elif choice == '2':
            windowed_calculator()
        elif choice == '3':
            area_of_shapes()
        elif choice == '4':
            perimeter_and_circumference()
        elif choice == '5':
            volume_of_solids()
        elif choice == '6':
            surface_area_of_solids()
        elif choice == '7':
            pythagorean_theorem()
        elif choice == '8':
            similar_triangles()
        elif choice == '9':
            complementary_angles()
        elif choice == '10':
            supplementary_angles()
        elif choice == '11':
            distance_formula()
        elif choice == '12':
            midpoint_formula()
        elif choice == '13':
            slope_formula()
        elif choice == '14':
            algebra_solver()
        elif choice == '15':
            print('Exiting...')
            time.sleep(1)
            print('Please wait...')
            time.sleep(0.5)
            print('Shutting off numpy')
            time.sleep(0.5)
            print('Shutting off sympy')
            time.sleep(0.5)
            print('Goodbye!')
            exit()
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main_menu()
