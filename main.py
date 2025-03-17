from ecdsa import NIST256p, SigningKey, VerifyingKey
import hashlib

# Step 1: Generate the private/public key pair
def generate_keys():
    # Generate private key (secret key)
    private_key = SigningKey.generate(curve=NIST256p)
    # Derive the corresponding public key
    public_key = private_key.get_verifying_key()

    # Save the keys to files
    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(private_key.to_pem())

    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(public_key.to_pem())

    print("Keys generated and saved to private_key.pem and public_key.pem")

# Step 2: Sign the product 
def sign_product(product_content):
    # Load private key
    with open("private_key.pem", "rb") as priv_file:
        private_key = SigningKey.from_pem(priv_file.read())

    # Hash the product content
    product_hash = hashlib.sha256(product_content.encode()).digest()

    # Sign the hash of the content
    signature = private_key.sign(product_hash)

    # Save the signature to a file
    with open("product_signature.sig", "wb") as sig_file:
        sig_file.write(signature)

    print("Product signed and signature saved to product_signature.sig")

# Step 3: Validate the product using the public key
def validate_product(product_content):
    # Load public key
    with open("public_key.pem", "rb") as pub_file:
        public_key = VerifyingKey.from_pem(pub_file.read())

    # Read the product's signature
    with open("product_signature.sig", "rb") as sig_file:
        signature = sig_file.read()

    # Hash the product content
    product_hash = hashlib.sha256(product_content.encode()).digest()

    # Verify the signature
    try:
        public_key.verify(signature, product_hash)
        print("Code certificate valid: execution allowed")
    except:
        print("Code certificate invalid: execution denied")

# Step 4: Main execution
def main():
    student_id = "11312063"  
    product_content = f"I am a software made by {student_id}"

    print("\n--- Product Output ---")
    print(product_content)

    generate_keys()
    sign_product(product_content)
    validate_product(product_content)

if __name__ == "__main__":
    main()