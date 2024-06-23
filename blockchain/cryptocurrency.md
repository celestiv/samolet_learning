# How does a cryptocurrency emission go?

Usual digital money has a physical equivalent, while the cryptocurrency is completely virtual. In fact, it is a digital asset protected by cryptography — complex math functions and formulas.

Cryptocurrency can be an alternative means of payment, or the basis for a separate product, it also can be issued in the form of tokens (more about it in the next lesson), and it can even be the basis of financial pyramids. There can be infinitely many reasons, but all of them start with an emission. Emission means the issue of cash or non-cash money into circulation. Cryptocurrencies refer to the second category.

## There are several types of cryptocurrency emission:

- Limited emission with a simultaneous issue of coins (without the possibility of mining) — coins are issued at once. It is impossible to get additional coins in the future. Holders get profit from exchange rate changes.

- Limited emission (with the possibility of mining) — coins are issued once with a quantitative limit, you can mine until the indicator is reached.

- Unlimited emission (with the possibility of mining)

## Fork
In the cryptocurrency world, a «fork» is a change in the blockchain protocol. Since cryptocurrencies most often operate on decentralized networks, all the participants must follow the same rules and work coordinately to preserve the history of the blockchain. Otherwise, a fork may occur, that means there will be two blockchains and two cryptocurrencies. Оne blockchain will adhere to the old rules, while the other will work according to the new rules. This phenomenon is also called chain branching.

## Transactions
To make a transaction with cryptocurrency, you will need two encryption keys: public and private. Such keys look like a random set of numbers and letters.

The public key can be seen by everyone, it is used to identify the user, like the address to send and receive the assets. Any user can see all the transactions and the balance of the wallet.

The private key is hidden and no one except the owner can see it. The user needs it to access his wallet and sign the transactions. It can be compared to a password. But you have no possibility to recover it in case of losing, so keep it very carefully. A public key is formed from the private key using an eleptic function and one-way SHA-256 algorithm. Therefore, having a private key you can get a public one, but having a public one you cannot get a private one.

Now let's take a step-by-step look at the transaction mechanism

## Cryptography

Content
Let's talk about the most commonly used hashing algorithm to keep the blockchain running. SHA-256 — secure hash algorithm. SHA-256 is a cryptographic hash function that takes random sized input and produces a fixed size (64 characters) output.

> Why SHA-256 is so popular in various blockchains
- High speed: fast hash computation for any input data
- One-way: it is impossible to compute the input data having a hash.
- The presence of an avalanche effect: any minor change in the input data radically changes the hash, without any references to the previous hash
- Collision resistance: it is impossible to get 2 identical hashes from different inputs
- Resistance to attacks: it is impossible to break the algorithm by brute force, or in any other way.

This function is used to create block headers by hashing all the information it contains. At the same time, the block identifier also contains the hash of the previous block. It means that changing one old transaction will entail changes in the headers of all subsequent blocks. So you can`t silently change something in the middle of the chain, this will certainly be visible.

In addition, SHA-256 algorithm participates in the creation of a public key. It also often ensures the mining process. We will talk about this in the next chapters.

