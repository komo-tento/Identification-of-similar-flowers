# Identification-of-similar-flowers
このシステムは機械学習を用いた類似した花に特化した花画像分類システムです。


現在のコードで識別している花は「アイリス」、「あやめ」、「花菖蒲」、「カキツバタ」の4種類を使用しています。

ファイル構造は下記のようになっています。

```bash
Identification-of-similar-flower/
    ├── main.py
    ├── inference.py
    ├── index.html
    ├── result.html
    ├── training.ipynb
    ├── Weights/
    ├── DataSet/
        ├── airisu/
        ├── ayame/
        ├── hanasyoubu/
        ├── kakitubata/
    ├── static/
        ├── css/
            ├── index.css

```

コード内にあるモジュールは適宜インストールしてください。
上記4つ以外の花を分類したい場合はDataSetの中ファイル名は分類したい花の名前に変更し、それぞれ対応する花の画像を50枚入れてください。
その後、他コードの対象部分も変更してください。
Weigthesは空のファイルを用意してください。
このファイルがないとエラーが起こる可能性があります。

このシステムを動かす場合は上記ファイル構造の形にコードを設置した後に下記のようにターミナルで動かしてください

```bash
$ uvicorn main:app --reload
```

 その際に出力されるUvicorn running on http://~ をクリックすることでWebサイトへ飛べるはずです。
