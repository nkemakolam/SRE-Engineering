pragma solidity ^0.4.24;
 contract CrowdFundingWithDeadline{
     enum State { Ongoing, Failed,Succeed,PaidOut }
     string public  name;
     uint public targetAmount;
     uint fundingDeadline;
     address public beneficiary;
     State public state;
     mapping(address => uint) public amounts;
     bool public collected;
     uint public totalCollected;

     modifier inState(State expectedState){
         require(state == expectedState, "Invalid State");
         _;
     }

     constructor (
         string contractName,
         uint targetAmountEth,
         uint durtionInMin,
         address beneficiaryAddress
     )
     public 
     {
        name = contractName; 
        targetAmount = targetAmountEth * 1 ether;
        fundingDeadline = currentTime() + durtionInMin * 1 minutes;
        beneficiary = beneficiaryAddress;
        state = State.Ongoing;
     }
      
      function contribute() public payable inState(State.Ongoing) {
          amounts[msg.sender] += msg.value;
          totalCollected += msg.value;

          if (totalCollected >= targetAmount) {
              collected = true;
          }
      }

     function currentTime() internal view returns(uint){
         return now;
     }
 }