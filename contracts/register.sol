//SPDX-License-Identifier: UNLICENSED

// Solidity files have to start with this pragma.
// It will be used by the Solidity compiler to validate its version.
pragma solidity ^0.8.0;

import "hardhat/console.sol";

contract VoterRegistry {
    string public name = "Vote Registry";

    address public owner;

    mapping(address => bool) public eligibleVoters;

    event VoterRegistered(address voter);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyAdmin() {
        require(msg.sender == owner, "Only admin can call this function.");
        _;
    }

    // 檢查是不是合法的投票者
    function isEligible(address voter) public view returns (bool) {
        return eligibleVoters[voter];
    }

    // 註冊投票者
    function registerVoter(address voter) public onlyAdmin {
        eligibleVoters[voter] = true;

        console.log(
            "Register voter",
            voter
        );

        emit VoterRegistered(voter);
    }
}