import os
import sys
import io
import unittest
import unittest.mock as mock
from runpy import run_module

"""同Directoryにあるモジュールの受け入れテストを行う
データファイルを元に、入力値のダミを取得し、標準出力結果をチェックする
テスト対象以外の.pyファイルがあると動作しない
"""

#settings
test_data_name = 'test_data.txt'  # 入力データと期待値が記入されたファイル名
#(option) 直接テストモジュールを指定することもできる。その場合はモジュール名を以下に記入する
# ex.) sample_module  # NG) sample_module.py
test_module_name = ""

def pickup_module():
    module_name = ""
    f_names = os.listdir(".")

    # *.pyのみ捜索する
    f_names = list(filter(lambda x: x.endswith(".py"),f_names))
    f_names = list(filter(lambda x: x!="uat_mymodule.py",f_names))  #このモジュールは除外

    #対象moduleが1つなら実行する
    f_num = len(f_names)
    if(f_num == 1) :
        module_name = f_names[0][0:-3] # .pyを除く
    else :
        module_name = ""

    return module_name

def test_data_reader():
    """test_data.txtを読み出しunittest用のテストリストを作成して返す
     :return test_list
    [データ構造]
    test_list = [test1,test2,test3.....] # 各テストのlist
　   test1 = [inputs,expected] # 1つのテスト / 入力値、出力期待値のペア
  　  inputs = ('input','input','input'.....) # input()をmockで置き換える文字列のtuple
                                               / input()が呼ばれる毎にリストの内容を順に返す
    　expected = "expect" # テストの期待値 / モジュール実行完了までに標準出力に出す全ての文字列
    """
    test_list = []

    with open(test_data_name, "rt") as fin:
        r_l = fin.readlines()

    # 読み出した内容を空改行ブロック区切りのデータリスト化する
    r_l.append("\n")  # split処理の共通化のため、改行追加
    all_d = "".join(r_l)
    d_block = all_d.split("\n\n")  # 期待値から末尾の改行が削除されるので注意
    d_block = list(filter(lambda x: x != "", d_block))  # 空行削除

    # 入力値、出力期待値のペアを作成
    len_block = len(d_block)
    for i in range(0, len_block, 2):
        if(i+1 > len_block-1):
            break;
        else:
            inputs = tuple(d_block[i].split("\n"))
            expected = d_block[i + 1] + "\n"  # 期待値の末尾の改行を復活

            test_list.append([inputs, expected])

    # print(test_list)
    return test_list


def test_para_gen(test_l):
    """１つのテスト用のパラメータを返すジェネレーター
    :return test_name,inputs,expected
    テストリストを元に、パラメーターを作成する。呼ばれる毎に、次のテストのパラメーターを返す。
    テスト名称はtest
    """
    total_test_num = len(test_l)

    for i in range(total_test_num):  # todo supportクラスを見ること
        yield test_l[i][0], test_l[i][1], "test pair : No.{0}".format(i+1)

class MyModuleTestCase(unittest.TestCase):
    def setUp(self):
        #データファイル確認
        df_exists = os.path.exists("{}".format(test_data_name))
        if(df_exists == False):
            self.fail("'{0}' is not found. Set {0} file in current dir.".format(test_data_name))

        #対象モジュール確認
        if test_module_name == "":
            # モジュール自動探索の場合
            self.test_module_name = pickup_module()
            if(self.test_module_name == ""):
                self.fail("Target module can't pickup.Check current dir.")
        else:
            # モジュール指定の場合
            self.test_module_name = test_module_name

        # テスト項目を作成
        self.tests = test_data_reader()

        # バックアップする / stdoutを文字列として取得し、expectedと比較するため
        self.orig_stdout = sys.stdout

    def tearDown(self):
        sys.stdout = self.orig_stdout

    def test_uat(self):
        for inputs_l, expected, test_name in test_para_gen(self.tests):
            # テストペア毎にサブテストを実行する
            with self.subTest(test_name):
                sys.stdout = io.StringIO()
                # input()をmock化する / 出力はinputs_lの順に置き換えられる
                with mock.patch('builtins.input', side_effect=inputs_l) as m:
                    run_module(self.test_module_name)
                    self.assertEqual(sys.stdout.getvalue(), expected)
                sys.stdout.close()


if __name__ == '__main__':
    unittest.main()
