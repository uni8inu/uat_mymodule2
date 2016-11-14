UAT MyModule
============
unittestのテンプレート。  
標準入力、標準出力を使うmoduleのUser Acceptance Test(受け入れテスト)をサポートする。

## Description
『標準入力、標準出力使っているmodule』の受け入れテストを簡単に実行する。  
"moduleの標準出力結果"と"test_data.txtの期待値"とをassertEqualする。  
"標準入力input()"は"test_data.txtの入力値"に適切に置き換えられ、実行される。  

## Demo
TBD see youtube

## Requirement
- Python3
- PyCharm(Recommend)

## Usage
TBD See Demo
- テスト対象のmoduleがあるDirectoryへ、"uat_mymodule.py"と"test_data.txt"をコピーする。
- "test_data.txt"に入力データと期待値を記入する
- "uat_mymodule.py"を実行する

## "test_data.txt" フォーマット
    input()の内容  
    :  
    input()の内容  
    (空行)  
    期待値の標準出力結果  
    (空行)
で一つのテストのペアとなります。  
![エビフライトライアングル](http://i.imgur.com/Jjwsc.jpg "サンプル")

具体的には"test_data.txt"のサンプルを見て下さい。    
複数のパラメータでテストを行う場合は、続けて上記のペアを記入して下さい。  
![エビフライトライアングル](http://i.imgur.com/Jjwsc.jpg "サンプル")  

## 注意
テスト対象はDirectoryに1個の状態にしてください。  
具体的には下記のような3ファイル構成にして下さい。  
パイソンファイルがいくつもあるととテスト実行しません。  

    ./  
     (テスト対象module).py  
    uat_mymodule.py    
    test_data.txt      

## VS.
TBD qiita記事
TBD shell diff記事

## Licence
[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author
uni8inu
