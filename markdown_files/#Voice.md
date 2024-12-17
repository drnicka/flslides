# Writing the text from the canvas into a markdown file

markdown_content = """
#Voice: A Public Good AI Enabled Governance & Preference Signalling dApp

## Who are Factory Labs?

Factory Labs is a UK-based blockchain and AI research company that creates tools to improve collective intelligence. Our mission is to use blockchain and AI to develop technologies that enhance how people coordinate and collaborate. We focus on human-centered, democratic, and innovative solutions that protect agency and build consensus.

### Factory Labs Team

- **Dr. Nick (CEO, Protocol Leader & Founder)**: Blockchain researcher and developer with expertise in token engineering, DAOs, and governance design. Holds a PhD in experimental physics and has an academic background in learning theory and governance.

- **Matthew (Head of Coordination & CoFounder)**: Experienced entrepreneur with a BSc in Computer Science. Specializes in Decentralized Governance, Coordination, and DAO patterns.

- **Christopher (CTO & CoFounder)**: Crypto innovator with expertise in IoT and deep learning algorithms. Former CTO of Lunyr and BitMesh. Holds MSc and BSc degrees in Mathematics and Computer Science.

## What is #Voice?

#Voice dApp helps the Scroll community find collective agreement through decentralized discussions and secure governance. It combines AI with identity-based voting to gather community input and highlight shared priorities. The platform turns insights into clear action points and fosters meaningful engagement.

## Why #Voice, Why Now?

#Voice captures and synthesizes individual input into collective intelligence. It’s a non-financial tool for discussion and decision-making that bridges the gap between crypto and AI. Key benefits include:

- **Easy Access**: Non-technical users can sign up with email, while crypto users have full control over wallets.
- **Fair Participation**: Identity gating builds secure and sybil-resistant contributions.
- **Better Usability**: Intuitive design and clear outputs make it easier to use than existing tools like Polis.

Factory Labs has successfully tested #Voice in London communities, proving its ability to engage diverse groups effectively.

## Features and Improvements Over Existing Tools

- **Simple Onboarding**: Email login creates wallets automatically. We can build in scroll namespace.
- **Clear Outputs**: Results are actionable and easy to understand.
- **Validated Data**: The data created by Voice is informed by theoretical research methodology. The data is rich contextual and multi-modal and ideal AI training data.

## The Factory Protocol

#Voice is powered by the Factory Protocol, a set of tools for building economic and decision-making systems. FactoryDAO served as a precursor to #Voice.

## Delivery Schedule

### Technical Build (Commence ASAP):

1. **Magic Link Alternative**: Research and integrate alternatives on Scroll.
2. **Scroll Name Service**: Integrate or find equivalent solutions.
3. **AI Integration**: Finalize and test.
4. **Smart Contracts**: Build and deploy #Voice factory smart contracts.
5. **Custom Front Ends**: Design and build new interfaces.
6. **Test Deployment**: Deploy on Scroll Sepolia Testnet (21.02.25).
7. **Focus Group Testing**: Conduct testing and collect feedback.
8. **Improvements**: Address bugs and refine.

### Launch:

1. Deploy on Scroll Mainnet (07.03.25).
2. Conduct final testing and improvements.
3. Showcase at Eth Denver (23.03.25).
4. Roll into DAO-funded event series as detailed in the DAO proposal.

### Maintenance:

- Initial maintenance covered by this budget. Future funding requests will focus on server and maintenance costs.

## Ask

Factory Labs seeks support from the Scroll Foundation to finalize #Voice as a public good. With 70% of development complete, we need additional support to:

1. Finish the roadmap.
2. Provide a fully functional, self-serve tool for the Scroll community.
3. Ensure long-term sustainability with minimal ongoing costs.

### Timeline Feasibility

We propose an 8-week development, testing, and deployment window starting the week of 16th December 2024. Despite the tight timeline, we are prepared to work through the holiday period to meet the deadline.

---

### Feedback Welcome

Please share your thoughts or suggestions to refine this proposal further.
"""

# Saving the markdown content to a file
file_path = "/mnt/data/voice_dapp_proposal.md"
with open(file_path, "w") as file:
    file.write(markdown_content)

file_path
