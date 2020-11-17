<!--
© 2020 Hanazono Serena
@Author brainbush
-->

<template>
    <div class="cover_copyright">Illustrated by <a target="_blank" rel="noopener noreferrer"
                                                   href="https://twitter.com/kokuri89490047"
                                                   style="padding-left: 2px"> kokuri</a>
    </div>
</template>

<script>
    export default {
        name: "mainPage",
        beforeCreate: function () {
            document.body.className = 'mainPage'
        }
    }
</script>

<style scoped>

    .cover_copyright {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        display: flex;
        align-items: flex-end;
        justify-content: flex-end;
        padding: 10px;
        color: #fefefe;
        text-shadow: black 0.1em 0.1em 0.1em;
    }

    .cover_copyright a:link {
        color: #fefefe;
    }

    .cover_copyright a:hover {
        color: #fefefe;
    }

    .cover_copyright a:active {
        color: #fefefe;
    }

    .cover_copyright a:visited {
        color: #fefefe;
    }
</style>
