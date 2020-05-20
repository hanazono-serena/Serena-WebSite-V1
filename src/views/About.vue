<template>
    <div style="padding-right: 30%;padding-top:50px">
        <h1>花園セレナ</h1>
        <h2>- Vtuber / 声優</h2>
        <div class="site_icons">
            <a target="_blank" rel="noopener noreferrer"
               href="https://www.youtube.com/channel/UCRXBTd80F5IIWWY4HatJ5Ug">
                <img class="site_icon" alt="YouTube" src="../assets/youtube_social_squircle_red.png">
            </a>
            <a target="_blank" rel="noopener noreferrer" href="https://twitter.com/hanazono_serena">
                <img class="site_icon" alt="Twitter" src="../assets/Twitter_Logo_Blue.png">
            </a>
            <a target="_blank" rel="noopener noreferrer" href="https://space.bilibili.com/380829248">
                <img class="site_icon" alt="BiliBili" src="../assets/bilibili-logo.png">
            </a>
        </div>
        <div class="">
            <p>こんにちは～！貴方の飼い猫 花園セレナです！<br>
                YouTube・ビリビリ動画で活動中です！<br>
                <br>
                歌・ゲーム・雑談をメインに活動しています！<br>
                よければ、貴方の飼い猫にしてください</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "About",
        beforeCreate: function () {
            document.body.className = 'aboutPage otherPages'
        }
    }
</script>

<style scoped>
    .site_icons {
        height: 40px;
        display: flex;
    }

    .site_icon {
        padding: 5px;
        height: 32px;
        width: 32px;
        /*background: rgb(255, 255, 255);*/
    }
</style>