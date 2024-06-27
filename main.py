def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_counts = count_characters(file_contents)
    generate_report(word_count, character_counts)


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered_string = text.lower()
    characters = {}
    for char in lowered_string:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
        
    return characters

def generate_report(word_count, character_counts):
    char_list = [{'char':k, 'num':v} for k, v in character_counts.items()]

    def sort_on(d):
        return d['num']

    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in document")
    print("")
    for item in char_list:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End Report ---")

    

main()

