---
title: Linuxの導入手順と防備録(デュアルブート)
slug: linux-installation-method-and-note-to-self
date: 2019-09-26T16:43:40+09:00
categories: 
 - PC関連
description: 
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/ddghc4l09/thumbnail/.jpg
draft: true
---

<!--more-->

以下は自分でLinux(Lubuntu)をデュアルブートするまでにしてきたことの記録である。
今後Linuxを使う上での防備録としても役に立てたい。

[toc]

<h2>1.導入用USBの作成からインストールまで</h2>

<ol>
<li>以下サイトからisoイメージをダウンロードする。
<a href="https://lubuntu.me/downloads/">Lubuntu iso Downlord</a>
(当時は"18.04.3 Bionic Beaver LTS (LXDE)"を選択)</p></li>
<li><p>インストール用メディアを作成する
デュアルブートで使用したかったので、以下のサイトを参考にUSBメディアを作成した。
<a href="https://report.hot-cafe.net/lubuntu-usb-bios-3035">無料OS『Lubuntu』…インストール用USBメモリの作り方とPC設定！</a></p></li>
<li><p>パーティションの設定
Lubuntuをインストールするための領域を決める。
Lubuntuのインストーラーからも設定できるが、今回はWindows側で予め未割り当ての領域(20000MBぐらい)を確保しておいた。
Windows側でパーティションの設定をするには、以下のリンクを参考にして行った。
<a href="https://cloud-work.net/linuxmint/ntfspartition/">NTFSディスクのパーティションサイズを変更してWindowsとLinux Mintのデュアルブート</a></p></li>
<li><p>インストールを開始
BIOS側の設定が正しく反映されていれば以下の選択画面が表示される。

<img src="https://4.bp.blogspot.com/-egq5yCQzQ_c/Um0tSEZpHZI/AAAAAAAAkU4/PUkenTgT_yc/s640/Lubuntu13.10_LiveMedia_BootMenu.jpg" alt="インストール画像" />

"Install Lubuntu"を選択後、以下のリンクの通りに作業すれば問題なくInstallされるはず。
<a href="https://kledgeb.blogspot.com/2013/10/lubuntu-1310-2-lubuntu-1310.html">Lubuntu 13.10 その2 - Lubuntu 13.10のインストール（ ライブメディアから起動 〜 インストールの種類）</a></p></li>
<li><p>Lubuntuを起動する
Installに成功していれば、PCの電源を入れると"起動するOSを選択する画面"が表示される。
Lubuntuにカーソルを合わせてEnterを押せばOK。
もちろんWindowsならWindowsが立ち上がってくれる。
<strong>しかし、私のPCではなぜか名称が"Lubuntu"ではなく"Ubuntu"になっている。</strong>
が、Ubuntuを選択して起動したら、しっかりとLubuntuが立ち上がってくれる。
(ここだけ調べてみても何故なのかわからなかったが、特に問題ないので放置することにした。)</p></li>
</ol>

<h2>2.インストール後にやった環境設定</h2>

<h5>ディレクトリの日本語表記を英語に変更した。</h5>

{{< blogcard url=http://puff000.web.fc2.com/pc/pc5/20140913-05/index.html >}}
<h5>GIFに関して</h5>

{{< blogcard url=https://iwb.jp/gif-animation-play-javascript/ >}}
<h5>CapsLockをCtrlに変えたので、変換メソッドの切り替え(Shift+CapsLock)やESCの代わり(CapsLock+角括弧)を使うようにした。</h5>

ちなみに.Xmodmapの内容を全部消して再起動すれば、これを初期化できる。
{{< blogcard url=https://lambdalisue.hatenablog.com/entry/2013/09/27/212118 >}}
<h5>タッチパッドに手のひらが触れてカーソルが動くのを防止した。</h5>

{{< blogcard url=https://qiita.com/uchan_nos/items/ccc4ef7e319cb6200cc9 >}}
<h5>[Eye of GNOME]をインストールして画像ビューはターミナルで[eog]と打てば表示されるようにした。</h5>

{{< blogcard url=https://help.gnome.org/users/eog/stable/index.html.ja#advanced >}}
<h5>コンソールの文字化け対策</h5>

{{< blogcard url=https://knowledge4linux.blogspot.com/2014/05/linux-tips.html >}}
<h2>3.vim環境設定(.vimrcの設定)</h2>

<h3>vim全般に関わる設定</h3>

<h5>URLが書かれた文字列上で[gx]と入力するとブラウザで表示されるようにした。</h5>

{{< blogcard url=https://easyramble.com/open-url-with-browser-from-vim.html >}}
<h5>ディレクトリツリーを表示できるプラグイン[NERDTree]を導入した。</h5>

{{< blogcard url=https://qiita.com/zwirky/items/0209579a635b4f9c95ee >}}
<h5>全角スペースのハイライト設定</h5>

{{< blogcard url=https://oki2a24.com/2019/02/22/attention-when-visualizing-double-byte-space-with-vim-and-error-when-failing/ >}}
<h5>文字化け対策</h5>

全角文字が重ならないようにする設定
{{< blogcard url=https://www.softel.co.jp/blogs/tech/archives/5890 >}}
<h5>auto fcitx(挿入モードからコマンドモードになった時、自動的に半角英数にする)</h5>

{{< blogcard url=http://www.nemotos.net/?p=2019 >}}
<h3>markdownの為に設定したこと</h3>

<h5>NeoBundle設定</h5>

{{< blogcard url=https://www.mk-mode.com/blog/2013/08/25/vim-install-neobundle/# >}}
<h5>.vimrcとNeoBundleでMarkdownの環境を構築した。</h5>

{{< blogcard url=https://www.mk-mode.com/blog/2013/08/25/vim-install-neobundle/# >}}
<h5>mdファイルをHTMLに変換するためにPandocを導入した。</h5>

{{< blogcard url=https://qiita.com/sky_y/items/3c5c46ebd319490907e8 >}}
<h5>pandocでMarkdownをHTMLに一発変換したりCSSを適応して変換するコマンド</h5>

{{< blogcard url=https://kawahara-zakki.com/vim-markdown/ >}}{{< blogcard url=https://qiita.com/fk_2000/items/d9ba2984349728bb5609 >}}
<h5>vim-quickrunがpandocに文章を渡すための設定</h5>

[blogcard url="https://kawahara-zakki.com/vim-markdown/]

<h5>vim(markdown)からWordPressの記事を投稿できるようにした</h5>

{{< blogcard url=https://hackheatharu.xyz/create-wordpress-blog-posts-from-vim-with-markdown-notation/ >}}
<h5>markdownで作成したWordPress記事のリンクを別タブで開けるようにする</h5>

{{< blogcard url=https://blog.takoyama.net/technique/md-link-tab/ >}}
<h2>[.vimrc]ソース</h2>

<pre><code class="vim">set number
syntax on
filetype plugin indent on
set laststatus=2
set statusline=%y


"""""全角スペースのハイライト設定
"[https://oki2a24.com/2019/02/22/attention-when-visualizing-double-byte-space-with-vim-and-error-when-failing/]
scriptencoding utf-8
augroup highlightIdegraphicSpace
  autocmd!
  autocmd Colorscheme * highlight IdeographicSpace term=underline ctermbg=Gray guibg=Gray
  autocmd VimEnter,WinEnter * match IdeographicSpace /　/
augroup END
colorscheme default 



"""""文字化け対策
"全角文字が重ならないようにする設定[https://www.softel.co.jp/blogs/tech/archives/5890]
set encoding=utf-8
set fileencodings=iso-2022-jp,euc-jp,sjis,utf-8
set ambiwidth=double 


"""""auto fcitx(挿入モードからコマンドモードになった時、自動的に半角英数にする)
let g:input_toggle = 1
function! Fcitx2en()
   let s:input_status = system("fcitx-remote")
   if s:input_status == 2
      let g:input_toggle = 1
      let l:a = system("fcitx-remote -c")
   endif
endfunction

set ttimeoutlen=150
"Leave Insert mode
autocmd InsertLeave * call Fcitx2en()



"""""NeoBundlei設定
"[https://www.mk-mode.com/blog/2013/08/25/vim-install-neobundle/#"] 
set nocompatible    "viとの互換性をとらない（vimの独自拡張機能を使う為）
filetype off 

if has('vim_starting')
  " neobudle.vimの関数を呼ぶためにインストールしたディレクトリを指定
  set runtimepath+=~/.vim/bundle/neobundle.vim/
endif

call neobundle#begin(expand('~/.vim/bundle/'))
NeoBundleFetch 'Shougo/neobundle.vim'

"管理するプラグイン
NeoBundle 'Shougo/neocomplcache'
NeoBundle 'tpope/vim-fugitive'
NeoBundle 'gregsexton/gitv'
NeoBundle 'vim-scripts/sudo.vim'
NeoBundle 'open-browser.vim'
NeoBundle 'plasticboy/vim-markdown'
NeoBundle 'kannokanno/previm'
NeoBundle 'tyru/open-browser.vim'
NeoBundle 'thinca/vim-quickrun'
NeoBundle 'scrooloose/nerdtree'
NeoBundle 'MrPeterLee/VimWordpress'
NeoBundle 'tpope/vim-markdown'

call neobundle#end()
filetype plugin indent on
NeoBundleCheck



"""""open-browser 設定
"[https://easyramble.com/open-url-with-browser-from-vim.html]
let g:netrw_nogx = 1 " disable netrw's gx mapping.
nmap gx &lt;Plug&gt;(openbrowser-smart-search)
vmap gx &lt;Plug&gt;(openbrowser-smart-search)



""""""MarkDown設定
au BufRead,BufNewFile *.md set filetype=markdown



""""""vim-quickrunがpandocに文章を渡すための設定
"[https://kawahara-zakki.com/vim-markdown/]
let g:quickrun_config = {}
let g:quickrun_config = {
      \ "markdown" :{
      \ 'type': 'markdown/pandoc',
      \ 'cmdopt': '-f markdown+hard_line_breaks'
      \}
\}
</code></pre>

<!-- Link  -->
