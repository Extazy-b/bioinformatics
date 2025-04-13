of = open("formed.fasta", 'w')

with open("./result.fasta") as f:
    for line in f:
        if line[0] != '>':
            of.write(line)
            continue
        new_line = ""
        i = 0
        for let in line:
            if i == 98:
                break

            if (ord(let.upper()) in range(65, 91)) or \
               (ord(let.upper()) in range(48, 58)) or \
               (ord(let.upper()) in (62, 95)):
                new_line += let.upper()
            else:
                new_line += '_'
            
            i += 1
        of.write(new_line)
        of.write('\n')
of.close()