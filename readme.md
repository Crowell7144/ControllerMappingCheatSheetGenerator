# Controll Mapping CheatSheet Generator

### これは、Googleスプレッドシートを読み込んで以下のようなチートシート形式のhtmlを作成するpythonスクリプトです。

![](https://i.imgur.com/apqoWV8.png)

## 必要な事前準備

python実行環境が必要です。Microsoftストアなどからダウンロードして、コマンドプロンプトからpythonを実行できるようにしてください。

最初はローカルフォルダのpaste.txtを読み込むようになっています。

Googleスプレッドシートを読み込んで、チートシート形式のhtmlを作成するには、[このスプレッドシート](https://docs.google.com/spreadsheets/d/1NIvgQVh1ZhREIm9pfodCtfDpS69uStkprdRDWNBEOG8/edit?usp=sharing)を自分のアカウントにコピーして編集してください。

![](https://i.imgur.com/BLCTSpa.png)

編集後、config.iniでデフォルトの読み込みファイルにURLを設定します。

スプレッドシートのページで、ファイル＞共有＞ウェブに公開＞読み込み対象のシート＞タブ区切りの値(.tsv)を選択してから、公開リンクをコピーして設定してください。

![](https://i.imgur.com/uH5OLNF.png)

![](https://i.imgur.com/8hCAwmZ.png)

スプレッドシートを使わず、paste.txtを直接編集することも可能です。タブ区切りを維持するように気をつけてください。

スプレッドシートの編集結果がなかなか反映されない場合は、paste.txtにテキストを貼り付けて確認することもできます。

作者のスプレッドシートのリンクが死んだりした場合は、paste.txtと同形式のタブ区切りデータが出力できるスプレッドシートを作るなどしてください。

mapping列で認識するボタン文字列は以下の通りです。

```
A, B, X, Y
LB, RB, LT, RT
LS, LS:X, LS:Y, LS:XY
RS, RS:X, RS:Y, RS:XY
Start, Back
▲, ▼, ▶, ◀
▲▶, ▼▶, ◀▼, ◀▲ (方向キー斜め)
LP1, LP2 (エリコン左パドル)
RP1, RP2 (エリコン右パドル)
/ (おまけ:コントローラーのアイコンになります)
```

## 実行方法

コマンドプロンプトから `python tsv2html.py `でフォルダ内にhtmlが出力されます。

ブラウザで開いて印刷するなりサブ画面に表示するなりして使ってください。

`python tsv2html.py -c 2` を実行すると、チートシートに出力される列が2つになります。

その他のオプションについては、`python tsv2html.py -h` を実行するとオプションコマンドの説明とか表示されます。


## 出力内容の調整について

カテゴリの順番や、サブカテゴリの表示非表示などはスプレッドシートのデータを編集して調整してください。

サブカテゴリを空欄にすればサブカテゴリ名の行は表示されなくなるので、スペースの調整に利用できます。

ボタンの表示にPromptFontを使っています。

promptfont.ttf と promptfont.css が出力したhtmlと同じフォルダにないとボタンの表示ができないため、他の場所にhtmlをコピーする際には注意してください。

## ライセンス

PromptFont以外の改変再配布は自由です

PromptFontを再配布に含める場合、以下のライセンス表記とPromptFont_LICENSE.txtを必ず含めてください。

PromptFont by Yukari "Shinmera" Hafner, available at https://shinmera.com/promptfont.
