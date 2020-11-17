<!--
© 2020 Hanazono Serena
@Author brainbush
-->

<template>
    <div style="padding-top:50px">
        <div class="wrapper">
            <div>
                <h2>ご依頼の際に</h2>
                <h2>下記の内容をご記入してお願いいたします</h2>
                <h3>お名前</h3>
                <h3>連絡先</h3>
                <h3>依頼内容</h3>
            </div>
            <div>
                <form id="contact" @submit.prevent="" style="padding-top: 30px">
                    <fieldset>
                        <label>
                            <input type="text" placeholder="お名前" tabindex="1" required autofocus v-model="name">
                        </label>
                    </fieldset>
                    <fieldset>
                        <label>
                            <input type="email" placeholder="メール" tabindex="2" required v-model="email">
                        </label>
                    </fieldset>
                    <fieldset>
                        <label>
                            <input type="text" placeholder="件名" tabindex="3" required v-model="title">
                        </label>
                    </fieldset>
                    <fieldset>
                        <label>
                            <textarea placeholder="メッセージ" tabindex="4" v-model="message"/>
                        </label>
                    </fieldset>
                    <fieldset>
                        <button v-on:click="submit()" tabindex="5" :disabled="on_submit===true">送信</button>
                    </fieldset>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Contact",
        data() {
            return {
                name: null,
                email: null,
                title: null,
                message: null,
                xsrf: null,
                on_submit: false
            }
        },
        beforeCreate: function () {
            document.body.className = 'contactPage otherPages'
        },
        methods: {
            submit: function () {
                this.on_submit = true
                let data = {name: this.name, email: this.email, title: this.title, message: this.message}
                try {
                    this.$http.post('https://contact.serena.moe/contact', data, {
                        withCredentials: true,
                        headers: {'X-XSRFToken': this.xsrf}
                    }).then(function (response) {
                        if (response.status === 200) {
                            alert('成功')
                            this.name = null
                            this.email = null
                            this.title = null
                            this.message = null
                            this.on_submit = false
                        } else {
                            alert('failed...')
                            this.on_submit = false
                        }
                    }.bind(this))
                } catch (e) {
                    alert('failed...')
                    this.on_submit = false
                }
            }
        },
        mounted() {
            this.$http.get('https://contact.serena.moe/contact', {withCredentials: true}).then(function (response) {
                this.xsrf = response.data.token
            }.bind(this))
        }
    }
</script>

<style scoped>
    .wrapper {
        display: grid;
        grid-template-columns: repeat(2, 30vw);
        grid-gap: 30px;
    }

    fieldset {
        border: medium none !important;
        margin: 0 0 5px;
        min-width: 100%;
        padding-right: 0;
        width: 100%;
    }

    #contact {
        width: 100%;
        min-width: 300px;
        margin: 0 auto;
        position: relative;
    }

    #contact input,
    #contact textarea,
    #contact button {
        width: 100%;
        border: 1px solid #ccc;
        background: #fff;
        margin: 0 0 5px;
        padding: 10px;
    }

    #contact textarea {
        height: 150px;
        max-width: 100%;
        resize: none;
    }

    #contact input:hover,
    #contact textarea:hover,
    #contact textarea:hover {
        border: 1px solid orange;
        transition: background-color 0.3s ease-in-out;
    }

    #contact input:focus,
    #contact textarea:focus,
    #contact button:focus,
    #contact textarea:focus {
        outline: 1px solid orange;
        border: 1px solid orange;
    }

    #contact button {
        cursor: pointer;
        width: 105%;
        border: none;
        background: orange;
        color: #fff;
        margin: 0 0 5px;
        padding: 10px;
        font-size: 15px;
    }
</style>
