---
title: HTMLの基礎を学び直す
slug: learn-the-basics-of-html
date: 2019-05-08T06:58:58+09:00
categories: 
 - HTML
description: 
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/ddghc4l09/thumbnail/.jpg
draft: true
---

<!--more-->

【WordPressをもっと使いこなすための技術メモ】

WEB系のプログラミングを学び直し、今後の将来と本ブログに活かすことを目的に書いていきます。

&nbsp;

&nbsp;

[toc]

&nbsp;

&nbsp;
<h2>タグ</h2>
タグとは『<strong>&lt;html&gt;</strong>』のように『<strong>&lt; &gt;</strong>』の中に半角英数の文字を入れたものを指す。

『<strong>&lt;html&gt; ～ &lt;/html&gt; </strong>』のように囲うことで、階層、テキストの文字の大きさや色、機能の付加を命令していく。

タグの中にある文字を<strong>要素名</strong>と呼び、先頭にあるタグを『<strong>開始タグ</strong>』、後ろの『<strong>&lt;/ &gt;</strong>』を『<strong>閉じタグ（終了タグ）</strong>』と呼ぶ。

例外として『<strong>&lt;img&gt;</strong>』など閉じタグを必要としないタグも存在し、これを『<strong>空要素タグ</strong>』と呼ぶ。

&nbsp;
<h2>要素</h2>
要素とは<strong>タグで囲ったもの全体</strong>を指す。

例えば以下はタグ&lt;p&gt;の要素である。

<img src="https://wp-p.info/reps/html-biginner/img/07_01.jpg" width="320" height="135" class="alignnone size-medium" />

&nbsp;

HTMLを作成する際『<strong>&lt;html&gt; &lt;body&gt; ～ &lt;/body&gt; &lt;/html&gt; </strong>』のようにタグの中にタグを入れて作成していく。

囲っているタグの事を『<strong>親要素</strong>』と呼び、親要素の中にあるタグを『<strong>子要素</strong>』と呼ぶ。

例でいうと&lt;html&gt;は&lt;body&gt;の親要素、&lt;body&gt;は&lt;html&gt;の子要素となる。

&nbsp;

&nbsp;
<h2>見出し・段落</h2>
↑のような大文字のタイトルを表現する時は『<strong>&lt;h1&gt;～&lt;/h1&gt;</strong>』タグを用いる。

"h"は『<strong>heading（見出し）</strong>』の略でh2～h6までの要素がある。

段落を表す時は『<strong>&lt;p&gt;~&lt;/p&gt;</strong>』タグを用いる。
<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code>&lt;h1&gt;1番大きい見出し&lt;/h1&gt;
&lt;h2&gt;2番大きい見出し&lt;/h2&gt;
&lt;h3&gt;3番大きい見出し&lt;/h3&gt;
&lt;h4&gt;4番大きい見出し&lt;/h4&gt;
&lt;h5&gt;5番大きい見出し&lt;/h5&gt;
&lt;h6&gt;6番大きい見出し&lt;/h6&gt;
&lt;p&gt;1段落目&lt;/p&gt;
&lt;p&gt;2段落目&lt;/p&gt;</code></pre>
</div>
&nbsp;

&nbsp;

&nbsp;
<h2>コメント</h2>
『<strong>&lt;!-- --&gt;</strong>』で囲むとコメントを書くことができる。

<strong>注意点</strong>
<ul>
 	<li>コメントをコメントで入れ子に出来ない</li>
 	<li>ブラウザによってはコメントの中で使ったハイフン（-）を終了と認識してしまう可能性があるので、中でハイフンは使わない方が良い。</li>
 	<li><span>現在、全てのブラウザではウェブサイトのHTMLソースをコメントアウト部分を含めてそのまま閲覧することができる。
よってコメントアウトしたらブラウザに映らないが、ソースコードを表示されたら普通に見られるので大事なことは書かないこと。</span></li>
</ul>
<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code>&lt;p&gt;タグで囲まれたものはブラウザに反映されるが&lt;/p&gt;

&lt;!-- ここに何を書いてもブラウザに反映されない --&gt;

&lt;!-- もちろん複数行もできる

　　　　 ∧＿∧
　　＿_／＿＿＿＼
　 (　＿|´･ω･`|＼<span>&lt;踊れ！カルメン！ </span>
　　＼ヽ ￣￣￣　 ｜
　　∠ノ　　　　 /｜
　～(　　　　　／／
　　 |　＿＿ノ￣￣)
　　 | /　　￣/ ／
　　 |/　　　/／

--&gt;

&lt;!-- &lt;!-- 
コメントアウトの中にコメントアウトを入れる”入れ子" は出来ない
--&gt; --&gt;

&lt;!-- &lt;!-- コメントアウトの中にコメントアウトを入れる”入れ子" は出来ない--&gt; --&gt;

&lt;!-- 
ブラウザには表示されないがソースコード表示（右クリックで"ソースコード表示"など）されると普通に見られるので
ここにパスワードなどを書いたらバカである
--&gt;</code></pre>
</div>
&nbsp;

&nbsp;
<h2>属性</h2>
HTMLの要素に対し『<strong>属性</strong>』という<strong>要素に対して＋αの設定を追加する</strong>方法がある。

書き方は『<strong>&lt;要素名 属性="属性値"&gt;</strong>』のように書く。
<ul>
 	<li>開始タグの要素名の後ろに<strong>半角スペース</strong>を開ける</li>
 	<li>属性の後ろに<code class="prettyprint prettyprinted"><span class="pun">=</span></code>（イコール）を付ける</li>
 	<li>属性値は<code class="prettyprint prettyprinted"><span class="str">"</span></code>（ダブルクオート）で<strong>囲む</strong></li>
</ul>
&nbsp;

&nbsp;
<h2>リンク</h2>
『<strong>&lt;a&gt;&lt;/a&gt;</strong>』で囲ったテキストはリンク文字にすることができる。

a<span>は「アンカー(anchor)」の略で、リンクの出発点と到達点を意味する。</span>

リンクを指定するには『<strong>&lt;a href="url"&gt;&lt;/a&gt;</strong>』のように『<strong>href属性</strong>』<strong>でURLを記述</strong>するとリンクを作ることができる。

hrefは『<strong>エイチレフ</strong>』と呼び、<span>hypertext referenceの略で、直訳すると「ハイパーテキストの参照」となる。</span>
<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code>&lt;a href="https://hackheatharu.xyz"&gt;このブログトップページへのリンク&lt;/a&gt;</code></pre>
</div>
&nbsp;

&nbsp;
<h2>画像を表示する（&lt;img&gt;タグ）</h2>
画像は『<strong>&lt;img&gt;</strong>』要素を使う（テキストで囲うことが無いので終了タグは不要）。

『<strong>&lt;img src="url"&gt;</strong>』のように<strong>『src属性』でURLを記述</strong>して使う。
<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code>&lt;img src="C:\画像\スクリーンショット\hoge.jpeg"&gt;</code></pre>
</div>
&nbsp;
<h2>リストを表示する（&lt;li&gt;タグ）</h2>
テキストをリストで表現するには『<strong>&lt;li&gt;&lt;/li&gt;</strong>』要素を使う。

この要素は『<strong>&lt;ul&gt;&lt;/ul&gt;</strong>』または『<strong>&lt;ol&gt;&lt;/ol&gt;</strong>』の間で使用しなければならない。

リストにした文字先頭に黒点を付ける場合は『<strong>&lt;ul&gt;&lt;/ul&gt;</strong>』要素で入れ子にする。
<ul>
 	<li>あ</li>
 	<li>い</li>
 	<li>う</li>
</ul>
連番の数字は『<strong>&lt;ol&gt;&lt;/ol&gt;</strong>』要素で入れ子にする。
<ol>
 	<li>あ</li>
 	<li>い</li>
 	<li>う</li>
</ol>
<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code>&lt;!-- 黒点 --&gt;
&lt;ul&gt;
  &lt;li&gt;あ&lt;/li&gt;
  &lt;li&gt;い&lt;/li&gt;
  &lt;li&gt;う&lt;/li&gt;
&lt;/ul&gt;


&lt;!-- 数字 --&gt;
&lt;ol&gt;
  &lt;li&gt;あ&lt;/li&gt;
  &lt;li&gt;い&lt;/li&gt;
  &lt;li&gt;う&lt;/li&gt;
&lt;/ol&gt;</code></pre>
</div>
関連項目
<ul>
 	<li><a href="https://hackheatharu.xyz/learn-the-basics-of-css/">list-styleプロパティ</a></li>
</ul>
&nbsp;

&nbsp;
<h2>&lt;html&gt; &lt;head&gt; &lt;body&gt;</h2>
HTMLファイルは<strong>&lt;html&gt;タグというルート要素</strong>（全てのタグの親要素）を最初に記述して作られる。

ルート要素の後は、主に<strong>&lt;head&gt;タグ</strong><strong>と&lt;body&gt;タグ</strong>で構成される。

head要素には<strong>メタデータ（<span> (</span>検索エンジン<span> や </span>ブラウザー<span> などが利用するページに関する情報</span>）</strong>を書く場所であり、Webページには何も表示されない。

body要素には<strong>Webページに表示したい内容</strong>を書く場所である。

ちなみにhtml要素で<strong>&lt;html lang="ja"&gt;</strong>とは必ずしも書かなくて良いらしい ⇒ <a href="https://seopack.jp/seoblog/20161111-use-hreflang/">Google「言語指定にlangは使うな」／公式発言</a>

&nbsp;
<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
  &lt;head&gt;
    head要素以下に取ることができる要素群。
    title要素などをはじめとしたそのHTML文書自身に関する情報からなる。
  &lt;/head&gt;
  &lt;body&gt;
    body要素以下に取ることができる要素群。
    HTML文書の本文となる情報を記述する。
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
&nbsp;

&nbsp;
<h2><span>&lt;!DOCTYPE html&gt;</span></h2>
&lt;head&gt;タグの前には必ず<span><strong>&lt;!DOCTYPE html&gt;</strong>を</span>書く。

これは『<strong>このファイルはHTML5で作成されたものです</strong>』とブラウザに解釈させるため最初に宣言しておくためのものと解釈して良い。

これを<strong>DTD(Document Type Definition)宣言</strong>と言う。

もう少し詳しく ⇒ <a href="https://qiita.com/NoxGit/items/74314d755222c0d971e4">https://qiita.com/NoxGit/items/74314d755222c0d971e4</a><a href="http://www.shoshinsha.com/hp/ref/html/dtd.html"></a>

&nbsp;

&nbsp;
<h2>&lt;head&gt;内で書くこと</h2>
<h3>文字コードの宣言</h3>
文字コードを宣言することでWebコンテンツの文字化けを防ぐ。

主に『<strong>utf-8</strong>』を指定する ⇒ <a href="https://www.graffe.jp/blog/1278/">https://www.graffe.jp/blog/1278/</a>

head要素に<strong>&lt;meta&gt;タグを用いて&lt;meta charset="utf-8"/&gt;</strong>と記述して文字コードを指定する。
<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;meta charset="utf-8"/&gt;

&lt;!-- ちなみにこういう書き方もできるが、めんどくさい --&gt;

&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8"/&gt;</code></pre>
</div>
&nbsp;
<h3>ページタイトル</h3>
<strong>&lt;title&gt;タグ</strong>でページのタイトルを指定する。

ここに書いたテキストはブラウザのタブに表記される。
<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;title&gt;ここにタイトルを書く&lt;/title&gt;</code></pre>
</div>
&nbsp;

&nbsp;
<h2>CSSファイルの読み込み</h2>
反映させたいCSSファイルを指定するために<strong>&lt;link&gt;タグ</strong>でファイルを指定する必要がある。

指定するには『<strong>&lt;link rel="stylesheet" href="読み込みたいCSSファイル名.css"&gt;</strong>』のように『<strong>rel属性</strong>』<strong>でファイルとの関係性、</strong>『<strong>href属性</strong>』<strong>でファイル名を記述</strong>する。

CSSファイルを呼び出すだけならrelの属性値は『<span><strong>stylesheet</strong>』と書く。</span>

relは『<strong>レル</strong>』と呼び、<span>relation（関係）の略である。</span>
<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code><span>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;link rel="stylesheet" href="</span><span class="highlight">読み込みたいCSSファイル名.css</span><span>"&gt;</span></code></pre>
</div>
&nbsp;

&nbsp;
<h2>ブロックレベル要素とインライン要素</h2>
<p class="honbun">HTMLで定義されている要素のうち、&lt;body&gt;～&lt;/body&gt;の中で使用される要素の多くは、 ブロックレベル要素（Block-Level Elements）か、インライン要素（Inline Elements）に分類される。</p>
<p class="honbun">分類することで、どの要素の内側にどの要素を配置できるかなどのルールが定める。</p>

<h3>ブロックレベル要素（Block-Level Elements）</h3>
<p class="honbun">ブロックレベル要素は<strong>『</strong><strong>見出し・段落・表』</strong>など、文書を構成する基本となる要素達を一つのブロック（かたまり）として認識する。</p>
<p class="honbun">ブラウザでの表示も一つのかたまりとして扱われることが多く、一般的なブラウザでは前後に改行が入る。</p>
<p class="honbun">以下は代表的なブロックレベル要素のタグである。</p>

<blockquote>
<div class="siyorei_source">&lt;address&gt;　&lt;blockquote&gt;　&lt;center&gt;</div>
<div class="siyorei_source">&lt;div&gt;　&lt;dl&gt;　&lt;fieldset&gt;　&lt;form&gt;</div>
<div class="siyorei_source">&lt;h1&gt;-&lt;h6&gt;　&lt;hr&gt;　&lt;noframes&gt;　&lt;noscript&gt;</div>
<div class="siyorei_source">&lt;ol&gt;　&lt;p&gt;　&lt;pre&gt;　&lt;table&gt;　&lt;ul&gt;</div></blockquote>
<h3>インライン要素（Inline Elements）</h3>
<p class="honbun">インライン要素は主に<strong>ブロックレベル要素の”内容”</strong>として用いられる要素で、文章の一部として扱われる。</p>
<p class="honbun">例えば、&lt;p&gt;要素の中の&lt;strong&gt;要素のように、段落のなかの一部を強調するような使われ方をする要素をこれに当たる。</p>
<p class="honbun">一般的なブラウザでは前後に改行が入らず、文章の一部として表示される。</p>
<p class="honbun">以下は代表的なインライン要素のタグである。</p>

<blockquote>
<div class="siyorei_source">&lt;a&gt;　&lt;abbr&gt;　&lt;acronym&gt;　&lt;b&gt;</div>
<div class="siyorei_source">&lt;basefont&gt;　&lt;bdo&gt;　&lt;big&gt;　&lt;br&gt;</div>
<div class="siyorei_source">&lt;cite&gt;　&lt;code&gt;　&lt;dfn&gt;　&lt;em&gt;</div>
<div class="siyorei_source">&lt;font&gt;　&lt;i&gt;　&lt;img&gt;　&lt;input&gt;　&lt;kbd&gt;</div>
<div class="siyorei_source">&lt;label&gt;　&lt;q&gt;　&lt;s&gt;　&lt;samp&gt;　&lt;select&gt;</div>
<div class="siyorei_source">&lt;small&gt;　&lt;span&gt;　&lt;strike&gt;　&lt;strong&gt;</div>
<div class="siyorei_source">&lt;sub&gt;　&lt;sup&gt;　&lt;textarea&gt;　&lt;tt&gt;　&lt;u&gt;　&lt;var&gt;</div></blockquote>
<div></div>
<h2>&lt;div&gt;</h2>
&lt;div&gt;タグとは、<span><strong>囲った部分をブロック要素としてまとめて扱うことができる</strong></span>ようになるタグになります。

HTML構造（レイアウト）に沿って要素を区切っていくように使う。

pタグであれば段落を区別するためのタグで、h1タグであれば見出しを作るためのタグになるが、divタグはそれ単体では<span><strong>意味を持たない</strong></span>特殊なタグである。

&nbsp;
<div>
<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code>&lt;div class="header"&gt;
/* headerグループのブロックレベル要素 */</code><code>&lt;div&gt;</code> <code>&lt;div class="main"&gt;
/* mainグループのブロックレベル要素 */</code><code>&lt;div&gt;</code><code>
&lt;div class="footer"&gt;
/* footerグループのブロックレベル要素 */</code><code>&lt;div&gt;</code></pre>
</div>
</div>
&nbsp;

&nbsp;
<h2>&lt;input&gt; &lt;textarea&gt;</h2>
<strong>&lt;input&gt;</strong>タグは1行のテキストを受け取る為の入力欄を作る要素である。

<strong>&lt;textarea&gt;</strong>タグは複数行のテキストを受け取る為の入力欄を作る要素である。

<span>&lt;input&gt;要素には<span class="highlight">type属性</span>を指定することができ、type属性に<span class="highlight">submit</span>を指定すると入力欄ではなく送信ボタンにる。</span>

<span>ボタンに表示されるテキストは、日本語のブラウザではデフォルトで「送信」になる。</span>

<span class="highlight">value属性</span><span>に任意の値を指定することで、ボタンに表示されるテキストを変更することができる。</span>

&nbsp;

&nbsp;
