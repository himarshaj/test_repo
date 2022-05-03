<template>
  <div id="app">
    <!-- <Register :createUser="createUser" :getUser="getUser" />
    <Homepage 
      :createUser="createUser" 
      :getUser="getUser" 
      :getVehicles="getVehicles" 
      :createVehicle="createVehicle" 
      :changeOwnership="changeOwnership" 
      :getPracticeQuestions="getPracticeQuestions" 
      v-if="alwaysFalse()"></Homepage> -->
    <Register :createUser="createUser" :getUser="getUser" v-if="!isRegistered()" />
    <Homepage 
      :createUser="createUser" 
      :getUser="getUser" 
      :getVehicles="getVehicles" 
      :createVehicle="createVehicle" 
      :changeOwnership="changeOwnership" 
      :getPracticeQuestions="getPracticeQuestions" 
      :upgraderealid="upgraderealid"
      v-if="isRegistered()"></Homepage>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import { default as Web3 } from 'web3';
import user_artifact from "../build/contracts/Users.json"
import vehicle_artifact from "../build/contracts/Vehicles.json"
import practice_questions_artifact from "../build/contracts/PracticeQuestions.json"
import { default as contract } from '@truffle/contract'
import Register from './components/Register.vue';
import Homepage from './components/Homepage.vue';

let Users = contract(user_artifact);
let Vehicles = contract(vehicle_artifact);
let PracticeQuestions = contract(practice_questions_artifact);
// let web3 = new Web3(new Web3.providers.HttpProvider('http://127.0.0.1:8545'));
const web3 = new Web3(new Web3.providers.HttpProvider("http://0.0.0.0:8545"));
// const web3 = new Web3(new Web3.providers.HttpProvider("http://127.0.0.1:8545"));
Users.setProvider(web3.currentProvider);
Vehicles.setProvider(web3.currentProvider);
PracticeQuestions.setProvider(web3.currentProvider);


export default {
  name: 'App',
  components: {
    Register,
    Homepage,
  },
  data() {
    return {
      firstName: null,
      lastName: null
    }
  },
  created: function(){
    console.log("before init")
    this.onInit();
    console.log("after init")

  },
  mounted: async function(){
    console.log("befoere mount")
    // await this.deactivateUser();
    this.getUser().then((data) => {
      localStorage.setItem("user", data);
    })
    console.log("after mount")

  },
  methods: {
    alwaysFalse: function(){
      return false;
    },

    isRegistered: function(){

      if(localStorage.getItem("user") && localStorage.getItem("user").split(",").length > 5){
        console.log(localStorage.getItem("user").split(",")[5], "done") 
        return localStorage.getItem("user").split(",")[5] == "true";
      }
      return false;
    },

    getUser: async function() {
        // console.log("hereeeeeeee");
        let users = await Users.deployed()
        
        let data = await users.checkUser({from: localStorage.getItem("realId")})
        console.log(data);
        return data;
    },

    onInit: async function(){
      await window.ethereum.enable();

      // web3.eth.getAccounts(function (error, accounts) {
      //   console.log("starting address", accounts[0]);
      //   localStorage.setItem("realId", accounts[0]);
      // });

      async function getAccount() {
        const accounts = await window.ethereum.enable();
        const account = accounts[0];
        // console.log(account)
        localStorage.setItem("realId", account);
        // console.log(localStorage.getItem("realId"))
        // do something with new account here'
      }

      getAccount();

      let instance = this;

      // Acccounts now exposed
      window.ethereum.on('accountsChanged', function () {
        // web3.eth.getAccounts(function (error, accounts) {
        //   localStorage.setItem("realId", accounts[0])
        //   console.log(accounts[0], 'current account after account change');
        //   console.log(accounts, ' full accounts');
        // });
        getAccount().then(function() {
              instance.getUser().then((data) => {
                localStorage.setItem("user", data);
                window.location.reload();
              })
        });
      });
    },

    createUser: async function(fname, lname, dob, addr, pw) {
        // web3.eth.getAccounts(function (error, accounts) {
        //   localStorage.setItem("realId", accounts[0])
        //   console.log(accounts[0], 'current account after account change');
        //   console.log(accounts, ' full accounts');
        // });

        let users_contract = await Users.deployed()

        console.log(users_contract)
        console.log(fname, lname, dob, addr, pw);
        console.log(localStorage.getItem("realId"))

        const realid = localStorage.getItem("realId")
        let data = await users_contract.createUser(fname, lname, realid ,dob, addr, pw, {from: realid});
        console.log("here");
        console.log(data);
        return data;
    },

    upgraderealid: async function () {
        let users_contract = await Users.deployed()
        users_contract.upgradeToRealID({from: localStorage.getItem("realId")});
    },

    deactivateUser: async function () {
        let users_contract = await Users.deployed()
        users_contract.deactiveUser({from: localStorage.getItem("realId")});
    },

    getVehicles: async function () {
        console.log("getVehicles")
        let vehicles = await Vehicles.deployed()
        console.log("cintract")
        let data = await vehicles.getVehicles({from: localStorage.getItem("realId")});
        console.log(data[0])
        return data.filter((item) => item[5]);
    },
    
    createVehicle: async function (vin, make, model, location) {
        let vehicles = await Vehicles.deployed();
        console.log("getItem");
        console.log(localStorage.getItem("realId"));
        let r, l, a, p;
        r=x=>~~(Math.random()*x)+'';l=()=>[...'ABCDEFGHIJKLMNOPQRSTUVWXYZ'][r(26)];a=[];while(a.length<1)p=r(10)+r(10)+r(10)+'-'+l()+l()+l(),!/ASS|666|69|KKK|SHT/.test(p)&&a.indexOf(p)<0&&a.push(p);
        console.log(r, l);
        let licenseNumber = a[0];
        let data = await vehicles.createVehicle(vin, make, model, location, licenseNumber, {from: localStorage.getItem("realId")});
        console.log(data)
        return data;
    },

    changeOwnership: async function(vin, to) {
      let vehicles = await Vehicles.deployed();
      console.log(vin, to); 
      let r, l, a, p;
      r=x=>~~(Math.random()*x)+'';l=()=>[...'ABCDEFGHIJKLMNOPQRSTUVWXYZ'][r(26)];a=[];while(a.length<1)p=r(10)+r(10)+r(10)+'-'+l()+l()+l(),!/ASS|666|69|KKK|SHT/.test(p)&&a.indexOf(p)<0&&a.push(p);
      console.log(r, l);
      let licenseNumber = a[0];
      vehicles.changeOwnership(vin, to, licenseNumber, {from: localStorage.getItem("realId")}).then(() => window.location.reload());
    },

    getPracticeQuestions: async function() {
      let practice_questions = await PracticeQuestions.deployed();
      let data = [];
      let randomInt;
      for(let i = 0; i < 2; ++i){
        randomInt = i;
        data.push(await practice_questions.getRandomQuestion(randomInt))
      }
      // let data = await practice_questions.getRandomQuestion();
      // console.log(data);
      return data;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
