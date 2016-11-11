import subprocess
from subprocess import Popen,PIPE

# -------ここから変更--------
#テストを行うファイル名
test_filename = "testmodule.py"

#TODO テストデータのファイル読み込み
#""" """の間に標準入力テストデータを貼り付ける
input_d ="""
wanko
"""
#""" """の間に期待する標準出力結果を貼り付ける
expect_d = """
wanko wanko
"""
# -------ここまで--------
run_cmd = "python " + test_filename

input_d = input_d[1:] # スライスで行頭削除 : 改行単位でinput()が実行される
expect_d = expect_d[1:] # スライスで行頭削除 : stdoutは行末に改行を含む

p = Popen(run_cmd,
          stdin=PIPE,stdout=PIPE,stderr=subprocess.PIPE,
          universal_newlines=True)

p.stdin.write(input_d) # stdin実行
stdout = p.communicate()[0] # stdout取得

#結果の表示
print("[{} stdout]\n{}".format(test_filename,stdout))
print("[expect]\n{}".format(expect_d))

if(expect_d != stdout):
    print("***TEST NG***")
else:
    print("!!!TEST OK!!!")