
# CS 764/864: Blockchains and Cryptocurrencies
## Module 3: Homework 3
### Himarsha Jayanetti, Spring 2022


#### Required Packages

* pycrypto  

  ```pip3 install pycrypto```

* pycryptodome  

  ```pip3 install pycryptodome```   

#### Usage

* Use the following command to run the code. The output will be printed on the screen.  
    
  ```python3 blockchain_implementation.py```


#### Homework Requirements

#### Steps
##### 1. Generating public-key/private-key pairs representing 5 customers
##### 2. Generating public-key/private-key pairs representing 2 merchants
##### 3. Generating the public-key/private-key pair for the single miner

Example key-pair:  
 ``` b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArclZVh8pdzpLswiLIgJb\nE46cTTuACv7aD2CgCaa3uS3hk5Ls0rLVT7sqlLecHBcyKAqeheZ3eyy4s271Yo9F\nPHP/4kiEL6urwWUXkYO2cPxq/2oK6/wTaATjPBBDr8cxjbuI+MYUXv/0c5cGHEjK\nBPAfkl+XYg/gHhmhEcYEF7mlBoelhXRbhZd/qoDROzIXFdKDug8aBYujkrSQYiGa\nBNlIywED0tpbkvC6ORGF42sJPmvfnPihKzt2/Kr4FXDO+DpCAdpdWSXc8i/ely05\n/7IdVqHncmdFmQPYaa2WDzQcixw/o8FnmiBi+sHNk5Cq9SrfzUCSZTgG702Fnble\nhQIDAQAB\n-----END PUBLIC KEY-----' ```   
 
 ``` Private RSA key at 0x7FC802D9D3D0 ```
 
##### 4. Generate 25 random transactions using the above transaction format

Example transaction (only the fields 1-4):  
``` Transaction 1: M2(O7aTE93I/Z/yqdZ8y) C4(RPeH+1O8jq9fTmeQD) 04/04/2017 $87.33 ```

#### Output

The output generated for the following questions is available at blockchain_out.txt.

##### 1. Print the list of transactions (just print fields 1-4 of each transaction)
##### 2. Increment the amount in transaction 15 (in block 15) by $10.00, and show how it can be detected by the customer.
##### 3. By searching through the blockchain, print all transactions for customer 3 (C3)
##### 4. By searching through the blockchain, print all transactions for merchant 2 (M2)


#### References

1. https://pycryptodome.readthedocs.io/en/latest/src/signature/pkcs1_v1_5.html
2. https://stackoverflow.com/questions/59126819/py-error-message-cannot-import-name-pkcs1-15
3. https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531
4. https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/
5. https://www.geeksforgeeks.org/create-simple-blockchain-using-python/
6. https://www.youtube.com/watch?v=zVqczFZr124
