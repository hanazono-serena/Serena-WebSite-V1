<template>
    <div class="wrapper">
        <div class="goods_item" v-for="(item,i) in shop_items" :key="i">
            <a :href="item.url" target="_blank">
                <div style="height: 150px;align-content: center;justify-content: center;display: grid">
                    <img :alt="item.name" :src="item.img" style="max-width: 200px; max-height:150px">
                </div>
            </a>
            <a :href="item.url" target="_blank">
                <div style="color: black;font-size: 14px;font-weight: bold;height: 50px">{{item.name}}</div>
            </a>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Goods",
        data() {
            return {
                shop_items: [
                    {
                        name: '【抱き枕カバー】抱き枕カバー♥ご主人様と一緒❤',
                        img: require('../assets/goods_img/SAMPLE両面2.png'),
                        url: 'https://hanazonoserena.booth.pm/items/2082176'
                    },
                    {
                        name: '【ホワイトデー】チュッ💓お返しが嬉しくて堪らないセレナちゃん【短編ボイス】',
                        img: require('../assets/goods_img/004ccfd5-7611-48be-bae1-8b06ca9714a6_base_resized.jpg'),
                        url: 'https://hanazonoserena.booth.pm/items/1272923'
                    },
                    {
                        name: '【コミケ販売】花園セレナお注射しちゃうよ❤アクリルキーホルダー',
                        img: require('../assets/goods_img/0c02bae673ae5ebde7710f13e2f76269.png'),
                        url: 'https://hanazonoserena.booth.pm/items/1758027'
                    },
                    {
                        name: '【バレンタインに💕】ちゅっちゅしちゃう短編ボイスドラマ＋リクエストボイス',
                        img: require('../assets/goods_img/028adcb0-46ea-4aa3-9eb3-820993ebb278_base_resized.jpg'),
                        url: 'https://hanazonoserena.booth.pm/items/1228720'
                    },
                    {
                        name: '【コミケ販売】花園セレナアクリルスタンド',
                        img: require('../assets/goods_img/3289f4cc56559c66ec249393cfcb5835.png'),
                        url: 'https://hanazonoserena.booth.pm/items/1758014'
                    },
                    {
                        name: '【第一弾】花園セレナリクエストボイス',
                        img: require('../assets/goods_img/0960036b-f6e0-4209-a78d-e9d6e2708712_base_resized.jpg'),
                        url: 'https://hanazonoserena.booth.pm/items/1217361'
                    },
                    {
                        name: '【初挑戦！バイノーラル録音】エッ！？シチュエーションボイス【花園セレナ】',
                        img: require('../assets/goods_img/d59c6275-bece-48b9-8f04-7ef52e9c7ec9_base_resized.jpg'),
                        url: 'https://hanazonoserena.booth.pm/items/1320270'
                    },
                    {
                        name: '💕花園セレナ＆くったんと一緒💕【アクリルキーホルダー】',
                        img: require('../assets/goods_img/04ecc14bacb19b7532e9cbfd53c0cd56.png'),
                        url: 'https://hanazonoserena.booth.pm/items/1600734'
                    }
                ]
            }
        },
        beforeCreate: function () {
            document.body.className = 'goodsPage otherPages'
        }
    }
</script>

<style scoped>
    .wrapper {
        display: grid;
        grid-template-columns: repeat(4, 230px);
        grid-template-rows: repeat(2, 200px);
        grid-gap: 15px;
        padding-top: 20px;
    }

    .goods_item {
        text-align: center;
        align-content: center;
        display: flex;
        flex-direction: column;
    }
</style>