//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/						/*Update Interval*/	/*Update Signal*/
	{"", "cat /tmp/recordingicon 2>/dev/null",				0,			9},
	{"", "/home/arch/dwmblocks/scripts/updates.sh",	0,			8},
	{"", "sb-memory",				10,			14}, 
	{"", "/home/arch/dwmblocks/scripts/cpu.sh",					10,			18}, 
	{"", "/home/arch/dwmblocks/scripts/volume.sh",	0,			10},
	{"", "sb-clock",							60,			1},
	{"Mem:", "free -h | awk '/^Mem/ { print $3\"/\"$2 }' | sed s/i//g",	30,			0},

	{"", "date '+%b %d (%a) %I:%M%p'",					5,			0},
};

//Sets delimiter between status commands. NULL character ('\0') means no delimiter.
static char *delim = "|";

// Have dwmblocks automatically recompile and run when you edit this file in
// vim with the following line in your vimrc/init.vim:

// autocmd BufWritePost ~/.local/src/dwmblocks/config.h !cd ~/.local/src/dwmblocks/; sudo make install && { killall -q dwmblocks;setsid dwmblocks & }
