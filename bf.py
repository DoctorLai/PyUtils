#!/usr/bin/env python
# http://acm.zhihua-lai.com
# Brainfuck Interpreter

from __future__ import print_function

# tuning machine has infinite array size
# increase or decrease here accordingly
arr = [0] * 30000
ptr = 0

def bf(src, left, right, data, idx):
    """
        brainfuck interpreter
        src: source string
        left: start index
        right: ending index
        data: input data string
        idx: start-index of input data string
    """
    if len(src) == 0: return
    global arr, ptr
    if left < 0: left = 0
    if left >= len(src): left = len(src) - 1
    if right < 0: right = 0
    if right >= len(src): right = len(src) - 1
    i = left
    while i <= right:
        s = src[i]
        if s == '>':
            ptr += 1
            # wrap if out of range
            if ptr >= len(arr):
                ptr = 0
        elif s == '<':
            ptr -= 1
            # wrap if out of range
            if ptr < 0:
                ptr = len(arr) - 1
        elif s == '+':
            arr[ptr] += 1
        elif s == '-':
            arr[ptr] -= 1
        elif s == '.':
            print(chr(arr[ptr]), end="")
        elif s == ',':
            if idx >= 0 and idx < len(data):
                arr[ptr] = data[idx]
                idx += 1
            else:
                arr[ptr] = 0 # out of input
        elif s =='[':
            j = i + 1
            while j <= right and src[j] != ']': j += 1
            if j <= right:
                while arr[ptr] > 0:
                    bf(src, i + 1, j - 1, data, idx)
                i = j
        i += 1

if __name__ == "__main__":
    src = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
    bf(src, 0, len(src) - 1, "", 0)
