#!/usr/bin/env julia

n = 1

for i = 1:20
    global n = lcm(n, i)
end

println(n)
