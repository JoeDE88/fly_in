import sys
from input_parser import parse_file

def main() -> None:
    print("Hello from fly-in!")
    try:
        if len(sys.argv) != 2:
            raise Exception(f"Usage example: python3 {sys.argv[0]} <file.txt>")
        file = sys.argv[1]
        parse_file(file)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
