# TFUG Utsunomiya Blog

TFUG Utsunomiya Blogを書くための手引

# 試した環境

* macOS Sierra 10.12
* Python 3.5.3
* git 2.13.1

## インストール

まずPelicanと依存パッケージをインストールします。また、gh-pagesブランチの操作を手軽にするghp-importをインストールします。

```
$ pip install pelican
$ pip install Markdown
$ pip install typogrify
$ pip install ghp-import
```

[tfug-utsunomiya/tfug-utsunomiya.github.ioレポジトリ](https://github.com/tfug-utsunomiya/tfug-utsunomiya.github.io)をクローンします。

```
$ git clone git@github.com:tfug-utsunomiya/tfug-utsunomiya.github.io.git
```

記事を書く具体的な方法を紹介する前に、レポジトリのブランチの役割と作業の流れを説明します。まず`pelican`ブランチで記事の作成します。次にツールを使って記事をHTMLファイルに変換し`master`ブランチにHTMLファイル等を移します。最後に`master`ブランチの内容をプッシュして公開が完了します。

```
$ cd ./tfug-utsunomiya.github.io
$ git checkout pelican
（注意）`pelican`ブランチに切り替えます
$ vim content/test.md
（注意）各自のエディタで作成してください
```

以下が記事の例となります。最初にタイトルや日時、カテゴリを決める記入する必要があります。後はMarkdown記法で文書を作成できます。最後に`test.md`を保存しましょう。

```
Title: Test
Date: 2017-06-18 12:00
Category: Test
Tags: tensorflow
Slug: test
Author: tfug-utsunomiya
Summary: TFUG Utsunomiya Blogのご紹介

### Test

Hello, world!
```

Markdown記法で書かれた記事をHTMLファイルに変換して、`master`ブランチにファイルを移動させます。

```
$ pelican content -o output -s pelicanconf.py
$ ghp-import output -b master
```

`master`ブランチに移動してGithubにプッシュして記事の公開が完了します。

```
$ git checkout master
$ git add .
$ git commit -m "Update."
$ git push origin master
```

# 参考

* [Installing Pelican - Pelican](http://docs.getpelican.com/en/stable/install.html)
* [Publishing to GitHub - Pelican](http://docs.getpelican.com/en/stable/tips.html?highlight=github)
