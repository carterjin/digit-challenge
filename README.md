# digit-challenge
A program solver based on python for a certain kind of online interview digit test

## The Problem

You are given a few known and unknown numbers and the operations and the final answer, you need to find the unknown numbers
that produce the final answer.
At most 4 numbers are given and you can't choose repeating numbers

![]('digit_image.jpeg')

## My Solution

First the user input an expression include ? as the unknown numbers. To address the parenthesis and */+- priority issues, the expression is converted to a stack using the Shunting-yard algorithm.

https://en.wikipedia.org/wiki/Shunting-yard_algorithm

Then a list of all possible number combination are generated as a list, each combination is checked to see if it produces the desired result.
