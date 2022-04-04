source $HOME/.config/nvim/vim-plug/plugins.vim


"Nord theme
"colorscheme nord

"Tokyo Night Theme
"colorscheme tokyonight
"Nord Them
colorscheme nord

" Airline
" source $HOME/.config/nvim/themes/airline.vim

set number


map <C-c> "+y
map <C-p> "+p


if has("autocmd")
  au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$")
    \| exe "normal! g'\"" | endif
endif
