


"""
The program is trying to translate a sentence captured as user input.
We first read in the text file textese.txt.
Then from the text file, we create a list of strings from each line in the text file. 
Then, we create a dictionary the list. 
Once the text file has been read into memory, we close the file. 

We then define a function for translating which evovles splitting the user input (sentence) into an 
array of strings ("enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

Once we have the array of strings representing the users input sentence, we 
loop through the each words, find the key matching the word and returns back the value tied to that word
in our dictionary.

After each word is translated, we then
print out the translated sentence to the user. 
"""

"""
main():
    set sentence = input()
    set dictionary = create_dictionary()
    translate(sentence, dictionary)
    
translate(sentence, dictionary):
    words = for each of the words in the sentence
    for each words, translate the word
    print translated sentence to the user
    
create_dictionary():
    read in textese.txt
    create list = each line from file
    close the file
    create a dict off the list
    return the dict

main()
"""

def main():
    sentence = input("Enter a sentence: ")
    dictionary = create_dictionary("textese.txt")
    translate(sentence, dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()
    return dict([word.split(",") for word in words])

    # #print("words", words)
    # translation = {}
    # for word in words: # "tonight, 2nite"
    #     [k, v] = word.split(",")
    #     translation[k] = v
    # # print(translation)
    # return translation

def translate(sentence, dictionary):
    # print("From translate", sentence)
    words = sentence.split()  #["enjoy", "the", "excellent", "band", "tonight"]
    for word in words:
        print(dictionary.get(word, word), " ", end="")
main()