#!/usr/bin/python
import json
import auth

# get all invoices
inv_all = auth.xero.invoices.all()

# get all contacts
contacts_all = auth.xero.contacts.all()

####################
# TESTING INVOICES #
####################

# print invoice contact details
print "###### PRINTING INVOICE ######"
for item in inv_all:
	print item['Contact']
	print item['Contact']['Phones'], "\n"

#####################################
# TESTING CONTACTS & CONTACT GROUPS #
#####################################

# print data from first client in list
print "### FIRST CONTACT DATA ###"
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

# print all supplier client names and their emails
print "### NON-SUPPLIER CLIENT NAMES AND EMAILS ###"
for item in contacts_all:
	if item['IsSupplier'] == 0:
		print item['Name']
		if item.has_key('EmailAddress'):
			print item['EmailAddress'], "\n"
		else:
			print "N/A\n"

# get all contact groups
contactGroup_all = auth.xero.contactgroups.all()

# print all contact group details
print "### CONTACT GROUPS DATA ###"
for item in contactGroup_all:
	print "######", item['Name'], "######"
	print item['Status']


####################
# TESTING PAYMENTS #
####################

# get specific invoice
#contact_single = auth.xero.contacts.get(u'e4a0afbd-aea0-450b-ae23-0ce921e84a77')
# get all invoices
#contact_all = auth.xero.contact.all()






