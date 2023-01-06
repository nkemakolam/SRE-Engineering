// SPDX-License-Identifier: UNLICENSED
pragma solidity ^ 0.8.0;

contract HelloWorld{
    uint public value;
    function setValue(uint newValue) public {
        value = newValue;
    }
    function remove() public {
        selfdestruct(payable(address(0x0)));
    }
} 

