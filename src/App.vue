<template>
<div id="app">
<button type=”button” name=”button” @click='getUsers'>get users</button>
  <h1>Superhero Index</h1>
  <!-- {{info}} -->
  <section v-if="erorred"> 
    <p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
  </section>

  <section>
    <div v-if="loading">Loading...</div>

    <div>
     
      <table>
        <th>Name</th>
        <th>Alias</th>

        <tbody>
        <tr  v-for="hero in info" :key='hero.key'>
          <td>{{hero.name}}</td>
          <td>{{hero.alias}}</td>
        </tr>
        </tbody>
        </table>
    </div>
  </section>
  <hr>
  <FormComponent>sdsd</FormComponent> 
</div>
</template>
<script>
import FormComponent from './components/FormComponent';

const axios = require('axios').default;
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
//  var form = document.querySelector('form')
//   var data = new FormData(form)




export default {
  components: {FormComponent},
  name: 'App',
  data () {
    return {
      info: null,
      loading: true,
      errored: false
 }
 },
 methods: {
 getUsers() {
    axios
      .get('http://127.0.0.1:8000/api/v1/heroes/?format=json')
      .then(response => {
        this.info = response.data
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(() => this.loading = false)
      
  },
 
 postUsers() {
   axios
    .post('http://127.0.0.1:8000/api/v1/heroes',)
    .then(response => {
    this.message = console.log(response);
})
 .catch(error => {
  console.log(error);
 })
 }
}
}

</script>
<style lang=”scss”>
</style>
