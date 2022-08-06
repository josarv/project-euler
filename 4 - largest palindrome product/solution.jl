#!/usr/bin/env julia

function is_palindrome(n)
    s = string(n)
    return s == reverse(s)
end

println(maximum(filter(is_palindrome, [i * j for i in 999:-1:100 for j in 999:-1:100])))
