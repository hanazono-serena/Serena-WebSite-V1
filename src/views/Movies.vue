<template>
  <div>
    <div id="videos-wrapper" style>
      <div v-for="(video,i) in movie_list" :key="i" style="padding: 20px; ">
        <img
          style="width: 500px;cursor: pointer;"
          :alt="video.name"
          :src="video.cover"
          v-on:click="display_modal(i)"
        />
      </div>
    </div>
    <div class="modal" id="modal" v-if="modal" @click="modal=false">
      <span class="modal_close cursor" v-on:click="modal=false">&times;</span>
      <div class="modal_content">
        <iframe
          width="960px"
          height="540px"
          :src="video_src"
          allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          style="border:none"
        ></iframe>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Movies",
  beforeCreate: function () {
    document.body.className = "moviesPage otherPages";
  },
  data() {
    return {
      movie_list: [
        {
          name: "你的猫咪(君の猫)",
          cover: "https://i.ytimg.com/vi/xpiAxt7YSIw/maxresdefault.jpg",
          video_src: "https://www.youtube.com/embed/xpiAxt7YSIw",
        },
        {
          name: "ダダダダ天使",
          cover: "https://i.ytimg.com/vi/jcE4Pd0Yxbc/maxresdefault.jpg",
          video_src: "https://www.youtube.com/embed/jcE4Pd0Yxbc",
        },
        {
          name: "五等分の気持ち",
          cover: "https://i.ytimg.com/vi/-vfa5IrYCE0/hqdefault.jpg",
          video_src: "https://www.youtube.com/embed/-vfa5IrYCE0",
        },
        {
          name: "おねがいマッスル",
          cover: "https://i.ytimg.com/vi/c9Exc0zzsRU/hqdefault.jpg",
          video_src: "https://www.youtube.com/embed/c9Exc0zzsRU",
        },
        {
          name: "グランドエスケープ",
          cover: "https://i.ytimg.com/vi/ER26yjAxpYY/hqdefault.jpg",
          video_src: "https://www.youtube.com/embed/ER26yjAxpYY",
        },
        {
          name: "勾指起誓",
          cover: "https://i.ytimg.com/vi/znnNgU5p_GM/hqdefault.jpg",
          video_src: "https://www.youtube.com/embed/znnNgU5p_GM",
        },
        {
          name: "Tulip",
          cover: "https://i.ytimg.com/vi/h6vKx1mygag/hqdefault.jpg",
          video_src: "https://www.youtube.com/embed/h6vKx1mygag",
        },
      ],
      modal: false,
      video_src: "",
    };
  },
  methods: {
    display_modal: function (i) {
      this.video_src = this.movie_list[i].video_src;
      this.modal = true;
    },
  },
};
</script>

<style scoped>
#videos-wrapper {
  display: flex;
  margin: 50px auto 0 auto;
  min-width: 1081px;
  width: min-content;
  flex-wrap: wrap;
}
</style>
