" Reference
" https://qiita.com/ykyk1218/items/ab1c89c4eb6a2f90333a
" MyVImCommand
source ~/.vim/mycommand.vim

" 1LienSetting
filetype plugin indent on
let loaded_matchparen = 1 "反対側の括弧をハイライトしない
syntax on
set number
" https://maku77.github.io/vim/settings/statusline.html
set statusline=%F%m%h%w\ %<[ENC=%{&fenc!=''?&fenc:&enc}]\ [FMT=%{&ff}]\ [TYPE=%Y]\ %=[CODE=0x%02B]\ [POS=%l/%L(%02v)]
set laststatus=2 "ステータス行を常に表示
set showcmd "ウィンドウの右下にまだ実行していない入力中のコマンドを表示
set title
set clipboard=unnamedplus
set hlsearch
set ruler
set noswapfile
set incsearch
set wildmenu wildmode=list:full

" autcmd
au BufRead,BufNewFile *.md set filetype=markdown " MarkDown設定

" KeyMap
inoremap <silent> <Esc> <Esc>`^
inoremap {<Enter> {}<Left><CR><ESC><S-o>
imap [ []<left>
imap ( ()<left>
noremap PP "0p
noremap x "_x

" auto reload .vimrc
augroup source-vimrc
  autocmd!
  autocmd BufWritePost *vimrc source $MYVIMRC | set foldmethod=marker
  autocmd BufWritePost *gvimrc if has('gui_running') source $MYGVIMRC
augroup END

" auto comment off
augroup auto_comment_off
  autocmd!
  autocmd BufEnter * setlocal formatoptions-=r
  autocmd BufEnter * setlocal formatoptions-=o
augroup END

" HTML/XML閉じタグ自動補完
augroup MyXML
  autocmd!
  autocmd Filetype xml inoremap <buffer> </ </<C-x><C-o>
  autocmd Filetype html inoremap <buffer> </ </<C-x><C-o>
augroup END



" 全角スペースのハイライト設定
" [https://oki2a24.com/2019/02/22/attention-when-visualizing-double-byte-space-with-vim-and-error-when-failing/]
scriptencoding utf-8
augroup highlightIdegraphicSpace
  autocmd!
  autocmd Colorscheme * highlight IdeographicSpace term=underline ctermbg=DarkGreen guibg=DarkGreen
  autocmd VimEnter,WinEnter * match IdeographicSpace /　/ 
augroup END
colorscheme default 


" 文字化け対策
set encoding=utf-8
set fileencodings=iso-2022-jp,euc-jp,sjis,utf-8
set ambiwidth=double "全角文字が重ならないようにする設定[https://www.softel.co.jp/blogs/tech/archives/5890]



" auto fcitx(挿入モードからコマンドモードになった時、自動的に半角英数にする)
let g:input_toggle = 1
function! Fcitx2en()
   let s:input_status = system("fcitx-remote")
   if s:input_status == 2
      let g:input_toggle = 1
      let l:a = system("fcitx-remote -c")
   endif
endfunction
 
set ttimeoutlen=150
" Leave Insert mode
autocmd InsertLeave * call Fcitx2en()



" NeoBundlei設定
" [https://www.mk-mode.com/blog/2013/08/25/vim-install-neobundle/#"] 

"" viとの互換性をとらない（vimの独自拡張機能を使う為）
set nocompatible 
filetype off 

if has('vim_starting')
"" neobudle.vimの関数を呼ぶためにインストールしたディレクトリを指定
  set runtimepath+=~/.vim/bundle/neobundle.vim/
endif

call neobundle#begin(expand('~/.vim/bundle/'))
NeoBundleFetch 'Shougo/neobundle.vim'

"" 管理するプラグイン
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
NeoBundle 'Shougo/neocomplete.vim' "http://engineerspirit.com/2016/12/03/post-216/
NeoBundle 'tpope/vim-markdown'
NeoBundle 'w0ng/vim-hybrid'
NeoBundle 'TwitVim'

call neobundle#end()
filetype plugin indent on
NeoBundleCheck

set background=dark
colorscheme hybrid


" open-browser 設定
" [https://easyramble.com/open-url-with-browser-from-vim.html]
let g:netrw_nogx = 1 " disable netrw's gx mapping.
nmap gx <Plug>(openbrowser-smart-search)
vmap gx <Plug>(openbrowser-smart-search)

" vim-quickrunがpandocに文章を渡すための設定
" [https://kawahara-zakki.com/vim-markdown/]
let g:quickrun_config = {}
let g:quickrun_config = {
      \ "markdown" :{
      \ 'type': 'markdown/pandoc',
      \ 'cmdopt': '-f markdown+hard_line_breaks'
      \}
\}


" neocompleteの設定
highlight Pmenu ctermbg=4
highlight PmenuSel ctermbg=1
highlight PMenuSbar ctermbg=4

" 補完ウィンドウの設定
set completeopt=menuone

" 補完ウィンドウの設定
set completeopt=menuone

" rsenseでの自動補完機能を有効化
let g:rsenseUseOmniFunc = 1
" let g:rsenseHome = '/usr/local/lib/rsense-0.3'

" auto-ctagsを使ってファイル保存時にtagsファイルを更新
let g:auto_ctags = 1

" 起動時に有効化
let g:neocomplcache_enable_at_startup = 1

" 大文字が入力されるまで大文字小文字の区別を無視する
let g:neocomplcache_enable_smart_case = 1

" _(アンダースコア)区切りの補完を有効化
let g:neocomplcache_enable_underbar_completion = 1

let g:neocomplcache_enable_camel_case_completion  =  1

" 最初の補完候補を選択状態にする
let g:neocomplcache_enable_auto_select = 1

" ポップアップメニューで表示される候補の数
let g:neocomplcache_max_list = 20

" シンタックスをキャッシュするときの最小文字長
let g:neocomplcache_min_syntax_length = 3

" 補完の設定
autocmd FileType ruby setlocal omnifunc=rubycomplete#Complete
if !exists('g:neocomplete#force_omni_input_patterns')
	let g:neocomplete#force_omni_input_patterns = {}
endif
let g:neocomplete#force_omni_input_patterns.ruby = '[^.*\t]\.\w*\|\h\w*::'

if !exists('g:neocomplete#keyword_patterns')
	let g:neocomplete#keyword_patterns = {}
endif
let g:neocomplete#keyword_patterns['default'] = '\h\w*'
