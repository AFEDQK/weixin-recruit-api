# -*- coding: utf-8 -*- #
# @Time : 2022/8/13 21:59
from app.utils.get_parse_data import seg_punc


def test_seg_punc():
    text = "内蒙呼和浩特 ，招天然气焊工班组 小区活20层 手把焊想干的联系详细自己打电话13196028432"
    res = seg_punc(text)
    print(res)


def main():
    test_seg_punc()


if __name__ == '__main__':
    main()
