# Level 1: Basic Functions - Sample Code
# Here's how to write functions that do something fun every time you call them!

# Party Playlist Function

# This function plays your favorite song whenever you call it
# Notice how you write the function once with def, then call it as many times as you want
def play_favorite_song():
    print("🎵 Now playing: Your favorite song!")
    print("♪ La la la, this song is amazing! ♪")
    print("🎶 Dance party time! 🎶")

# Call the function to make it work
play_favorite_song()
# You can call it again
play_favorite_song()

# Pet Simulator Function

# This function feeds your virtual pet and shows you how happy they are
# The function does the same thing every time, perfect for repetitive tasks
def feed_virtual_pet():
    print("🐱 Your cat is purring! She loved the treats!")
    print("  /\\_/\\  ")
    print(" ( ^.^ ) ")
    print("  > ^ <  ")
    print("Happiness level: MAX! 💕")

# Feed your pet
feed_virtual_pet()




# Level 2: Functions with Parameters - Sample Code
# Now we're adding parameters so the function can do different things based on what you tell it!

# Personalized Greeting Generator
# The name parameter lets you customize the greeting for anyone
# Whatever you put in the parentheses becomes the value of name inside the function
def greet_friend(name):
    print(f"Hey {name}! You're awesome! 🌟")
    print(f"So glad to see you, {name}!")

# Try it with different names
greet_friend("Emma")
greet_friend("Sofia")
greet_friend("Alex")

# Custom Smoothie Maker
# This function takes TWO parameters so you can customize both the fruit and topping
# The order matters: first parameter is fruit, second is topping
def make_smoothie(fruit, topping):
    print(f"🥤 One {fruit} smoothie with {topping} coming right up!")
    print(f"Blending {fruit}... adding {topping}... Perfect! ✨")

# Make different smoothies
make_smoothie("strawberry", "chocolate chips")
make_smoothie("mango", "coconut flakes")
make_smoothie("blueberry", "granola")

# Social Media Post Creator
# This function combines two pieces of information to create a fun status update
# You can use parameters to make your functions super flexible
def post_status(mood, activity):
    print(f"📱 New Post: Feeling {mood} while {activity}! 💻✨")
    print(f"❤️ 47 likes | 💬 12 comments")

# Create different posts
post_status("excited", "learning to code")
post_status("happy", "playing with my dog")
post_status("creative", "drawing digital art")


# Level 3: Functions with Return Values - Sample Code
# These functions calculate something and give you back a result using return!

# Friendship Score Calculator

# The return keyword sends the calculated score back to wherever you called the function
# Then you can use that score to make decisions
def calculate_friendship_score(shared_interests, inside_jokes):
    total_score = shared_interests + inside_jokes
    return total_score

# Get the score and use it
my_score = calculate_friendship_score(8, 12)
print(f"Your friendship score is: {my_score}")

# Use the score to determine friendship level
if my_score > 15:
    print("🌟 BFF Status!")
elif my_score >= 10:
    print("😊 Great Friends!")
else:
    print("👋 Getting There!")


# Gaming Level Calculator

# This function does math and returns the result
# Notice how we can use the returned value in other calculations or comparisons
def calculate_xp(monsters_defeated, quests_completed):
    monster_xp = monsters_defeated * 10
    quest_xp = quests_completed * 50
    total_xp = monster_xp + quest_xp
    return total_xp

# Calculate your XP
my_xp = calculate_xp(15, 3)
print(f"You earned {my_xp} XP!")

# Check if you leveled up
if my_xp >= 200:
    print("🎉 LEVEL UP! You're now level 2!")
else:
    print(f"You need {200 - my_xp} more XP to level up!")

# Allowance Tracker
# This function returns money saved so you can check if you can afford something
# The returned value is like getting an answer back from the function
def calculate_savings(weeks, weekly_amount):
    total_saved = weeks * weekly_amount
    return total_saved

# See how much you would save
savings = calculate_savings(8, 10)
print(f"After 8 weeks, you'll have ${savings}!")

# Check if you can buy something
game_price = 60
if savings >= game_price:
    print(f"🎮 Yes! You can buy that game!")
else:
    print(f"💰 Save ${game_price - savings} more to get it!")






#############################################################
# Bonus Challenge: Dream Room Designer - Complete Program
# Here's how all three types of functions work together in one awesome program!

# Function with parameter but no return value
def paint_walls(color):
    print(f"🎨 Painting walls {color}... Looking great!")

# Function with parameter but no return value
def add_furniture(item):
    print(f"🛋️ Adding {item} to your room!")

# Function with parameter AND return value
def calculate_room_awesomeness(num_decorations):
    awesomeness = num_decorations * 10
    return awesomeness

# Design your dream room
print("=== DREAM ROOM DESIGNER ===")
paint_walls("lavender")
paint_walls("one accent wall in teal")
add_furniture("a cozy reading nook")
add_furniture("LED strip lights")
add_furniture("a gaming chair")

# Calculate final awesomeness
score = calculate_room_awesomeness(5)
print(f"\n✨ Room Awesomeness Score: {score}/100")

# Evaluate the room
if score >= 50:
    print("🌟 Your room is AMAZING!")
else:
    print("👍 Your room is pretty cool!")



# Quick Tips for Running Your Code
# Copy any of these code blocks into your Python editor like IDLE, VS Code, or Replit 
# and run them to see the magic happen! Try changing the values when you call the functions 
# to learn what each part does. 
# Experiment by mixing and matching by calling the same function multiple times with different inputs 
# to see how flexible functions are. The best way to learn is by playing around with the code and breaking things, 
# then fixing them!
print("yey! 😜")