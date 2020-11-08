from AnagramCommand import AnagramCommand
import sys

if __name__ == '__main__':
    command = AnagramCommand()

    if command.args["cmd"] == "encode":
        command.encode(command.args["text"])
    
    elif command.args["cmd"] == "decode":
        command.decode(command.args["text"])

    elif command.args["cmd"] == "similar":
        command.similar(command.args["text"])

    elif command.args["cmd"] == "generator":
        command.generator()

    elif command.args["cmd"] == "help":
        command.help()
        
    else:
        sys.stdout.write("use: anagram help")