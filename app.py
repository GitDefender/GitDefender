import sys

def main():
    try:
        from library.exec_from_command_line import exec_from_command_line
    except ImportError as e:
        raise ImportError(
            "Couldn't import crawltool-component."
        ) from e
    
    exec_from_command_line(sys.argv)

if __name__ == "__main__":
    main()