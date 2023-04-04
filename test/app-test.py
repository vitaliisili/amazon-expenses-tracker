import sys
import time

import pexpect

args = ["vitalii", "pass1A#", "1", "11-12-2023", "book", "10", "2", "2", "2", "3"]

child = pexpect.spawn("python3 ../amazon_expenses_tracker.py vitalii pass1A#", encoding='utf-8')
# child.logfile_read = sys.stdout



child.expect("Please enter phone number to continue: ")
child.sendline("+491234")

i = child.expect(['Phone number is not valid, .+ number', 'Please login .+ password'])

if i == 0:
    print("PHONE NOT VALID")
    child.kill(0)

if i == 1:
    print("PHONE OK")



# child.expect("Please enter phone number to continue: ")
# child.sendline("+491234567890")
#
child.expect("Username: ")
child.sendline("vitalii")

child.expect("Password: ")
child.sendline("pass1A#")

child.expect("Enter your choice .+: ")
child.sendline("1")

child.expect("Enter the date of the purchase in format .+: ")
child.sendline("11-12-2023")

child.expect("Enter the item purchased: ")
child.sendline("book")

child.expect("Enter the cost of the item in Euro: ")
child.sendline("10")

child.expect("Enter the weight of the item in kg: ")
child.sendline("2")

child.expect("Enter the quantity purchased: ")
child.sendline("2")

child.expect("Enter your choice .+: ")
child.sendline("2")

child.expect("Enter your choice .+: ")
child.sendline("3")



