import  re
def search(x):
    regex = re.compile(r'([a-zA-Z]{2,})(\.)([a-zA-Z]{2,})')
    x=(regex.findall(x))
    return x[-1][-1]