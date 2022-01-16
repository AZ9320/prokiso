import json
from pathlib import Path

# https://qiita.com/t4t5u0/items/530d3eb7453aa8ad8abf より
# jsonファイルの枠組みを作る関数
def json_make(path: Path, obj: dict) -> None:
    ls = None
    with open(path, 'r+') as f:
        ls = f.readlines()
        if ls == []:
            ls.append('[\n')
        if ls[-1] == ']':
            ls[-1] = ','
        ls.insert(len(ls), f'{json.dumps(obj, indent=4 ,ensure_ascii=False)}')
        ls.insert(len(ls), '\n]')

    with open(path, 'w') as f:
        f.writelines(ls)

# 待ち時間を計算してleft_secondに入れる関数
# people_insideは考慮していない → 定員人数も考えてない
def calc_time(
    floors,
    people_outside,
    elevator_position,
    left_second,
    time_per_stair,
    ):

    for geton in range(1,floors+1):
        elevator = elevator_position.index(1) + 1 # エレベーターが止まっている階

        if geton>elevator: # 下からくるver
            left_second[geton-1]  = sum(people_outside[elevator-1:geton-1]) # 乗り降りにかかる時間
            left_second[geton-1] += 15*(geton-elevator)-15*(people_outside[elevator-1:geton-1].count(0)) # 階に止まるごとに15秒追加
            left_second[geton-1] += time_per_stair*(geton-elevator) # 移動時間

        elif geton<elevator: # 上からくるver
            left_second[geton-1]  = sum(people_outside[geton:elevator]) # 乗り降りにかかる時間
            left_second[geton-1] += 15*(elevator-geton)-15*(people_outside[geton:elevator].count(0)) # 階に止まるごとに15秒追加
            left_second[geton-1] += time_per_stair*(elevator-geton) # 移動時間

        else:
            left_second[geton-1] = 0 #その階にエレベーターがいるなら待ち時間はゼロ

    return left_second