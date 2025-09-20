# Codewars collections

[![Views statistics +1 👀](https://img.shields.io/badge/dynamic/xml?color=success&label=views&query=//*[name()=%27text%27][3]&url=https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fanviks%2Fcodewars-collections)](https://hits.seeyoufarm.com/api/count/graph/dailyhits.svg?url=https://github.com/anviks/codewars-collections)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/anviks/codewars-collections)
![Total code lines](https://img.shields.io/endpoint?url=https://ghloc.vercel.app/api/anviks/codewars-collections/badge&label=Total%20code%20lines&color=red)

[![Profile badge](https://www.codewars.com/users/anviks/badges/large)](https://www.codewars.com/users/anviks)

[Codewars](https://www.codewars.com) is an online educational platform for computer programming.
On the platform, users known as *code warriors* attempt to solve programming challenges, known as
*kata*, to practice programming skills and earn honor points. Each kata is assigned a *kyū* rank
based on its subject and difficulty (8 kyū being the easiest and 1 kyū being the most difficult).
The more difficult the kata, the more points will be awarded.
All code warriors start at a rank of 8 kyū and advance through the ranks to the final 2 dan.

## Overview

This repository contains my solutions, translations and forks of katas I have completed on Codewars.
grouped by language and difficulty level. Each kata is stored in a separate folder, named after the
kata's slug. Inside each folder, you will find the following files:

- `README.md` - a description of the kata, including the problem statement, examples, and notes.
- `solution_{slug}.{ext}`/`{slug}_solution.{ext}`/`{solution_class}.{ext}` - a file containing my solution to the kata.
- `test_{slug}.{ext}`/`{slug}_test.{ext}`/`{test_class}.{ext}` - a file containing the test cases for the kata.
- Additional files depending on the language (`mod.rs` in rust solutions, header files in C and C++ solutions, etc.).

Generally, I don't include solutions, that are easier than 6 kyu, because most of
them are simple enough, that even copying them here takes more time,
than just solving them in the codewars editor.

## Quick access table

| Language   | 7 kyu                                                          | 6 kyu                                                          | 5 kyu                                                          | 4 kyu                                                          | 3 kyu                                                          | 2 kyu                                                          | 1 kyu                                                          |
|------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| C          | [✅](c/src/solutions/7kyu)                                      | [✅](c/src/solutions/6kyu)                                      | [✅](c/src/solutions/5kyu)                                      | [✅](c/src/solutions/4kyu)                                      | [✅](c/src/solutions/3kyu)                                      | [✅](c/src/solutions/2kyu)                                      | [✅](c/src/solutions/1kyu)                                      |
| C++        | [✅](cpp/src/solutions/7kyu)                                    | [✅](cpp/src/solutions/6kyu)                                    | [✅](cpp/src/solutions/5kyu)                                    | [✅](cpp/src/solutions/4kyu)                                    | [✅](cpp/src/solutions/3kyu)                                    | [✅](cpp/src/solutions/2kyu)                                    | [✅](cpp/src/solutions/1kyu)                                    |
| Go         | [✅](go/src/solutions/7kyu)                                     | [✅](go/src/solutions/6kyu)                                     | [✅](go/src/solutions/5kyu)                                     | [✅](go/src/solutions/4kyu)                                     | [✅](go/src/solutions/3kyu)                                     | [✅](go/src/solutions/2kyu)                                     | [✅](go/src/solutions/1kyu)                                     |
| Java       | [✅](java/src/main/java/me/anviks/codewars/solutions/_7kyu)     | [✅](java/src/main/java/me/anviks/codewars/solutions/_6kyu)     | [✅](java/src/main/java/me/anviks/codewars/solutions/_5kyu)     | [✅](java/src/main/java/me/anviks/codewars/solutions/_4kyu)     | [✅](java/src/main/java/me/anviks/codewars/solutions/_3kyu)     | [✅](java/src/main/java/me/anviks/codewars/solutions/_2kyu)     | [✅](java/src/main/java/me/anviks/codewars/solutions/_1kyu)     |
| Javascript | [✅](javascript/src/solutions/7kyu)                             | [✅](javascript/src/solutions/6kyu)                             | [✅](javascript/src/solutions/5kyu)                             | [✅](javascript/src/solutions/4kyu)                             | [✅](javascript/src/solutions/3kyu)                             | [✅](javascript/src/solutions/2kyu)                             | [✅](javascript/src/solutions/1kyu)                             |
| Kotlin     | [✅](kotlin/src/main/kotlin/me/anviks/codewars/solutions/_7kyu) | [✅](kotlin/src/main/kotlin/me/anviks/codewars/solutions/_6kyu) | [✅](kotlin/src/main/kotlin/me/anviks/codewars/solutions/_5kyu) | [✅](kotlin/src/main/kotlin/me/anviks/codewars/solutions/_4kyu) | [✅](kotlin/src/main/kotlin/me/anviks/codewars/solutions/_3kyu) | [✅](kotlin/src/main/kotlin/me/anviks/codewars/solutions/_2kyu) | [✅](kotlin/src/main/kotlin/me/anviks/codewars/solutions/_1kyu) |
| PHP        | [✅](php/src/solutions/7kyu)                                    | [✅](php/src/solutions/6kyu)                                    | [✅](php/src/solutions/5kyu)                                    | [✅](php/src/solutions/4kyu)                                    | [✅](php/src/solutions/3kyu)                                    | [✅](php/src/solutions/2kyu)                                    | [✅](php/src/solutions/1kyu)                                    |
| Python     | [✅](python/src/solutions/7kyu)                                 | [✅](python/src/solutions/6kyu)                                 | [✅](python/src/solutions/5kyu)                                 | [✅](python/src/solutions/4kyu)                                 | [✅](python/src/solutions/3kyu)                                 | [✅](python/src/solutions/2kyu)                                 | [✅](python/src/solutions/1kyu)                                 |
| Rust       | [✅](rust/src/solutions/_7kyu)                                  | [✅](rust/src/solutions/_6kyu)                                  | [✅](rust/src/solutions/_5kyu)                                  | [✅](rust/src/solutions/_4kyu)                                  | [✅](rust/src/solutions/_3kyu)                                  | [✅](rust/src/solutions/_2kyu)                                  | [✅](rust/src/solutions/_1kyu)                                  |
| Typescript | [✅](typescript/src/solutions/7kyu)                             | [✅](typescript/src/solutions/6kyu)                             | [✅](typescript/src/solutions/5kyu)                             | [✅](typescript/src/solutions/4kyu)                             | [✅](typescript/src/solutions/3kyu)                             | [✅](typescript/src/solutions/2kyu)                             | [✅](typescript/src/solutions/1kyu)                             |
