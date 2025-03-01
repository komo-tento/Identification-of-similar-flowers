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

また、今回airisuのファイルやWeightsのファイル内に.gitkeepという白紙のファイルがありますが、githubにて空のフォルダを作成できないため、仮に置いているだけのファイルなのでシステム運用時には必要ありません。

上記4つ以外の花を分類したい場合はDataSetの中ファイル名は分類したい花の名前に変更し、それぞれ対応する花の画像を50枚入れてください。
その後、他コードの対象部分も変更してください。

Weigthtsは空のファイルを用意してください。

このファイルがないとエラーが起こる可能性があります。

このシステムを動かす場合は必ず最初にtraining.ipynbを回してください。

training.ipynbを回すことでResNetを用いた機械学習の学習モデルがWeightsの中に保存され、Webサイト内で動くようになります。

その後に下記のようにターミナルで動かしてください

```bash
$ uvicorn main:app --reload
```

 その際に出力されるUvicorn running on http://~ をクリックすることで類似した花に特化した花画像分類システムが動くWebサイトへ飛べるはずです。
