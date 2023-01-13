import re


with open("./potential-contacts.txt", "r") as f:
    text_from_file = f.read()

# same pattern as before
phone_pattern = r"\b(?:\+?1[-. ]?)?\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})|([0-9]{7})\b$"
email_pattern = r"[\w.+-]+@[\w-]+\.[\w.-]+"

# re.findall() return a list of matches

phone_nums = set(re.findall(phone_pattern, text_from_file))
email_addy = set(re.findall(email_pattern, text_from_file))


# re.search() searches the entire string, but stops after the first

print(phone_nums)
print(email_addy)

phone_nums = sorted(phone_nums)
email_addy = sorted(email_addy)

new_phone_list = ['{}-{}-{}'.format(number[0], number[1], number[2]) for number in phone_nums]


# Add to files

with open("new_emails.txt", "w") as f:
    for emails in email_addy:
        f.write(emails + "\n")

with open("new_contacts.txt", "w") as f:
    for numbers in new_phone_list:
        f.write(numbers + "\n")


# assert len(phone_nums) == 10
print(f"Found {len(phone_nums)} phone numbers")
print(f"Found {len(email_addy)} email addresses")

