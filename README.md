# Django フレームワークで Heroku に REST API を作成するテスト用アプリ

Django フレームワークを用いて Heroku 上に REST API を作成する練習。


## 実施内容

Heroku の python チュートリアルの内容を元に、別のテスト用 Django アプリケーションを Heroku 上にデプロイ。


## 参考にした Django アプリケーション (django_rest_framework_test) に追加で準備したファイル

- requirements.txt （必要なライブラリを記載）
- Procfile （ gunicorn で Django アプリケーションを起動するために必要）
- README.md（ github 上にファイルを置くため、説明を記載）
- django_rest_framework_test/settings.py （動作確認用に ALLOWED_HOSTS を編集）


## 追加で準備したもの（ Heroku アプリデバッグ用 API ）

heroku 上のアプリをデバッグするために、 debug_message_file を準備。
- /debug_ls ：ファイル一覧 (ls -al 結果 ) を出力。 path パラメタでディレクトリを指定可能。
- /debug_cat ：ファイル内容 (cat 相当 ) を出力。 path パラメタでディレクトリを指定可能。
- /debug_cmd ：コマンド実行とその結果を出力。 cmd パラメタと param1 ～ param3 パラメタで実行するコマンドを指定可能。
- /debug_setup ：Heroku 上に Miniconda 環境を構築できるか確認。 Miniconda が利用できれば少しアプリの自由度は上がるのかと思い実験。 30 秒でタイムアウトしてしまうので、成功するかは不安定。一度構築できたら、その環境を使えば良いと思われる。


## 参考にしたサイト
- https://devcenter.heroku.com/ja/articles/getting-started-with-python
- https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8
- https://qiita.com/esehara@github/items/27c0d1f76bea8ac9169e


## Notice

Django アプリケーション (django_rest_framework_test) は以下を参考に作成しました。
- Copyright (c) 2015 kimihiro_n
- https://github.com/pistatium/django_rest_framework_test
