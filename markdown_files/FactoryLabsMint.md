# MINT (NFT & SBT Issuance) – Canonical Deck Template

## Slide 1: Introduction
**What is MINT?**  
- A flexible NFT and SBT (Soulbound Token) issuance framework.
- Defines who can mint (eligibility) and at what price (price gates) in a modular fashion.
- Ideal for governance badges, event attendance tokens, identity tokens, or collectible sales.

**Why MINT?**  
- Highly customizable eligibility and pricing logic.
- On-chain verifiability combined with off-chain metadata on IPFS.
- Streamlined user experience with deterministic access control.

---

## Slide 2: Core Mechanisms
**Eligibility Gates:**  
- Determine which addresses can mint and how many they can claim.
- Can be open (anyone), whitelisted (via Merkle proofs), or governed by other custom conditions.

**Price Gates:**  
- Set the cost of minting (e.g., fixed price, Dutch auction, or free).
- Integrate seamlessly with eligibility gates, allowing flexible monetization or free distribution strategies.

---

## Slide 3: Eligibility Options
1. **MerkleEligibility:**  
   - Uses Merkle proofs to whitelist specific addresses.
   - Enforces per-address and total mint caps.

2. **AmaluEligibility:**  
   - Open eligibility, allowing anyone to mint.
   - Useful for public sales or community giveaways.

**Outcome:**  
- Precisely control who mints and how many tokens they get.

---

## Slide 4: Price Gate Options
1. **FixedPricePassThruGate:**  
   - A static ETH price per token.
   - Excess ETH returned if price changes during confirmation.

2. **DutchAuctionPriceGate:**  
   - Price decays over time from a max to a min.
   - Buyers pay the current price; any overpayment is refunded.

3. **AmaluPriceGate:**  
   - Always returns zero cost.
   - Ideal for free claim events or reward distributions.

**Outcome:**  
- Monetize NFT issuance or offer free mints, seamlessly integrated with eligibility logic.

---

## Slide 5: NFT Contracts and SBTs
**NFT Contracts (e.g. VoterID, VoterSBT):**  
- ERC-721 compatible tokens with optional Soulbound properties (non-transferable).
- Minting occurs through the MerkleIdentity contract after passing eligibility and price checks.
- Metadata stored on IPFS for immutability and verification.

**Soulbound Tokens (SBTs):**  
- Non-transferable identity or governance tokens.
- Ideal for DAO membership badges, POAP-like credentials, or community roles.

---

## Slide 6: The Minting Process
**Workflow:**
1. **Setup:**  
   - Founders configure eligibility gates (e.g., whitelist or open) and price gates (fixed, auction, or free).
   - Deploy/point to the NFT contract and set it as minter on MerkleIdentity.

2. **Adding a Merkle Tree (Optional):**  
   - If using MerkleEligibility, generate and upload a Merkle root for whitelisted addresses.
   - Add the tree to MerkleIdentity with references to the eligibility and price gates, plus the NFT contract and IPFS metadata root.

3. **User Action:**  
   - User calls `withdraw()` function on MerkleIdentity with their Merkle proof and/or payment.
   - Contracts verify eligibility and price, then mint the token.

---

## Slide 7: Integration and Services
**Backend & Frontend:**
- The frontend fetches eligibility data and proofs from a backend service.
- Backend services:
  - Pre-calculate Merkle proofs.
  - Pin metadata on IPFS.
  - Provide token URIs, handle events via subscriber services.

**On-Chain:**
- MerkleIdentity contract orchestrates all logic calls:
  - Checks user eligibility via IEligibility interface.
  - Checks price via IPriceGate interface.
  - Mints token by calling the NFT contract.

---

## Slide 8: Security & Audits
- Contracts rely on simple, audited interfaces.
- Eligibility and price checks performed atomically before mint.
- Dutch auctions and fixed prices ensure fairness and prevent exploitative mints.
- Non-transferable SBTs prevent phishing or scam-based token sales.

---

## Slide 9: User Experience & Benefits
**For Founders/Managers:**
- Complete control over who can mint and how many.
- Dynamic pricing strategies (auctions, fixed price, or free) to suit various campaigns.
- Scalable: Add thousands of addresses to whitelist without massive gas costs.

**For Recipients:**
- Clear conditions for minting (e.g., provide a proof or pay a known price).
- Seamless UI via frontend connected to backend services for proofs and metadata.
- Trustless verification ensures no favoritism or hidden rules.

---

## Slide 10: Example Use Cases
- **POCs (Proof of Contribution):** Issue free SBT badges to contributors using MerkleEligibility + AmaluPriceGate.
- **Limited-Edition Art Drops:** Use DutchAuctionPriceGate for price discovery and MerkleEligibility to ensure fair access.
- **DAO Membership Tokens:** Grant governance tokens at zero cost to all whitelisted DAO members.

---

## Slide 11: Summary
**Key Takeaways:**
- MINT offers a modular, extensible system for NFT/SBT issuance.
- Eligibility and pricing are decoupled, enabling endless configuration possibilities.
- Integrated with IPFS, Merkle proofs, and audited contracts for secure, fair, and transparent distribution experiences.

---
