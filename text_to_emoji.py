def main():
    print(convert(input("Enter text: ")))

def convert(txt):
    return txt.replace(":(", "🙁").replace(":)", "🙂")

main()