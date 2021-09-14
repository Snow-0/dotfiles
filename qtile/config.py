from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "f", lazy.spawn("firefox"), desc="Launches broswer"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

	
layout_theme = {
		"border_width": 3,
		"margin": 8,
		"border_focus": "88c0d0",
		"border_normal": "3b4252"
}
	
layouts = [
    layout.Columns(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme)
]

colors = [["#2e3440", "#2e3440"], #nord0
          ["#3b4252", "#3b4252"], #nord1
          ["#434c5e", "#434c5e"], #nord2
          ["#4c566a", "#4c566a"], #nord3
          ["#d8dee9", "#d8dee9"], #nord4
          ["#e5e9f0", "#e5e9f0"], #nord5
          ["#eceff4", "#eceff4"], #nord6
          ["#8fbcbb", "#8fbcbb"], #nord7
          ["#88c0d0", "#88c0d0"], #nord8
          ["#81a1c1", "#81a1c1"], #nord9
          ["#5e81ac", "#5e81ac"], #nord10
          ["#bf616a", "#bf616a"], #nord11
          ["#d08770", "#d08770"], #nord12
          ["#ebcb8b", "#ebcb8b"], #nord13
          ["#a3be8c", "#a3be8c"], #nord14
          ["#b48ead", "#b48ead"]] #nord15



widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [

               widget.GroupBox(font="Ubuntu Mono",
                        fontsize = 14,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        active = colors[6],
                        inactive = colors[6],
                        rounded = False,
                        highlight_color = colors[3],
                        highlight_method = "block",
                        this_current_screen_border = colors[3],
                        this_screen_border = colors [0],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[6],
                        background = colors[0]
                        ),
				
               widget.Sep(
                        linewidth = 0,
                        padding = 15,
				   		background = colors[0]
                        ),
				
               widget.WindowName(
                        foreground = colors[14],
                        background = colors[0],
                        padding = 0
                        ),
				
               widget.CurrentLayout(
                        foreground = colors[0],
                        background = colors[10],
                        padding = 5
                        ),
			   widget.Battery(
                        foreground = colors[0],
                        background = colors[8],
                        padding = 5
                        ),
               widget.CPU(
                        format='CPU {freq_current}GHz {load_percent}%',
                        update_interval=1.0,
                        foreground=colors[0],
                        background=colors[7],
                        padding = 5
                        ),
                       
               widget.TextBox(
                        text=" 🌡",
                        padding = 2,
                        foreground=colors[0],
                        background=colors[10],
                        fontsize=11
                        ),
				
               widget.ThermalSensor(
                        foreground=colors[0],
                        background=colors[10],
                        padding = 5,
                        tag_sensor = "tdie"
                        ),

               widget.TextBox(
                        text=" 🖬",
                        foreground=colors[0],
                        background=colors[8],
                        padding = 0,
                        fontsize=14
                        ),
               widget.Memory(
                        foreground = colors[0],
                        background = colors[8],
                        padding = 5
                        ),

               widget.Net(
                        interface = "enp34s0",
                        format = '{down} ↓↑ {up}',
                        foreground = colors[0],
                        background = colors[9],
                        padding = 5
                        ),

               widget.TextBox(
                       text=" Vol:",
                        foreground=colors[0],
                        background=colors[7],
                        padding = 0
                        ),
               widget.Volume(
                        foreground = colors[0],
                        background = colors[7],
                        padding = 5
                        ),


               widget.Clock(
                        foreground = colors[0],
                        background = colors[8],
                        format="%A, %B %d  [ %I:%M %p ]"
                        ),

            ],
            24,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
