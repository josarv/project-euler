#!/usr/bin/env julia

println(maximum(i * j for i in 999:-1:100 for j in 999:-1:100 if string(i * j) == reverse(string(i * j))))
