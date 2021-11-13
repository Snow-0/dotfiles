source $HOME/.config/nvim/vim-plug/plugins.vim


"Nord theme
colorscheme nord

" Airline
source $HOME/.config/nvim/themes/airline.vim

setlocal spell
set spelllang=nl,en_us
inoremap <C-l> <c-g>u<Esc>[s1z=`]a<c-g>u
let g:UltiSnipsExpandTrigger = '<tab>'
let g:UltiSnipsJumpForwardTrigger = '<tab>'
let g:UltiSnipsJumpBackwardTrigger = '<s-tab>'

map S :! zathura %<.pdf & <CR><CR>
map I :w \| :! pdflatex %<CR><CR>
