window.onload = function () {
  Vue.component('dispatcher-item', {
    props: ['dispatcher'],
    template: '<li class="d-flex no-block card-body border-top"><i class="fas fa-user-circle w-30px m-t-5 text-danger"></i><div><a v-bind:href="dispatcher.url" class="m-b-0 font-medium p-0">{{ dispatcher.fullname }}</a><span class="text-muted"></span></div><div class="ml-auto"><div class="tetx-right"><span class="text-muted font-16">Диспетчер</span><h5 class="text-muted m-b-0">{{ dispatcher.user_no }}</h5></div></div></li>'
  })

  var app7 = new Vue({
    el: '#Dispatcher',
    data() {
      return {
        dispatcherList: null,
        interval: null,
        status: 'Загрузка...'
      };
    },
    created() {
      this.interval = setInterval(this.refreshData, 10000)
      this.refreshData();
    },
    beforeDestroy() {
      clearInterval(this.interval)
    },
    methods: {
      refreshData() {
        axios.get("http://127.0.0.1:8000/api/dispatchers/")
          .then(response => {
            this.dispatcherList = response.data;
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

  // aria-valuemin="0" aria-valuemax="100"

  Vue.component('ongraph-item', {
    props: ['ongraph'],
    template: `<div>
  <div class="d-flex no-block align-items-center m-t-25">
      <span><a :href="ongraph.url">{{ ongraph.name }}:</a>
      {{ ongraph.orders_percent }}%</span>
      <div class="ml-auto">
          <span>{{ ongraph.orders }}шт.</span>
      </div>
  </div>
  <div class="progress">
    <div class="progress-bar" :class="ongraph.bgcolor" role="progressbar" v-bind:style="{ width: ongraph.orders_percent + '%' }"></div>
    
  </div>
</div>`
  })

  var app8 = new Vue({
    el: '#ongraph',
    data() {
      return {
        ongraphList: null,
        interval: null,
        status: 'Загрузка...'
      };
    },
    created() {
      this.interval = setInterval(this.refreshData, 10000)
      this.refreshData();
    },
    beforeDestroy() {
      clearInterval(this.interval)
    },
    methods: {
      refreshData() {
        axios.get("http://127.0.0.1:8000/api/ongraph/")
          .then(response => {
            this.ongraphList = response.data.orders;
            this.status = null;
          })
          .catch(error => {
            console.log(error);
            this.status = error
            this.errored = true;
          })
      }
    }
  })

}