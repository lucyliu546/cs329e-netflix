import sys

def truncate(reader, writer):
    for line in reader:
        line.strip()
        line = line[:-13]
        writer.write(line)
        writer.write('\n')

truncate(sys.stdin, sys.stdout)
