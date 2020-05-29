---
title: 謎の英数字ツイートの意味を解説する
slug: explain-the-meaning-of-mysterious-alphanumeric-tweets
date: 2019-12-06T10:56:21+09:00
categories: 
 - PC関連
description: 
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/ddghc4l09/thumbnail/.jpg
draft: true
---

<!--more-->

フォロワーの<a href="https://twitter.com/chiisann_"><strong>ちぃさん</strong></a>からこんな質問を頂きました。

{{< tweet 1202218364971565062 >}}&nbsp;

私も以下のような似た遊びをしたことがあるのですよ。
このような数値の羅列は大抵何かしらの文字コードですからね。

{{< tweet 1126054814842933248 >}}&nbsp;

ちなみに知識としては<strong>『ほぼ独学』</strong>です。
勉強するなら以下の書籍が大変役に立ちました。
オススメです。

<iframe style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=25haruhiro03-22&language=ja_JP&o=9&p=8&l=as4&m=amazon&f=ifr&ref=as_ss_li_til&asins=4048869574&linkId=49297cb9b2ded4af6e1a5e042cd607d1"></iframe>

&nbsp;

というわけで今回の記事は以上です。
ありがとうございました(';')

&nbsp;
&nbsp;

<h2>どうやってコンピュータは文字を表現しているか</h2>

と、終わってしまったら元も子もないので、一緒にちぃさんがなんて言っていたか解読しましょうね。

さて、解読する前に、世間一般の人から見たらバグったように見える彼女のツイートは何なのかについて簡単に説明しましょう。
かなり端折って説明するので
&nbsp;

<img src="http://1kuchi.way-nifty.com/photos/uncategorized/2011/09/06/0010.gif" alt="こまけぇこたぁいいんだよ" />

&nbsp;

という広い心で読んでください。

&nbsp;

まず、コンピュータは文字も画像も何もかも<strong>『0 or 1』</strong>で表現します。
したがって今読んでいるこの文字も、実は0と1で表現されているのです。
これを<strong>ビットパターン</strong>と呼び、コンピュータが扱うことができる<strong>最小単位(bit)</strong>です。

コンピュータは0と1だけで表現すると都合いいんですけど、人間側は0と1だけじゃ困るんです。
おっぱいを0と1で表現したと言われたって困るじゃないですか。

というわけで、0と1を使って数字や文字、色や音を表現できるようにするのです。
今回は数字と文字について勉強してみましょう。

1bitは1と0を表現できますが、2以上の表現はどうすべきか。
2bit用意して10と表現（繰り上げ）します。3なら11です。
どっかで聞いたことがあることであるはずの<strong>2進数</strong>というものです。

2bitあれば数字の3まで表現できました。
こんな感じで表現したい数字、文字、英語の大文字小文字や特殊記号と増やして、最終的に通信することも考えると8bit必要になりました。

これが<strong>8bit = 1バイト(byte)</strong>です。
<strong>『0000 0000 ～ 1111 1111』</strong>で表現するのがコンピュータの仕組みで一般化されました。
&nbsp;

ここまでいくと流石に桁数が大きくなってきて、2進数を読み取るのはだりぃよ……と人間側は思うわけです。

というわけで2進数を使うコンピュータと相性が良く、人間が読みやすい形式の<strong>16進数</strong>という表現が誕生しました。
<strong>『1111 1111』</strong> ⇒ <strong>『FF』</strong>のように変換することですね。

<img src="https://tech.nikkeibp.co.jp/it/pc/article/NPC/20061228/257991/1.gif" alt="2進数と16進数" />

&nbsp;

こうして人間はコンピュータで数字や文字を表現できる幅を広げていきました。
しかし、表現方法が統一されていない時代があったのです。
極端な例ですが、0000をaにする人がいたりbにする人がいて困るわけです。

そこでこの状態を解決するために<a href="https://ja.wikipedia.org/wiki/%E7%B1%B3%E5%9B%BD%E5%9B%BD%E5%AE%B6%E8%A6%8F%E6%A0%BC%E5%8D%94%E4%BC%9A"><strong>米国規格協会</strong></a>が<strong>『米国標準交換コード(American Standard Code for Information Interchange)』</strong>という基準を採用しました。

これを<strong>『ASCII（アスキー）』</strong>と呼び、コンピュータのビットパターンからテキストを表現する<strong>文字コード</strong>の１つとして誕生しました。
ここまで長い説明でしたが、<strong>冒頭のちぃさんはアスキー表現で文字をツイートしていた</strong>ということなんです。

&nbsp;

<h2>答え合わせ</h2>

というわけで彼女がなんて呟いたか変換してみましょう。
やり方は簡単です。
<strong>変換表を見て文字に置き換え</strong>ればいいのです！

{{< blogcard url=http://www12.plala.or.jp/mz80k2/electronics/ascii/ascii.html >}}&nbsp;

さぁ頑張って下さい!……といっても死ぬほどめんどくさいので、素直に変換してくれるサイトを使いましょう。

{{< blogcard url=http://web-apps.nbookmark.com/ascii-converter/ >}}
&nbsp;

で、変換した結果が以下です。

<blockquote>
  <strong>【変換前】</strong>
  57 68 79 20 77 6f 75 6c 64 20 79 6f 75 20 66 69 6e 64 20 6f 75 74 20 77 68 61 74 20 74 68 69 73 20 66 6f 72 6d 20 69 73 20 41 53 43 49 49 20 63 6f 64 65 3f
  48 61 76 65 20 79 6f 75 20 65 76 65 72 20 73 74 75 64 69 65 64 20 74 68 69 73 3f
  
  <strong>【変換後】</strong>
  Why would you find out what this form is ASCII code?
  Have you ever studied this?
  
  <strong>【翻訳】</strong>
  貴様、なぜASCIIであることがわかった？
</blockquote>

良ければこの記事のサムネ画像もなんて書いてあるか調べてみてください。
**※ちなみに冒頭で紹介した私のツイートはASCIIで変換されていません。気になる方はUTF-8をで変換してみてください。
**
