## emoji-extractor

extracts high-resolution emoji pngs from `/System/Library/Fonts/Apple Color Emoji.ttf`

### usage

```
$ file /System/Library/Fonts/Apple\ Color\ Emoji.ttf
/System/Library/Fonts/Apple Color Emoji.ttf: TrueType font data

$ ruby emoji_extractor.rb

$ file images/160x160/1.png
images/160x160/1.png: PNG image data, 160 x 160, 8-bit/color RGBA, non-interlaced
```
