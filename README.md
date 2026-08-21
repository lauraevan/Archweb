# Arch Linux WebTTY

A faithful, in-browser recreation of an Arch Linux console — boot to shell to a full
desktop shell. Full-black TTY, white text. Open `index.html` (or serve the folder) and
it boots. Your changes persist across reloads (localStorage).

![Arch Linux WebTTY](https://img.shields.io/badge/Arch-WebTTY-1793D1)

## Project layout

A real multi-file web project — HTML, CSS, JavaScript and Python:

```
index.html        the TTY, boot, shell, editor, Noctalia session   (HTML + JS + inline CSS)
games.css         flat catalog stylesheet                          (CSS)
games-data.js     window.GAME_DATA    — 6082 games with cover art  (generated JS)
games-noicon.js   window.NOICON_GAMES — 407 UGS name-tile games    (generated JS)
tools/build_games.py   generates the two catalog files from tools/sources/  (Python)
tools/serve.py         static dev server that mirrors production           (Python)
```

Regenerate the catalog data and serve it locally:

```sh
python3 tools/build_games.py     # -> games-data.js, games-noicon.js
python3 tools/serve.py           # -> http://localhost:8000/
```

## Deploy (githack)

The site is plain static files, so any static host works. To serve it straight from
this repo with correct content-types, open the file through **githack**:

```
https://raw.githack.com/lauraevan/archweb/<branch>/index.html
```

The catalog's `games-data.js` / `games-noicon.js` load relatively, and cover art loads
from the games repository, so the full catalog renders on the deployed URL. (A single
self-contained preview that can't fetch those files falls back to a small sample.)

## What makes it real

- **Real fastfetch logo.** The ASCII art is pulled verbatim from fastfetch's own
  source (`src/logo/ascii/a/arch.txt`), including its `$1`/`$2` color slots, both of
  which map to `FF_COLOR_FG_CYAN` in the builtin table — so it renders in the exact
  iconic Arch cyan (`#1793d1`), not a lookalike.
- **Real boot screen.** Dim kernel timestamp lines (`loglevel=3 quiet`) followed by
  systemd unit startup with green `[  OK  ]` tags, then an `archlinux login:` prompt
  that logs you in and drops to a shell.
- **A real shell.** A virtual filesystem plus a command line with variable/command
  expansion (`$VAR`, `$(...)`), pipes `|`, redirects `> >>`, and `;` `&&` `||`
  chaining. Commands: `fastfetch`, `pacman`, `ls/cd/cat/mkdir/rm/mv/cp/tree/find`,
  `grep/wc/sort/head/tail`, `uname/free/df/lsblk/lscpu`, `nano/vim`, and more, with
  tab-completion, history, and `Ctrl+C/L/U/A/E/W` editing.

## Compile and run real code

- **C — an authentic gcc pipeline.** `gcc file.c -o out` runs cpp → cc1 → as →
  collect2/ld with real diagnostics: `file.c:line:col: error/warning:` with a source
  gutter and caret, `-Wall` implicit-declaration warnings, `undefined reference to
  'main'` link errors, `-c` to emit `.o` objects, linking objects, and `-v` verbose
  stage output. Success is silent, like the real thing. `./out` runs the program
  (main, functions, `int/char/float/double`, arrays, arithmetic, `if/for/while`,
  `printf/puts/putchar`).
- **make:** parses a real `Makefile` (variables, targets, recipes) or falls back to
  the implicit rule.
- **JavaScript:** `node file.js` / `node -e "…"` executes real JS in the page engine.
- **Bash:** `bash script.sh` runs a working interpreter (variables, `$()`, `if`,
  `for`, `while`, pipes, redirects) — inline or multi-line.
- **git:** `git init/clone/add/commit/status/log/branch/checkout/config` operate on a
  genuine in-tree commit model.
- **coreutils:** `printf seq cut chmod du ps basename dirname alias type cd -` and the
  usual `ls/grep/wc/sort/head/tail/…`, with `|` pipes, `>`/`>>` redirects, and
  `&&`/`||`/`;` chaining.

```
echo 'int main(){ for(int i=0;i<3;i++) printf("hi %d\n", i); }' > hi.c
gcc hi.c -o hi && ./hi
```

## Install & launch Noctalia

```
sudo pacman -S noctalia-shell     # AUR/makepkg build: deps → git clone → meson/ninja → install
noctalia                          # launch the desktop shell
```

Noctalia is a **native Wayland/OpenGL-ES** desktop shell — it cannot execute inside a
browser. So this uses the **real** [`noctalia-dev/noctalia-shell`](https://github.com/noctalia-dev/noctalia-shell)
repository (v5.0.0, MIT): the install bundles the project's actual files
(`README`, `LICENSE`, `example.toml`, `meson.build`, `builtin_palettes.cpp`, the real
`noctalia.svg` logo) into `~/.cache/aur/noctalia-shell/noctalia/`, and the launched
session reproduces Noctalia's UI from its **own source of truth**:

- the exact dark palette from `src/theme/builtin_palettes.cpp`
  (`primary #fff59b`, `surface #070722`, `secondary #a9aefe`, `tertiary #9BFECE`,
  `error #FD4663`, `onSurface #f3edf7`, …),
- the real bar layout from `example.toml` (`start: launcher/wallpaper/workspaces` ·
  `center: clock` · `end: media/tray/notifications/clipboard/network/bluetooth/volume/
  brightness/battery/control-center/session`),
- the real `noctalia.svg` logo.

The session is interactive: launcher (app search + `/calc`), control center (toggles +
volume/brightness sliders), workspaces, a lock screen, and a session menu. **Session →
Log Out** returns you to the terminal.

## Open real HTML files

`~/pages/` ships real HTML pages; `open` / `xdg-open` / `firefox` renders them (and
`.svg`) in a browser-style window straight from the filesystem. Write your own with
`nano hello.html`, save with `^O`, then `open hello.html`.

## Design & persistence

Committed single-visual-world: a pure-black console in `JetBrains Mono`, colors painted
explicitly, `prefers-reduced-motion` honored. The filesystem, installed packages, git
repos, and history are saved to `localStorage`, so a reload — or `reboot` — keeps your
session. `reset-fs` wipes it back to defaults.

## Credits

Noctalia assets and palette © noctalia-dev, used under the MIT License. Arch logo ASCII
from the fastfetch project.
