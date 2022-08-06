#!/usr/bin/env julia

num = 600851475143
i = 2

while i ^ 2 < num
    while num % i == 0
        global num = num ÷ i
    end
    global i += 1
end

println(num)
