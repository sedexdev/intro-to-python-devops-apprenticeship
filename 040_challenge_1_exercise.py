# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that
#  - takes a list of words
#  - returns a report of all the words that
#      - are longer than 10 characters
#      - don't contain a hyphen.
#  - if those words are longer than 15 characters
#      - they should be shortened to 15 characters with an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")


def filter_words(words):
    filtered = []
    for word in words:
        if len(word) > 10 and "-" not in word:
            filtered.append(word)
    return filtered


def truncate_word(word):
    return word[0:15] + "..."


def report_long_words(words):
    report = "These words are quite long: "
    filtered = filter_words(words)
    for i, word in enumerate(filtered):
        if len(word) > 15:
            word = truncate_word(word)
        if i != len(filtered)-1:
            report += word + ", "
        else:
            report += word
    return report


check_that_these_are_equal(
    report_long_words([
        'hello',
        'nonbiological',
        'Kay',
        'this-is-a-long-word',
        'antidisestablishmentarianism'
    ]),
    "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
    report_long_words([
        'cat',
        'dog',
        'rhinosaurus',
        'rhinosaurus-rex',
        'frog'
    ]),
    "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
    report_long_words([
        'cat'
    ]),
    "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
