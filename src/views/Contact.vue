<template>
    <div style="padding-top:50px">
        <div class="wrapper">
            <div>
                <h1>ご依頼の際は</h1>
                <p>要求</p>
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
                            <textarea placeholder="メッセージ" v-model="message"></textarea>
                        </label>
                    </fieldset>
                    <fieldset>
                        <button v-on:click="submit()">送信</button>
                        <!--                        <button>送信</button>-->
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
                message: null
            }
        },
        beforeCreate: function () {
            document.body.className = 'contactPage otherPages'
        },
        methods: {
            submit: function () {
                let data = {name: this.name, email: this.email, title: this.title, message: this.message}
                this.$http.post('http://localhost:6001/contact', data).then(function (response) {
                    if (response.status === 200) {
                        alert('成功')
                        this.name = null
                        this.email = null
                        this.title = null
                        this.message = null
                    } else {
                        alert('failed...')
                    }
                }.bind(this))
            }
        }
    }
</script>

<style scoped>
    .wrapper {
        display: grid;
        grid-template-columns: repeat(2, 30vw);
        grid-gap: 30px;
        /*grid-auto-rows: minmax(100px,auto);*/
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