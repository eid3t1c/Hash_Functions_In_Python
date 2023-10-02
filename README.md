
# Hash Functions and Hash Tables

A hash function is a mathematical function that can take any amount of data and convert it into a fixed-size result. This result is commonly referred to as a hash value, hash code, or simply a hash. These hash values serve the purpose of organizing data within a fixed-size structure known as a hash table. The entire process of employing a hash function alongside a hash table is known as hashing or scatter storage addressing.

# Properties of a Hash Function

1. **One-Way Function**:
   - A one-way function is a property of a hash function where it is computationally infeasible to reverse the process and retrieve the original input from its hash value. This property ensures that hash functions are used to protect sensitive data like passwords.
   - given  y ∈ Y its impossible to find such x ∈ X such that h(x) = y

2. **Strong Collision Resistance**:
   - Strong collision resistance means that it is highly improbable for two different inputs to produce the same hash value (collision). In other words, it should be computationally infeasible to find two distinct inputs that result in an identical hash. This property       is crucial for ensuring data integrity and security in various applications, including digital signatures and cryptographic protocols.
   - given x ∈ X it is computationally infeasible to find a value x’ such that x’ ≠ x ∈ 𝑋,  h(x’) = h(x)
3. **Weak Collision Resistance (Second Preimage Resistance)**:
   - Weak collision resistance, also known as second preimage resistance, ensures that given a specific input and its hash value, it is computationally challenging to find a different input that produces the same hash value. In simpler terms, if you have an original         piece of data and its hash, it should be difficult to find another piece of data that hashes to the same value. This property is essential for protecting against malicious tampering with data.
   - it is computationally infeasible to find two distinct values x’ ≠ x ∈ 𝑋, such that  h(x’) = h(x)

## Broken Hash Functions

Some hash functions are considered "broken" or insecure due to vulnerabilities that make them unsuitable for cryptographic purposes. Here are a few examples:


1. **MD4 (Message Digest 4)**:
   - MD4 is an older hash function that is considered broken due to various vulnerabilities, including collision attacks. It is not suitable for cryptographic applications and should be avoided.

2. **MD5 (Message Digest 5)**:
   - MD5 was widely used in the past, but it is now considered broken because researchers have found collision vulnerabilities. In other words, it is possible to find two different inputs that produce the same MD5 hash.

3. **SHA-1 (Secure Hash Algorithm 1)**:
   - SHA-1 was once considered secure but is now deprecated for cryptographic use due to collision vulnerabilities. Attacks on SHA-1 have been demonstrated, making it insecure for critical security applications.

## Secure Hash Functions

1. **SHA-256 (Secure Hash Algorithm 256-bit)**:
   - SHA-256 is part of the SHA-2 family and is widely considered secure for cryptographic purposes. It produces a 256-bit hash value and is used in various security applications, including digital signatures and certificate authorities.

2. **SHA-3 (Secure Hash Algorithm 3)**:
   - SHA-3 is the latest member of the Secure Hash Algorithm family and offers strong security guarantees. It was designed as a response to potential vulnerabilities in SHA-2, making it a reliable choice for cryptographic applications.

# Attacks on Hash Functions

Hash functions are fundamental tools in computer science and cryptography for ensuring data integrity and security. However, they are not immune to attacks, and various vulnerabilities have been identified over time. Understanding these attacks is essential for selecting appropriate hash functions and employing best practices to protect your data.

**Collision Attack**: In a collision attack, attackers aim to find two different inputs that produce the same hash value. This undermines the integrity of the hash function as it should be exceedingly difficult to find such collisions.

**Preimage Attack**: In a preimage attack, attackers attempt to find an input that matches a given hash value. 

**Second Preimage Attack**: Also known as weak collision resistance, this attack involves finding a second input that produces the same hash value as a given input.

**Length Extension Attack**: Length extension attacks exploit hash functions susceptible to extending the hash of a known message without knowing the original data, potentially leading to unauthorized data manipulation.

**Birthday Attack**: The birthday attack is a statistical phenomenon where the probability of two different inputs producing the same hash becomes surprisingly high as the number of inputs increases.

**Rainbow Table Attack**: Rainbow table attacks involve the use of precomputed tables of hash values (rainbow tables) to quickly recover the original input corresponding to a hash value. This attack exploits weaknesses in hash functions and can compromise password security.
