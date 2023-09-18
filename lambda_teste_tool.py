import json
import importlib.util
import sys
import tkinter as tk
from tkinter import filedialog

print("Ferramente de teste para lambda local")
def main(args):
    print("Argumentos",args)

    print("Path da aplicação lambda: ",args[0])
    print("Nome do metódo Handler: ",args[1])
    print("Path dos eventos: ",args[2])
    print("Path das dependencias da lambda: ",args[3])
    
    if(args[4] == "debug"):
        caminho_evento = filedialog.askopenfilename(
            filetypes=[('Evento Json', '*.json')],
            initialdir=args[2],
            title="Selecione o evento Json")
        with open(caminho_evento, 'r') as file:
            event = json.load(file)
    elif(args[4]=="ui"):
        event = json.loads(args[2])
    
    module_directory = args[3]
    sys.path.append(module_directory)
    
    module = import_lambda(args[0],args[1])
    
    handler = getattr(module, args[1])
    
    resultado =  handler(event,lambda_context())
    
    print("Lambda executada com sucesso, resultado:",resultado)

def import_lambda(file_path,handler):
    
    spec = importlib.util.spec_from_file_location(handler, file_path)

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)
    return module

def lambda_context():
    class LambdaContext:
        def __init__(self):
            self.function_name = "test-func"
            self.memory_limit_in_mb = 128
            self.invoked_function_arn = "arn:aws:lambda:eu-west-1:809313241234:function:test-func"
            self.aws_request_id = "52fdfc07-2182-154f-163f-5f0f9a621d72"

        def get_remaining_time_in_millis(self) -> int:
            return 1000

    return LambdaContext()

def start(args):
    root = tk.Tk()
    root.withdraw()
    try:
        main(args)
    except Exception as ex:
        print("Ocorreu um erro na invocação da lambda: ",ex)
        
if __name__ == '__main__':
    args = sys.argv[1:]
    args.append("debug")
    start()