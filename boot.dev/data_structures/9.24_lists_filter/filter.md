# FILTER MESSAGES
You are about to write a bit more code in a single function than you have before.

Do *not* try to write it all at once. Start with the outermost loop, and work your way inwards. Add extra `print()` statements and run your code often to make sure it's doing what you expect. Just make sure to remove the extra `print()` statements before submitting your code.

Running your code often to make sure each line is doing what you expect is called "debugging". All programmers, even seasoned professionals, break large problems down into small ones that they can debug line by line.

## ASSIGNMENT
We need to filter the profanity out of our game's live chat feature! Complete the `filter_messages` function. It takes a list of chat messages as input and returns 2 new lists:

1. A list of the same messages but with all instances of the word `dang` removed.
2. A list containing the number of `dang` words that were removed from the message at that particular index.

For example:

```python
messages = ["dang it bobby!", "look at it go"]
filter_messages(messages) # returns ["it bobby!", "look at it go"], [1, 0]
```

Here are the steps for you to follow:

- Create the 2 empty lists that you'll return at the end. One for the filtered messages, and one for counts of words removed.
- For each message in the input list:
  1. Split the message into a list of words using the [.split()](https://docs.python.org/3/library/stdtypes.html#str.split) string method (see below for help).
  2. Create a new empty list for all the non-bad words for this message.
  3. Create a `counter` variable and set it to `0`. We'll increment this when we remove words from this message.
  4. For each word in the message:
      - If the word is `dang`, increment the counter
      - If it is *not* `dang`, add the word to the non-bad word list you created
  5. Join the list of non-bad words into a single string using the `.join()` method (see below for help)
  6. Append the new clean message to the final list of filtered messages
  7. Append the count of bad words removed to its list
  8. Return the filtered messages first, then the counters

## TIPS
### SPLIT A STRING INTO A LIST OF WORDS
The `.split()` method is called on a string. If you don't pass it any arguments, it will just split the words in the string on the whitespace.

```python
message = "hello there sam"
words = message.split()
print(words)
# Prints: ["hello", "there", "sam"]
```

### JOIN A LIST OF STRINGS INTO A SINGLE STRING
The `.join()` method is called on a delimiter (what goes between all the words in the list), and takes a list of strings as input.

```python
list_of_words = ["hello", "there", "sam"]
sentence = " ".join(list_of_words)
print(sentence)
# Prints: "hello there sam"
```


