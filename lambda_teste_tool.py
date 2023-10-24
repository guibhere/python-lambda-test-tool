import json
import importlib.util
import sys
from Utils.file_helper import File_Helper
from Utils.lambda_context_mock import lambda_context

def main(args):
    if args[4] == "debug":
        file_helper = File_Helper()
        event = json.loads(file_helper.carregar_json_file(args[2]))
    elif args[4] == "ui":
        event = json.loads(args[2])
        
    module_directory = args[3]
    sys.path.append(module_directory)

    module = import_lambda(args[0], args[1])

    handler = getattr(module, args[1])

    resultado = handler(event, lambda_context())

    print("Lambda executada com sucesso, resultado:", resultado)


def import_lambda(file_path, handler):
    spec = importlib.util.spec_from_file_location(handler, file_path)

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)
    return module


def start(args):
    try:
        main(args)
    except Exception as ex:
        print("Ocorreu um erro na invocação da lambda: ", ex)


if __name__ == "__main__":
    args = sys.argv[1:]
    args.append("debug")
    start()
