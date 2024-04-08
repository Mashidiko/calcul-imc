import tkinter as tk 
def calculate_bmi():
    try:
        height = float(entry_height.get()) /100
        weight = float(entry_weight.get())
        bmi = weight / (height**2)
        label_result['text']= f"votre IMC est : {bmi:.2f}"
    except ValueError:
        label_result['text']="Veuillez entrer des valeurs valides."

root = tk.Tk()
root.title("Calculateur d'IMC")
root.geometry("200x200")
root.config(pady=30)

label_height = tk.Label(root, text="Entrez votre taille (en cm) :")
label_height.pack()

entry_height = tk.Entry(root) 
entry_height.pack()

label_weight = tk.Label(root, text="Entrez votre poids (en kg) :")
label_weight.pack()

entry_weight = tk.Entry(root)
entry_weight.pack()

button_calculate = tk.Button(root, text="Calculer l'IMC", command=calculate_bmi)
button_calculate.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()