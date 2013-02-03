#!/usr/bin/env python
# Solves RSA "manually", showing all work
# Usage: Public domain
# Author: Daniel Farrell

import fractions

# Default message is 7, only p and q required to run test
def do_rsa(p, q, e = None, m = 7, sign_verify = False):
  # Show given data
  print "Given:\np =", p, "\nq =", q, "\ne =", e, "\nm =", m

  # Step one
  print "\nStep one is done since we are given p and q, such that they are two distinct prime numbers."

  # Step two
  print "\nStep two, get n where n = pq"
  print "n =", p,"*",q
  n = p * q
  print "n =", n 

  # Step three
  print "\nStep three, get \"phe\" where phe(n) = (p - 1)(q - 1)"
  print "phe(" + str(n) + ") = (" + str(p) + " - 1)(" + str(q) + " - 1)"
  phe = (p - 1) * (q - 1)
  print "phe(" + str(n) + ") =", phe

  # Step four
  print "\nStep four, select e such that e is relatively prime to phe(n); gcd(phe(n), e) = 1 where 1 < e < phe(n)"
  print "gcd(" + str(phe) +  ", e) = 1; 1 < e <", phe

  if e is not None:
    print "Given: e =", e
  else:
    for pos_e in range(2, phe):
      if fractions.gcd(phe, pos_e) == 1:
        e = pos_e
        print "gcd(" + str(phe) +  ",", str(e) + ") = 1; 1 <", e, "<", phe
        print "e =", e
        break

  # Step five
  print "\nStep five, determine d such that d*e % phe(n) = 1; d < phe(n)"
  print "d *", e, "%", phe, "= 1; d <", phe

  d = None
  for pos_d in range(1, phe):
    if ((pos_d * e) % phe) == 1:
      d = pos_d
      print d, "*", e, "%", phe, "= 1;", d, "<", phe
      break

  print "d =", d

  # Find public key
  print "\nPublic key KU = [e, n]"
  print "KU = [" + str(e) + ", " + str(n) + "]"

  # Find private key
  print "\nPrivate key KR = [d, n]"
  print "KR = [" + str(d) + ", " + str(n) + "]"

  # Do encryption
  print "\nEncryption c = m^e % n; m < n"
  print "c =", str(m) + "^" + str(e), "%", str(n) + ";", m, "<", n
  c = m**e % n
  print "c =", c

  # Do decryption
  print "\nDecryption m = c^d % n"
  print "m =", str(c) + "^" + str(d), "%", str(n)
  found_m = c**d % n
  print "m =", found_m

  # Confirm result
  if found_m != m:
    print "Failure: Decrypted message is incorrect"
  else:
    print "Success: Message decrypted correctly"

  # If not doing signature, exit
  if not sign_verify:
    return

  # Find signature
  print "\nSign s = m^d % n; m < n"
  print "s =", str(m) + "^" + str(d), "%", str(n) + ";", m, "<", n
  s = m**d % n
  print "s =", s

  # Verify signature
  print "\nVerify m = s^e % n"
  print "m =", str(s) + "^" + str(e), "%", str(n)
  verify_m = s**e % n
  print "m =", verify_m

  # Confirm result
  if verify_m != m:
    print "Failure: Message verification failed"
  else:
    print "Success: Message verification succeeded"
    

print "PROBLEM 21.6 A\n"
do_rsa(p = 3, q = 11, e = 7, m = 5)
print "\n\nPROBLEM 21.6 B\n"
do_rsa(p = 5, q = 11, e = 3, m = 9)
print "\n\nPROBLEM 21.6 c\n"
do_rsa(p = 7, q = 11, e = 17, m = 8)
print "\n\nPROBLEM 21.6 D\n"
do_rsa(p = 11, q = 13, e = 11, m = 7)
print "\n\nPROBLEM 21.6 E\n"
do_rsa(p = 17, q = 31, e = 7, m = 2)

print "\n\nPROBLEM RSA\n"
do_rsa(p = 5, q = 31, m = 25, sign_verify = True)
