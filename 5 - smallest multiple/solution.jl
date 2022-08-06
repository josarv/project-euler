#!/usr/bin/env julia

println(reduce((x, y) -> lcm(x, y), 1:20))
