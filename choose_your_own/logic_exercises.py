############################################################
# Python Logic Practice – Interactive Exercises
# Topics: if / elif / else, numbers, string checks, and logic
############################################################


############################################################
# Exercise 1: Reading Challenge
#
# Ask the user how many pages they read today.
#
# Rules:
# - Print "Gold Reader" if pages_read >= 60
# - Print "Silver Reader" if pages_read >= 30
# - Otherwise print "Keep reading!"
############################################################

pages_read = int(input("How many pages did you read today? "))

if pages_read >= 60:
    print("Gold Reader")
elif pages_read >= 30:
    print("Silver Reader")
else:
    print("Keep reading!")

print("\n---------------------------------\n")


############################################################
# Exercise 2: Detect a Fantasy Book
#
# Ask the user to enter a book title.
#
# If the title contains "magic" or "dragon", print:
# "This is probably a fantasy book!"
#
# Otherwise print:
# "This might be a different genre."
#
# Hint: use "in" to check if a word is inside the title.
############################################################

book_title = input("Enter a book title: ")

title = book_title.lower()

if "magic" in title or "dragon" in title:
    print("This is probably a fantasy book!")
else:
    print("This might be a different genre.")

print("\n---------------------------------\n")


############################################################
# Exercise 3: Book Review Quality Checker
#
# Ask the user for:
# - number of stars (1–5)
# - a short review sentence
#
# Print "Featured Review" ONLY if:
# - stars >= 4
# - AND the review contains the word "amazing"
#
# Otherwise print:
# "Thanks for the review!"
############################################################

stars = int(input("How many stars did you give the book (1-5)? "))
review = input("Write a short review: ")

review_lower = review.lower()

if stars >= 4 and "amazing" in review_lower:
    print("Featured Review")
else:
    print("Thanks for the review!")

print("\n---------------------------------\n")


############################################################
# Exercise 4: Library Borrowing Rules
#
# Ask the user:
# - their age
# - how many days overdue their current book is
#
# A student can borrow a rare book if:
# - age >= 12
# - AND days_overdue <= 0
#
# Print:
# "Rare book approved"
# or
# "Rare book denied"
############################################################

age = int(input("What is your age? "))
days_overdue = int(input("How many days overdue is your current book? "))

if age >= 12 and days_overdue <= 0:
    print("Rare book approved")
else:
    print("Rare book denied")

print("\n---------------------------------\n")


############################################################
# Exercise 5: Adventure Class Sorter
#
# Ask the user:
# - their magic test score
# - teacher notes about their abilities
#
# Rules:
# - if score >= 90 AND "telepathy" appears in notes
#       -> print "Mind Training Group"
# - elif score >= 80
#       -> print "Advanced Training"
# - else
#       -> print "General Training"
############################################################

score = int(input("Enter your magic test score: "))
notes = input("Enter teacher notes about your abilities: ")

notes_lower = notes.lower()

if score >= 90 and "telepathy" in notes_lower:
    print("Mind Training Group")
elif score >= 80:
    print("Advanced Training")
else:
    print("General Training")

print("\n---------------------------------\n")


############################################################
# Exercise 6: Smart Book Recommendation
#
# Ask the user:
# - what genre they want
# - how many pages they want in the book
# - a keyword describing the story
#
# Rules:
# - if genre == "fantasy" AND pages_wanted >= 300
#       -> print "Try an epic fantasy series"
#
# - elif "dragon" appears in the keyword
#       -> print "Try a dragon adventure book"
#
# - elif pages_wanted <= 150
#       -> print "Try a short mystery book"
#
# - else
#       -> print "Try a general adventure novel"
############################################################

genre = input("What genre do you want? ")
pages_wanted = int(input("How many pages do you want in the book? "))
keyword = input("Give a keyword describing the story: ")

genre = genre.lower()
keyword = keyword.lower()

if genre == "fantasy" and pages_wanted >= 300:
    print("Try an epic fantasy series")
elif "dragon" in keyword:
    print("Try a dragon adventure book")
elif pages_wanted <= 150:
    print("Try a short mystery book")
else:
    print("Try a general adventure novel")


print("\nEnd of exercises!")