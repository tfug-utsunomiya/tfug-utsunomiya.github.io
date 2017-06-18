Title: TensorFlow Utsunomiya Blogです。
Date: 2017-06-18 15:38
Category: News
Tags: tfug, python, tensorflow
Slug: helloworld
Author: tfug-utsunomiya
Summary: TensorFlow Utsunomiya Blogのご紹介

# TensorFlow Utsunomiya Blogを公開しました！

以下の構成でこのブログを構築してみました。

* 静的サイトの生成
    * Pelican
* ホスティング
    * GitHub Pages

Markdownのテスト

## リスト

箇条書き

* Hoge
* Foo
* Bar

番号付き

1. Hoge
2. Foo
3. Bar

## 画像

```
![test](/images/150x150.png)
```

![test](/images/150x150.png)

## テーブル

|||
|:-|:-:|
|A|hoge|
|B|foo|
|C|bar|

## サンプルコード

```python
#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

a = tf.constant(1, name="a")
b = tf.constant(2, name="b")
c = tf.add(a, b, name="add")

with tf.Session() as sess:
    ret = sess.run(c)
    print(ret)
```