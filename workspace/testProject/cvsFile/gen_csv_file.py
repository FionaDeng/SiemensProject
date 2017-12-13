"""
功能: 生成csv文件，第一行为SEQUENTIAL，
    其他行格式为：010001000101010101;[authentication username=010001000101010101 password=010001000101010101]
    这里面的id：010001000101010101为实际的设备号，如室内机、梯口机、围墙机、管理机

设备定义方式：
    期(issue): 01
    区(area): 0001
    栋(build): 0001
    单元(unit): 01
    层(floor): 01
    房(room): 01
    "%2d%4d%4d%2d%2d%2d" ->>> "{期}{区}{栋}{单元}{层}{房}
    室内机：010001000101010101
    梯口机：010001000101000001
    围墙机：010001000000000050（区）   010000000000000050（期）
    管理机：010001000000000001（区)    010000000000000001（期）

服务器实际存在的设备有：
1期：5个区*20栋*10单元期：5个区*20栋*1单元*20层*10房

"""
import os
import csv


csv.register_dialect('split', delimiter=';')   # 使用适当的分隔符来注册一种新的dialect，dialect默认是逗号分隔符，指定的分隔符是“;”
with open('./csv_file/reg_all.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, dialect='split')
    writer.writerow(['SEQUENTIAL'])
    # 室内机 010001000101010101
    for area in range(1,6):
        for build in range(1, 21):
            for unit in range(1, 11):
                room_dev = '01' + '%04d%04d%02d010101'% (area, build, unit)
                auth = '[authentication username=%s password=%s]'%(room_dev, room_dev)
                writer.writerow([room_dev, auth])
    for area in range(1, 6):
        for build in range(1,21):
            for floor in range(1,21):
                for room in range(1, 11):
                    room_dev = '02' + '%04d%04d01%02d%02d01' % (area, build, floor, room)
                    auth = '[authentication username=%s password=%s]' % (room_dev, room_dev)
                    writer.writerow([room_dev, auth])
    # 围墙机
    for issue in range(1,3):
        for area in range(0,6):
            wall_dev = '%02d%04d'%(issue, area) + '000000000050'
            auth = '[authentication username=%s password=%s]' % (wall_dev, wall_dev)
    # 管理机
    for issue in range(1,3):
        for area in range(0,6):
            manage_dev = '%02d%04d'%(issue, area) + '000000000001'
            auth = '[authentication username=%s password=%s]' % (manage_dev, manage_dev)

with open('./csv_file/reg_stair.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, dialect='split')
    writer.writerow(['SEQUENTIAL'])
    # 梯口机
    for area in range(1,6):
        for build in range(1, 21):
            for unit in range(1, 11):
                stair_dev = '01' + '%04d%04d%02d000001'% (area, build, unit)
                auth = '[authentication username=%s password=%s]'%(stair_dev, stair_dev)
                writer.writerow([stair_dev, auth])

# 将reg_all.csv按每隔1000行拆分成另一个文件
cf_all = open('./csv_file/reg_all.csv', 'r', newline='')
reader = csv.reader(cf_all, dialect='split')
count = 0
for row in reader:
    if len(row) <= 1:
        continue
    if count % 1000 == 0:
        cf = open('./csv_file/reg_room_%d.csv'%(count // 1000), 'w', encoding='utf-8', newline='')
        subwriter = csv.writer(cf, dialect='split')
        subwriter.writerow(['SEQUENTIAL'])
    else:
        pass
    subwriter.writerow(row)
    count += 1

# # 遍历目录中的文件去除空行
# for file in os.listdir('./csv_file'):
#     file_path = './csv_file' + os.sep + file
#     with open(file_path, 'r') as rf:
#         content = rf.readlines()
#         content.pop()
#         with open(file_path, 'w') as wf:
#             wf.writelines(content)
