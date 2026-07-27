name = input("Enter your Name: ")
date = "Oct 10"

letter = '''Dear, {}. You are Selected!.{} '''
print(letter.format(name.capitalize(), date))

print(f'Dear, {name.capitalize()}. You are Selected!.{date}')