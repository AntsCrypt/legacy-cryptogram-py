from AnagramCommand import AnagramCommand
import sys

if __name__ == '__main__':
    command = AnagramCommand()

    # select command
    try:
        if command.args["cmd"] == "encode":
            command.load_database()
            command.encode(command.args["text"])
        
        elif command.args["cmd"] == "decode":
            command.load_database()
            command.encode(command.args["text"])

        elif command.args["cmd"] == "similar":
            command.load_database()
            command.similar(command.args["text"])

    except (IndexError, KeyError):
        sys.stdout.write("[!] ERROR! use: anagram [encode/decode] [hash] [text]")

    finally:
        print()

