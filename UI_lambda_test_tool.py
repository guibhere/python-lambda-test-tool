import sys
import tkinter as tk
from tkinter import ttk
import json
from UI_functions import JsonFileManager, DirectoryManager
from UI_logger import OutputRedirector
import lambda_teste_tool
from dependency_installer import DependencyInstaller

global args
args = sys.argv[1:]

if not args:
    args = ["", "", "", "E:/Projetos/python-serverless-api/serverless-api/src/", ""]

dep_installer = DependencyInstaller(args[3] + "requirements.txt")
    
# Create the main application window
app = tk.Tk()
app.title("Python Lambda Test Tool")

# Create a menu bar
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

dir_manager = DirectoryManager(app, None, args)


# Create a PanedWindow for the resizable text box and small text boxes
main_paned_window = tk.PanedWindow(app, orient="horizontal")
main_paned_window.pack(fill="x", expand=True)

# Create a Frame for the two small text boxes
small_text_frame = tk.PanedWindow(main_paned_window, orient="horizontal")
main_paned_window.add(small_text_frame)

# Create the first small text box widget
label1 = tk.Label(small_text_frame, text="Aplicação lambda:")
small_text_frame.add(label1)
small_text_box1 = tk.Text(small_text_frame, height=1, width=20)
small_text_frame.add(small_text_box1)
small_text_box1.insert(tk.END, args[0])
carrega_path_button = tk.Button(app, text="Selecionar lambda function", command=lambda:
                                (small_text_box1.delete("1.0", tk.END),
                                 small_text_box1.insert(tk.END, dir_manager.select_directory())))
main_paned_window.add(carrega_path_button)
# Create a Label for the first small text box

# Create the second small text box widget
label1 = tk.Label(small_text_frame, text="Lambda Handler:")
small_text_frame.add(label1)
small_text_box2 = tk.Text(small_text_frame, height=1, width=20)
small_text_frame.add(small_text_box2)
small_text_box2.insert(tk.END, args[1])

# Seleção de evento
def selecionar_evento(evento):
    opcao = combo_var.get()
    json_file_manager.open_json_file_selection(dir=args[2], file_name=opcao)


combo_var = tk.StringVar()
combobox = ttk.Combobox(app, textvariable=combo_var,
                        values=dir_manager.list_json_files(args[2]))
combobox.pack(pady=10)
combo_var.set("Selecione um evento")
combobox.bind("<<ComboboxSelected>>", selecionar_evento)

# Create a PanedWindow for resizable text box
paned_window = tk.PanedWindow(app, orient="vertical")
paned_window.pack(fill="both", expand=True)

# Create a text box widget
text_box = tk.Text(paned_window, height=10, width=40)
paned_window.add(text_box)

json_file_manager = JsonFileManager(app, text_box)

# Create a "File" menu with "Open JSON" and "Save JSON" options
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(
    label="Abrir JSON", command=json_file_manager.open_json_file)
file_menu.add_command(
    label="Salvar JSON", command=lambda:  (json_file_manager.save_json_file(),
                                           dir_manager.set_combobox_value(combobox, args[2])))
file_menu.add_command(
    label="Selecionar diretorio de eventos", command=lambda: dir_manager.select_event_dir(combobox))
file_menu.add_command(
    label="Instalar dependencias do projeto (requirements.txt)", command=lambda: dep_installer.InstalarDependenciasNovasRequirements())
# Create a label widget
label = tk.Label(app, text="Edit JSON:")
label.pack()

text_widget = tk.Text(app, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=True)

# Redirect stdout to the Text widget
sys.stdout = OutputRedirector(text_widget)

# Example JSON text to initialize the text box
example_json = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert the example JSON to a formatted string
example_json_text = json.dumps(example_json, indent=4)

# Insert the example JSON text into the text box
text_box.insert(tk.END, example_json_text)

# Create a button widget and define a callback function to parse JSON


def invoke_lambda():
    try:
        json_text = text_box.get("1.0", tk.END)
        parsed_json = json.loads(json_text)

        params = []
        params.append(small_text_box1.get("1.0", tk.END).strip())
        params.append(small_text_box2.get("1.0", tk.END).strip())
        params.append(json.dumps(parsed_json))
        params.append(args[3])
        params.append("ui")

        lambda_teste_tool.start(params)
    except json.JSONDecodeError as e:
        result_label.config(text="JSON Error:\n" + str(e))


parse_button = tk.Button(app, text="Invoke lambda", command=invoke_lambda)
parse_button.pack()

# Create a label to display the parsed JSON or error message
result_label = tk.Label(app, text="", justify="left", anchor="w")
result_label.pack()

# Start the GUI event loop
app.mainloop()
