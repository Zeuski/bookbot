def word_count(story):
    num_words = 0
    for word in story:
        num_words += 1
    return(f"Found {num_words} total words")
    

def char_count(story):
    story = story.lower()
    count = {}

    for char in story:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    return(count)

def print_report(dick, num):
    #print(dick)
    d = sorted(dick.items(), key=lambda item: item[1], reverse=True)
    #print(d)
    print("============ BOOKBOT ============")
    print("alyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(num)
    print("--------- Character Count -------")
    for key, value in d:
        print(f"{key}: {value}")

    print("============= END ===============")
