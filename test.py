#!/usr/bin/python
import json
import auth

####################
# TESTING INVOICES #
####################
'''
# get specific invoice
inv_single = auth.xero.invoices.get(u'e4a0afbd-aea0-450b-ae23-0ce921e84a77')
# get all invoices
inv_all = auth.xero.invoices.all()

# print all data for single invoice
# TypeError: datetime.datetime(2016, 6, 24, 17, 10, 44, 150000) is not JSON serializable
# ^using json.dumps() ???
print "### PRINTING SINGLE INVOICE ###"
print inv_single
print inv_single[0]						
print "\n"

# print pretty data under Addresses array
print "### PRINTING INVOICE ADDRESS INFO ### "
print(json.dumps(inv_single[0]['Contact']['Addresses'], indent=2))
print "\n"

# printing all "AddressType" of Addresses inside single invoice
print "### PRINTING ADDRESSTYPES ###"
for item in inv_single[0]['Contact']['Addresses']:
	print "Printing Address Type"
	print item["AddressType"]
	print "\n"

# print data from each invoice
for item in inv_all:
	print "PRINTING EACH INVOICE INFO"
	print item
	print "\n"#
'''
####################
# TESTING CONTACTS #
####################

# get specific contact
contacts_single = auth.xero.contacts.get(u'565acaa9-e7f3-4fbf-80c3-16b081ddae10')
# get all contacts
contacts_all = auth.xero.contacts.all()

# print data from first client in list
print "### ALL CONTACT DATA ###"
print contacts_all[0]

# print all non-suppleir client names and their emails
print "### NON-SUPPLIER CLIENT NAMES AND EMAILS ###"
for item in contacts_all:
	if item['IsSupplier'] == 1:
		print item['Name']
		if item.has_key('EmailAddress'):
			print item['EmailAddress'], "\n"
		else:
			print "N/A\n"

# print all suppleir client names and their emails
print "### NON-SUPPLIER CLIENT NAMES AND EMAILS ###"
for item in contacts_all:
	if item['IsSupplier'] == 0:
		print item['Name']
		if item.has_key('EmailAddress'):
			print item['EmailAddress'], "\n"
		else:
			print "N/A\n"



####################
# TESTING PAYMENTS #
####################

# get specific invoice
#contact_single = auth.xero.contacts.get(u'e4a0afbd-aea0-450b-ae23-0ce921e84a77')
# get all invoices
#contact_all = auth.xero.contact.all()






