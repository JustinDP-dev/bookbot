def main():
    book_title = "books/frankenstein.txt"
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #Count Words
        words = count_words(file_contents)
        #Count Characters
        characters = count_characters(file_contents)
        #Sort Characters
        sort = convert_dict(characters)

        #Print the Report
        print(f"--- Begin report of {book_title} ---")
        print(f"{words} words found in the document\n")

        for s in sort:
            print(f"The '{s['character']}' character was found {s['count']} times")

        print("--- End Report ---")

#Count the number of words in the string
def count_words(contents: str):
    words = contents.split()
    num_words = len(words)
    return num_words

#Count the number of characters in a string
def count_characters(contents: str):
    #convert all to lowercase
    lower_case = contents.lower()
    #Declare a empty dictionary
    letter_dict = {}

    #Loop through the characters and add them to the dictionary or update the count
    for char in lower_case:
        get_value = letter_dict.get(char)
        if get_value == None:
            letter_dict[char] = 1
        else:
            letter_dict[char] = get_value + 1

    return letter_dict

#Key for the List sorting based on the count
def sort_on(dictionary: dict):
    return dictionary["count"]

#Convert the dictionary to a list of dictionaries to sort
def convert_dict(dictionary: dict):
    list_of_dicts = []

    #Loop through the key value pairs
    for key, value in dictionary.items():
        #Check if the key is an alpha and append this list if so
        if key.isalpha():
            list_of_dicts.append({"character": key, "count": value})
    
    #Call the sort function
    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts

    
#Run main loop
if __name__ == '__main__':
    main()