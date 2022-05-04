<template>
<div>

  <h2>Registration Form</h2> <br /><br />

  <b-form style="width: 50%; left: 25%; position: absolute;" @submit="submit">
      <b-form-group id="input-group-1" label="Your First Name:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="firstName"
          placeholder="Enter first name"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Your Last Name:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="lastName"
          placeholder="Enter last name"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-3" label="Address:" label-for="input-3">
        <b-form-textarea
          id="input-3"
          v-model="addr"
          placeholder="Enter current address"
          required
        ></b-form-textarea>
      </b-form-group>

      <b-form-group id="input-group-4" label="Password:" label-for="input-4">
        <b-form-textarea
          id="input-4"
          v-model="pw"
          placeholder="Enter Password"
          required
        ></b-form-textarea>
      </b-form-group>

      <!-- <b-form-group id="input-group-5" label="Birthday:" label-for="input-5">
        <b-form-textarea
          id="input-4"
          v-model="birthDate"
          placeholder="Enter Birthdate MM/DD/YYY"
          required
        ></b-form-textarea>
      </b-form-group> -->

      <div>
        <label for="example-datepicker">Enter birthdate</label>
        <b-form-datepicker required id="example-datepicker" v-model="birthDate" class="mb-2"></b-form-datepicker>
      </div>
      <br />
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>

<!-- 

        First Name : <input type="text" v-model="firstName">
        Last Name : <input type="text" v-model="lastName">

        <button v-on:click="submit"> Submit </button> -->
</div>

</template>

<script>
export default {
  name: 'Register',
  data() { 
    return {
      firstName: "",
      lastName: "",
      addr: "",
      birthDate: "",
      pw: ""
    }
  },
  props: {
    createUser: {type: Function},
    getUser: {type: Function},
  },
  methods: {
      submit: function(e){
          e.preventDefault();
          console.log(this.lastName);
          console.log(this.birthDate);
          this.createUser(this.firstName, this.lastName, this.birthDate, this.addr, this.pw).then(() => {
              this.getUser().then((data) => {
              localStorage.setItem("user", data);
              window.location.reload()
            })
          });
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
