pragma solidity 0.8.3;

// SPDX-License-Identifier: MIT

import "./lib/StringUtils.sol";


contract PracticeQuestions {

    struct QuestionData {
        string question;
        string[] options;
        uint answerNumber;
        bool isActive;
    }

    struct ResponseData {
        address questionAddr;
        uint chosenAnswerNumber;
        bool isActive;
    }

    function getUniqueId() public view returns (address) {
        // bytes20 b = bytes20(keccak256(abi.encodePacked(msg.sender, block.timestamp)));
        // uint addr = 0;
        // for (uint index = b.length-1; index+1 > 0; index--) {
        //     addr += uint(uint8(b[index])) * (16 ** ((b.length - index - 1) * 2));
        // }
        // return address(addr);
        return address(bytes20(sha256(abi.encodePacked(msg.sender, block.timestamp))));

    }

    function random() public view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty)));
    }

    mapping(address => QuestionData) public questionLookup;
    address[] public questionAddrs;

    function addQuestion(
        string memory question,
        string[] memory options,
        uint answerNumber
    ) public {
        address qAddr = getUniqueId();
        questionAddrs.push(qAddr);
        questionLookup[qAddr] = QuestionData(question, options, answerNumber, true);
    }

    function getRandomQuestion(uint randomInt) public view returns(address, string  memory, string[] memory, uint) {
        // uint randomInt = uint256(keccak256(abi.encodePacked(now, block.difficulty)));
        address qaddr = questionAddrs[randomInt];
        QuestionData memory qdata = questionLookup[qaddr];
        return (qaddr, qdata.question, qdata.options, qdata.answerNumber);
    }


}