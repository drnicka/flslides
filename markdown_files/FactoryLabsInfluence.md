# INFLUENCE (Off-Chain Governance) – Canonical Deck Template

## Slide 1: Introduction
**What is INFLUENCE?**  
- An off-chain governance and decision-making framework that complements on-chain token ownership.
- Allows creating proposals, asking questions, and conducting votes without incurring on-chain gas costs for every action.
- Integrates with IPFS for immutable records of governance data.

**Why INFLUENCE?**  
- Reduces overhead and friction for voting and deliberation.
- Supports multiple voting strategies (token-weighted, NFT-based, binary, quadratic).
- Ensures verifiability and trustlessness while keeping user costs low.

---

## Slide 2: Core Mechanisms
**Off-Chain Proposals and Questions:**  
- Proposals define a scenario or decision that needs voting.
- Questions allow flexible input formats—open-ended responses, multiple-choice answers, or media submissions.

**IPFS Integration:**  
- All proposals, questions, and submissions are pinned to IPFS.
- Ensures data immutability and verifiable historical records.
- Decouples data storage from the blockchain, reducing costs.

---

## Slide 3: Voting Strategies
1. **Token Weighted Quadratic Voting (ERC20):**  
   - Distributes voting power across multiple choices with a quadratic cost function.
   - Token balance multiplied by a strategy factor determines vote power.

2. **Token Weighted Binary Voting (ERC20):**  
   - Single-choice yes/no votes.
   - Vote weight proportional to token holdings.

3. **Quadratic Voting (ERC721):**  
   - Assigns vote power per NFT ID, enabling complex weighting per token.
   - Useful for non-fungible governance rights.

4. **Binary Voting (ERC721):**  
   - Single-choice (yes/no) voting using NFT-based vote power.

5. **Aggregated Quadratic & Binary (ERC721):**  
   - Aggregates multiple NFT IDs held by a user.
   - Assigns vote power based on the total number of NFTs owned, applying quadratic or binary logic accordingly.

**Outcome:**  
- Tailor governance to the DAO’s tokens and fairness preferences.

---

## Slide 4: Question Types
**Text-Only:**  
- Collects written opinions, suggestions, or feedback.

**Media-Only (YouTube, Twitter, Vimeo, TikTok, Images):**  
- Gathers multimedia content as submissions, facilitating rich community interactions.

**Mixed Submissions:**  
- Accepts both text and media, providing maximum flexibility in member responses.

---

## Slide 5: Off-Chain and On-Chain Interaction
**Off-Chain Execution:**  
- Creating proposals, posting responses, and conducting votes do not require on-chain transactions.
- Minimizes gas costs and onboarding friction.

**On-Chain Verification:**  
- User identity confirmed via wallet signatures (no gas).
- Votes can be verified against on-chain balances (ERC20 or ERC721) at a snapshot block.
- IPFS records ensure tamper-proof evidence of all votes and content.

---

## Slide 6: Architecture
**Frontend:**  
- Users connect wallets, explore proposals, and cast votes or submit answers.
- No on-chain call needed for each action—just cryptographic signatures for proof of identity.

**Backend (Influence-Hub):**  
- Stores proposals, questions, and submissions.
- Manages IPFS pinning, caching, and event subscriber services for quick data retrieval.

**Chain Scripts & Subscriber Services:**  
- Continuously sync on-chain events (like token transfers) to update voting power contexts.
- Serve data to frontends and backends promptly, ensuring accurate snapshots at voting time.

---

## Slide 7: Security & Verifiability
- **Cryptographic Integrity:** Signatures ensure only authorized addresses can submit votes or proposals.
- **Immutable Records via IPFS:** Ensures no proposal or vote tampering.
- **Voting Strategy Contracts:** Off-chain queries confirm token/NFT balances at specific blocks to validate voting power.

**Result:**  
- Trust-minimized governance without mandatory on-chain overhead.

---

## Slide 8: User Experience & Benefits
**For DAO Administrators:**
- Easily create realms (governance spaces), proposals, and questions.
- Flexible voting strategies allow experimentation with new governance models.
- Low friction: members vote and deliberate without constant on-chain fees.

**For DAO Members:**
- Submit votes or answers with a simple wallet signature.
- Access rich media submissions and proposal data in one interface.
- Transparent processes with verifiable outcomes stored permanently off-chain.

---

## Slide 9: Example Use Cases
- **Protocol Parameter Adjustments:** Token-weighted binary votes to decide on fee changes.
- **Community Brainstorms:** Open-ended questions for soliciting text and media feedback.
- **Art Contests or Grants Allocation:** Quadratic voting ensures fairer distribution of influence across multiple choices.

---

## Slide 10: Summary
**Key Takeaways:**
- INFLUENCE provides an off-chain, gas-free governance solution, backed by on-chain verifiability.
- Multiple voting strategies and question formats enable DAOs to evolve unique governance patterns.
- IPFS and cryptographic signatures ensure trustless, immutable, and inclusive decision-making.

---
