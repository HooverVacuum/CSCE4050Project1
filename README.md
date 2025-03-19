Code Signing with ECDSA - Project This project demonstrates the process of code signing and validation using the ECDSA (Elliptic Curve Digital Signature Algorithm). The project includes the signing of a product with a private key and validating the signature using a public key. The main purpose is to ensure the integrity of software by verifying that it hasn’t been tampered with.
1.	Table of Contents
2.	Environment Setup
3.	Dependencies
4.	Installing Dependencies
5.	Running the Project
6.	Code Signing Process
7.	Validation Process
•	Environment Setup This project is designed to run in a Python environment. The instructions below will help you set up the environment and install all necessary libraries.

•	Requirements: Python 3.6+: Make sure you have Python 3.6 or higher installed on your system. You can check your Python version by running: python --version Operating System: This project can be run on any operating system that supports Python (Linux, macOS, Windows). The steps in the README are compatible with all platforms.

•	Dependencies This project requires the following Python libraries: ecdsa: For generating and verifying ECDSA signatures. pycryptodome: A Python library for cryptographic operations. (Used for handling cryptographic operations related to signature verification.) Libraries Needed: ecdsa pycryptodome

•	Installing Dependencies Step 1: Create a Virtual Environment (Optional but Recommended) To avoid conflicts with other projects, it's best to use a virtual environment. You can set it up by following these steps: Install virtualenv if you don’t have it: pip install virtualenv Create a virtual environment: virtualenv venv Activate the virtual environment: On Windows: venv\Scripts\activate On macOS/Linux: source venv/bin/activate Step 2: Install Required Libraries Once the virtual environment is active, install the necessary dependencies by running the following command: pip install ecdsa pycryptodome This will install both ecdsa (used for signing and verifying digital signatures) and pycryptodome (used for cryptographic operations).

•	Running the Project Step 1: Clone the Repository Clone the project repository to your local machine using git: git clone https://github.com/HooverVacuum/CSCE4050Project1.git cd ecdsa-code-signing Step 2: Run the Code The project consists of three main functions:
Key Generation: Generates a public/private key pair for signing and verifying. 
Signing the Product: Signs a product (software) with the private key. 
Validating the Product: Verifies the product's signature using the public key. You can run the main script main.py to go through the signing and validation process: python main.py
•	Expected Output When you run the project, you should see output similar to the following: Keys generated and saved to private_key.pem and public_key.pem Product signed and signature saved to product_signature.sig Code certificate valid: execution allowed
If the signature is tampered with, the output will be: Code certificate invalid: execution denied

•	Simulating an attack: TO simulate a simple attack like the one in the demo put this line of code int line 69: 

with open("product_signature.sig", "wb") as sig_file:
  sig_file.write(b"corruptedsignaturedata")

•	Code Signing Process Key Generation The private key is used to sign the product. It is stored in the private_key.pem file. The public key is used to verify the signature and is stored in the public_key.pem file. It is shared with users. Signing the Product The product is a simple message that includes the student ID:
product_content = "I am a software made by {11312063}"
The product is then signed using the private key, and the signature is saved in the product_signature.sig file.

•	Validating the Product The product can be validated using the public key and the signature file. The code verifies if the signature matches the product content and prints whether the product is valid or invalid.
