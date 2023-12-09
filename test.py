from WSPR import WSPR

wspr = WSPR()

callsign = 'ON3URE'
locator = 'JO20'
dbm = 30

print('{%s}' % ','.join(
        str(x) for x in wspr.wspr_encode(callsign, locator, dbm)))