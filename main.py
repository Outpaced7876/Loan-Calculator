import tkinter as tk
import tkinter.messagebox


class MainWindow:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Loan Calculator")
        self.frame = tk.Frame(self.root)
        self.frame.grid()
        self.root.resizable(width=False, height=False)
        self.root.geometry('500x400')
        self.Buttons()
        self.label_loan_amount()
        self.textbox_loan_amount()
        self.label_loan_term()
        self.textbox_loan_term()
        self.label_interest_rate()
        self.textbox_interest_rate()
        self.label_monthly_payment()
        self.textbox_monthly_payment()
        self.root.mainloop()

    def Buttons(self):
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, width=7, height=1)
        self.reset_button.grid(row=5, column=2, padx=10, pady=10, sticky=tk.SE)

        self.calculate_button = tk.Button(self.frame, text='Calculate', command=self.calculate, width=7, height=1)
        self.calculate_button.grid(row=5, column=3, padx=10, pady=10, sticky=tk.SE)

        self.exit_button = tk.Button(self.frame, text='Exit', command=self.root.destroy, width=7, height=1)
        self.exit_button.grid(row=5, column=1, padx=10, pady=10, sticky=tk.SE)

    def label_loan_amount(self):
        self.label_loan_amount = tk.Label(self.frame, text="Loan amount $:")
        self.label_loan_amount.grid(row=1, column=2, sticky='E', padx=10, pady=10)

    def textbox_loan_amount(self):
        self.textbox_loan_amount = tk.Entry(self.frame)
        self.textbox_loan_amount.grid(row=1, column=3, sticky='W', padx=10, pady=10)

    def label_loan_term(self):
        self.label_loan_term = tk.Label(self.frame, text="Loan term (in months):")
        self.label_loan_term.grid(row=2, column=2, sticky='E', padx=10, pady=10)

    def textbox_loan_term(self):
        self.textbox_loan_term = tk.Entry(self.frame)
        self.textbox_loan_term.grid(row=2, column=3, sticky='W', padx=10, pady=10)

    def label_interest_rate(self):
        self.label_interest_rate = tk.Label(self.frame, text="Interest rate %:")
        self.label_interest_rate.grid(row=3, column=2, sticky='E', padx=10, pady=10)

    def textbox_interest_rate(self):
        self.textbox_interest_rate = tk.Entry(self.frame)
        self.textbox_interest_rate.grid(row=3, column=3, sticky='W', padx=10, pady=10)

    def label_monthly_payment(self):
        self.label_monthly_payment = tk.Label(self.frame, text="Monthly payment $: ")
        self.label_monthly_payment.grid(row=4, column=2, sticky='E', padx=10, pady=10)

    def textbox_monthly_payment(self):
        self.textbox_monthly_payment = tk.Entry(self.frame)
        self.textbox_monthly_payment.grid(row=4, column=3, sticky='W', padx=10, pady=10)

    def reset(self):
        self.textbox_loan_amount.delete(0, tk.END)
        self.textbox_loan_term.delete(0, tk.END)
        self.textbox_interest_rate.delete(0, tk.END)
        self.textbox_monthly_payment.delete(0, tk.END)


    def calculate(self):

            try:
                # Get input values from textboxes
                loan_amount = float(self.textbox_loan_amount.get())
                loan_term = int(self.textbox_loan_term.get())
                interest_rate = float(self.textbox_interest_rate.get())

                # Calculate monthly payment using formula
                monthly_interest_rate = interest_rate / 1200.0
                monthly_payment = (loan_amount * monthly_interest_rate /
                                   (1 - (1 / (1 + monthly_interest_rate) ** (loan_term * 12))))

                # Display monthly payment in textbox
                self.textbox_monthly_payment.delete(0, tk.END)
                self.textbox_monthly_payment.insert(0, f"{monthly_payment:.2f}")

            except ValueError:
                # Show error message box if any input value is invalid
                tkinter.messagebox.showerror("Invalid Input",
                                             "Please enter valid numbers for loan amount, loan term, and interest rate.")





if __name__ == '__main__':
    MainWindow()











