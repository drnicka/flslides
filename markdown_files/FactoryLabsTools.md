# Overview of Core Components and Mechanisms

This document summarizes the primary components and mechanisms within the Factory Labs DAO infrastructure suite. The suite encompasses **BANK**, **LAUNCH**, **YIELD**, **MINT**, and **INFLUENCE** applications, each addressing distinct lifecycle phases for a DAO’s token economy and governance processes.

## Core Infrastructure Modules

**FactoryDAO** is modular, allowing DAOs to select and assemble components as needed:

1. **BANK** – Secure token vesting and distribution.
2. **LAUNCH** – Controlled token launches via auctions.
3. **YIELD** – Staking pools and yield generation.
4. **MINT** – NFT and SBT issuance with flexible eligibility and pricing.
5. **INFLUENCE** – Off-chain governance (proposals, voting) integrated with IPFS.

---

## BANK: Token Vesting and Distribution

**Purpose:**  
Enables controlled, scalable token vesting. Tokens can be granted and gradually released to recipients such as founders, employees, investors, or community members.

**Key Mechanisms:**
- **Merkle Trees:** Efficient, private distribution lists using Merkle proofs.  
- **Vesting Types:**
  - *Airdrop:* Immediate, one-time token claim.
  - *Resistor Vesting:* User selects vesting duration. They receive a portion upfront and must wait to claim the remainder.
  - *Linear Vesting:* Tokens unlock from a start to end time, with an optional partial withdrawal date.

**Security & Risk:**
- BANK contracts may hold large amounts of tokens long-term.  
- Contracts are audited and minimize attack surfaces.  
- Simple variants (e.g., `TimeVault`) reduce complexity and risk.

---

## LAUNCH: Token Auctions

**Purpose:**  
Manages initial token distributions via auction-style launches, enabling price discovery and equitable allocation.

**Key Mechanisms:**
- **Auction Tranches:** Tokens are sold in batches. Price may start high and decay until the tranche sells out.  
- **Dynamic Pricing:** When a tranche is sold out, the next one forms with new parameters (size, price, decay).  
- **Liquidity Management:** Management can push in or withdraw tokens after the event.

**Security & Risk:**
- Previously audited code.  
- The contract autonomously handles price decay and token distribution.

---

## YIELD: Staking Pools and Rewards

**Purpose:**  
Allows users to stake tokens in pools and earn reward tokens over time.

**Key Mechanisms:**
- **Multiple Pools:** Each pool can have distinct deposit/reward tokens, durations, and rates.  
- **Rewards Calculation & Distribution:** Users claim principal plus accrued rewards upon pool maturity.

**Security & Risk:**
- Pools may hold significant TVL.  
- Contracts audited and designed to handle large inflows and outflows safely.

---

## MINT: Flexible NFT and SBT Issuance

**Purpose:**  
Issues NFTs and SBTs under configurable eligibility and pricing conditions—ideal for governance tokens, community badges, event-based NFTs, or collectible drops.

**Key Mechanisms:**
- **Eligibility Gates:**  
  - *MerkleEligibility:* Whitelisted addresses proven via Merkle proofs.  
  - *AmaluEligibility:* Open eligibility for everyone.
- **Price Gates:**  
  - *FixedPricePassThruGate:* A set cost per NFT.  
  - *DutchAuctionPriceGate:* Price decays over time, buyer pays the current rate.  
  - *AmaluPriceGate:* Zero-cost minting.
- **On-Chain + Off-Chain Integration:** Metadata is on IPFS; eligibility and pricing checked on-chain. Minting triggers on-chain verification before NFT issuance.

**Security & Risk:**
- Primarily short-term token custody.  
- Audited contracts ensure correct handling of eligibility and pricing logic.

---

## INFLUENCE: Off-Chain Governance

**Purpose:**  
Provides an environment for proposal creation, voting, and decision-making off-chain, backed by on-chain verifiability and IPFS immutability.

**Key Mechanisms:**
- **Proposals & Questions:**  
  - *Proposals:* Typically token-weighted or NFT-based voting scenarios.  
  - *Questions:* Can be open-ended, allowing various types of submissions.
- **Voting Strategies:**  
  - *Token Weighted / Quadratic / Binary / Aggregated* strategies to ensure fair and flexible decision-making.  
- **IPFS Integration:** Off-chain data (proposals, votes) are pinned to IPFS for tamper-proof records, reducing gas costs and on-chain storage requirements.

**Security & Risk:**
- Off-chain process, but verified cryptographically.  
- Flexible identity verification through NFTs or ERC20 balances.

---

## Cross-Component Interactions

- **Shared Libraries & Services:**  
  - *MerkleLib:* Used for Merkle proof verifications across BANK and MINT.  
  - *Subscriber Service & Servment:* Backend services to track on-chain events, cache data, and serve state to frontends.
  
- **Ownership & Access Control:**  
  - Roles (e.g., owner, management) allow certain critical parameter changes.  
  - Ensures only authorized entities update merkle roots, price parameters, or vesting schedules.

- **Factory Pattern & Modular Design:**  
  - Core logic contracts are deployed once, with factories creating instances as needed.  
  - Reusable modules (eligibility gates, price gates) ensure flexible configuration without re-deploying entire systems.

---

## Conclusion

The FactoryDAO suite offers a cohesive toolkit for DAOs to manage their token ecosystems and governance frameworks. By integrating audited, modular components—from vesting (BANK) and launch (LAUNCH), through yield (YIELD), minting (MINT), and governance (INFLUENCE)—DAOs can streamline their operational workflows while maintaining security, scalability, and flexibility.
