def filter_messages(messages):
    
    filtered_messages = []
    count_of_bad_words = []
    
    for message in messages:
        
        words = message.split()
        good_words = []
        bad_words_count = 0
        
        for word in words:
            if word == "dang":
                bad_words_count += 1
            else:
                good_words.append(word)

        filtered_message = " ".join(good_words)
        filtered_messages.append(filtered_message)
        count_of_bad_words.append(bad_words_count)

    return filtered_messages, count_of_bad_words