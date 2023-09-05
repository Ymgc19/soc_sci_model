import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import japanize_matplotlib
import base64
from datetime import datetime, timedelta

# フルスクリーン
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(
    page_title="webpage of yama frog",
    layout="wide", 
    initial_sidebar_state="auto",
    page_icon=":paintbrush:"
)

st.title("2章の章末問題に関して")

st.markdown("メモ，山口．あんまりメモ取れませんでした．")

st.markdown("#### 1問目")
st.markdown("生徒会になる前は「ぶっ潰してやる」とか言うけど，実際に生徒会に入ったら中庸になる．")
st.markdown("権力を持つにつれて異なる意見に接触する機会が減って，意見を変えにくくなる．けど，委員会とかでは他の意見に接触する機会が増えて，意見を変えやすくなる．")



st.markdown("#### 2問目")
st.markdown("自分で参加する委員会を選べる→自分の関心のある委員会に参加→極端な意見を持っている人が集まる→でも中庸")
st.markdown("極端な意見を持っている人が集まっても，みんな同じ意見の方向性だとは限らない．いろんな意見の人が混じって結局中庸に．")
st.markdown("上院6年，下院2年．任期")
st.markdown("下院の方が権力が小さいとすれば，下院が極端な意見を持つと言うことはありうる．責任が小さいため．")
st.markdown("福祉問題よりも外交の方が責任が重いので，上院のが外務員のメンバーの方が極端な意見を持つ．いやでも，他の委員でも似たような傾向が見られるって書いてあるやん．")
st.markdown("上院でも下院でも極端な意見になるのであれば，18ページの第二のモデルは矛盾する．")
st.markdown("自分の意見ではなく，他の人の意見が採用されてしまうと，社会が悪くなると思われるので，自分の考えを突き通す（先鋭化）")
st.markdown("福祉問題よりも外交の方が責任が重いので，上院のが外務員のメンバーの方が極端な意見を持つ．")


st.markdown("#### 3問目")
st.markdown("##### 文脈A")
st.markdown("もう当選することがないので，人道的な行為だ．")
st.markdown("##### 文脈B")
st.markdown("2と両立")
st.markdown("##### 文脈C")
st.markdown("両方とも両立しそう")
st.markdown("##### 文脈D")
st.markdown("両立しない")

st.markdown("お金たくさんかけた方が，市民に対する心象が良くなる．マイノリティの中間票を動かす．")
st.markdown("マイノリティが虐げられた結果，犯罪率が上がるとすれば，論理的に考えてマイノリティを支援する政策を作る．")
st.markdown("人道的な行動をするときに100パーセント同情だけで行動する？　合理的に考えて行動する．論理的に社会問題を解決しようとしている．")

st.markdown("#### 4問目")
st.markdown("##### a")
st.markdown("##### 理論1")
st.markdown("逸脱行動で報酬が得られるようにするのは良くない．効用を下げたらいい（授業サボって体育館裏に行った方が効用が大きい→体育館裏を汚くて臭くする）")

st.markdown("##### 理論2")
st.markdown("目上の人を敬うようにする")
st.markdown("別のことに気を向けさせる．不満や怒りを別のところに向けさせる．旅行のチケットをあげたりする．")

st.markdown("##### 理論3")
st.markdown("アファーマティブアクション")
st.markdown("差別を受けている人に恩恵を与えることで，差別を受けていない人に対して差別っぽくなる．アメリカの受験の事例．")

st.markdown("##### 理論4")
st.markdown("ナメダルマ．アメフト部．")
st.markdown("犯罪者の家宅捜索とかをしていて，アニメとかのサブカルを嗜んでいた証拠を見つけて晒しあげている．")

st.markdown("##### b")
st.markdown("アメリカ社会，黒人が窓ガラスを破りまくる．日頃から不満が溜まっていて，これに乗じてやってやろう．")
st.markdown("聞いてなかった")

st.markdown("#### 問題5")
st.markdown("##### a")
st.markdown("自分と似ている主人公が好まれる．社会の変化とともに女性の働き方・立場とかも変わる．女性が置かれている立場が変わっていき，好みも変わる．")

st.markdown("##### b")
st.markdown("人々は自分と近しいものに共感する．女性の社会的な立場は変化する．")

st.markdown("##### c")
st.markdown("雑誌編集者は，各時代の典型的な女性像をもとに，雑誌小説を選ぶ．")
st.markdown("")

st.markdown("##### d")
st.markdown("人は憧れいている人に対して憧れを抱き，憧れの対象になるようなヒロインの小説が多くなる")


st.markdown("#### 9-12")
st.markdown("##### 10")
st.markdown("相手からの評価を気にして，途中で抜けたりやめたりしないようにする．")
st.markdown("繰り返しゲーム的な考え方，短期的にはだるい電話を切って利益を出したいけど，長期的には悪評を広められない方がいい．")
