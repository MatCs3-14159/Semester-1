def counter(file):
    file_dict = {
        "word": 0,
        "character": 0,
        "vowel": 0,
        "digit": 0 ,
        "other" : 0
    }
    vowel = "aeiouAEIOU"
    try:
        with open(file,"r") as f:
            content = f.read()
            for ch in content:
                file_dict["character"] += 1
                if ch.isdigit():
                    file_dict["digit"] += 1
                elif ch in vowel:
                    file_dict["vowel"] += 1
                elif not ch.isalpha() and ch != " " and ch!= "\n":
                    file_dict["other"] += 1
            file_dict["word"] = len(content.split())
        return file_dict
    except FileNotFoundError:
        print ("File dosent exist or not found.")
        return None
    except Exception as e:
        print (f"An error occured: {e}")
        return None
        
def main():
    filename = input("Enter your filename: ")
    result = counter(filename)
    if result:
        for key, value in result.items():
            print(key,":",value)
    
if __name__ == "__main__":
    main()
