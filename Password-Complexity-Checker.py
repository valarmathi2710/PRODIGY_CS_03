def assess_password_strength(password):
  length = len(password)
  has_lowercase = any(char.islower() for char in password)
  has_uppercase = any(char.isupper() for char in password)
  has_digit = any(char.isdigit() for char in password)
  has_special = any(char in '!@#$%^&*()-_+=[]{}|:;"\',.<>?/~`' for char in password)

  strength = 0

  if length >= 8:
      strength += 1
  if has_lowercase:
      strength += 1
  if has_uppercase:
      strength += 1
  if has_digit:
      strength += 1
  if has_special:
      strength += 1

  if strength == 5:
      return "Strong"
  elif strength >= 3:
      return "Moderate"
  else:
      return "Weak"

# Example usage:
password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Password strength:", strength)
