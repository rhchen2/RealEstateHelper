from src.main.classes.Zillow import search 

if __name__ == '__main__':
    result = search("X1-ZWz17jvxcowwln_7lwvq", "60611", "420 E Ohio St")
    for r in result:
        print(vars(r))
