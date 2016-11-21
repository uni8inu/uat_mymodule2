UAT MyModule
============
![ICON](https://raw.githubusercontent.com/uni8inu/uat_mymodule2/master/imgs/uat_mm_120.png "icon")  
Pythonのunittestのテンプレート。  
標準入力、標準出力を使うmoduleへのUser Acceptance Test(受け入れテスト)をサポートする。

## Description
『標準入力、標準出力使っているmodule』への受け入れテストを簡単に実行する。  
例えば[piza](https://paiza.jp)のオンラインジャッジ問題など。  
  
"moduleの標準出力結果"と"test_data.txtの期待値"とをassertEqualする。  
"標準入力input()"は"test_data.txtの入力値"に適切に置き換えられ、実行される。  


## Demo
[![How to Use](http://img.youtube.com/vi/qUYUl-1E2cs/0.jpg)](https://www.youtube.com/watch?v=qUYUl-1E2cs)

## Requirement
- Python3
- PyCharm(Recommend)

## Usage
See Demo
+ テスト対象のmoduleがあるDirectoryへ、"uat_mymodule.py"と"test_data.txt"をコピーする。
+ "test_data.txt"に入力データと期待値を記入する
+ "uat_mymodule.py"を実行する

### "test_data.txt" フォーマット
    input()の内容  
    :  
    input()の内容  
    (空行)  
    期待値の標準出力結果  
    (空行)
で一つのテストのペアとなります。  
具体的には"test_data.txt"のサンプルを見て下さい。   
![説明1](https://raw.githubusercontent.com/uni8inu/uat_mymodule2/master/imgs/setumei01.png "explain 1")
  
複数のパラメータでテストを行う場合は、続けて上記のペアを記入して下さい。  
![説明2](https://raw.githubusercontent.com/uni8inu/uat_mymodule2/master/imgs/setumei02.png "explain 2")  

## 注意
テスト対象はDirectoryに1個の状態にしてください。  
具体的には下記のような3ファイル構成にして下さい。  
パイソンファイルがいくつもあるととテスト実行しません。  

    ./  
     (テスト対象module).py  
    uat_mymodule.py    
    test_data.txt      

## VS.
###shell diffを使う
    diff <(python foo.py < IN.txt) OUT.txt
thanks [teamikl](https://teratail.com/questions/53736)

###Qiita Posts
[競技プログラミングのローカル環境での実行](http://qiita.com/falloutkids/items/9e053d801ef366b7f30c#_reference-219e7208d3f25c808c75)  
[paiza のような標準入出力を使うコーディングテストで制限時間ギリギリ使って解くための１つの方法](http://qiita.com/kkoiwai/items/d70c21f92eaca6bf9939#_reference-c98f8a96edbb107f40a4)  
[[.NET] 競技プログラミングで解いたプログラムをローカル環境でテストしたい時に便利な裏ワザ](http://qiita.com/nia_tn1012/items/0bad76d75161ecc51e15)  

## Licence
[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author
uni8inu
