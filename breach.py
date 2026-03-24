from core.args import init_parser
from core.display import banner, Message
from core.loader import load_module
from core.validator import validate
from core.executor import execute

def main():
    args, remaining = init_parser()
    
    if not args.category:
        # show banner and help
        banner()
    elif not args.module:
        # category level help
        pass
    else:
        category, module = args.category, args.module
        # route to module
        data = load_module(category, module)
        if data:
            if validate(data):
                execute(data, remaining)

if __name__ == "__main__":
    main()
