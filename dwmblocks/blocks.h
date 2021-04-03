//Modify this file to change what commands output to your statusbar, and recompile using the make command.

//static char *fonts[] = { "JetBrains Mono Nerd Font;size=20" };
static const Block blocks[] = {
	/*Icon*/	/*Command*/				/*Update Interval*/	/*Update Signal*/
	{"  ",	"~/dwmblocks/src/volume.sh",			1,			10},
	{"  ",	"~/dwmblocks/src/ram.sh",			10,			0},
	{"  ",   "~/dwmblocks/src/clock.sh",			60,			0},
	
};

//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim[] = "  |  ";
static unsigned int delimLen = 9;
