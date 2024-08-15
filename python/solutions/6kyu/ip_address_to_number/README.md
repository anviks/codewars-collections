An [IPv4 address](http://en.wikipedia.org/wiki/IP_address) is a 32-bit number that identifies a device on the internet.

While computers read and write IP addresses as a 32-bit number, we prefer to read them in dotted-decimal notation, which is basically the number split into 4 chunks of 8 bits, converted to decimal, and delmited by a dot.

In this kata, you will create the function `ipToNum` (or `ip_to_num`, depending on the language) that takes an `ip` address and converts it to a number, as well as the function `numToIp` (or `num_to_ip`) that takes a number and converts it to an IP address string.  Input will always be valid.

## Conversion Example
'192.168.1.1' converts to 3232235777
'10.0.0.0'    converts to  167772160
'176.16.0.1'  converts to 2953838593
```
    
### numToIp / num_to_ip
```
3232235777 converts to '192.168.1.1'
 167772160 converts to    '10.0.0.0'
2953838593 converts to  '176.16.0.1'
```
