---
title: Wordpressのブログ記事をvimからMarkdown記法で投稿する
slug: create-wordpress-blog-posts-from-vim-with-markdown-notation
date: 2019-10-12T15:07:25+09:00
categories: 
 - PC関連
description: 
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/ddghc4l09/thumbnail/.jpg
draft: true
---

<!--more-->

当ブログはWordpressによる運営をしています。
今までビジュアルビュワーを使ってコツコツ記事を投稿してきました。
しかし普段使うEditerはvimですし、ささいなメモ書きだろうとMarkdown記法で書いているため『Markdownで書いたデータをvimで投稿してぇ』という願望が湧くのです。
&nbsp;

というわけで、これを実現するための努力をした結果、やっとそれらしい環境を整えることに成功しました。
もちろん、この記事もMarkdownで書いてvimから投稿したブログ記事です。
&nbsp;

この環境を作り上げるまでにしてきたことの防備録や、知識の共有を目的に記事を作成しました。
同じような思いを抱くvim初心者の役に立てれば幸いです。
&nbsp;<br />
&nbsp;

<h2>"VimWordPress"を導入する</h2>

初めにvimからブログサイトへアクセスを可能にするプラグインを導入します。
そのプラグインとは<strong><a href="https://github.com/MrPeterLee/VimWordpress">VimWordPress</a></strong>というものです。
&nbsp;

導入方法はプラグインの管理方法によって異なります。
こればっかりは人それぞれなので各自で調べてください。
私の場合はvimのプラグイン管理に<strong>NeoBundle</strong>を採用しているため、<code>.vimrc</code>に以下のような記述をしてインストールしました。
&nbsp;

<pre><code class="vim">NeoBundle 'MrPeterLee/VimWordpress'
</code></pre>

&nbsp;

無事インストールできたのであればホームディレクトリに<code>.vimpressrc</code>というファイルを作成します。
このファイルにはvimでアクセスして編集ブログの情報を記入します。
以下の例のように記述しましょう。
&nbsp;

<pre><code class="vim">[Blog0]
blog_url = http:// https://hackheatharu.xyz/
username = **********         (ブログのユーザー名)
password = **********         (ブログのパスワード)
</code></pre>

&nbsp; 
これで準備完了です。
vimから<code>:BlogList</code>とコマンドすることで記事一覧が表示されます。
この一覧表示から記事を選んで<code>Enter</code>を押すとその記事が開き、<code>delete</code>を押せば記事をゴミ箱に移動させます。
&nbsp;

VimWordPressで使用できるコマンドは、自分が調べた限りだと以下の通りです。
また、基本的に以下のコマンドは<code>:BlogList</code>で記事を選ぶか<code>:BlogNew</code>で記事を作成するかしないとコマンドは使えない。
&nbsp;

<table>
<thead>
<tr>
  <th align="left">command</th>
  <th align="left">Processed</th>
</tr>
</thead>
<tbody>
<tr>
  <td align="left">-BlogList <br>-BlogList page NUM <br>-BlogList post NUM</td>
  <td align="left">投稿した記事の一覧を表示する。<br><code>page(投稿記事)</code>か<code>post(固定ページ)</code>が無指定ならpageが表示される。<br><code>NUM</code>が無指定なら30件表示される。</td>
</tr>
<tr>
  <td align="left">-BlogNew <br>-BlogNew page<br>-BlogNew post</td>
  <td align="left">新規作成を行う。<br>無指定ならpageで作成される。</td>
</tr>
<tr>
  <td align="left">-BlogSave <br>-BlogSave draft <br>-BlogSave publish</td>
  <td align="left">作成した記事を保存する。<br><code>draft</code>は下書き。<br><code>pablish</code>は公開。<br>無指定なら未公開で保存される。</td>
</tr>
</tbody>
</table>

&nbsp;

実は上記リスト以外にもコマンドは存在しますが、バグで動かない、もしくはそんなに使わないものばかりなので割愛しました。
逆に言うと、これらを使えれば十分です。
&nbsp; 
&nbsp;

<h2>vimから記事を作成・編集してみる</h2>

記事を作成する時、最初の10行には記事の設定を記述する項目が設けられます。
&nbsp;

<pre><code class="HTML">
"=========== Meta ============
"StrID : 
"Title : 
"Slug  :
"Cats  :
"Tags  :
"=============================
"EditType   : post
"EditFormat : HTML
"BlogAddr   : http://haya14busa.com
"========== Content ==========
</code></pre>

&nbsp;

<strong><code>StrID</code></strong>は自動で割り振られるので記述することは無いと思います。
<strong><code>Title</code></strong>はブログタイトルを記入してください。空白だとエラーになります。
<strong><code>Slug</code></strong>はパーマリンクです。
<strong><code>Cats</code></strong>はカテゴリです。自分がWordPress側で用意したカテゴリしか指定できません。
<strong><code>Tags</code></strong>はタグです。これは書いたものをそのまま新規タグとして生成してくれます。
<strong><code>EditType</code></strong>で投稿記事か固定ページを選択しますが、基本いじらないでしょう。
<strong><code>BlogAddr</code></strong>も複数ブログを運営しない限り編集しないですね。

<strong><code>EditFormat</code>に関してはバグがあり少々やっかいなので後述します。</strong>

&nbsp;

あとはContent以下にブログ内容を記述していくだけです。
お使いのvim環境に合わせてHTMLで書いてもいいですしMarkdownで書いてもOKです。
&nbsp;

ただし、デフォルトでは<code>filetype</code>が指定されていないはずなので<code>:set filetype=markdown</code>と形式を指定してから書こう。

&nbsp;

<h2>"Markdown Editer"を使ってWordpress側でMarkdown形式に変換してもらう</h2>

ここまでの手順を終えたならばvimでブログ記事を投稿できるようになっているはずです。
が、肝心なMarkdown記法で投稿する設定が済んでいません。
&nbsp;

Markdown記法でpostしてもWordpress側はHTMLに変換してくれません。
このままではWordpressのテキストビュワーのような使い方で終わってしまいます。
なのでWordPress側のプラグインの力を借ります。
&nbsp;

検索すると多数のプラグインがありますが<a href="https://ja.wordpress.org/plugins/markdown-editor/">『Markdown Editer』</a>を選んでください。
理由は２つあります。

<ol>
<li>ダウンロードして有効化するだけで良いから楽。</li>
<li>他プラグインではBlogListで記事を取得すると<strong>HTMLに変換された状態で取得してしまう</strong>が、なぜか「Markdown Editer」のみMarkdown形式を保ったまま取得してくれる。</li>
</ol>

1の理由はともかく2が最も重要です。
2019年9月現在までにあるWordpressプラグインを一通り試したつもりですが、他のものでは文章がHTMLに変換されてしまうのです。
せっかくMarkdown記法で書いたものをHTMLで書き直す羽目になってしまいます。
&nbsp;

もし「Markdown Editer」を使うのが嫌であれば<strong>『下書きを.mdで別に保存しおく』</strong>ことが必要になってしまいます。
これはこれでめんどくさいと思いますので、特別な理由が無い限りは素直に「Markdown Editer」を使うことをオススメします。
&nbsp;

<h2>VimWordPressの注意点</h2>

実はWordpressプラグインに頼らなくてもMarkdown形式に変換する方法があります。
というのもVimWordPressには最初からその機能が備わっています。
&nbsp;

[blogcard url="https://tsuchikazu.net/vim_markdown_wordpress/"]

&nbsp;

<code>pip3 install markdown2</code> とコンソールからPython3にmarkdown2をインストールします。
<code>BlogNew</code>などで記事を作成した際<code>"EditFormat : HTML</code>の部分を<code>"EditFormat : Markdown</code>と変更したら、晴れてmarkdownで投稿できた<strong>はずでした</strong>。

が、残念ながら<strong>Python側でエラーが発生(たぶんバグ)</strong>するため使うことができません。
以下、参考サイト
&nbsp;

[blogcard url="http://skrby1.com/?p=142"]

&nbsp;

Pythonのソースをいじれば直せそうですが、前述した「Markdown Editer」で運用しちゃった方が楽です。
少なくとも私はPostする際、markdown形式の投稿が出来ればいいだけなので、どうしてもVimWordPressの機能を使いたいわけじゃなかったので。

&nbsp;

<h2>「Markdown Editer」でコードハイライトが中央揃えになる不具合</h2>

「Markdown Editer」を使用する際、１つだけ沼にハマったことがありました。
<strong>コードハイライトが中央揃えになってしまう不具合</strong>に遭遇しました(2019/8時点)。

この不具合については以下のサイト様を参考にWordPress側で<code>function.php</code>に2行のコードを加えることで解決できました。

参考サイト
[blogcard url="https://cod-sushi.com/wordpress-markdown-editor-code/"]

追加するコード

<pre><code class="php">add_filter( 'markdown_editor_highlight', '__return_false' );
add_filter( 'markdown_editor_clipboard', '__return_false' );
</code></pre>

<h2>Markdownで作成したリンクを別タブで開くためには</h2>

Markdownでリンクを挿入する<code>[タイトル](URL)</code> と記述しますが、このままだと今見ているタブにリンクのサイトが表示されてしまいます。
これを解決するには

<code>&lt;a href="URL" target=”_blank”  rel="noopener noreferrer"&gt;タイトル&lt;/a&gt;</code>

とHTMLで記述しなければいけないのです。

流石にめんどうなので<strong>Wordpressのheader.phpにMarkdownで書いたリンク文字を別タブで開くものとして認識してもらう</strong>ことにします。

やり方は以下を参考にしました。

[blogcard url="https://decoy284.net/markdown-link-target-blank/"]

<h2>使ってみた感想</h2>

動画・画像のURL記述、プラグイン特有の記述等はWordpress側でやった方が楽です。
ですが、やはり<strong>Vimでブログ記事を書ける</strong>というのは楽です。
とても作業が捗ります。

最大のメリットはブログ作成時、基本vimしか立ち上げないのでくっそ軽いです。
当然といえば当然ですが外出時のクソ雑魚デザリングや貧弱Wifiのような環境なぞvimで文章を書くだけなら大した問題じゃありません。
個人的にはvimerがWordPressでブログ更新する最適解かなと思います。
