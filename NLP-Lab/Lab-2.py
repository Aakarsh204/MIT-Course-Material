import re
def remove_char(string):
    pattern = r"^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$"
    result = re.sub(pattern, "", string)
    print("Modified Sentence: ", result)

def count_char(string):
    pattern = r"[a-zA-Z0-9]"
    result = re.sub(pattern, "", string)
    print("Number of characters: ", len(result))

def replace_char(string):
    pattern = r"[^a-zA-Z0-9]"
    char = input("Enter the replacement character\n")
    result = re.sub(pattern, char, string)
    print("Modified Sentence: ", result)

if __name__ == "__main__":
    string = input("Enter a string\n")
    remove_char(string)
    count_char(string)
    replace_char(string)
