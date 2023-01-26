## emoji-extractor

extracts high-resolution emoji pngs from `/System/Library/Fonts/Apple Color Emoji.ttf` (OS X 10.11) or `/System/Library/Fonts/Apple Color Emoji.ttc` (macOS 10.12).
Also tested for [AppleColorEmoji-160px.ttc (for iOS 14+)](https://github.com/PoomSmart/EmojiLibrary)

### usage
#### Ruby

```
$ ruby emoji_extractor.rb

$ ls images
20x20  32x32  40x40  48x48  64x64  96x96  160x160

$ file images/160x160/1.png
images/160x160/1.png: PNG image data, 160 x 160, 8-bit/color RGBA, non-interlaced
```
#### Python3

```
$ python emoji_extractor.py

$ ls images
40x40  64x64  96x96  160x160

$ file images/160x160/1.png
images/160x160/1.png: PNG image data, 160 x 160, 8-bit/color RGBA, non-interlaced
```
