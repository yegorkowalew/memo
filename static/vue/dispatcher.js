Vue.component('todo-item', {
  props: ['todo'],
  template: '<li class="d-flex no-block card-body border-top"><i class="fas fa-user-circle w-30px m-t-5 text-danger"></i><div><a href="#" class="m-b-0 font-medium p-0">{{ todo.fields.fullname }}</a><span class="text-muted"></span></div><div class="ml-auto"><div class="tetx-right"><span class="text-muted font-16">Диспетчер</span><h5 class="text-muted m-b-0">{{ todo.fields.user_no }}</h5></div></div></li>'
})

var app7 = new Vue({
  el: '#Dispatcher',
  data() {
    return {
      groceryList: null,
      interval: null,
      status: 'Загрузка...'
    };
  },
  created() {
    this.interval = setInterval(this.refreshData, 10000)
    this.refreshData(); // не работает
  },
  beforeDestroy() {
    clearInterval(this.interval)
  },
  methods: {
    refreshData() {
      axios.get("http://127.0.0.1:8000/on/adm/json/")
        .then(response => {
          this.groceryList = response.data;
          this.status = null
        })
        .catch(error => {
          console.log(error);
          this.status = error
          this.errored = true;
        })
    }
  }
})