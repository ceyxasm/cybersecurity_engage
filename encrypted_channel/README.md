As discussed in solution architecture, we need to enforce the encryption of sensitive data. Below is the code to set up an encrypted channel using AES encryption.
* Use of 16 bit key
* Data transmitted should be multiple of 16 bits and therefore must be padded appropriately.
* Initialization vectors used are randomly generated
* For larger messages, Cipher Block Chaining Mode of AES is utilized. 