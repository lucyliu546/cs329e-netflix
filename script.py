import sys

def truncate(reader, writer):
    for line in reader:
        line.strip()
        if line[-1] != ':':
            temp = line.split(',')
            writer.write(temp[0])
            writer.write('\n')
            continue
        writer.write(line.strip())
        writer.write('\n')
truncate(sys.stdin, sys.stdout)
