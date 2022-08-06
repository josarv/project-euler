#!/usr/bin/env julia

println(maximum(filter(function(n) s = string(n); return s == reverse(s) end, [i * j for i in 999:-1:100 for j in 999:-1:100])))
