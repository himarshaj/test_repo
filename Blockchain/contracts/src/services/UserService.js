// import { default as Web3 } from 'web3';
// import { default as contract } from '@truffle/contract'
// import user_artifact from "../../build/contracts/Users.json"

// let Users = contract(user_artifact);
// let web3 = new Web3(new Web3.providers.HttpProvider('http://127.0.0.1:8545'));

class UserService {
    async getUser(Users) {
        console.log("in getuser")
        let users = await Users.deployed()
        let data = await users.checkUser({from: localStorage.getItem("realId")})
        console.log("done getuser")
        return data;
    }
}

export default new UserService()