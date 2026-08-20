# Arch Linux WebTTY

A faithful, in-browser recreation of an Arch Linux console — boot to shell — in a
single self-contained `index.html`. Full-black TTY, white text, no build step, no
dependencies. Open the file (or serve it) and it boots.

![Arch Linux WebTTY](https://img.shields.io/badge/Arch-WebTTY-1793D1)

## What makes it real

- **Real fastfetch logo.** The ASCII art is pulled verbatim from fastfetch's own
  source (`src/logo/ascii/a/arch.txt`), including its `$1`/`$2` color slots, both of
  which map to `FF_COLOR_FG_CYAN` in the builtin table — so it renders in the exact
  iconic Arch cyan (`#1793d1`), not a lookalike.
- **Real boot screen.** Dim kernel timestamp lines (`loglevel=3 quiet`) followed by
  systemd unit startup with green `[  OK  ]` tags, then a `archlinux login:` prompt
  that logs you in and drops to a shell.
- **Real commands.** A working shell with a virtual filesystem: `fastfetch`,
  `pacman` (`-Syu`, `-S`, `-Q`, `-Ss`, `-Si`, `-Qi`, animated progress bars),
  `ls`/`cd`/`cat`/`mkdir`/`touch`/`rm`/`mv`/`cp`/`tree`/`find`, `uname`, `free`,
  `df`, `lsblk`, `lscpu`, `systemctl`, `nano`/`vim`, and more. Tab completion,
  command history (↑/↓), and the usual `Ctrl+C/L/U/A/E/W` line editing all work.
- **Open real HTML files.** `~/pages/` ships real HTML pages; `open` / `xdg-open` /
  `firefox` renders them in a browser-style window straight from the filesystem.
  Write your own with `nano hello.html`, save with `^O`, then `open hello.html`.

## Try it

```
help                     # list every command
fastfetch                # the real logo + system info
pacman -Syu              # full system upgrade (animated)
open ~/pages/welcome.html
nano notes.html          # write a file, ^O to save, ^X to exit
open notes.html          # …then open the file you just wrote
```

Press any key (or tap) to skip the boot sequence.

## Design

Committed single-visual-world: a pure-black console rendered in `JetBrains Mono`.
Colors are painted explicitly (no theme toggle by design) and honor
`prefers-reduced-motion` — the boot log and progress bars render instantly for
readers who ask for reduced motion.
