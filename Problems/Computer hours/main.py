# Make sure your output matches the assignment *exactly*
duration = int(input())
print(
    "That's rare nowadays!" if duration < 2 else
    "This seems reasonable" if duration < 4 else
    "Don't forget to take breaks!"
)
