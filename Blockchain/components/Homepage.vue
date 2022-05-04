<template>
<div>

<!--     <b-modal id="changeOwnership" hide-footer >
    <template #modal-title>
      Change Ownership
    </template>
    <div style="text-align:center">
        Selected Vin : {{this.selectedVin}}
        <br /><br />
        Send to : <input type="text" v-model="toAddr" />
        <br />
        <br />
        <b-button class="mt-2 changeOwnershipBtn" variant="outline-success" block @click="toggleModal">Change Ownership</b-button>
    </div>

    </b-modal> -->

    <b-button v-b-toggle.sidebar-no-header class="toggle-sidebar">Menu</b-button>

        <div style="position:absolute; float:right; right:10px; top:20px;">
        Hello {{ getName() }}
    </div>
    <b-sidebar id="sidebar-no-header" aria-labelledby="sidebar-no-header-title" no-header shadow>
      <template #default="{ hide }">
        <div class="p-3">
          <h4 id="sidebar-no-header-title">Menu</h4>
          <p>
              Please choose from the below menu items.
          </p>
          <nav class="mb-3">
            <b-nav vertical>
              <!-- <b-nav-item :active="page == 'table'" @click="(page = 'table') && hide()">Renew License</b-nav-item>
              <b-nav-item :active="page == 'table'" @click="(page = 'table') && hide()">Change Address</b-nav-item> -->
              <b-nav-item :active="page == 'real_id'" @click="(page = 'real_id') && hide()">Obtain RealID</b-nav-item>
              <b-nav-item :active="page == 'table'" @click="(page = 'table') && hide()">My Vehicles</b-nav-item>
              <b-nav-item :active="page == 'add'" @click="(page = 'add') && hide()">Title My Vehicle</b-nav-item>
              <b-nav-item :active="page == 'practice'" @click="(page = 'practice') && hide()">Practice Questions</b-nav-item>
              <b-nav-item :active="page == 'records'" @click="(page = 'records') && hide()">Vital Records</b-nav-item>
              <b-nav-item :active="page == 'sellVehicle'" @click="(page = 'sellVehicle') && hide()">Sell Vehicle</b-nav-item>
              <b-nav-item :active="page == 'renewRegistration'" @click="(page = 'renewRegistration') && hide()">Renew Registration</b-nav-item>
            </b-nav>
          </nav>
          <b-button variant="danger"  @click="hide">Close Sidebar</b-button>
        </div>
      </template>
    </b-sidebar>

    <div v-if="page == 'records'">
    <h2>Vital Records</h2> <br />
    <b-card style="width: 50%; text-align: left; display: inline-block; cursor: pointer" @click="downloadFile">
        Download Birth record
    </b-card>

    </div>

    <div v-if="page == 'real_id'">
    <h2 v-if="page == 'real_id'">Obtain Real ID</h2> <br />
      <b-card style="width: 50%; text-align: left; display: inline-block; cursor: pointer" @click="upgradeID">
        Upgrade Now
      </b-card>

      <!-- <div v-if="real_id_obtained" class="card text-white bg-success mb-3" style="max-width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">You have upgraded your DL to RealID </h5>
        </div>
      </div>
      <div v-if="real_id_obtained_already" class="card text-white bg-secondary mb-3" style="max-width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">You already Obtained RealID </h5>
        </div>
      </div> -->

    </div>


    <div v-if="page == 'practice'">
    <h2 v-if="page == 'practice'">Practice Questions</h2> <br />
        <div v-for="question in questions" :key="question.text">
            <b-card style="width: 50%; text-align: left; display: inline-block">
                {{ question.text }}
                <br />
                <br />

                <div v-for="option in question.options" :key="option">
                    {{ option }}
                </div>
                <br />
            </b-card>
        </div>
    </div>

    <br />

        <div v-if="page == 'sellVehicle'">
    <h2>Sell My Vehicle</h2> <br />

    Please click the vehicle to sell/donate.  <br/><br/>


    <b-table 
        style="width: 80%; left: 10%; position: absolute;" 
        striped hover 
        :items="vehicleData" 
        v-if="page == 'sellVehicle'"

        @row-clicked="function (item, index, event) { sellInfo(item) }"

    >
    </b-table>
    <br /><br /><br />
    <br /><br /><br />
    <br /><br /><br />
    <br /><br /><br />
    <br /><br /><br />
    <div v-if="sold" style="text-align:center">
        Selected Vin : {{this.selectedVin}}
        <br /><br />
<!--         Send to : <input type="text" v-model="toAddr" />
        <br />
        <br /> -->
        <b-button class="mt-2 changeOwnershipBtn" variant="outline-success" block @click="deleteVehicleRecord">Sell Selected Vehicle</b-button>
    </div>

    </div>



<div v-if="page == 'renewRegistration'">
    <h2>Renew My Vehicle</h2> <br />

    Please click the vehicle to renew registration.  <br/><br/>


    <b-table 
        style="width: 80%; left: 10%; position: absolute;" 
        striped hover 
        :items="vehicleData" 
        v-if="page == 'renewRegistration'"

        @row-clicked="function (ritem, rindex, revent) { renewInfo(ritem) }"

    >
    </b-table>
    <br /><br /><br />
    <br /><br /><br />
    <br /><br /><br />
    <br /><br /><br />
    <br /><br /><br />
    <div v-if="renew" style="text-align:center">
        Selected Vin : {{this.selectedVin}}
        <br /><br />
<!--         Send to : <input type="text" v-model="toAddr" />
        <br />
        <br /> -->
        <b-button class="mt-2 changeOwnershipBtn" variant="outline-success" block @click="renewVehicleRecord">Renew Registration</b-button>
    </div>
    </div>



    <div v-if="page == 'table'">
    <h2 >My Vehicles</h2> <br />
    <button v-if="page == 'table'" @click="page = (page == 'sellVehicle')?'table':'sellVehicle'">
        {{ this.page == 'sellVehicle' ? "Close": "Sell Vehicle" }}
    </button>
    <br/>  <br/>
    <button v-if="page == 'table'" @click="page = (page == 'renewRegistration')?'table':'renewRegistration'">
        {{ this.page == 'renewRegistration' ? "Close": "Renew Registration" }}
    </button>

<!--           <b-card style="width: 20%; text-align: center; display: inline-block; cursor: pointer" @click="page == 'sellVehicle'">
        Sell Vehicle
      </b-card>
 -->
    </div>
    <h2 v-if="page == 'add'">Title My Vehicle</h2> <br />

<!--     <button v-if="(page == 'add') || (page == 'table')" @click="page = (page == 'add')?'table':'add'">
        {{ this.page == 'add' ? "Close": "Add Car" }}
    </button> -->

<!--     <br /> -->
    <br />


    <b-table 
        style="width: 80%; left: 10%; position: absolute;" 
        striped hover 
        :items="vehicleData" 
        v-if="page == 'table'"
        >
    </b-table>


    <div v-if="page == 'add'">
        <b-form style="width: 50%; left: 25%; position: absolute;" @submit="registerTitle">
            <b-form-group id="input-group-1" label="Vin :" label-for="input-1">
                <b-form-input
                id="input-1"
                v-model="vin"
                placeholder="Enter VIN"
                required
                ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-2" label="Make :" label-for="input-2">
                <b-form-input
                id="input-2"
                v-model="make"
                placeholder="Enter Make"
                required
                ></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-3" label="Model :" label-for="input-3">
                <b-form-input
                id="input-3"
                v-model="model"
                placeholder="Enter Model"
                required
                ></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-4" label="Location :" label-for="input-4">
                <b-form-input
                id="input-4"
                v-model="location"
                placeholder="Enter Location of registration"
                required
                ></b-form-input>
            </b-form-group>
            <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
    </div>

</div>
</template>

<script>

import { jsPDF } from "jspdf";


export default {
  name: 'Homepage',
  data() { 
    return {
        vehicleData: [],
        vin: null,
        make: null,
        model: null,
        location: null,
        RegExpdate: null,
        page: "table",
        selectedVin: "",
        toAddr: "",
        questions: [{
            text: 'Loading...',
            options: [] 
        }],
        sold: false,
        renew: false,
    }
  },
  props: {
    createUser: {type: Function},
    getUser: {type: Function},
    getVehicles: {type: Function},
    createVehicle: {type: Function},
    changeOwnership: {type: Function},
    getPracticeQuestions: {type: Function},
    upgraderealid: {type: Function},
    renewVehicle:{type: Function},
    deleteVehicle:{type: Function}
  },

  mounted: async function() {
    //   let data = await this.getVehicles({from: localStorage.getItem("realId")});
    //   let ndata = [];
    //   for(let i = 0; i < data.length; ++i){
    //       ndata.push({
    //           "Vin": data[i][0],
    //           "Make": data[i][1],
    //           "Model": data[i][2]
    //       })
    //   }
    //   this.vehicleData = ndata;
    this.fetchVehicleData();
    this.fetchPracticeQuestions();
  },
  methods: {

    upgradeID: async function() {

      console.log(localStorage.getItem("realId"));
      let userdata = await this.getUser();
      // userdataafter[7] is the boolean value for RealID
      if(!userdata[7]){
        await this.upgraderealid({from: localStorage.getItem("realId")});
        console.log("You have successfully obtained Real ID");
        // real_id_obtained=true;
      }
      else{
        console.log("You already have obtained Real ID");
        // real_id_obtained_already=true;
      }
      
    },

    downloadFile: function() {
        const doc = new jsPDF();
        doc.text("Birth record for " + this.getName(), 10, 10);
        doc.text("Record details", 10, 20);

        doc.save("BirthRecord.pdf");
    },
    isTable: function() {
        return this.page == 'table';
    },
    log: console.log,
    // showModal: function(item) {
    //     this.selectedVin = item.Vin;
    //     this.$bvModal.show("changeOwnership");
    // },

    sellInfo: function(item) {
        this.selectedVin = item.Vin;
        this.sold = true;
        // console.log(item)
    },

    deleteVehicleRecord: function() {
        console.log("Delete Vehicle")
        console.log(this.selectedVin)
        this.deleteVehicle(this.selectedVin)
        // this.changeOwnership(this.selectedVin, this.toAddr);
        // this.$bvModal.hide("changeOwnership");
    },

    renewInfo: function(ritem) {
        this.selectedVin = ritem.Vin;
        this.renew = true;
        // console.log(item)
    },
    renewVehicleRecord: function() {
        console.log("renewVehicleRecord")
        console.log(this.selectedVin)
        this.renewVehicle(this.selectedVin)
        // this.changeOwnership(this.selectedVin, this.toAddr);
        // this.$bvModal.hide("changeOwnership");
    },

    fetchVehicleData: async function() {
      // console.log("Here")
      let data = await this.getVehicles({from: localStorage.getItem("realId")});
      let ndata = [];
      for(let i = 0; i < data.length; ++i){
          let expdate = new Date(data[i][6] * 1000);
          ndata.push({
              "Vin": data[i][0],
              "Make": data[i][1],
              "Model": data[i][2],
              "Location": data[i][3],
              "License Plate": data[i][4],
              "Registration Expiry Date": expdate
          })
      }
      this.vehicleData = ndata;
    },
    fetchPracticeQuestions: async function() {
        let data = await this.getPracticeQuestions();
        let ndata = [];
        for(let i = 0; i < data.length; ++i){
            console.log("demo ", data);
            ndata.push({
                text: data[i][1],
                options: data[i][2]
            })
        }
        console.log(ndata);
        this.questions = ndata;
    },
    resetVars: function () {
        this.vin = "";
        this.make = "";
        this.model = "";
        this.location = "";
    },
    registerTitle: function(e){
          e.preventDefault();
          console.log(this.vin, this.make, this.model);
          this.createVehicle(this.vin, this.make, this.model, this.location).
          then(async () => {
            await this.fetchVehicleData();
            this.resetVars();
            this.page = 'table';
        })
    },
    getName: function(){

      if(localStorage.getItem("user") && localStorage.getItem("user").split(",").length > 5){
        console.log(localStorage.getItem("user").split(","), "done") 
        return localStorage.getItem("user").split(",")[0] + " " + localStorage.getItem("user").split(",")[1];
      }
      return "";
    },

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


.toggle-sidebar {
    position: absolute;
    top:20px;
    left: 20px;
}

.active {
  color: white;
  background-color: grey;    
}
.nav-item > a:hover {
  color: black;
}

.changeOwnershipBtn {
    /* position: absolute; */
    width: 50%;
    left: 25%;
    margin-left: auto;
    margin-right: auto;
}

.bcard {
    width: 50%;
    text-align: left;
}

</style>
