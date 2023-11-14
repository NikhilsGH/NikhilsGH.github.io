
def is_palindrome(string):
  stack = []
  for char in string:
    stack.append(char)
  for char in string:
    if char != stack.pop():
      return False
  return True


string = input("Please enter a word or phrase to be tested: ")

if is_palindrome(string):
  print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")




