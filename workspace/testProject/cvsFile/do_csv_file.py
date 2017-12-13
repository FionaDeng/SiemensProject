import os
import csv

"""
服务器实际存在的设备有：
1期：5个区*20栋*10单元
2期：5个区*20栋*1单元*20层*10房
格式：010001000101010101:[authentication username=010001000101010101 password=010001000101010101]
"""
class CSVMethod(object):
    csv.register_dialect('split', delimiter=':')

    def write_csvfile(self):
        with open('./csv_file2/reg_file.csv', 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile, dialect='split')
            # 室内机
            for area in range(1, 6):
                for build in range(1, 21):
                    for unit in range(1, 11):
                        room_format = '01' + '%04d%04d%02d010101'%(area, build, unit)
                        actual_output = '[authentication username=%s password=%s]'%(room_format,room_format)
                        writer.writerow([room_format,actual_output])

            for area in range(1, 6):
                for build in range(1, 21):
                    for floor in range(1, 21):
                        for room in range(1,11):
                            room_format = '02' + '%04d%04d01%02d%02d01'%(area, build, floor, room)
                            actual_output = '[authentication username=%s password=%s]'
                            writer.writerow([room_format, actual_output])

    def read_csvfile(self):
        file_open = open('./csv_file2/reg_file.csv', 'r', newline='')
        reader = csv.reader(file_open, dialect='split')
        count = 0
        for row in reader:
            if len(row) <= 1:
                continue
            if count % 1000 == 0:
                file_split = open('./csv_file2/reg_room_%d.csv'% (count // 1000), 'w', newline='', encoding='utf-8')
                subwriter = csv.writer(file_split, dialect='split')
            else:
                pass
            subwriter.writerow(row)
            count += 1

if __name__ == '__main__':
    temp = CSVMethod()
    temp.write_csvfile()
    temp.read_csvfile()





