# num-tracker
 
相席系居酒屋の人数可視化ツールです！  
対応している居酒屋はag、oriental lounge、相席屋です。  
全店舗対応してます(2022/4/25現在)

相席した人にシェアしまくろう！！
 
# DEMO
 
![num-tracker](https://user-images.githubusercontent.com/67764965/165044520-2b6e73ea-8535-4c81-80ed-f5107a708f79.PNG)
# Features
 
 各店舗のサイトを10分間隔で巡回して人数データを取得するプログラムをpythonで作成し、  
 Herokuにデプロイしています。(データの保存にはHerokuのPostgresqlを使っています。)

 データの可視化にはStreamlitを使用しています。  
 こちらはStreamlit Cloudにデプロイしています。
 
# Usage
 
https://share.streamlit.io/soogle44/num-tracker へアクセス！  
ページ上部に主要な店の最新データを表示させています。  
ドロップボックスで店舗・日付を指定すると下部に人数の時間変化のグラフと元データが表示されます。

# Note
 
 データベースはHerokuの無料枠につき、同時接続の上限が20となっております。  
 接続できないときは待ちましょう！