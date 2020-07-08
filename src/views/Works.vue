<template>
    <div>
        <div class="wrapper">
            <div class="work_item" v-for="(item,i) in works" :key="i">
                <div class="work_image_container" :style="{backgroundImage:'url('+item.image+')'}"
                     v-on:click="display_modal(i)"></div>
                <div style="color: black;font-size: 16px;font-weight: bold;cursor: pointer"
                     v-on:click="display_modal(i)">
                    {{item.name}}
                </div>
            </div>
        </div>
        <div class="modal" id="modal" v-if="modal" @click="modal=false">
            <span class="modal_close cursor" v-on:click="modal=false">&times;</span>
            <div class="modal_content">
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
    export default {
        name: "Works",
        beforeCreate: function () {
            document.body.className = 'worksPage otherPages'
        },
        data() {
            return {
                modal: false,
                // img:require('../assets/works'),
                works: [
                    {
                        name: 'ポカリスエット 青と夏 海辺篇【CMパロ】',
                        image: require('../assets/works/Cx6JNgKRHEk.jpg'),
                        description: '<p>ポカリスエットのCMをガチで作ってみました！！</p>' +
                            '<p>今回は演出および編集を担当してます！</p>' +
                            '<p>撮影協力に絢瀬和さん、ナレーションはVtuberの花園セレナさんにご協力いただきました喷水鲸鱼</p>' +
                            '<p>徳島の絶景とともにお楽しみください！</p>' +
                            '<iframe width="350" height="215" src="https://www.youtube.com/embed/Cx6JNgKRHEk"' +
                            ' style="border: 0" allow="accelerometer; autoplay; encrypted-media; gyroscope;' +
                            ' picture-in-picture" allowfullscreen></iframe>'
                    }, {
                        name: '株式会社REALITY Factory リアルイベント「夢ノ花園へようこそ♥」',
                        image: require('../assets/works/temp1.png'),
                        description: 'this is the first line\nthis is the second line\n<a href="https://twitter.com/hanazono_serena">Twitter</a>'
                    }, {
                        name: 'ビリビリ動画 リアルイベント「BiliBili World 広州」',
                        image: require('../assets/works/temp1.png'),
                        description: 'this is the first line\nthis is the second line\n'
                    }, {
                        name: '株式会社プロバキャスト リアルイベント 「Vtu"Bar"~Sappro Rog-inn Vtuber~」',
                        image: require('../assets/works/temp1.png'),
                        description: 'this is the first line\nthis is the second line\n'
                    }, {
                        name: 'ビリビリ動画 リアルイベント「BiliBili World 成都」',
                        image: require('../assets/works/temp1.png'),
                        description: 'this is the first line\nthis is the second line\n'
                    }, {
                        name: 'ビリビリｘ猫耳FM ラジオドラマ 「非科学定制」主役：美奈子',
                        image: require('../assets/works/temp1.png'),
                        description: 'this is the first line\nthis is the second line\n'
                    }, {
                        name: 'ビリビリ動画 オンラインイベント「课后V派对」EP02',
                        image: require('../assets/works/temp1.png'),
                        description: 'this is the first line\nthis is the second line\n'
                    }, {
                        name: 'ビリビリ動画 オンラインイベント「bilibili 春のV祭り」',
                        image: require('../assets/works/temp1.png'),
                        description: 'this is the first line\nthis is the second line\n'
                    }, {
                        name: 'Overidea オンラインイベント 「歌え！国境なき日中新年企画！」2019',
                        image: require('../assets/works/temp1.png'),
                        description: 'this is the first line\nthis is the second line\n'
                    }, {
                        name: 'ビリビリ生放送部 オンラインイベント 「寻梦异世镜」第三回&第四回',
                        image: require('../assets/works/temp1.png'),
                        description: 'this is the first line\nthis is the second line\n'
                    }, {
                        name: 'ビリビリ生放送部 オンラインイベント 「氷火歌合戦」SP',
                        image: require('../assets/works/temp1.png'),
                        description: 'this is the first line\nthis is the second line\n'
                    }, {
                        name: 'Overidea オンラインイベント 「歌え！国境なき世界新年企画！」2020',
                        image: require('../assets/works/temp1.png'),
                        description: 'this is the first line\nthis is the second line\n'
                    },
                ],
                modal_content: null
            }
        },
        methods: {
            display_modal(i) {
                this.modal_content = this.works[i]
                this.modal = true
            }
        }
    }
</script>

<style scoped>
    .wrapper {
        display: grid;
        grid-template-columns: repeat(4, 230px);
        grid-template-rows: repeat(2, 180px);
        grid-gap: 15px;
        padding-top: 40px;
    }

    .work_item {
        text-align: center;
        align-content: center;
        display: flex;
        flex-direction: column;
    }

    .work_image_container {
        width: 240px;
        height: 135px;
        background-size: cover;
        cursor: pointer;
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