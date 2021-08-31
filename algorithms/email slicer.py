email_id = input(f'Enter your email id ').strip()
username = email_id[:email_id.index('@')]
domain = email_id[email_id.index('@') + 1:]

print(f'Your username: {username}\nYour domain name: {domain}')

