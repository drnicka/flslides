# BANK (Token Vesting & Distribution) – Canonical Deck Template

## Slide 1: Introduction
**What is BANK?**  
- A system for secure, scalable token distribution and vesting.
- Uses Merkle proofs to efficiently manage large distributions.
- Supports flexible release patterns: Airdrop, Resistor, and Linear Vesting.

**Why BANK?**  
- Reduces trust requirements.
- Minimizes on-chain data storage and gas costs.
- Ensures verifiable and fair token access for recipients.

---

## Slide 2: Core Mechanisms
**Merkle Trees**  
- Commit to large distributions with a single root.
- Users prove entitlement with a Merkle proof.
- Scalable and gas-efficient.

**Token Vesting Types**  
1. **Airdrop:** Immediate withdrawal, no waiting.  
2. **Resistor:** User-controlled waiting period, partial upfront payout.  
3. **Linear Vesting:** Predefined schedule, tokens unlock over time.

---

## Slide 3: Airdrop (MerkleDropFactory)
**Mechanism**  
- Founder sets `(address -> amount)` in a Merkle tree.
- Recipients claim tokens in one go, instantly.

**Capabilities**  
- **Founders/Managers:** Add a Merkle tree, deposit tokens.  
- **Recipients:** Provide proof and withdraw all tokens immediately.

**Use Case**  
- Instant community token distribution.

---

## Slide 4: Resistor (MerkleResistor)
**Mechanism**  
- Founder defines min/max vesting periods, initial payouts.
- Recipients choose their vesting duration and initialize.
- Receive partial tokens upfront, the rest after waiting.

**Capabilities**  
- **Founders/Managers:** Configure vesting constraints, load Merkle tree.  
- **Recipients:** Pick vesting length, get partial tokens immediately, full payout later.

**Use Case**  
- Flexible lockups where recipients decide their wait time.

---

## Slide 5: Vesting (MerkleVesting)
**Mechanism**  
- Founder sets start, end, and optional lock period for each allocation.
- Tokens release linearly over time.
- Recipients initialize after start, withdraw at set points.

**Capabilities**  
- **Founders/Managers:** Predefine strict vesting schedules and deposit tokens.  
- **Recipients:** After initialization, withdraw partially or fully as schedule permits.

**Use Case**  
- Long-term alignment of team/investors with strict unlock times.

---

## Slide 6: Contract Structure & Key Functions
- **MerkleDropFactory.sol:** Immediate airdrops.
- **MerkleResistor.sol:** Customized, user-chosen vesting.
- **MerkleVesting.sol:** Linear, time-based token release.
- **MerkleLib.sol:** Efficient proof verification.

**Workflow**  
1. Off-chain: Generate Merkle tree (addresses, amounts, parameters).  
2. On-chain: Add tree + deposit tokens.  
3. Recipients: Call `initialize()` or `withdraw()` using their Merkle proof.

---

## Slide 7: Security & Audits
- Primarily interacts with ERC20 tokens.
- Minimizes external calls to reduce attack surfaces.
- Audited by Code4rena and others.
- Time-based and count-based checks prevent premature or multiple claims.

---

## Slide 8: User Experience & Benefits
**For Founders/Managers:**
- Flexible distribution options.
- Scalable to thousands of recipients.
- Gas-efficient and trust-minimized.

**For Recipients:**
- Simple claiming via Merkle proof.
- Transparency and security ensured by smart contracts.
- Choice and control over vesting timelines (Resistor model).

---

## Slide 9: Example Use Cases
- **Founder/Team Vesting:** Long-term linear schedules.
- **Community Airdrops:** Quick token release to early supporters.
- **Advisors & Partners:** Let them choose vesting duration within constraints.

---

## Slide 10: Summary
**Key Takeaways:**
- BANK provides a flexible, audited, and trustless framework for token distribution and vesting.
- Merkle proofs and modular vesting options enable secure, customizable token release scenarios.
- Recipients and founders both benefit from clarity, efficiency, and reliability.

---
