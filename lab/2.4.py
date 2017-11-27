# coding: utf-8
zero = int(raw_input("Dolna"))
liczba = int(raw_input("Gorna"))
while (zero <= liczba):
  if(zero % 17 == 0 and zero % 2 == 1):
     print zero
     zero = zero + 1
  else:
      zero = zero + 1
