# Django フレームワークで heroku に REST API を作成するテスト用アプリ

Django フレームワークを用いて Heroku 上に REST API を作成する練習。

## 実施内容

Heroku の python チュートリアルの内容を元に、別のテスト用 Django アプリケーションを Heroku 上にデプロイ。

## 参考にした Django アプリケーションに追加で準備したファイル

- requirements.txt （必要なライブラリを記載）
- Procfile （ gunicorn で Django アプリケーションを起動するために必要）
- README.md（ github 上にファイルを置くため、説明を記載）


## 参考にしたサイト
- https://devcenter.heroku.com/ja/articles/getting-started-with-python
- https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8

## 謝辞

- Django アプリケーション作成時に以下のソースコードを利用させていただきました。
-- Copyright (c) 2015 kimihiro_n
-- https://github.com/pistatium/django_rest_framework_test

