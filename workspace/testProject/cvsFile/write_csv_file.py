import csv


class CsvMethod(object):
    def writeInCvs(self):
        file_dir = "./csv_file2/csv_test.csv"
        csv_file = open(file_dir, 'w', encoding='utf-8', newline='')
        writer = csv.writer(csv_file)
        writer.writerow(['id', 'url'])
        data = [('1', 'xxxxxxx'),
                ('2', 'ccccccc')]
        writer.writerows(data)
        csv_file.close()

if __name__ == '__main__':
    init_ = CsvMethod()
    init_.writeInCvs()