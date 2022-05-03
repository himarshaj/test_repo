pragma solidity 0.8.3;

// SPDX-License-Identifier: MIT

import "./lib/StringUtils.sol";


contract Vehicles {

    struct VehicleData {
        string vin;
        string make;
        string model;
        string location;
        string licenseNumber;
        bool isActive;
        uint RegExpdate;
    }

    mapping(address => VehicleData[]) public vehicles;

    function createVehicle(
        string memory vin, 
        string memory make,
        string memory model,
        string memory location,
        string memory licenseNumber

    ) public returns(VehicleData[] memory) {        
        uint RegExpdate = block.timestamp + 365 days;
        vehicles[msg.sender].push(
            VehicleData(vin, make, model, location, licenseNumber, true, RegExpdate));
        return vehicles[msg.sender];
    }

    function getVehicles() public view returns(VehicleData[] memory) {
        return vehicles[msg.sender];
    }

    function changeOwnership(string memory vin, address to, string memory licenseNumber) public {
        // VehicleData memory vdata;
        uint RegExpdate = block.timestamp + 365 days;
        for (uint i = 0; i < vehicles[msg.sender].length; i++) {
            if (StringUtils.compare(vehicles[msg.sender][i].vin, vin) == 0) {
                vehicles[msg.sender][i].isActive = false;
                // deleteVehicle(vin);
                vehicles[to].push(
                    VehicleData(
                        vin, vehicles[msg.sender][i].make, vehicles[msg.sender][i].model, vehicles[msg.sender][i].location, licenseNumber, true, RegExpdate
                    )
                );
                break;
            }
        }
    }

    function deleteVehicle(string memory vin) public {
        VehicleData[] memory vehicleData = new VehicleData[](vehicles[msg.sender].length - 1);
        uint j = 0;
        for (uint i = 0; i < vehicles[msg.sender].length; i++) {
            if (StringUtils.compare(vehicles[msg.sender][i].vin, vin) != 0) {
                vehicleData[j] = vehicles[msg.sender][i];
                j += 1;
            }
        }
        delete vehicles[msg.sender];
        for (uint k = 0; k < vehicleData.length; ++k) {
            vehicles[msg.sender].push(vehicleData[k]);
        }
        // vehicles[msg.sender] = vehicleData;
    }

    function deactivateVehicle(string memory vin) public {
        VehicleData[] memory vehicleData = vehicles[msg.sender];
        VehicleData memory vData;
        for (uint i = 0; i < vehicleData.length; i++) {
            if (StringUtils.compare(vehicles[msg.sender][i].vin, vin) == 0) {
                vData = vehicles[msg.sender][i];
                vData.isActive = false;
                vehicles[msg.sender][i] = vData;
            }
        }
    }


}