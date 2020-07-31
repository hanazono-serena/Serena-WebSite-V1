<template>
    <div>
        <div class="container_box">
            <div class="swiper-button-next"></div>
            <div class="swiper-container">
                <div class="swiper-wrapper" style="margin: 0 auto;width: 80vw">
                    <div class="wrapper swiper-slide" v-for="(page_item,i) in works" :key="i">
                        <div class="work_item" v-for="(item,j) in page_item" :key="j" @click="display_modal(i,j)">
                            <div class="work_image_container" :style="{backgroundImage:'url('+item.image+')'}"></div>
                            <div style="color: black;font-size: 16px;font-weight: bold;cursor: pointer">
                                {{item.name}}
                            </div>
                        </div>
                    </div>
                </div>
                <div class="swiper-pagination"></div>
            </div>
            <div class="swiper-button-prev"></div>
        </div>
        <div class="modal" id="modal" v-if="modal" @click.self="modal=false">
            <span class="modal_close cursor" @click="modal=false">&times;</span>
            <div class="modal_content" @click="null">
                <div style="width: 900px;height: 650px;background:white;">
                    <div class="work_modal_content">
                        <div class="work_modal_left_image"
                             :style="{backgroundImage:'url('+modal_content.image+')'}"></div>
                        <div>
                            <h1>{{modal_content.name}}</h1>
                            <div class="modal_description">
                                <div v-html="modal_content.description"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Swiper, {Navigation, Pagination} from 'swiper'

Swiper.use([Navigation, Pagination])
export default {
    name: "Works",
    beforeCreate: function () {
        document.body.className = 'worksPage otherPages'
    },
    data() {
        return {
            modal: false,
            works: [
                [{
                    name: 'ポカリスエット 青と夏 海辺篇【CMパロ】',
                    image: require('../assets/works/201908-3.png'),
                    description: '<p>ポカリスエットのCMをガチで作ってみました！！</p>' +
                        '<p>今回は演出および編集を担当してます！</p>' +
                        '<p>撮影協力に絢瀬和さん、ナレーションはVtuberの花園セレナさんにご協力いただきました喷水鲸鱼</p>' +
                        '<p>徳島の絶景とともにお楽しみください！</p>' +
                        '<iframe width="350" height="215" src="https://www.youtube.com/embed/Cx6JNgKRHEk"' +
                        ' style="border: 0" allow="accelerometer; autoplay; encrypted-media; gyroscope;' +
                        ' picture-in-picture" allowfullscreen></iframe>'
                }, {
                    name: 'ビリビリ動画 リアルイベント「BiliBili World 広州」',
                    image: require('../assets/works/201908-1.png'),
                    description: '<p>中国の大規模サブカルイベント「BILIBILI WORLD 2019 広州」が開催されます。</p>' +
                        '<p>イベントではOveridea所属のVTuberの他、ゲストとしてにじさんじやホロライブなど、多数のVTuberが出演します。</p>' +
                        '<a href="https://bw.bilibili.com/2019/index.html#/guangzhou/">Bilibili World 広州</a>'
                }, {
                    name: '株式会社REALITY Factory リアルイベント「夢ノ花園へようこそ♥」',
                    image: require('../assets/works/201904.jpg'),
                    description: '<p>VTuber花園セレナ&ユメノシオリが初めてのリアルイベントを開催！</p>' +
                        '<p>2人のトークと2対1のお話し会(1人60秒まで)で彩る2人の"夢ノ花園へようこそ♡"</p>' +
                            '<a href="https://t.livepocket.jp/e/yumenohanazono">livepocket</a>'
                    }, {
                        name: '株式会社プロバキャスト リアルイベント 「Vtu"Bar"~Sappro Rog-inn Vtuber~」',
                        image: require('../assets/works/201911.jpg'),
                        description: '<p>第2回北海道Vtuberリアルイベント開催！</p>' +
                            '<p>第1回で見つかった課題点を改善し、より迫力のある映像をお届けするため、この回より巨大スクリーンとプロジェクターを導入。</p>' +
                            '<p>参加数も伸びており、初の3人別枠の開催で、イメージドリンクやフードも非常に好評でした！</p>' +
                            '<a href="https://v-tieup.net/2020/07/11/vtubarvol-1%e3%80%90%e7%b4%a1%e9%9f%b3%e3%82%8c%e3%81%84%e6%a7%98%e3%83%bb%e7%99%bd%e9%9f%b3%e3%81%93%e3%82%86%e3%81%8d%e6%a7%98%e9%bb%92%e9%9f%b3%e3%82%88%e3%82%8b%e6%a7%98%e3%80%91/">V-Tieup</a>'
                    }, {
                        name: 'ビリビリ動画 リアルイベント「BiliBili World 成都」',
                        image: require('../assets/works/201912-1.jpg'),
                        description: '<p>ビリビリワールド2019成都</p>' +
                            '<p>花園serenaも出演することになりました！</p>' +
                            '<p>とてもうれしく思います！</p>' +
                            '<p>また中国のご主人様に会えるなんて(´;ω;｀)</p>' +
                            '<a target="_blank" href="https://bw.bilibili.com/2019/index.html#/chengdu/">Bilibili World 成都</a>'
                    }, {
                        name: 'ビリビリｘ猫耳FM ラジオドラマ 「非科学定制」主役：美奈子',
                        image: require('../assets/works/202001-1.png'),
                        description: '<p>「非科学定制」というビリビリ公式ボイスドラマ</p>' +
                            '<p>「美奈子」役を演じさせていただきました！</p>' +
                            '<a target="_blank" href="https://www.bilibili.com/bangumi/media/md28226990/">非科学定制</a>'
                    }, {
                        name: 'ビリビリ動画 オンラインイベント「课后V派对」EP02',
                        image: require('../assets/works/202001-2.jpg'),
                        description: '<a target="_blank" href="https://www.bilibili.com/video/BV1b7411i7b9">配信録画</a>'
                    }, {
                        name: 'ビリビリ動画 オンラインイベント「bilibili 春のV祭り」',
                        image: require('../assets/works/202003.png'),
                        description: '人気Vtuber続々出演の6時間特番' +
                            '<p>「bilibili春のV祭り」3月22日（日）13時～19時より</p>' +
                            '<p>bilibiliにて「bilibili春のV祭り赏樱会」と題した</p>' +
                            '<p>Vtuberだらけの6時間スペシャル特番を配信いたします。</p>' +
                            '<p>AnimeJapan2020で実施予定だったプログラムを中心に編成し</p>' +
                            '<p>bilibili公式チャンネルと、ニコニコ公式生放送で同時配信します！</p>' +
                            '<p>日中同時配信という特性も踏まえた、日本と中国のファンの対話につながる企画も実施。</p>' +
                            '<p>VTuberやアニメといった素晴らしいコンテンツ文化を</p>' +
                            '<p>2020年もより力強く国際的に花開かせる意図を込めた企画の数々をお見逃しなく！</p>' +
                            '<a target="_blank" href="https://live2.nicovideo.jp/watch/lv324837798">NicoNico生放送</a>'
                    }, {
                        name: 'Overidea オンラインイベント 「歌え！国境なき日中新年企画！」2019',
                        image: require('../assets/works/202002.jpg'),
                        description: '<p>本放送では総勢３３名にもなるVTuberが世界中にいる皆さんにワンコーラスでメドレー式に歌をお届けします。</p>' +
                            '<p>歌の後には実際に登場して頂きトークをしますが、当日ご多忙な参加者からは素敵なメッセージ動画が届きます。</p>' +
                            '<p>中国と日本、新しいVTuberを知ってみる良い機会ですね！</p>' +
                            '<p>なお、本企画はビリビリ動画とOverideaによる共同主催となります。</p>' +
                            '<a target="_blank" href="https://www.youtube.com/watch?v=h-Qh0-t4JqI">配信録画</a>'
                }, {
                    name: 'ビリビリ生放送部 オンラインイベント 「寻梦异世镜」第三回&第四回',
                    image: require('../assets/works/201908-2.png'),
                    description: '<a href="https://www.bilibili.com/blackboard/live/activity-xmysj3xmm.html">第三回</a>' +
                        '<a target="_blank" href="https://www.bilibili.com/blackboard/live/activity-xmysj4xjg.html">第四回</a>'
                }, {
                    name: 'ビリビリ生放送部 オンラインイベント 「氷火歌合戦」SP',
                    image: require('../assets/works/201912-2.jpg'),
                    description: '<a target="_blank" href="https://www.bilibili.com/video/BV1yJ411Y7Zm">配信録画</a>'
                }, {
                    name: 'Overidea オンラインイベント 「歌え！国境なき世界新年企画！」2020',
                    image: require('../assets/works/202002.jpg'),
                    description: '<p>本放送では総勢６０名以上にもなるVTuberが世界中にいる皆さんにワンコーラスでメドレー式に歌をお届けします。</p>' +
                        '<p>歌の後にはVTR出演もしくは生出演で交流！国境を超えたものがここにはある。そう感じて頂ければ幸いです。</p>' +
                        '<p>これを期に、様々なVTuberさんと出会ってみてはいかがでしょう？</p>' +
                        '<p>なお、本企画はビリビリ動画とOverideaによる共同主催となります。</p>' +
                        '<a target="_blank" href="https://www.youtube.com/watch?v=ljspl1k_TjQ">配信録画</a>'
                }], [{
                    name: 'ポカリスエット 青と夏 海辺篇【CMパロ】',
                    image: require('../assets/works/201908-3.png'),
                    description: '<p>ポカリスエットのCMをガチで作ってみました！！</p>' +
                        '<p>今回は演出および編集を担当してます！</p>' +
                        '<p>撮影協力に絢瀬和さん、ナレーションはVtuberの花園セレナさんにご協力いただきました喷水鲸鱼</p>' +
                        '<p>徳島の絶景とともにお楽しみください！</p>' +
                        '<iframe width="350" height="215" src="https://www.youtube.com/embed/Cx6JNgKRHEk"' +
                        ' style="border: 0" allow="accelerometer; autoplay; encrypted-media; gyroscope;' +
                        ' picture-in-picture" allowfullscreen></iframe>'
                }, {
                    name: 'ビリビリ動画 リアルイベント「BiliBili World 広州」',
                    image: require('../assets/works/201908-1.png'),
                    description: '<p>中国の大規模サブカルイベント「BILIBILI WORLD 2019 広州」が開催されます。</p>' +
                        '<p>イベントではOveridea所属のVTuberの他、ゲストとしてにじさんじやホロライブなど、多数のVTuberが出演します。</p>' +
                        '<a href="https://bw.bilibili.com/2019/index.html#/guangzhou/">Bilibili World 広州</a>'
                }, {
                    name: '株式会社REALITY Factory リアルイベント「夢ノ花園へようこそ♥」',
                    image: require('../assets/works/201904.jpg'),
                    description: '<p>VTuber花園セレナ&ユメノシオリが初めてのリアルイベントを開催！</p>' +
                        '<p>2人のトークと2対1のお話し会(1人60秒まで)で彩る2人の"夢ノ花園へようこそ♡"</p>' +
                        '<a href="https://t.livepocket.jp/e/yumenohanazono">livepocket</a>'
                }, {
                    name: '株式会社プロバキャスト リアルイベント 「Vtu"Bar"~Sappro Rog-inn Vtuber~」',
                    image: require('../assets/works/201911.jpg'),
                    description: '<p>第2回北海道Vtuberリアルイベント開催！</p>' +
                        '<p>第1回で見つかった課題点を改善し、より迫力のある映像をお届けするため、この回より巨大スクリーンとプロジェクターを導入。</p>' +
                        '<p>参加数も伸びており、初の3人別枠の開催で、イメージドリンクやフードも非常に好評でした！</p>' +
                        '<a href="https://v-tieup.net/2020/07/11/vtubarvol-1%e3%80%90%e7%b4%a1%e9%9f%b3%e3%82%8c%e3%81%84%e6%a7%98%e3%83%bb%e7%99%bd%e9%9f%b3%e3%81%93%e3%82%86%e3%81%8d%e6%a7%98%e9%bb%92%e9%9f%b3%e3%82%88%e3%82%8b%e6%a7%98%e3%80%91/">V-Tieup</a>'
                }, {
                    name: 'ビリビリ動画 リアルイベント「BiliBili World 成都」',
                    image: require('../assets/works/201912-1.jpg'),
                    description: '<p>ビリビリワールド2019成都</p>' +
                        '<p>花園serenaも出演することになりました！</p>' +
                        '<p>とてもうれしく思います！</p>' +
                        '<p>また中国のご主人様に会えるなんて(´;ω;｀)</p>' +
                        '<a target="_blank" href="https://bw.bilibili.com/2019/index.html#/chengdu/">Bilibili World 成都</a>'
                }, {
                    name: 'ビリビリｘ猫耳FM ラジオドラマ 「非科学定制」主役：美奈子',
                    image: require('../assets/works/202001-1.png'),
                    description: '<p>「非科学定制」というビリビリ公式ボイスドラマ</p>' +
                        '<p>「美奈子」役を演じさせていただきました！</p>' +
                        '<a target="_blank" href="https://www.bilibili.com/bangumi/media/md28226990/">非科学定制</a>'
                }, {
                    name: 'ビリビリ動画 オンラインイベント「课后V派对」EP02',
                    image: require('../assets/works/202001-2.jpg'),
                    description: '<a target="_blank" href="https://www.bilibili.com/video/BV1b7411i7b9">配信録画</a>'
                }, {
                    name: 'ビリビリ動画 オンラインイベント「bilibili 春のV祭り」',
                    image: require('../assets/works/202003.png'),
                    description: '人気Vtuber続々出演の6時間特番' +
                        '<p>「bilibili春のV祭り」3月22日（日）13時～19時より</p>' +
                        '<p>bilibiliにて「bilibili春のV祭り赏樱会」と題した</p>' +
                        '<p>Vtuberだらけの6時間スペシャル特番を配信いたします。</p>' +
                        '<p>AnimeJapan2020で実施予定だったプログラムを中心に編成し</p>' +
                        '<p>bilibili公式チャンネルと、ニコニコ公式生放送で同時配信します！</p>' +
                        '<p>日中同時配信という特性も踏まえた、日本と中国のファンの対話につながる企画も実施。</p>' +
                        '<p>VTuberやアニメといった素晴らしいコンテンツ文化を</p>' +
                        '<p>2020年もより力強く国際的に花開かせる意図を込めた企画の数々をお見逃しなく！</p>' +
                        '<a target="_blank" href="https://live2.nicovideo.jp/watch/lv324837798">NicoNico生放送</a>'
                }, {
                    name: 'Overidea オンラインイベント 「歌え！国境なき日中新年企画！」2019',
                    image: require('../assets/works/202002.jpg'),
                    description: '<p>本放送では総勢３３名にもなるVTuberが世界中にいる皆さんにワンコーラスでメドレー式に歌をお届けします。</p>' +
                        '<p>歌の後には実際に登場して頂きトークをしますが、当日ご多忙な参加者からは素敵なメッセージ動画が届きます。</p>' +
                        '<p>中国と日本、新しいVTuberを知ってみる良い機会ですね！</p>' +
                        '<p>なお、本企画はビリビリ動画とOverideaによる共同主催となります。</p>' +
                        '<a target="_blank" href="https://www.youtube.com/watch?v=h-Qh0-t4JqI">配信録画</a>'
                }, {
                    name: 'ビリビリ生放送部 オンラインイベント 「寻梦异世镜」第三回&第四回',
                    image: require('../assets/works/201908-2.png'),
                    description: '<a href="https://www.bilibili.com/blackboard/live/activity-xmysj3xmm.html">第三回</a>' +
                        '<a target="_blank" href="https://www.bilibili.com/blackboard/live/activity-xmysj4xjg.html">第四回</a>'
                }, {
                    name: 'ビリビリ生放送部 オンラインイベント 「氷火歌合戦」SP',
                    image: require('../assets/works/201912-2.jpg'),
                    description: '<a target="_blank" href="https://www.bilibili.com/video/BV1yJ411Y7Zm">配信録画</a>'
                }, {
                    name: 'Overidea オンラインイベント 「歌え！国境なき世界新年企画！」2020',
                    image: require('../assets/works/202002.jpg'),
                    description: '<p>本放送では総勢６０名以上にもなるVTuberが世界中にいる皆さんにワンコーラスでメドレー式に歌をお届けします。</p>' +
                        '<p>歌の後にはVTR出演もしくは生出演で交流！国境を超えたものがここにはある。そう感じて頂ければ幸いです。</p>' +
                        '<p>これを期に、様々なVTuberさんと出会ってみてはいかがでしょう？</p>' +
                        '<p>なお、本企画はビリビリ動画とOverideaによる共同主催となります。</p>' +
                        '<a target="_blank" href="https://www.youtube.com/watch?v=ljspl1k_TjQ">配信録画</a>'
                },]
            ],
            modal_content: null,
            swiper: null
        }
    },
    mounted() {
        this.$nextTick(() => {
            this.swiper = new Swiper('.swiper-container', {
                pagination: {
                    el: '.swiper-pagination',
                    clickable: true
                    // type: 'fraction'
                },
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                }
            })
        })
    },
    methods: {
        display_modal(i, j) {
            this.modal_content = this.works[i][j]
            this.modal = true
        }
    }
}
</script>
<style lang="scss">
//$themeColor: #fefefe;
@import '~swiper/swiper-bundle';
@import '~swiper/components/navigation/navigation';

:root {
  --swiper-theme-color: #fefefe;
}
</style>
<style scoped>
/*.swiper-button-prev:after, .swiper-button-next:after {*/
/*    color: #fefefe;*/
/*    text-shadow: black 0.1em 0.1em 0.2em;*/
/*}*/
.swiper-button-prev:after, .swiper-button-next:after {
    text-shadow: black 0.1em 0.1em 0.2em;
}

.swiper-button-next {
    right: 80px
}

.swiper-button-prev {
    left: 80px
}

.container_box {
    display: flex;
    margin: auto;
}

.wrapper {
    padding-top: 20px;
    display: flex;
    flex-wrap: wrap;
    text-align: center;
    justify-content: center;
}

.work_item {
    width: 230px;
    text-align: center;
    align-content: center;
    display: flex;
    flex-direction: column;
    margin: 5px 15px;
}

    .work_image_container {
        width: 240px;
        height: 135px;
        background-size: contain;
        cursor: pointer;
        background-repeat: no-repeat;
        background-position: center;
    }

    .work_modal_content {
        display: grid;
        grid-template-columns: repeat(2, 450px);
    }

    .work_modal_left_image {
        max-width: 430px;
        justify-content: center;
        align-items: center;
        display: grid;
        height: 650px;
        padding: 5px;
        background-repeat: no-repeat;
        background-position: center;
        background-size: contain;
    }

    .modal_description {
        white-space: pre-wrap;
        color: black;
        padding: 5px;
    }
</style>