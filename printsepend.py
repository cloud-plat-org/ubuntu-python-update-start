# Recommended modern approach
today = "Monday"
name = "Alex"
print(f"Hello, {name}. The day is {today}")
print(f"Hello, {name}", f"The day is {today}", sep=" | ")

# For special cases with multiple variables:
print("Hello", name, "The day is", today, sep=" | ", end="---\n")
