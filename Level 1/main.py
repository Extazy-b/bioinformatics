from json import load


step = 3
start = 'ATG'
stop = ('TAA', 'TAG', 'TGA')
min_len = 75
with open("./code.json") as f: code = load(f)


def fasta_to_data(file: str) -> dict[str]:
    result = {}
    with open(file) as f:
        name = ''
        for line in f:
            if line[0] == '>':
                name = line[:-1]
                result[name] = ''
            else:
                result[name] += line[:-1]
    return result


def data_to_file(file: str, data: dict[str]) -> None:
    with open(file, 'w') as f:
        for key in data.keys():
            f.write(key + '\n')
            for note in data[key]:
                f.write('\t' + str(note) + '\n')
            f.write('\n')


def compliment(seq: str) -> str:
    result = ''
    for let in seq[::-1]:
        if let == 'A':
            result += 'T'
        elif let == 'T':
            result += 'A'
        elif let == 'C':
            result += 'G'
        elif let == 'G':
            result += 'C'
    return result


def find(seq: str, dir: int) -> list[tuple[str, int, int, str]]:
    result = []
    for i in range(3):
        tmp_protein = ''
        tmp_start = 0
        flag = False
        lenght = len(seq)
        for let in range(i, len(seq)-2, step):
            if tmp_start:
                if seq[let:let+3] in stop:
                    if let - tmp_start > min_len:
                        if dir:
                            result.append(('forward', tmp_start, let+3, tmp_protein))
                        else:
                            result.append(('backward',lenght - tmp_start + 1, lenght - let - 2, tmp_protein))
                    tmp_start = 0
                    tmp_protein = ''
                else:
                    tmp_protein += code[seq[let]][seq[let+1]][seq[let+2]]
            elif seq[let:let+3] == start:
                tmp_start = let + 1
                tmp_protein += code[seq[let]][seq[let+1]][seq[let+2]]
    return result


data = fasta_to_data("./fasta.txt")

result = {}
for key in data.keys():
    seq = data[key]
    proteins = find(seq, 1) + find(compliment(seq), 0)
    result[key] = sorted(proteins, key=lambda x: -abs(x[2] - x[1]))


data_to_file("./result.txt", result)