def main():
    dic = {"you": "thou", "shall":"shalt", "are":"art", "y'all":"thee", "friend":"cousin", "your":"thy", "yours":"thine", "yes":"ay", "wish":"would", "allow me to":"give me leave to", "unfortunately":"alas", "goodbye":"adieu", "sir":"sirrah"}
    phrase = input("Enter something: ")
    print(change(phrase.lower(), dic))

def change(word, dictionary):
    for x, y in dictionary.items():
        word = word.replace(x, y)
    return word
    

main()
