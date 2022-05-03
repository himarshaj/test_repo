pragma solidity 0.8.3;

// SPDX-License-Identifier: MIT

import "./lib/StringUtils.sol";


contract Users {

    struct User {
        string firstName;
        string lastName;
        address realId;
        string birthDate;
        string addr;
        bool isActive;
        bool isValid;
        bool isRealID;
        string password;
    }

    mapping(address => User) public users;

    event UserLoggedIn(string firstName, string lastName);
    event UserLoggedOut(string username);
    event UserDeactivated(string firstName, string lastName, bool isActive);
    event UserCreated(string firstName, string lastName, string birthDate, string addr);
    event UserLastNameBroadcasted(string lastName);
    event UserRetrieved(string firstName,string lastName,address realId,
                        string birthDate,string addr,bool isActive,bool isValid,bool isRealID);
    event UserUpgradedToRealID(string firstName, string lastName, bool isRealID);

    // constructor() {
    //     users[msg.sender] = User("Gavindya","Jayawardena", msg.sender, 12121994, "1049 W norfolk", true, true);
    // }

    function createUser(
        string memory firstName, 
        string memory lastName, 
        address realID,
        string memory birthDate,
        string memory addr,
        string memory password
    ) public returns(User memory) {
        
        users[msg.sender] = User(
            // firstName, lastName, msg.sender, birthDate, addr, true, true, false, password
            firstName, lastName, realID, birthDate, addr, true, true, false, password
        );

        emit UserCreated(firstName, lastName, birthDate, addr);

        return users[msg.sender];
    }

    function checkUser() public view returns(User memory) {
        return users[msg.sender];
    }

    function deactivateUser() public {
        User memory user = users[msg.sender];
        if (user.isValid) {
            user.isActive = false;
            users[msg.sender] = user;
            emit UserDeactivated(user.firstName, user.lastName, user.isActive);
        }
    }

    function getUserInfo() public returns (string memory) {
        User memory user = users[msg.sender];
        if (user.isValid) {
            emit UserRetrieved(user.firstName, user.lastName, user.realId, 
                                user.birthDate, user.addr, user.isActive, user.isValid,user.isRealID);
            return user.lastName;
        }
        return "User not found"; 
    }

    function logIn(string memory pw) public returns (string memory) {
        User memory user = users[msg.sender];
        if (user.isValid) {
            if (StringUtils.equal(pw,user.password)){
                emit UserLoggedIn(user.firstName, user.lastName);
                return "Successfully Logged In";
            }
            return "Incorrect Password. Please Try again!";
        }
        else{
            return "Account Does not Exist. Please Create an Account.";
        }
    }

    function upgradeToRealID() public returns (string memory) {
        User memory user = users[msg.sender];
        if (user.isValid) {
            user.isRealID = true;
            users[msg.sender] = user;
            emit UserUpgradedToRealID(user.firstName, user.lastName, user.isRealID);
            return "Upgraded to Real ID";
        }
        return "User not found"; 
    }

}