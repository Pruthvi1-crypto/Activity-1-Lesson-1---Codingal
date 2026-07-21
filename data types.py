
# Store Raj's friends' birthdays
birthdays = {
	'Arjun': '2014-07-03',      # 3 July 2014
	'Pruthvi': '2014-08-28',    # 28 August 2014
	'Darsh': '2013-12-01',      # 1 December 2013
	'Atharv': '2014-06-05',     # 5 June 2014
	'Anay': '2013-04-03'        # 3 April 2013
}
print("Raj's friends' birthdays are:")
for friend, birthday in birthdays.items():
    print(friend + " was born on " + birthday)
