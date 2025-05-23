#prompt user for name of file
#output media type of file
#any unrecognized file type should output application/octet-stream

def main():
    file = input("PLease input your file name including the suffix. ").lower().strip()
    code_ext(file)

def code_ext(suffix):
    if suffix.endswith(".gif"):
        print("image/gif")
    elif suffix.endswith(".jpg"):
        print("image/jpeg")
    elif suffix.endswith(".jpeg"):
        print("image/jpeg")
    elif suffix.endswith(".png"):
        print("image/png")
    elif suffix.endswith(".pdf"):
        print("application/pdf")
    elif suffix.endswith(".txt"):
        print("text/plain")
    elif suffix.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()
