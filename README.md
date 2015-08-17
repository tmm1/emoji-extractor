## emoji-extractor

This is a small ruby script that extracts the Apple Color Emoji PNG Symbols from their corresponding system font located at `/System/Library/Fonts/Apple Color Emoji.ttf`. The extracted assets will be placed in a subfolder for each resolution in a subfolder called "image" in the containing folder. File system structure as follows:
```
.
├── README.md
├── emoji_extractor.rb
└── images
    ├── 160x160
    ├── 20x20
    ├── 21x21
    ├── 32x32
    ├── 40x40
    ├── 48x48
    ├── 64x64
    └── 96x96
```
It was updated to work with current versions of ruby and include assets for the new emojis as introduced in OS X 10.10.3 / iOS 8.3 (defined in Unicode standard 7.0).

### usage

Just run the ruby script, no arguments need to be passed. It will check for the Apple Color Emoji.ttf at it's default location, so you should make shure that it exists.
```
$ file /System/Library/Fonts/Apple\ Color\ Emoji.ttf
/System/Library/Fonts/Apple Color Emoji.ttf: TrueType font data

$ ruby emoji_extractor.rb

$ ls images
20x20  32x32  40x40  48x48  64x64  96x96  160x160

$ file images/160x160/1.png
images/160x160/1.png: PNG image data, 160 x 160, 8-bit/color RGBA, non-interlaced
```
