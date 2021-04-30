const Zm = new Vue({
    el: '#Zm',
    delimiters: ['[[',']]'],
    data: {
        posts: [],
        ZPost: {
            "author": "",
            "title": null,
            "description": "",
            "image": null
        },
        csrf_token: "",
    },
    methods: {
        loadZellis: function() {
            axios({
                method: 'get',
                url: '/api/v1/posts/'
            }).then(response => {
                this.posts = response.data
            })
        },
        createZPost: function() {
            axios({
                method: 'post',
                url: '/api/v1/posts/',
                headers: {
                    'X-CSRFToken': this.csrf_token
                },
                data: this.ZPost
            })
        }
    },
    created: function() {
        console.log('load zellis worked')
        this.loadZellis()
    },
    mounted: function() {
        this.csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    }
})