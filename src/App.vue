<template>
    <div id="app">
        <div class="top_window">
            <div class="top_container page_container">
                <div v-if="$route.name==='mainPage'">
                    <div style="font-size: 5em">花園セレナ</div>
                </div>
                <div v-else>
                    <router-link :to="{name:'mainPage'}" style="font-size: 5em">花園セレナ</router-link>
                </div>
                <div class="top_container_inline_box">
                    <router-link :to="{name:'about'}" class="top_box_item">
                        <div class="top_box_text">About</div>
                    </router-link>
                    <router-link :to="{name:'works'}" class="top_box_item">
                        <div class="top_box_text">Works</div>
                    </router-link>
                    <router-link :to="{name:'movies'}" class="top_box_item">
                        <div class="top_box_text">Movies</div>
                    </router-link>
                    <router-link :to="{name:'goods'}" class="top_box_item">
                        <div class="top_box_text">Goods</div>
                    </router-link>
                    <router-link :to="{name:'contact'}" class="top_box_item">
                        <div class="top_box_text">Contact</div>
                    </router-link>
                </div>
            </div>
            <RouterView/>
        </div>

    </div>
</template>

<script>
    export default {
        name: 'App',
        components: {},
    }
</script>

<style>
    body {
        background-size: cover;
        width: auto;
        height: auto;
        background-attachment: fixed;
        font-family: source-han-sans-cjk-ja, sans-serif;
        font-weight: 400;
        font-style: normal;
    }

    #app {
        top: 0;
        left: 0;
        width: 100%;
        position: absolute;
        z-index: 1;
    }

    body {
        background-position: center;
    }

    body.mainPage {
        background-image: url("./assets/2.jpg");
    }

    body.aboutPage {
        background-image: url("./assets/4.png");
    }

    body.worksPage {
        background-image: url("./assets/1.jpg");
    }

    body.moviesPage {
        background-image: url("./assets/6.png");
    }

    body.goodsPage {
        background-image: url("./assets/1.jpg");
    }

    body.contactPage {
        background-image: url("./assets/2.jpg");
    }

    .page_container {
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center;
    }

    .top_box_item {
        padding: 20px;
        width: 80px;
    }

    .top_box_text {
        font-size: 1.5em;
    }

    .top_container div {
        color: #fefefe;
        text-shadow: black 0.1em 0.1em 0.2em;
        /*padding-top: 20px;*/
    }

    .top_window {
        width: auto;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        /*justify-content: center;*/
    }

    .otherPages .top_window {
        background: rgba(255, 255, 255, 0.8);
    }

    .mainPage .top_window {
        justify-content: center;
    }

    .top_container a:link {
        text-decoration: none;
        color: #fefefe;
    }

    .top_container a:active {
        text-decoration: blink;
        color: #fefefe;
    }

    .top_container a:hover {
        text-decoration: underline;
        color: #fefefe;
    }

    .top_container a:visited {
        text-decoration: none;
        color: #fefefe;
    }

    .top_container_inline_box .router-link-active {
        /*background-color: black;*/
    }

    .top_container_inline_box {
        display: flex;
    }

    div {
        box-sizing: border-box;
    }

    .modal {
        display: flex;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        height: 100%;
        width: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.9);
        justify-content: center;
        align-items: center;
    }

    .modal_close {
        color: white;
        position: absolute;
        top: 10px;
        right: 25px;
        font-size: 35px;
        font-weight: bold;
    }

    .modal_close:hover,
    .modal_close:focus {
        color: #999;
        text-decoration: none;
        cursor: pointer;
    }

    .modal_content {
        display: flex;
        margin: auto;
        /*text-align: center;*/
    }


</style>
