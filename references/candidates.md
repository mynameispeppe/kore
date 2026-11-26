# Candidates

Alternative values for `canvas` and the fonts, the two starting choices of a project, and ready palettes for a user who has none. Every other color is derived (see Custom palette) or chosen by the user (`accent`). `references/tokens.yaml` holds the active values; every alternative we evaluate is added to its list.

## canvas — light

| Name | Hex | |
|---|---|---|
| Ice | `#F8FAFB` | active |
| Ghost White | `#F8F8FF` |  |
| Snow Drift | `#F8FBF8` |  |
| Vista White | `#FDFCFA` |  |
| White Smoke | `#F5F5F5` |  |
| Vivid White | `#F8F8F4` |  |

## canvas — dark

| Name | Hex | |
|---|---|---|
| Night | `#0C090A` | active |
| Crow | `#0D0907` |  |
| Spider | `#040200` |  |
| Sable | `#060606` |  |
| True Black | `#0A0B0B` |  |

## Palettes

Theme is the theme the colors are given for. `gradient` is glassmorphism's Page background in that theme.

| Id | Name | Theme | `canvas` | `primary` | `accent` | `ink` | `gradient` |
|---|---|---|---|---|---|---|---|
| 1 | Sage and Lemon | light | `#F0FFF7` | `#017E44` | `#E7C104` | `#01321B` | `linear-gradient(to right top, #7efec2, #95f99a, #b4f170, #d7e645, #fcd615)` |
| 1 | Sage and Lemon | dark | `#000F07` | `#7EFEC2` | `#FCD615` | `#CDFEE7` | `linear-gradient(to right top, #017e44, #469339, #78a529, #adb514, #e7c104)` |
| 3 | Cobalt and Saffron | light | `#EAECF6` | `#2C3C68` | `#ADAB48` | `#0B0C19` | `linear-gradient(to right top, #97a7d3, #59b5d8, #35beb9, #70bf83, #b7b554)` |
| 3 | Cobalt and Saffron | dark | `#0A0C17` | `#97A7D3` | `#B7B554` | `#E5E7F4` | `linear-gradient(to right top, #2c3c68, #784472, #af5360, #c27a46, #adab48)` |
| 4 | Lagoon and Flame | light | `#ECF9F4` | `#266D55` | `#B95741` | `#0C2219` | `linear-gradient(to right top, #92d9c0, #97c18b, #a7a45d, #b78243, #be5c46)` |
| 4 | Lagoon and Flame | dark | `#06120E` | `#92D9C0` | `#BE5C46` | `#DEF3EB` | `linear-gradient(to right top, #266d55, #4a703c, #706d27, #976527, #b95741)` |
| 5 | Graphite and Cobalt | light | `#F6F9F7` | `#33523C` | `#5B6B95` | `#09100B` | `linear-gradient(to right top, #adccb6, #89bbb4, #6da9b4, #6393b1, #6b7ba4)` |
| 5 | Graphite and Cobalt | dark | `#050806` | `#ADCCB6` | `#6B7BA4` | `#EEF5F0` | `linear-gradient(to right top, #33523c, #225c55, #186470, #316988, #5b6b95)` |
| 6 | Cedar and Magenta | light | `#FBFCE9` | `#646E12` | `#DD22BE` | `#161604` | `linear-gradient(to right top, #e4ed90, #febf60, #ff875e, #ff4684, #dc23bd)` |
| 6 | Cedar and Magenta | dark | `#151603` | `#E4ED90` | `#DC23BD` | `#FBFBE7` | `linear-gradient(to right top, #646e12, #976200, #c94626, #e90867, #dd22be)` |
| 7 | Terracotta and Sun | light | `#FAEEEB` | `#77381D` | `#A8A829` | `#150905` | `linear-gradient(to right top, #e2a287, #ebab79, #ecb76b, #e5c55f, #d6d558)` |
| 7 | Terracotta and Sun | dark | `#130805` | `#E2A287` | `#D6D558` | `#FAEEEA` | `linear-gradient(to right top, #77381d, #8c501c, #9b6c1b, #a5891d, #a8a829)` |
| 8 | Emerald and Cherry Red | light | `#EEF7EF` | `#2E6035` | `#A95163` | `#081109` | `linear-gradient(to right top, #9fd1a6, #adb479, #b9945f, #bb735c, #ad5668)` |
| 8 | Emerald and Cherry Red | dark | `#09130A` | `#9FD1A6` | `#AD5668` | `#ECF6ED` | `linear-gradient(to right top, #2e6035, #586024, #7d5b26, #9a543e, #a95163)` |
| 9 | Orchid and Sunset | light | `#FFF0FB` | `#90046F` | `#E45C07` | `#2D0121` | `linear-gradient(to right top, #fb6fdb, #ff5baf, #ff5480, #ff5d50, #f86f1b)` |
| 9 | Orchid and Sunset | dark | `#0D000A` | `#FB6FDB` | `#F86F1B` | `#FED4F3` | `linear-gradient(to right top, #90046f, #b40060, #cf0c4c, #df3732, #e45c07)` |
| 10 | Midnight Blue and Hot Pink | light | `#E9E7F4` | `#3C2F65` | `#92455D` | `#120F1F` | `linear-gradient(to right top, #a79bd0, #b08fc1, #b783af, #ba789b, #ba6e86)` |
| 10 | Midnight Blue and Hot Pink | dark | `#0F0C1A` | `#A79BD0` | `#BA6E86` | `#E3E0F0` | `linear-gradient(to right top, #3c2f65, #573266, #6e3664, #823c61, #92455d)` |
| 11 | Ice and Ultramarine | light | `#F6FBFD` | `#1B536F` | `#4E32CD` | `#07141D` | `linear-gradient(to right top, #8ec7e4, #49abe9, #008aeb, #0065e4, #4e32cd)` |
| 11 | Ice and Ultramarine | dark | `#02070A` | `#8EC7E4` | `#4E32CD` | `#E1EFF8` | `linear-gradient(to right top, #1b536f, #00548e, #0052ac, #0049c2, #4e32cd)` |
| 13 | Sky and Electric | light | `#F8FBFC` | `#2F596A` | `#3B92B5` | `#0D1416` | `linear-gradient(to right top, #95c0d1, #84b9ce, #73b2cb, #60aac8, #4ba3c5)` |
| 13 | Sky and Electric | dark | `#040708` | `#95C0D1` | `#4BA3C5` | `#E7EEF1` | `linear-gradient(to right top, #2f596a, #32677c, #36758e, #3883a1, #3b92b5)` |
| 14 | Amethyst and Violet | light | `#F8F6F9` | `#56355F` | `#9D3DB8` | `#0D0C0E` | `linear-gradient(to right top, #c1a0ca, #bb8bc8, #b576c6, #ae60c4, #a747c1)` |
| 14 | Amethyst and Violet | dark | `#09070A` | `#C1A0CA` | `#A747C1` | `#F1F0F2` | `linear-gradient(to right top, #56355f, #673874, #793b8a, #8b3ca1, #9d3db8)` |
| 15 | Amber and Glacier | light | `#FEF9F6` | `#852D0A` | `#10ABD5` | `#2B0D03` | `linear-gradient(to right top, #f59d7a, #fd95b1, #d7a2e7, #8ab7ff, #2bc6ef)` |
| 15 | Amber and Glacier | dark | `#0B0501` | `#F59D7A` | `#2BC6EF` | `#FCDED4` | `linear-gradient(to right top, #852d0a, #a5345a, #975da3, #5e88d0, #10abd5)` |
| 16 | Peony and Lemon | light | `#FDF2F5` | `#800F36` | `#C7CD18` | `#1C030A` | `linear-gradient(to right top, #f07da5, #ff8787, #ff9f62, #ffc23d, #e2e732)` |
| 16 | Peony and Lemon | dark | `#0F0206` | `#F07DA5` | `#E2E732` | `#FCE2E9` | `linear-gradient(to right top, #800f36, #aa372f, #c6651e, #d19800, #c7cd18)` |
| 17 | Mint and Orchid | light | `#F3FCFA` | `#1C6952` | `#C133BF` | `#061812` | `linear-gradient(to right top, #95e3cc, #00d1e5, #00b6ff, #608bff, #cb3ec9)` |
| 17 | Mint and Orchid | dark | `#030C0A` | `#95E3CC` | `#CB3EC9` | `#E7F9F3` | `linear-gradient(to right top, #1c6952, #007383, #0077bf, #1b69df, #c133bf)` |
| 20 | Fog and Pumpkin | light | `#F7F7F8` | `#494252` | `#7B6B60` | `#161419` | `linear-gradient(to right top, #b4acbd, #b5a3ae, #b29b9f, #aa9490, #9e8f84)` |
| 20 | Fog and Pumpkin | dark | `#060607` | `#B4ACBD` | `#9E8F84` | `#E7E5EA` | `linear-gradient(to right top, #494252, #5b4a56, #6a5358, #745e5b, #7b6b60)` |
| 21 | Fuchsia and Orange | light | `#F6EFF4` | `#512F49` | `#987D57` | `#160D15` | `linear-gradient(to right top, #d0aec8, #d2a1af, #cc9794, #bd907b, #a78c67)` |
| 21 | Fuchsia and Orange | dark | `#110A0F` | `#D0AEC8` | `#A78C67` | `#F1E7EF` | `linear-gradient(to right top, #512f49, #6c3d4c, #824f4c, #90654f, #987d57)` |
| 22 | Lavender and Acid Lime | light | `#FCF5FF` | `#590381` | `#73EF06` | `#1A0123` | `linear-gradient(to right top, #d57efc, #ff60b3, #ff834f, #ffc500, #7cf90e)` |
| 22 | Lavender and Acid Lime | dark | `#08000B` | `#D57EFC` | `#7CF90E` | `#F6DEFE` | `linear-gradient(to right top, #590381, #c4005d, #ed4015, #d6a200, #73ef06)` |
| 23 | Slate and Fuchsia | light | `#D9E4FC` | `#0B337A` | `#AF12C4` | `#030F26` | `linear-gradient(to right top, #83adf4, #839dff, #9688ff, #b56bff, #d83aed)` |
| 23 | Slate and Fuchsia | dark | `#030D24` | `#83ADF4` | `#D83AED` | `#DAE6FC` | `linear-gradient(to right top, #0b337a, #333793, #5937a9, #832fb9, #af12c4)` |
| 24 | Ruby and Sprout | light | `#FEF0EC` | `#85210A` | `#84EA10` | `#220802` | `linear-gradient(to right top, #f58f79, #fe9e56, #f2b62b, #cdd200, #89ee14)` |
| 24 | Ruby and Sprout | dark | `#110501` | `#F58F79` | `#89EE14` | `#FDE5DF` | `linear-gradient(to right top, #85210a, #a24f00, #af8100, #a8b500, #84ea10)` |
| 25 | Copper and Electric Blue | light | `#FEF9F6` | `#863A0E` | `#1319B9` | `#200E04` | `linear-gradient(to right top, #f1a579, #fa7977, #f14b91, #c634be, #454aec)` |
| 25 | Copper and Electric Blue | dark | `#0A0401` | `#F1A579` | `#454AEC` | `#FBE8DD` | `linear-gradient(to right top, #863a0e, #9a0124, #a1004b, #8b0080, #1319b9)` |
| 26 | Cobalt and Sunflower | light | `#D7E0FE` | `#05248A` | `#DFB007` | `#01071E` | `linear-gradient(to right top, #7494fa, #e781e3, #ff78a5, #ff985c, #f8ca22)` |
| 26 | Cobalt and Sunflower | dark | `#010926` | `#7494FA` | `#F8CA22` | `#E2E8FE` | `linear-gradient(to right top, #05248a, #97007d, #d81e59, #ee6b2d, #dfb007)` |
| 28 | Ocean and Sky | light | `#ECF0F3` | `#344C60` | `#47769E` | `#12171C` | `linear-gradient(to right top, #9fb7cb, #8fadc6, #80a3c1, #7099bd, #608fb8)` |
| 28 | Ocean and Sky | dark | `#0B0F12` | `#9FB7CB` | `#608FB8` | `#E2E7EC` | `linear-gradient(to right top, #344c60, #39566f, #3d617e, #426b8e, #47769e)` |
| 29 | Garnet and Cobalt | light | `#FBF5F4` | `#652925` | `#4268B3` | `#160A08` | `linear-gradient(to right top, #da9f9b, #d08b9f, #b97caa, #9174b6, #4b71bc)` |
| 29 | Garnet and Cobalt | dark | `#0C0504` | `#DA9F9B` | `#4B71BC` | `#F7EBE9` | `linear-gradient(to right top, #652925, #772d44, #7d3b6a, #6f5092, #4268b3)` |
| 30 | Sunflower and Ultramarine | light | `#F9F9E6` | `#74711A` | `#2630A6` | `#252508` | `linear-gradient(to right top, #e5e28b, #ffaf6e, #ff7983, #d75ab3, #5762d9)` |
| 30 | Sunflower and Ultramarine | dark | `#1B1A06` | `#E5E28B` | `#5762D9` | `#F6F6D8` | `linear-gradient(to right top, #74711a, #97500e, #aa1a37, #960070, #2630a6)` |
| 31 | Midnight Blue and Flame | light | `#DFDAFB` | `#1A0E77` | `#E01A3E` | `#090529` | `linear-gradient(to right top, #9286f1, #bf6ad5, #de49ab, #eb2878, #e51d41)` |
| 31 | Midnight Blue and Flame | dark | `#080424` | `#9286F1` | `#E51D41` | `#DAD6FA` | `linear-gradient(to right top, #1a0e77, #6b0075, #9f0069, #c60055, #e01a3e)` |
| 33 | Poppy and Sun | light | `#FFECEB` | `#810C03` | `#C4D605` | `#2D0101` | `linear-gradient(to right top, #fc877e, #ff9b67, #ffb64b, #ffd72f, #e7fa28)` |
| 33 | Poppy and Sun | dark | `#160200` | `#FC877E` | `#E7FA28` | `#FED1D1` | `linear-gradient(to right top, #810c03, #a14200, #b87200, #c4a300, #c4d605)` |
| 35 | Sapphire and Neon Green | light | `#EBE5FF` | `#130080` | `#00D154` | `#05001F` | `linear-gradient(to right top, #9380ff, #00b2ff, #00d6ff, #00f0db, #30ff84)` |
| 35 | Sapphire and Neon Green | dark | `#050018` | `#9380FF` | `#30FF84` | `#E6E1FF` | `linear-gradient(to right top, #130080, #0050c4, #0081c9, #00ac98, #00d154)` |
| 36 | Cherry and Fire Red | light | `#F7F3F3` | `#5E3331` | `#AF3631` | `#0E0B0B` | `linear-gradient(to right top, #cfa3a1, #d1908d, #d17d79, #d06964, #cd5450)` |
| 36 | Cherry and Fire Red | dark | `#0B0707` | `#CFA3A1` | `#CD5450` | `#F3F0F0` | `linear-gradient(to right top, #5e3331, #723532, #873632, #9b3632, #af3631)` |
| 38 | Mauve and Scarlet | light | `#FCDEF0` | `#800A4F` | `#D43511` | `#1D0212` | `linear-gradient(to right top, #f57dc4, #ff6aa4, #ff597f, #fc5057, #ee502c)` |
| 38 | Mauve and Scarlet | dark | `#220315` | `#F57DC4` | `#EE502C` | `#FDE0F2` | `linear-gradient(to right top, #800a4f, #9b0049, #b4003e, #c7182d, #d43511)` |
| 39 | Slate and Electric Blue | light | `#F5F7FA` | `#273C68` | `#1D56C9` | `#121317` | `linear-gradient(to right top, #99add8, #829edc, #6b8fdf, #5380e2, #3770e3)` |
| 39 | Slate and Electric Blue | dark | `#06080B` | `#99ADD8` | `#3770E3` | `#E9EAEE` | `linear-gradient(to right top, #273c68, #244380, #1f4a98, #1c50b0, #1d56c9)` |
| 41 | Old Rose and Glacial Mint | light | `#F7DFE8` | `#761E3B` | `#31BCBF` | `#18060B` | `linear-gradient(to right top, #e088a5, #c597d4, #8dadef, #49bfec, #40cacd)` |
| 41 | Old Rose and Glacial Mint | dark | `#1F0811` | `#E088A5` | `#40CACD` | `#F9E7EC` | `linear-gradient(to right top, #761e3b, #7a457e, #5572b2, #009ac7, #31bcbf)` |
| 42 | Ash and Pistachio | light | `#F7F5F3` | `#544936` | `#748C5A` | `#100D0A` | `linear-gradient(to right top, #c9beaa, #bfb799, #b1b08a, #a1aa7d, #8da572)` |
| 42 | Ash and Pistachio | dark | `#0B0907` | `#C9BEAA` | `#8DA572` | `#F5F2EF` | `linear-gradient(to right top, #544936, #60583c, #6a6844, #707a4e, #748c5a)` |
| 44 | Basil and Glacier | light | `#F4FAF8` | `#30694D` | `#488C9D` | `#0A150F` | `linear-gradient(to right top, #97cfb4, #85c6b6, #75bcb8, #6ab2b8, #64a7b7)` |
| 44 | Basil and Glacier | dark | `#050B09` | `#97CFB4` | `#64A7B7` | `#EAF5EF` | `linear-gradient(to right top, #30694d, #2b7362, #2c7c78, #36848b, #488c9d)` |
| 45 | Burnt Orange and Lemon | light | `#FFF8F5` | `#822703` | `#F0D105` | `#1E0901` | `linear-gradient(to right top, #fca07b, #ffaa68, #ffb752, #ffc738, #fada11)` |
| 45 | Burnt Orange and Lemon | dark | `#0B0300` | `#FCA07B` | `#FADA11` | `#FEEAE3` | `linear-gradient(to right top, #822703, #a54e00, #c47700, #dea300, #f0d105)` |
| 46 | Cobalt | light | `#F4F3F7` | `#373258` | `#493C90` | `#131217` | `linear-gradient(to right top, #aea8ce, #a199cc, #958bc9, #887cc6, #7b6ec3)` |
| 46 | Cobalt | dark | `#09080C` | `#AEA8CE` | `#7B6EC3` | `#EAE9EE` | `linear-gradient(to right top, #373258, #3b3566, #403774, #443a82, #493c90)` |
| 47 | Stone and Emerald | light | `#F2EEED` | `#4C3C38` | `#66815F` | `#1A1514` | `linear-gradient(to right top, #c6b6b2, #c0aea0, #b4a88f, #a0a383, #85a07e)` |
| 47 | Stone and Emerald | dark | `#120E0D` | `#C6B6B2` | `#85A07E` | `#ECE7E6` | `linear-gradient(to right top, #4c3c38, #5c4a3d, #665b43, #696d4d, #66815f)` |
| 48 | Sage and Ultramarine | light | `#E8FDF1` | `#0A753A` | `#124DD9` | `#032611` | `linear-gradient(to right top, #88f5b9, #00dcd3, #00bdf6, #0097ff, #2762ed)` |
| 48 | Sage and Ultramarine | dark | `#02160B` | `#88F5B9` | `#2762ED` | `#DBFCE8` | `linear-gradient(to right top, #0a753a, #00786b, #0076aa, #006cd9, #124dd9)` |
| 49 | Emerald and Lake | light | `#F5FCF2` | `#307218` | `#25A796` | `#0C1D06` | `linear-gradient(to right top, #a6e78f, #8ee59f, #78e2ae, #65dfbc, #57dac9)` |
| 49 | Emerald and Lake | dark | `#060E03` | `#A6E78F` | `#57DAC9` | `#E9F9E3` | `linear-gradient(to right top, #307218, #25803c, #198e5c, #159b7a, #25a796)` |
| 52 | Dove and Acid Lime | light | `#F1F0F4` | `#3D3649` | `#7A7F5C` | `#110F15` | `linear-gradient(to right top, #bbb4c8, #c7a9b7, #c9a39e, #bba188, #9ea380)` |
| 52 | Dove and Acid Lime | dark | `#0C0B0F` | `#BBB4C8` | `#9EA380` | `#EBE9EF` | `linear-gradient(to right top, #3d3649, #5d414e, #74514d, #7e664e, #7a7f5c)` |
| 53 | Forest and Electric Blue | light | `#EDFEE7` | `#298109` | `#0D13C9` | `#0A2202` | `linear-gradient(to right top, #9df67d, #00deb1, #00bbfc, #008dff, #353bf2)` |
| 53 | Forest and Electric Blue | dark | `#071601` | `#9DF67D` | `#353BF2` | `#E4FDDC` | `linear-gradient(to right top, #298109, #007c59, #0070af, #005ce7, #0d13c9)` |
| 54 | Meadow and Fresh Grass | light | `#E8F7E8` | `#1D7D1C` | `#08F604` | `#101E10` | `linear-gradient(to right top, #84e482, #73ea6f, #5ef059, #44f63e, #0cfb07)` |
| 54 | Meadow and Fresh Grass | dark | `#081708` | `#84E482` | `#0CFB07` | `#E2F0E2` | `linear-gradient(to right top, #1d7d1c, #1c9a1c, #19b81a, #13d614, #08f604)` |
| 56 | Basil and Sky | light | `#E4F9E1` | `#216C13` | `#1F77B2` | `#071604` | `linear-gradient(to right top, #9fec92, #4ee1b5, #00d1d4, #00bde4, #4da5e0)` |
| 56 | Basil and Sky | dark | `#092006` | `#9FEC92` | `#4DA5E0` | `#EBFBE8` | `linear-gradient(to right top, #216c13, #00754e, #007a81, #007ba4, #1f77b2)` |
| 57 | Aquamarine and Cobalt | light | `#EBFAFA` | `#1E7B7B` | `#2D46B4` | `#092525` | `linear-gradient(to right top, #85e1e1, #34c8e4, #00abe9, #008be6, #4a64d2)` |
| 57 | Aquamarine and Cobalt | dark | `#051414` | `#85E1E1` | `#4A64D2` | `#DAF6F6` | `linear-gradient(to right top, #1e7b7b, #00758f, #006ca7, #005eb6, #2d46b4)` |
| 58 | Terracotta and Orange | light | `#F1E8E4` | `#6A3A25` | `#CC531E` | `#1B1513` | `linear-gradient(to right top, #d9a994, #dd997b, #e08963, #e1794b, #e16732)` |
| 58 | Terracotta and Orange | dark | `#1B120E` | `#D9A994` | `#E16732` | `#ECE6E3` | `linear-gradient(to right top, #6a3a25, #824124, #9a4723, #b34d21, #cc531e)` |
| 59 | Lagoon and Sea | light | `#F6F9F9` | `#2A5B5A` | `#29BCBA` | `#121616` | `linear-gradient(to right top, #a5d6d5, #92d6d5, #7dd6d4, #65d6d4, #44d6d3)` |
| 59 | Lagoon and Sea | dark | `#050808` | `#A5D6D5` | `#44D6D3` | `#E8ECEC` | `linear-gradient(to right top, #2a5b5a, #2d7271, #2e8a88, #2da3a1, #29bcba)` |
| 60 | Sapphire and Magenta | light | `#ECEAFA` | `#271B6F` | `#C8328C` | `#0C0925` | `linear-gradient(to right top, #9e91e4, #ac7fd7, #b96ac5, #c553ad, #cd3892)` |
| 60 | Sapphire and Magenta | dark | `#070515` | `#9E91E4` | `#CD3892` | `#DDDAF6` | `linear-gradient(to right top, #271b6f, #551f7b, #7e2384, #a4298a, #c8328c)` |
| 62 | Mint and Ultramarine | light | `#EFFBF9` | `#207466` | `#3268BD` | `#09201A` | `linear-gradient(to right top, #89dfd1, #4bc9d5, #00b1da, #0095d9, #4076cc)` |
| 62 | Mint and Ultramarine | dark | `#040F0D` | `#89DFD1` | `#4076CC` | `#DEF6F0` | `linear-gradient(to right top, #207466, #00767f, #00769b, #0072b3, #3268bd)` |
| 64 | Plum and Glacial Mint | light | `#FDEDFC` | `#6F115E` | `#1CBAB0` | `#280621` | `linear-gradient(to right top, #ee8fdd, #b2adff, #57c7ff, #00d9ff, #45e3d8)` |
| 64 | Plum and Glacial Mint | dark | `#10020F` | `#EE8FDD` | `#45E3D8` | `#F9D5F2` | `linear-gradient(to right top, #6f115e, #4f4c9b, #0077bc, #009bbf, #1cbab0)` |
| 65 | Graphite and Sunset | light | `#EBEFF0` | `#3B4D4E` | `#8E826B` | `#141A1A` | `linear-gradient(to right top, #afc1c3, #9fb5af, #96a798, #939882, #938770)` |
| 65 | Graphite and Sunset | dark | `#0F1314` | `#AFC1C3` | `#938770` | `#E6ECEC` | `linear-gradient(to right top, #3b4d4e, #485c56, #5a6a5b, #737761, #8e826b)` |
| 67 | Ochre and Lake | light | `#FBF5E9` | `#745616` | `#25C1BE` | `#1F1405` | `linear-gradient(to right top, #e9cc8d, #c7d38d, #a0d89c, #72dbb7, #3cdad8)` |
| 67 | Ochre and Lake | dark | `#171004` | `#E9CC8D` | `#3CDAD8` | `#FAF0E2` | `linear-gradient(to right top, #745616, #6c742c, #5d9054, #43aa86, #25c1be)` |
| 68 | Poppy and Saffron | light | `#FCE9E9` | `#781912` | `#C39C1D` | `#240905` | `linear-gradient(to right top, #ed8e88, #f69476, #f89f62, #f1ac4e, #e2bc3d)` |
| 68 | Poppy and Saffron | dark | `#140303` | `#ED8E88` | `#E2BC3D` | `#FADFDB` | `linear-gradient(to right top, #781912, #913912, #a65910, #b77a12, #c39c1d)` |
| 69 | Indigo and Pumpkin | light | `#F5E5FB` | `#5B127D` | `#C9591D` | `#1A0524` | `linear-gradient(to right top, #ca81ed, #ef6bc2, #fe6091, #f86461, #e27336)` |
| 69 | Indigo and Pumpkin | dark | `#14041A` | `#CA81ED` | `#E27336` | `#EFD9FA` | `linear-gradient(to right top, #5b127d, #91006b, #b30053, #c62f39, #c9591d)` |
| 70 | Fog and Shadow | light | `#EFEBED` | `#493C41` | `#64687D` | `#1C1719` | `linear-gradient(to right top, #c4b7bc, #b7aab3, #a89dab, #9692a3, #83879b)` |
| 70 | Fog and Shadow | dark | `#130F11` | `#C4B7BC` | `#83879B` | `#E9E4E6` | `linear-gradient(to right top, #493c41, #53464f, #5b505e, #615c6e, #64687d)` |
| 75 | Sage and Fuchsia | light | `#F6FEF7` | `#108420` | `#C318AC` | `#05290B` | `linear-gradient(to right top, #7bef8a, #cec730, #ff8e31, #ff4578, #e73ad0)` |
| 75 | Sage and Fuchsia | dark | `#010B02` | `#7BEF8A` | `#E73AD0` | `#D4FADB` | `linear-gradient(to right top, #108420, #7b7300, #bb4e00, #de0050, #c318ac)` |
| 76 | Ash and Smoke | light | `#F9FBFB` | `#3C4849` | `#816A78` | `#151819` | `linear-gradient(to right top, #b6c2c3, #a5b3ba, #9ba2b0, #9790a1, #957e8c)` |
| 76 | Ash and Smoke | dark | `#050707` | `#B6C2C3` | `#957E8C` | `#E6E9EA` | `linear-gradient(to right top, #3c4849, #455259, #545b69, #696374, #816a78)` |
| 77 | Sugared Almond and Sea | light | `#F4EBEE` | `#552B39` | `#4D998C` | `#1B0E12` | `linear-gradient(to right top, #d4aab9, #bcaacc, #92afd4, #69b2c6, #65b1a4)` |
| 77 | Sugared Almond and Sea | dark | `#150B0E` | `#D4AAB9` | `#65B1A4` | `#F1E3E8` | `linear-gradient(to right top, #552b39, #594465, #446288, #2d8094, #4d998c)` |
| 78 | Ruby and Flame | light | `#F9F6F6` | `#502F37` | `#8C4051` | `#0F0B0C` | `linear-gradient(to right top, #cfadb5, #cb9ea9, #c7909c, #c38190, #be7283)` |
| 78 | Ruby and Flame | dark | `#090606` | `#CFADB5` | `#BE7283` | `#F4F0F1` | `linear-gradient(to right top, #502f37, #5f333e, #6d3844, #7d3c4b, #8c4051)` |
| 80 | Aquamarine and Scarlet | light | `#E3F1F2` | `#285B5D` | `#A54557` | `#0D1F21` | `linear-gradient(to right top, #a1d5d7, #85bddc, #939dd3, #b178ac, #b9586a)` |
| 80 | Aquamarine and Scarlet | dark | `#0C1A1B` | `#A1D5D7` | `#B9586A` | `#DFF0F2` | `linear-gradient(to right top, #285b5d, #1d5e7a, #4d5a8a, #854d7e, #a54557)` |
| 84 | Mauve and Pistachio | light | `#FAF5F7` | `#553045` | `#76A05A` | `#10090D` | `linear-gradient(to right top, #d0abc0, #db9fa1, #d29b7b, #b29f5f, #7ba55f)` |
| 84 | Mauve and Pistachio | dark | `#0B0608` | `#D0ABC0` | `#7BA55F` | `#F5EDF1` | `linear-gradient(to right top, #553045, #784043, #8d5b3b, #8c7c3c, #76a05a)` |
| 85 | Raspberry and Lemon | light | `#FBF9F9` | `#5E3B44` | `#908B5A` | `#130C0E` | `linear-gradient(to right top, #c5a2ab, #c99d9a, #c69c88, #ba9d78, #a5a06f)` |
| 85 | Raspberry and Lemon | dark | `#060404` | `#C5A2AB` | `#A5A06F` | `#F3ECEE` | `linear-gradient(to right top, #5e3b44, #744a47, #855d4a, #8e734e, #908b5a)` |
| 86 | Lagoon and Glacial Mint | light | `#F4FBF8` | `#22674C` | `#2BAB78` | `#0D1C16` | `linear-gradient(to right top, #97dcc0, #88dab8, #77d8b1, #66d6a8, #53d4a0)` |
| 86 | Lagoon and Glacial Mint | dark | `#040B08` | `#97DCC0` | `#53D4A0` | `#E4F3ED` | `linear-gradient(to right top, #22674c, #247757, #268862, #29996d, #2bab78)` |
| 87 | Stone and Orchid | light | `#F0F2ED` | `#4A523D` | `#806085` | `#0F120D` | `linear-gradient(to right top, #bac2ac, #beae95, #c0988b, #b68591, #98799d)` |
| 87 | Stone and Orchid | dark | `#10120D` | `#BAC2AC` | `#98799D` | `#EFF2ED` | `linear-gradient(to right top, #4a523d, #62543c, #7a5448, #875663, #806085)` |
| 88 | Pistachio and Acid Lime | light | `#F3F7E4` | `#63721D` | `#AAC520` | `#1B1E0B` | `linear-gradient(to right top, #d4e28d, #d0e17b, #cce167, #c8e053, #c3df3a)` |
| 88 | Pistachio and Acid Lime | dark | `#191D09` | `#D4E28D` | `#C3DF3A` | `#F1F4E0` | `linear-gradient(to right top, #63721d, #74861f, #869b20, #98b020, #aac520)` |
| 89 | Wisteria and Cherry Red | light | `#E9E0FF` | `#280080` | `#CC0000` | `#07001A` | `linear-gradient(to right top, #a77fff, #de5fdb, #ff39a8, #ff1c6e, #ff3231)` |
| 89 | Wisteria and Cherry Red | dark | `#090020` | `#A77FFF` | `#FF3231` | `#EBE3FF` | `linear-gradient(to right top, #280080, #790070, #a70054, #c30032, #cc0000)` |
| 90 | Orchid and Saffron | light | `#FBE4F4` | `#781154` | `#CDCD1D` | `#23051A` | `linear-gradient(to right top, #ee86c9, #ff86a3, #ff9973, #ffbc45, #e2e133)` |
| 90 | Orchid and Saffron | dark | `#1D0415` | `#EE86C9` | `#E2E133` | `#FADDF1` | `linear-gradient(to right top, #781154, #b02a4a, #d45a34, #de9215, #cdcd1d)` |
| 92 | Forest and Fuchsia | light | `#EFF7ED` | `#336228` | `#92409C` | `#10210D` | `linear-gradient(to right top, #a8d79d, #cbb76b, #e98f65, #ea6a8a, #b662bf)` |
| 92 | Forest and Fuchsia | dark | `#0A1308` | `#A8D79D` | `#B662BF` | `#E2F2DF` | `linear-gradient(to right top, #336228, #695904, #96451f, #ad2d57, #92409c)` |
| 93 | Dove and Electric | light | `#EEEFEB` | `#434639` | `#6A7F81` | `#10110E` | `linear-gradient(to right top, #c2c5b8, #afb9ad, #9cada4, #8ca09d, #7d9395)` |
| 93 | Dove and Electric | dark | `#131410` | `#C2C5B8` | `#7D9395` | `#F1F2EF` | `linear-gradient(to right top, #434639, #4a5449, #53635b, #5d716e, #6a7f81)` |
| 94 | Mint and Scarlet | light | `#E7FDFD` | `#097D86` | `#C8210E` | `#021C1D` | `linear-gradient(to right top, #7bedf6, #69daad, #97bd54, #ca9010, #f14a36)` |
| 94 | Mint and Scarlet | dark | `#021818` | `#7BEDF6` | `#F14A36` | `#E1FCFD` | `linear-gradient(to right top, #097d86, #007e5c, #4d7714, #8c6100, #c8210e)` |
| 96 | Indigo and Orange | light | `#F4F2F8` | `#41305A` | `#8C614A` | `#0E0B14` | `linear-gradient(to right top, #b5a4cf, #c499b9, #c990a0, #c48c88, #b68b74)` |
| 96 | Indigo and Orange | dark | `#09070D` | `#B5A4CF` | `#B68B74` | `#EEEBF4` | `linear-gradient(to right top, #41305a, #613557, #783f51, #864f4b, #8c614a)` |
| 97 | Cedar and Sun | light | `#F7F5F2` | `#6E5C2B` | `#D19F15` | `#131210` | `linear-gradient(to right top, #d5c392, #dac17c, #dfbe65, #e5bb4c, #eab82e)` |
| 97 | Cedar and Sun | dark | `#0C0A07` | `#D5C392` | `#EAB82E` | `#EFEEEC` | `linear-gradient(to right top, #6e5c2b, #856c29, #9d7d25, #b78e1f, #d19f15)` |
| 99 | Ice and Bubblegum | light | `#F1FCFE` | `#066B7F` | `#CD0A6B` | `#022127` | `linear-gradient(to right top, #7ee4f9, #5cccff, #8ba9ff, #ce78e4, #f53495)` |
| 99 | Ice and Bubblegum | dark | `#010C0E` | `#7EE4F9` | `#F53495` | `#DAF8FD` | `linear-gradient(to right top, #066b7f, #006a9f, #545fb0, #9d439f, #cd0a6b)` |
| 100 | Sky and Sunset | light | `#EFF5FA` | `#224168` | `#B26138` | `#0C1B27` | `linear-gradient(to right top, #98b8de, #b0a3d6, #cd8bb7, #d87985, #c7764e)` |
| 100 | Sky and Sunset | dark | `#050B11` | `#98B8DE` | `#C7764E` | `#D8E7F3` | `linear-gradient(to right top, #224168, #594374, #89436c, #a94a55, #b26138)` |

## font — sans (body and UI)

| Font | |
|---|---|
| Figtree | active |
| Geist |  |
| Outfit |  |
| Urbanist |  |
| DM Sans |  |
| Manrope |  |
| Rubik |  |
| Nunito |  |
| Quicksand |  |
| Varela Round |  |

## font — display (large headlines)

| Font | |
|---|---|
| Outfit | active |
| Figtree |  |
| Fraunces |  |
| Urbanist |  |

## font — mono (code)

| Font | |
|---|---|
| Geist Mono | active |
| DM Mono |  |
| Red Hat Mono |  |
| JetBrains Mono |  |
| IBM Plex Mono |  |
| Martian Mono |  |
