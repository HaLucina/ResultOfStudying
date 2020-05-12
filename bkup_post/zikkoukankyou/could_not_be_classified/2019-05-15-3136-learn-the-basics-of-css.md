---
title: CSSの基礎を学び直す
slug: learn-the-basics-of-css
date: 2019-05-15T05:09:46+09:00
categories: 
 - HTML
description: 
thumbnailImagePosition: left
thumbnailImage: //d1u9biwaxjngwg.cloudfront.net/japanese-test-post/peak-140.jpg
draft: true
---
<!--more-->

【WordPressをもっと使いこなすための技術メモ】

WEB系のプログラミングを学び直してWordPressに活かすことを目的に書いていきます。

<strong>※随時編集中</strong>

[toc]

<h2>CSSとは</h2>

<span>CSS（Cascading Style Sheets、カスケーディング・スタイル・シート）とは、ウェブページのスタイルを指定する言語。</span>

つまりHTMLで記述した要素に対し色や大きさなどを変化させるために使う。

HTMLには<code>&lt;center&gt;</code>や<code>&lt;font&gt;</code>などの装飾目的の要素（タグ）や属性が存在しているが、あくまでHTMLは情報構造（Webページの組み立て）を定義するための言語であり、<strong>見栄えを制御するためにはCSSを使う</strong>。

CSSは<strong>セレクタ</strong>（HTMLの要素）を選択（セレクト）し、セレクタで何をしたいか<strong>プロパティ</strong>を指定して記述する。

例えば<code>&lt;h1&gt;</code>要素に対するCSSの書き方は以下が基本である。

<img src="http://yume.hacca.jp/koiki/css/sample1.gif" width="391" height="123" class="alignnone size-medium" />

この時、<strong>プロパティの末尾はコロン（：）、行末はセミコロン（；）,</strong>を付ける。

<h2>コメント</h2>

『<strong>/* */</strong>』で囲むとコメントを書くことができる。

ただし、コメントをコメントで入れ子に出来ない

<pre><code class="CSS">/* ここのテキストはコメントになる */

/* もちろん複数行もできる

　　　　 ∧＿∧
　　＿_／＿＿＿＼
　 (　＿|´･ω･`|＼ &lt;踊れ！カルメン！
　　＼ヽ ￣￣￣　 ｜
　　∠ノ　　　　 /｜
　～(　　　　　／／
　　 |　＿＿ノ￣￣)
　　 | /　　￣/ ／
　　 |/　　　/／

</code></pre>

<h2>色</h2>

色の変更は『<strong>color</strong>』プロパティを使う。

記述できる値は以下がある。

<ul>
    <li><strong>色の名前</strong>（Webカラーネーム）
redなど名前で指定する方法。
⇒ <a href="http://www.recipi.jp/1414#section300">カラーネーム</a>。</li>
    <li><strong>カラーコード
</strong>『<strong>color: #ff0000;</strong>』のように値は<strong>16進数のカラーコード</strong>で指定する方法。
ちなみに『#ffffff』のように同じ値が続く場合『#fff』のように省略できる。
⇒  <a href="http://sakichin.com/other/color_code.html">カラーコード参考</a>
⇒ <a href="http://webcre8.jp/think/design-color-code.html">デザイナーっぽくカラーコードの16進数を覚えたくないですか？</a></li>
    <li><strong>RGB
『color: rgb<span>(255,0,0);</span>』</strong>のように0~255で表された光の三原色を指定する方法。
<strong>値を0~255ではなく0~100%にして表すことが可能。</strong>
ちなみに<strong>『</strong><strong>rgba』</strong>プロパティを使うと透明度も指定できる。
⇒ <a href="https://www.webcreatorbox.com/webinfo/color-name">RGB値参考</a>
⇒ <a href="http://raining.bear-life.com/css/css3%E3%81%AE%E3%80%8Crgba%E3%80%8D%E3%81%A7%E8%83%8C%E6%99%AF%E8%89%B2%E3%82%92%E9%80%8F%E9%81%8E%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95">rgbaとは</a></li>
    <li><strong>HSL</strong>
<strong>『color: <span>hsl(0,100%,50%)</span><span>;</span>』</strong>のように<span>色相環での角度（ 0～359度 ）で色を、そのあと彩度と輝度を％で「,（カンマ）」で区切って表す方法。</span><span>
</span>ちなみに<strong>『</strong><strong>rgba』</strong>のように『<strong>hsla</strong>』プロパティを使うと透明度も指定できる。<span>
</span>⇒ <a href="https://www.peko-step.com/html/hsl.html">HSLとは</a>
⇒ <a href="https://cssroller.com/hsl/">CSSでの使い方参考</a></li>
</ul>

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>/* 以下は全部 "赤" を表現 */

h1{
 color: red;
 color: #ff0000;
 color: rgb(255,0,0);
 color: hsl(0,100%,50%);
}</code></pre>
</div>

 

<h3>Webセーフカラー</h3>

<strong>ブラウザや OS の種類に関係なく、Web ページで常に表示できる 216 色のカラーのこと。</strong>

Web セーフカラー<span>のみを使用して画像を作成した場合、</span>Web<span> ブラウザーで表示する限り、常に正確に表示されることになる。</span>

⇒ <a href="http://www.htmq.com/color/websafe216.shtml">Webセーフカラー</a>

 

<h2>文字の大きさ・種類・太さ</h2>

<a name=""></a>文字の大きさの変更は『<b>font-size</b>』プロパティを使う。

値の単位は『<strong>px</strong> <strong>(ピクセル)</strong>』で指定する。

文字の種類は『<strong>font-family</strong>』プロパティを使う。

明朝体は『<strong>serif</strong>』、ゴシック体は『<strong>sans-serif</strong>』など様々な種類があるので、主要なもの以外覚える必要は無い。

<strong>ただし、フォント名にスペースがある場合はダブルクォーテーション（"）で囲まなければならない。</strong>

<span><span class="inline-code">『<strong>font-weight</strong>』</span>プロパティを用いると文字の太さを変更することができる。</span>

<span><span class="inline-code">normal</span>または<span class="inline-code">boldを指定するが、</span></span><span><span class="inline-code">

&lt;

h1></span>~<span class="inline-code">

&lt;

h6></span>の要素は初期状態で<span class="inline-code">font-weight: bold;</span>となっているので『<span class="inline-code">font-weight: normal;』</span>と指定すれば文字が細くなります。</span>

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>h1{
 font-size: 10px;
 font-family: serif;
 <span><span class="inline-code">font-weight: normal;</span></span>
}

p{
 font-size: 20px;
 font-family: "Avenir Next";
 <span><span class="inline-code">font-weight: bold;</span></span>
}</code></pre>
</div>

 

 

 

<h2>横幅、高さの変更</h2>

要素の横幅、高さの変更は『<strong>width</strong>』と『<strong>hight</strong>』プロパティを用いる。

画像であれば単純に画像の大きさ、テキストであれば要素の表示範囲が影響する。

<img src="https://saruwakakun.com/wp-content/uploads/2017/01/bdr44405-O4HRWW-02-min-2.png" width="550" height="291" class="alignnone size-medium" />

 

値の単位は<strong>『</strong><strong>px』</strong>または『<strong>%</strong>』で指定する。

また、値に『<strong>auto</strong>』と記述すると初期値が指定され、要素の幅及び高さは自動で決められる。

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>p {
  width: 100px;
  height: 100px;
}</code></pre>
</div>

 

<h2>要素の中央寄せ</h2>

要素を中央寄せする方法は主に２つ。

<ul>
    <li>
<p class="slide-top__title"><span>『<strong>margin: 0 auto;</strong>』 </span></p>
</li>
    <li>
<p class="slide-top__title"><span></span><span>『<strong>text-align: center;</strong>』</span></p>
</li>
</ul>

<span class="highlight">広い範囲を囲うような<strong>ブロック要素</strong></span><strong>の場合は<span class="inline-code">margin</span></strong><span>、</span><span class="highlight">テキストやボタンのような<strong>インライン要素・インラインブロック要素</strong></span><strong>の場合は<span class="inline-code">text-align</span></strong><span>を使うようにする。</span>

 

 

 

<h2>Webページの背景関連</h2>

<h3>背景色の変更</h3>

ある要素範囲に対する背景色を変更するには『<strong>background-color</strong>』プロパティを使う。

単純に背景を変更するのではなく、例えばテキストの背後を任意の色にするなど使いどころは幅広い。

色の指定方法は『<strong>文字の色の変更</strong>』と同じ。

<img src="https://www.sejuku.net/blog/wp-content/uploads/2018/05/bg2.jpg" width="700" height="268" class="alignnone size-medium" />

 

 

<h3>背景に画像を指定する</h3>

背景に画像を指定するには『<span><strong><span class="inline-code">background-image』</span></strong>プロパティを用いる。</span>

<span><span class="inline-code">『<strong>background-image: url(画像のURL);</strong>』で画像を指定することができるが、このままだと背景を埋め尽くすまで画像が繰り返し表示される。</span></span>

そのため『<strong>background-size: cover;</strong>』も同時に設定し、<span class="highlight">1枚の画像で表示範囲を埋め尽くす</span><span>よう画像の大きさが拡大縮小させる。</span>

 

 

<h2>class</h2>

同じタグが複数個ある場合、タグ全てにCSSは適応されてしまう。

『<strong><li class="aiueo"></strong>』のように、htmlファイル側でタグに<strong>classプロパティ</strong>を指定すると、タグに対して個別の名前を付けることが出来る。

これを利用することで、タグを識別してCSSの適応をさせることができる。

普段のセレクタを書く時との違いは『<strong>.aiueo{ ... }</strong>』のように<strong>クラス名の前にドット（.）を必ず付ける。</strong>

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code><ul>
 <li>あいうえお</li>
 <li class="aiueo">あいうえお</li>
 <li class="oeuia">おえういあ</li>
</ul></code></pre>
</div>

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>/* 特に指定無く全部に適応させたい場合
   （タグにはドットを付けない） */

li{
 color:red;
}


/* クラスで指定する時はドットを付ける */
.aiueo{
 color:green;
}

.oeuia{
 color:blue;
}</code></pre>
</div>

 

<h2>display</h2>

<span>『display』プロパティとは要素の表示形式を指定するプロパティである。</span>

以下にブロック要素・インライン要素の特徴を列挙する。

【ブロック要素】

<ul>
    <li>縦に積まれていく</li>
    <li>幅 width と高さ height が指定できる</li>
    <li>上下左右に margin を指定できる</li>
    <li>上下左右に padding を指定できる</li>
    <li>text-align は要素の中身に適応される。</li>
    <li>vertical-align は指定できない。</li>
</ul>

【インライン要素】

<ul>
    <li>横に並んでいく</li>
    <li>幅 width と高さ height は指定できない。幅や高さは文字列の長さや文字の大きさなど、内容物のサイズ。</li>
    <li>左右だけ margin を指定できる</li>
    <li>左右に padding を指定できる。（実は上下も指定できるけど、前後の行や要素にかぶってしまうので、あまり効果はわからない）</li>
    <li>text-align を親ブロックに付けることで指定できる。</li>
    <li>vertical-align を指定できる。</li>
</ul>

 

 

<h2>list-style</h2>

<li>タグを使用した時、先頭の黒点を表示させたくない場合は『<strong>list-style</strong>』<strong>プロパティ</strong>を用いて値に<strong>none</strong>を指定すると消すことができる。

『<strong>list-style-type</strong>』プロパティなら<span>記号やアルファベットなどをマーカーに指定することができる。</span>

『<strong><span>list-style-image</span></strong>』プロパティなら<span>画像をマーカーに指定することができる。</span>

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code><span><ul class=”list″></span>
<span> <li>項目1</li></span>
<span> <li>項目2</li></span>
<span> <li>項目3</li></span>
<span></ul></span></code></pre>
</div>

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>.list {

/* 先頭の点を無くす */
  list-style: none; 

/* 先頭が白丸になる */
  <span>list-style-type: circle;</span>

/* 小文字のアルファベット順 */
  <span>list-style-type: lower-alpha;</span>

/* 画像を指定したい場合の例 */
  <span>list-style-image: url(“hoge.png”);</span>

}</code></pre>
</div>

 

 

<h2>float</h2>

『<strong>float</strong>』プロパティは主に<strong>要素を横並びにする</strong>時などに使用する。

例えば<li>タグはそのまま使うと縦並びになるが、これを指定すると見た目を横並びにすることができる。

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code><span><ul class=”list″></span>
<span> <li>項目1</li></span>
<span> <li>項目2</li></span>
<span> <li>項目3</li></span>
<span></ul></span></code></pre>
</div>

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>.list {

/* 左寄せで横並びにする */
  <span class="crayon-t">float</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-v">left</span><span class="crayon-sy">;</span> 

/* 右寄せで横並びにする */
  <span class="crayon-t">float</span><span class="crayon-o">:</span><span class="crayon-h"> </span><span class="crayon-v">right</span><span class="crayon-sy">;</span>

/* 初期値で配置を指定しない（ほぼ使わない） */
  <span class="crayon-t">float</span><span class="crayon-o">:</span><span class="crayon-h"> none</span><span class="crayon-sy">;</span>

}</code></pre>
</div>

 

 

<h2>margin</h2>

『<strong>margin</strong>』プロパティは要素に対して<strong>外側に余白を作りたい場合</strong>に使用するプロパティである。

単位はpxで、上下左右に対して余白を指定することができる。

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>p{
 /* 上下左右に余白が20px作られる */
 margin: 20px;

 /* 上右下左、それぞれに余白を指定できる */
 margin-top: 20px;
 margin-right: 30px;
 margin-bottom: 40px;
 margin-left: 50px;

 /* 上記は以下のように短縮して記述することも可能 */
 margin: 20px 30px 40px 50px;

/* 値を２つだけにすると上下、または左右に適応される */
margin: 20px 40px;
margin: 30px 50px;

}</code></pre>
</div>

 

 

 

<h2>padding</h2>

『<strong>padding</strong>』プロパティは要素に対して<strong>内側に余白を作りたい場合</strong>に使用するプロパティである。

単位はpxで、上下左右に対して余白を指定することができる。

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>p{
 /* 上下左右に余白が20px作られる */
 padding: 20px;

 /* 上右下左、それぞれに余白を指定できる */
 padding-top: 20px;
 padding-right: 30px;
 padding-bottom: 40px;
 padding-left: 50px;

 /* 上記は以下のように短縮して記述することも可能 */
 padding: 20px 30px 40px 50px;

/* 値を２つだけにすると上下、または左右に適応される */
padding: 20px 40px;
padding: 30px 50px;

}</code></pre>
</div>

 

 

<h2>span</h2>

<span>文中の一部にCSSを適用させたい場合、HTML側で適応したい文章を</span><span><strong><span class="highlight"><span></span>タグ</strong>で囲み、</span><span>CSSで<strong>spanプロパティ</strong>を指定することでその文章のみCSSを適応することができる。</span>

<span><span>要素は前後には改行は必要ないインライン要素の１つである。</span>

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code><p>この花は<span>赤く</span>染まっている</p></code></pre>
<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>span{
 color: red;
}</code></pre>
</div>
</div>

 

 

<h2>border</h2>

<span><span class="highlight">『<strong>border』</strong></span><strong>プロパティ</strong>はボーダー（枠線）を表現することができる要素で</span><span>、枠線の<span class="highlight">太さ</span>、<span class="highlight">種類</span>、<span class="highlight">色</span>を指定して使用する。</span>

<span>上下左右すべてに線を付けたい場合はborderとし、特定の場所にのみ付けたい場合は『border-方向』で記述する。</span>

 

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>h1{
 /* 値は太さ・種類・色の順で指定する */
 border: 5px solid red;


/* 例えば下線を表現したい場合、以下のように方向を指定する */
 border-bottom: 5px solid red;
}</code></pre>
</div>

 

<h3><span>border-radius</span></h3>

『<span>border-radius</span>』<span>プロパティは、ボックスの４つのコーナーを</span><span>角丸に指定することができる。</span>

 

 

<h2>opacity</h2>

『opacity』プロパティは要素の透明度の設定ができる。

<span>透明度は0.0(完全に透明) ~ 1.0(完全に不透明)の数値で指定する。</span>

<strong>値に単位は必要ない。</strong>

<span><span class="inline-code">また、opacity</span>には<strong>要素の<span class="highlight">中身全てを透明にする</span>性質</strong>がある。</span>

背景色のみを透明にするには<strong><span class="inline-code">rgba</span></strong>というものを使う必要がある ⇒ <a href="#文字の色を変更">文字の色の変更</a>

 

<h2><span>letter-spacing</span></h2>

『<strong>letter-spacing</strong>』プロパティは文字の間隔を指定することができる。

値はpxで指定する。

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>p{
 <span>letter-spacing; 2px;
</span> <span>letter-spacing; 10px;</span>
}</code></pre>
</div>

 

<h2><span>line-height</span></h2>

『<strong>line-height</strong>』プロパティは行の高さを指定することができる。

値はpxで指定する。

<span><span class="highlight">本来は行間を調整するたｍのものだが、要素の縦方向の中央</span>に文字を配置するのにも使える。</span>

<span><span class="inline-code">line-height</span>プロパティの「高さの中心」に文字が配置されるため、要素の高さと<span class="inline-code">line-height</span>プロパティを同じ値にすると、文字がちょうど中央に配置されるようになる。</span>

 

<h2>hover</h2>

『<strong>hover</strong>』とは、これが指定されている要素にマウスカーソルでのクリック等がされた時、動的な変化（色が変わるアニメーションなど）を起こすことができる疑似クラスである。

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>a:hover {
  color: orange;
}</code></pre>
</div>

 

<h2>transition</h2>

<span><span class="inline-code">『<strong>transition</strong>』プロパティは</span>アニメーションを付与する。</span>

<span>「変化の対象」や、「変化にかかる時間」などを指定できる。</span>

<span>「変化の対象」には<span class="inline-code">color</span>などのプロパティを指定するが、<span class="inline-code">all</span>を指定すると全てのプロパティに適用される。</span>

<strong><span class="inline-code">transition</span>は多くの場合<span class="inline-code">hover</span>と組み合わせて使用する。</strong>

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>div{
 transition: all 1s; /* 1秒かけて要素を赤く表示する */
}</code></pre>
</div>

 

<h2>position</h2>

『<strong>position</strong>』プロパティを用いると、要素を重ねて表示させるように出来る。

基準位置は左上とし、その<span>位置から</span><span class="inline-code">top・</span><span class="inline-code">left・</span><span class="inline-code">right・</span><span class="inline-code">bottom</span><span>を用いて指定する。</span>

また、基準位置は変更できる。

<ul>
    <li><span>absolute・・・</span>サイト全体の左上を基準にする。</li>
    <li><span>relative  ・・・基準にしたい要素に設定すると、それの左上を基準位置にする。</span></li>
</ul>

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-html" data-lang="HTML"><code><div class="parent">
 <p class="child">hoge</p>
</div></code></pre>
</div>

<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-css" data-lang="CSS"><code>parent{
 position: absolute;
}

child{
 position: relative;
 top: 30px;
 left: 30px;
}
</code></pre>
 

</div>
