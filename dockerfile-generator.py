

def writeFile(dockerfile):
    with open("Dockerfile", "w+") as dockerfile:
        add_text = "FROM base-image"
        print(add_text, file=dockerfile)
        dockerfile.close()

def readFile(dockerfile):
    with open(dockerfile, 'r') as dockerfile:
        print(dockerfile.read())

def main():
    dockerfile_temp = input("Dockerfile template: ")
    path_file = dockerfile_temp + "/Dockerfile"
    readFile(path_file)

# If name is main, run main func
if __name__ == '__main__':
    main()
