def writeFile():
    with open("Dockerfile", "w+") as external_file:
        add_text = "FROM base-image"
        print(add_text, file=external_file)
        external_file.close()

def main():
    writeFile()

# If name is main, run main func
if __name__ == '__main__':
    main()
