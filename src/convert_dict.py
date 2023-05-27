import pathlib
import csv

dict_path = pathlib.Path(__file__).parent.joinpath('dict')
yuet_dict = {}
with open(dict_path.joinpath('dict.txt'), "r") as txt_obj:
    line = txt_obj.readlines()
    line = [x.replace("\n", "").split("\t") for x in line]
    txt_obj.close()
for item in line:
    if item[0] in yuet_dict.keys():
        if item[1] not in yuet_dict[item[0]]:
            yuet_dict[item[0]].append(item[1])
    else:
        yuet_dict[item[0]] = [item[1]]

for key in yuet_dict.keys():
    yuet_dict[key] = '/'.join(yuet_dict[key])

yuet_list = list(map(list, yuet_dict.items()))
yuet_list.insert(0, ["Kanji", "YuetPing"])

with(open(dict_path.joinpath('yuet_dict.csv'), "w")) as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(yuet_list)
pass