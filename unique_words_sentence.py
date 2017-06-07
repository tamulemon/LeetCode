import string
def num_of_unique_words(sentence):
    sentence += ' ' #this will make sure the last word get captured
    output_dict = {}
    last_pos = 0

    for i in range(len(sentence)):
        if sentence[i] == ' ' :
            substring = sentence[last_pos:i].lower().translate(None, string.punctuation)
            if (substring not in output_dict.keys()):
                output_dict[substring] = 1
            else:
                output_dict[substring] += 1
            last_pos = i + 1
    return output_dict

sentence = 'This is a -beautiful 1beautiful day.'


for k, v in num_of_unique_words(sentence).items():
    print k, v
