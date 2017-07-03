#!/usr/bin/python
import auth

# grab all invoice data
inv = auth.xero.invoices.all()
# grab all contact data
contacts = auth.xero.contacts.all()
# get all contact groups
contactGroup = auth.xero.contactgroups.all()
# grab all payments data
payments = auth.xero.payments.all()


####################
# TESTING INVOICES #
####################

# print invoice contact details
print "###### PRINTING INVOICE DATA ######"
for item in inv:
	c = auth.xero.contacts.get(item['Contact']['ContactID'])
	#print c[0]
	print "NAME / COMPANY:", c[0]['Name']
	print "DATE CREATED:", item['Date']
	print "DUE DATE:", item['DueDate']
	print "INVOICE NO:", item['InvoiceNumber']
	print "REFERENCE (PROJ NO):", item['Reference']
	print "UNIT:", "???"
	print "DESCRIPTION:", "???"
	print "SUBTOTAL:", item['SubTotal']
	print "TOTAL:", item['Total']
	print "GST:", item['TotalTax']
	print "ACCOUNT:", "???"
	print "STATUS:", item['Status'] #status every 15 mins
	print "\n"

#####################################
# TESTING CONTACTS & CONTACT GROUPS #
#####################################

# print data from first client in list
print "### FIRST CONTACT DATA ###"
print contacts[0]

# print all non-suppleir client names and their emails
print "### NON-SUPPLIER CLIENT NAMES AND EMAILS ###"
for item in contacts:
	if item['IsSupplier'] == 1:
		print item['Name']
		if item.has_key('EmailAddress'):
			print item['EmailAddress'], "\n"
		else:
			print "N/A\n"

# print all supplier client names and their emails
print "### NON-SUPPLIER CLIENT NAMES AND EMAILS ###"
for item in contacts:
	if item['IsSupplier'] == 0:
		print item['Name']
		if item.has_key('EmailAddress'):
			print item['EmailAddress'], "\n"
		else:
			print "N/A\n"

# print all contact group details
print "### CONTACT GROUPS DATA ###"
for item in contactGroup:
	print "######", item['Name'], "######"
	print item['Status']


####################
# TESTING PAYMENTS #
####################






