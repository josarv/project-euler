fibonacci(previous, current, n) = current > 4e6 ? n : fibonacci(current, previous + current, current % 2 == 1 ? n : n + current)
println(fibonacci(1, 2, 0))
