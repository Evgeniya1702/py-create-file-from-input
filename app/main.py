def create_file_from_input() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    with open(file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")


def main() -> None:
    create_file_from_input()


if __name__ == "__main__":
    main()
