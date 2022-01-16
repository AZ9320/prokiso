from IPython.core.display import update_display  #なんか自動で入ってきたよくわからんやつ
from ele_functions import json_make, calc_time
from pathlib import Path
import os

# この4つはDB等から取得したい
floors = 5
people_outside = [1,0,3,0,1]
elevator_position = ["0","0","0","1","0"] # i階にあるとき、i番目は"1"で他は"0""のリスト
people_inside = 3

left_second = [0]*floors
time_per_stair = 4 #移動時間一定にするならリストにする必要なし(というかそうしたい)

left_second = calc_time(floors,people_outside,elevator_position,left_second,time_per_stair)

# jsonファイルにデータを書き込む
def main(floors,people_outside,elevator_position,left_second,time_per_stair):
    left_second = calc_time(floors,people_outside,elevator_position,left_second,time_per_stair)
    path = Path(__file__).parent/'output2.json'
    os.remove("output2.json")
    f = open('output2.json', 'w')
    f.close()
    for i in range(floors):
        dict_obj = {'floor':f'{i+1}',
                    'people_outside':f'{people_outside[i]}',
                    'elevator_position': f'{elevator_position[i]}',
                    'people_inside': f'{people_inside}',
                    'left_second': f'{left_second[i]}'                     
                    }
        json_make(path, dict_obj)


if __name__ == '__main__':
    main()
