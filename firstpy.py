#!usr/bin/python
from xero import Xero
from xero.auth import PrivateCredentials

keystring = "KEYSTRING"
credentials = PrivateCredentials("QSIAPZ0......", keystring)
xero = Xero(credentials)
xero.contacts.all()