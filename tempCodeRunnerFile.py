import tkinter as tk
from tkinter import messagebox

def calculate_distance(x1, x2, x3, x4, x5, dataset):
    distances = []
    for data in dataset:
        dist = ((x1 - data[0]) ** 2 + (x2 - data[1]) ** 2 + (x3 - data[2]) ** 2 +
                (x4 - data[3]) ** 2 + (x5 - data[4]) ** 2) ** 0.5
        distances.append(dist)
    return distances

def get_risk_level(bodytemp, intervisit, Ssym, Csym, IntCovid, dataset):
    distances = calculate_distance(bodytemp, intervisit, Ssym, Csym, IntCovid, dataset)
    sorted_distances, sorted_risk = zip(*sorted(zip(distances, [data[5] for data in dataset])))

    n1 = sorted_risk[:7].count('lowrisk')
    n2 = sorted_risk[:7].count('moderate')
    n3 = sorted_risk[:7].count('highrisk')

    if n1 > n2 and n1 > n3:
        return 'Low risk, stay at home 🏠', 'green'
    elif n2 > n1 and n2 > n3:
        return 'Moderate risk, you must have a checkup.', 'yellow'
    elif n3 > n1 and n3 > n2:
        return 'High risk, urgent checkup required!', 'red'
    else:
        return 'Unable to determine risk level. Please consult a doctor.', 'orange'

def on_submit():
    try:
        bodytemp = float(body_temp_entry.get())
        if not (35 <= bodytemp <= 42.5):
            raise ValueError("Invalid body temperature range.")

        intervisit = int(inter_visit_var.get())
        Ssym = int(severe_symptoms_var.get())
        Csym = int(common_symptoms_var.get())
        IntCovid = int(interaction_var.get())

        result, color = get_risk_level(bodytemp, intervisit, Ssym, Csym, IntCovid, dataset)
        result_label.config(text=result, fg=color)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Dataset for KNN model
dataset = [
    [37.0, 1, 4, 3, 0, 'highrisk'], [36.5, 0, 2, 2, 0, 'highrisk'],
    [36.5, 0, 0, 1, 1, 'lowrisk'], [37.2, 1, 2, 2, 0, 'moderate'],
    [36.8, 1, 5, 3, 1, 'highrisk'], [37.5, 0, 0, 0, 0, 'lowrisk'],
    [36.91, 1, 1, 0, 1, 'moderate'], [37.3, 0, 5, 3, 1, 'highrisk'],
    [36.3, 0, 2, 1, 1, 'lowrisk'], [37.1, 1, 4, 3, 1, 'highrisk'],
    # Additional dataset entries...
]

# Create the main Tkinter window
root = tk.Tk()
root.title("K-Nearest Neighbor Risk Assessment")
root.configure(bg="#f0f8ff")

# Input Fields
body_temp_label = tk.Label(root, text="Enter Body Temperature (°C):", bg="#f0f8ff", font=("Arial", 12))
body_temp_label.pack(pady=5)
body_temp_entry = tk.Entry(root, font=("Arial", 12))
body_temp_entry.pack(pady=5)

# International Visit (Yes/No options)
inter_visit_label = tk.Label(root, text="International Visit (Yes/No):", bg="#f0f8ff", font=("Arial", 12))
inter_visit_label.pack(pady=5)
inter_visit_var = tk.StringVar(value="0")
inter_visit_yes = tk.Radiobutton(root, text="Yes", variable=inter_visit_var, value="1", bg="#f0f8ff", font=("Arial", 12))
inter_visit_no = tk.Radiobutton(root, text="No", variable=inter_visit_var, value="0", bg="#f0f8ff", font=("Arial", 12))
inter_visit_yes.pack()
inter_visit_no.pack()

# Severe Symptoms (Dropdown)
severe_symptoms_label = tk.Label(root, text="Number of Severe Symptoms (0-5):", bg="#f0f8ff", font=("Arial", 12))
severe_symptoms_label.pack(pady=5)
severe_symptoms_var = tk.StringVar(value="0")
severe_symptoms_entry = tk.OptionMenu(root, severe_symptoms_var, *range(6))
severe_symptoms_entry.pack(pady=5)

# Common Symptoms (Dropdown)
common_symptoms_label = tk.Label(root, text="Number of Common Symptoms (0-6):", bg="#f0f8ff", font=("Arial", 12))
common_symptoms_label.pack(pady=5)
common_symptoms_var = tk.StringVar(value="0")
common_symptoms_entry = tk.OptionMenu(root, common_symptoms_var, *range(7))
common_symptoms_entry.pack(pady=5)

# Interaction with COVID+ Patient (Yes/No options)
interaction_label = tk.Label(root, text="Interaction with COVID+ Patient (Yes/No):", bg="#f0f8ff", font=("Arial", 12))
interaction_label.pack(pady=5)
interaction_var = tk.StringVar(value="0")
interaction_yes = tk.Radiobutton(root, text="Yes", variable=interaction_var, value="1", bg="#f0f8ff", font=("Arial", 12))
interaction_no = tk.Radiobutton(root, text="No", variable=interaction_var, value="0", bg="#f0f8ff", font=("Arial", 12))
interaction_yes.pack()
interaction_no.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=on_submit, bg="#4CAF50", fg="white", font=("Arial", 12), width=15)
submit_button.pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", fg="blue", font=("Arial", 14, "bold"), wraplength=400, justify="center", bg="#f0f8ff")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
