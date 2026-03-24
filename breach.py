from core.args import init_parser
from core.display import banner, Message

def main():
    args, remaining = init_parser()
    
    if not args.category:
        # show banner and help
        banner()
    elif not args.module:
        # category level help
        pass
    else:
        # route to module
        pass

if __name__ == "__main__":
    main()
