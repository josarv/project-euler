cmake_minimum_required(VERSION 3.23)
project(project_euler C)

set(CMAKE_C_STANDARD 11)

add_executable(1 "1 - multiples of 3 or 5/solution.c")
add_executable(2 "2 - even fibonacci numbers/solution.c")
add_executable(3 "3 - largest prime factor/solution.c")
target_link_libraries(3 PRIVATE m)