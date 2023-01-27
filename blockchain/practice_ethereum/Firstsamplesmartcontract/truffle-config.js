module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 8545,  
      gas: 5000000,
      network_id: "*"
    },
 
    test: {
      host: "127.0.0.1",
      port: 7545,
      gas: 5000000,
      network_id: "*"
    }
   
  }
};
