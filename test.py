2#!/usr/bin/python
import json
import auth

# get specific invoice
json_single = auth.xero.invoices.get(u'e4a0afbd-aea0-450b-ae23-0ce921e84a77')

# get all invoices
json_all = auth.xero.invoices.all()

######################
# TESTING GET METHOD #
######################

# print all data for single invoice
# TypeError: datetime.datetime(2016, 6, 24, 17, 10, 44, 150000) is not JSON serializable
# ^using json.dumps() ???
print "PRINTING SINGLE INVOICE"
print json_single
print json_single[0]						
print "\n"

# print pretty data under Addresses array
print "PRINTING INVOICE ADDRESS INFO"
print(json.dumps(json_single[0]['Contact']['Addresses'], indent=2))
print "\n"

# printing all "AddressType" of Addresses inside single invoice
print "OTHER"
for item in json_single[0]['Contact']['Addresses']:
	print "Printing Address Type"
	print item["AddressType"]
	print "\n"

# print data from each invoice
#for item in json_all:
#	print "PRINTING EACH INVOICE INFO"
#	print item
#	print "\n"

######################
# TESTING PUT METHOD #
######################




#######################
# TESTING POST METHOD #
#######################





