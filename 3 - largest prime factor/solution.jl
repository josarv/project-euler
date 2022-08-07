#!/usr/bin/env julia

import Pkg
Pkg.add("Primes")
import Primes

n = 600_851_475_143
println(iterate(n ÷ i for i in 1:n if n % i == 0 && Primes.isprime(n ÷ i))[1])
