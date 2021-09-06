# LAMMPSのダンプファイルの保存について

## 概要

LAMMPSの`dump`コマンドで保存されるトラジェクトリでは、座標が`0<x,y,z<1`にスケールされる。それを確認するためのサンプル。

最初に、

```sh
python3 generate_config.py
```

により、`test.atoms`が作成される。シミュレーションボックスは

```txt
-10 30 xlo xhi
-10 30 ylo yhi
-10 30 zlo zhi
```

と、`-10 < x,y,z < 30`となっている。

入力ファイルは`test.input`であり、時間発展をせずに、そのままダンプファイル`test.lammpstrj`を出力する。

```txt
dump id all atom 1 test.lammpstrj

run 0
```

このダンプファイル`test.lammpstrj`を読み込み、粒子番号を調べて、横軸に「inputファイルでのx座標」、縦軸に「dumpファイルでのx座標」をプロットする。

```sh
python3 check.py > test.dat
gnuplot test.plt
```

すると、以下の図を得る。

![test.png](fig/test.png)

`-10 < x < 30`として入力された座標が、`0<x<1`にリスケールされていることがわかる。ダンプファイルから座標を得るには、

```txt
x = (xhi - xlo)*x + xlo
```

の変換をしてやる必要がある。
