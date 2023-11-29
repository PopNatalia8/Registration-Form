from tkinter import *

window = Tk()
window.geometry('500x300')
window.title('Registration Formn')


def getvals():
    print('Accepted')


label = Label(window, text='Registration Form', font=('Arial', 20, 'bold'))
label.grid(row=0, column=3)


name = Label(window, text='Name', font=('Arial', 15))
name.grid(row=1, column=2)

phone = Label(window, text='Phone', font=('Arial', 15))
phone.grid(row=2, column=2)

gender = Label(window, text='Gender', font=('Arial', 15))
gender.grid(row=3, column=2)

emergency = Label(window, text='Emergency', font=('Arial', 15))
emergency.grid(row=4, column=2)

payment_mood = Label(window, text='Payment Mood', font=('Arial', 15))
payment_mood.grid(row=5, column=2)

# Variable for storing data
name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
emergency_value = StringVar()
payment_mood_value = StringVar()
check_value = IntVar()

name_entry = Entry(window, font=('Arial', 15), textvariable=name_value)
phone_entry = Entry(window, font=('Arial', 15), textvariable=phone_value)
gender_entry = Entry(window, font=('Arial', 15), textvariable=gender_value)
emergency_entry = Entry(window, font=('Arial', 15), textvariable=emergency_value)
payment_mood_entry = Entry(window, font=('Arial', 15), textvariable=payment_mood_value)

name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
emergency_entry.grid(row=4, column=3)
payment_mood_entry.grid(row=5, column=3)

# Creating Checkbox

check_button = Checkbutton(text='Remember me?', font=('Arial', 15), variable=check_value)
check_button.grid(row=6, column=3)

# Submit button
submit_button = Button(window, text='Submit', font=('Arial', 15), command=getvals)
submit_button.grid(row=7, column=3)

window.mainloop()
