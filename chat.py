from hashlib import new
import os


def read_file(filename):
    lines = []
    with open(filename, 'r' , encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Sing':
            person = 'Sing'
            continue
        elif line == 'Vicky':
            person = 'Vicky'
            continue
        
        if person:
            new.append(person + ': ' + line)
    return new

def white_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    white_file('output.txt', lines)

main()