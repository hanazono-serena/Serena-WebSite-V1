<template>
    <div>
        <h1 style="padding-top:50px">花園セレナ</h1>
        <div class="wrapper">
            <div>
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
                <div>
                    <p>
                        初めまして、<br>
                        貴方の飼い猫 バーチャルライバーの花園セレナと申します！<br>
                        <br>
                        国境を超えて「bilibili動画」「YouTube」等で活動しています！<br>
                        日本と海外を繋ぐ架け橋になれるように日々頑張っています✨<br>
                    </p>
                </div>
            </div>
            <div>
                <h2>Fan Groups</h2>
                <p class="fan_group_item">
                    <a href="https://t.me/HanazonoSerena" target="_blank">
                        <img src="../assets/telegram-app.png" class="fan_group_icon" alt="telegram" align="center">Telegram
                    </a>
                </p>
                <p class="fan_group_item">
                    <a href="https://jq.qq.com/?_wv=1027&k=IrBVYvwY" target="_blank">
                        <img src="../assets/qq.png" class="fan_group_icon" alt="qq" align="center">QQ
                    </a>
                </p>
            </div>
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

.fan_group_item {
    font-size: 20px;
}

.fan_group_item a {
    text-decoration: none;
    color: black;
}

.fan_group_icon {
    height: 50px;
    width: 50px;
}

.wrapper {
    display: grid;
    grid-template-columns: repeat(2, 30vw);
    grid-gap: 30px;
}

.site_icon {
    padding: 5px;
    height: 32px;
    width: 32px;
    /*background: rgb(255, 255, 255);*/
}
</style>
