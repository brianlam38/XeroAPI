#!/usr/bin/python
import json
import auth

# get specific invoice
json_single = auth.xero.invoices.get(u'e4a0afbd-aea0-450b-ae23-0ce921e84a77')

# get all invoices
json_all = auth.xero.invoices.all()