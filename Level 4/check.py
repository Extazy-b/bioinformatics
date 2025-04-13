import sys
from collections import defaultdict

def get_total_lines(file_path):
    """Подсчет общего количества строк в файле"""
    with open(file_path, 'r') as f:
        return sum(1 for _ in f)

def check_fasta(file_path, report_interval=1000):
    """Анализ FASTA-файла с выводом прогресса"""
    total_lines = get_total_lines(file_path)
    processed = 0
    max_length = 0
    current_id = None
    sequences = defaultdict(list)
    duplicates = set()

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            processed += 1
            
            # Обновление прогресса
            if processed % report_interval == 0 or processed == total_lines:
                remaining = total_lines - processed
                print(f"Обработано: {processed}/{total_lines} | "
                      f"Осталось: {remaining} | "
                      f"Текущий максимум: {max_length} bp", flush=True)
            
            if line.startswith('>'):
                current_id = line[1:].split()[0]
                if current_id in sequences:
                    duplicates.add(current_id)
                sequences[current_id].append('')
            elif current_id is not None:
                sequences[current_id][-1] += line
                max_length = max(max_length, len(sequences[current_id][-1]))

    # Вывод итогов
    print("\nРезультаты:")
    print(f"Максимальная длина последовательности: {max_length} bp")
    print(f"Уникальных идентификаторов: {len(sequences)}")
    print(f"Найдено дубликатов ID: {len(duplicates)}")
    if duplicates:
        print("\nПримеры дубликатов:")
        for i, dup in enumerate(list(duplicates)[:5], 1):
            print(f"{i}. {dup}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python fasta_check.py <file.fasta>")
        sys.exit(1)
        
    check_fasta(sys.argv[1])
