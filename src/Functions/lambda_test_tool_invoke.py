import json
import importlib.util
import sys
from src.Utils.file_helper import File_Helper
from src.Utils.lambda_context_mock import lambda_context

class Lambda_Test_Tool_Invoke():
    def main(self,args):
        if args[4] == "debug":
            file_helper = File_Helper()
            event = json.loads(file_helper.carregar_json_file(args[2]))
        elif args[4] == "ui":
            event = json.loads(args[2])
            
        module_directory = args[3]
        sys.path.append(module_directory)

        module = self.import_lambda(args[0], args[1])

        handler = getattr(module, args[1])

        resultado = handler(event, lambda_context())

        print("Lambda executada com sucesso, resultado:", resultado)


    def import_lambda(self,file_path, handler):
        spec = importlib.util.spec_from_file_location(handler, file_path)

        module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(module)
        return module


    def start(self,args):
        try:
            self.main(args)
        except Exception as ex:
            print("Ocorreu um erro na invocação da lambda: ", ex)


if __name__ == "__main__":
    args = sys.argv[1:]
    args.append("debug")
    Lambda_Test_Tool_Invoke.start(args)
