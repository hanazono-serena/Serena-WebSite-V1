<template>
    <div>
        <div style="display: flex;padding-top: 50px;">
            <div v-for="(video,i) in movie_list" :key="i" style="padding: 20px">
                <img style="max-width: 512px;cursor: pointer" :alt="video.name" :src="video.cover"
                     v-on:click="display_modal(i)">
            </div>
        </div>
        <div class="modal" id="modal" v-if="modal" @click="modal=false">
            <span class="modal_close cursor" v-on:click="modal=false">&times;</span>
            <div class="modal_content">
                <iframe width="960px" height="540px" :src="video_src"
                        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen style="border:none"></iframe>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Movies",
        beforeCreate: function () {
            document.body.className = 'moviesPage otherPages'
        },
        data() {
            return {
                movie_list: [
                    {
                        name: '你的猫咪(君の猫)',
                        cover: 'https://i.ytimg.com/vi/xpiAxt7YSIw/maxresdefault.jpg',
                        video_src: 'https://www.youtube.com/embed/xpiAxt7YSIw'
                    },
                    {
                        name: 'ダダダダ天使',
                        cover: 'https://i.ytimg.com/vi/jcE4Pd0Yxbc/maxresdefault.jpg',
                        video_src: 'https://www.youtube.com/embed/jcE4Pd0Yxbc'
                    }
                ],
                modal: false,
                video_src: ""
            }
        },
        methods: {
            display_modal: function (i) {
                this.video_src = this.movie_list[i].video_src
                this.modal = true
            }
        }
    }
</script>

<style scoped>

</style>