<section>
  <h1>#VOICE: Onboarding Communities with Semantic Ballot Voting</h1>
  <p>An app for collective decision-making and onboarding to Scroll.</p>
</section>

<section>
  <h2>What is #VOICE?</h2>
  <p>#VOICE is a next-generation governance app that empowers communities to:</p>
  <ul>
    <li>Engage in structured, deliberative decision-making.</li>
    <li>Express nuanced preferences using Semantic Ballot Voting (SBV).</li>
    <li>Seamlessly onboard to Scroll through collective sensemaking.</li>
  </ul>
</section>

<section>
  <h2>Why #VOICE for Scroll?</h2>
  <p>#VOICE solves key challenges in community governance:</p>
  <ul>
    <li>Brings clarity to collective priorities with structured votes.</li>
    <li>Reduces noise by combining quantitative preferences with qualitative reasoning.</li>
    <li>Onboards new communities by aligning incentives and priorities.</li>
  </ul>
</section>

<section>
  <h2>The Decision Space: Semantic Tags</h2>
  <p>In #VOICE, decisions are represented as **semantic tags**.</p>
  <ul>
    <li>Each tag corresponds to a distinct priority or option.</li>
    <li>Participants allocate votes to express preferences across these tags.</li>
  </ul>
  <p>\( T = \{ t_1, t_2, \dots, t_n \} \)</p>
  <ul>
    <li>\( T \): The set of semantic tags.</li>
    <li>\( t_i \): Each individual decision axis or option within the set.</li>
  </ul>
</section>

<section>
  <h2>Participants and Voting Budgets</h2>
  <p>Each participant in #VOICE receives a finite voting budget.</p>
  <ul>
    <li>The budget ensures participants prioritize their preferences.</li>
    <li>Votes are allocated thoughtfully across the decision space.</li>
  </ul>
  <p>\( P = \{ p_1, p_2, \dots, p_m \} \)</p>
  <ul>
    <li>\( P \): The set of participants.</li>
    <li>\( p_j \): A participant who allocates votes across the semantic tags.</li>
  </ul>
</section>

<section>
  <h2>Quadratic Voting: Fair and Balanced</h2>
  <p>#VOICE uses **Quadratic Voting** to prevent vote concentration.</p>
  <ul>
    <li>The cost of voting grows quadratically to discourage over-allocating votes to a single tag.</li>
    <li>This ensures fair influence across community priorities.</li>
  </ul>
  <p>\( \text{Cost}_{j,i} = v_{j,i}^2 \)</p>
  <ul>
    <li>\( \text{Cost}_{j,i} \): The cost for participant \( p_j \) to allocate \( v_{j,i} \) votes to tag \( t_i \).</li>
    <li>\( v_{j,i} \): The number of votes participant \( p_j \) assigns to tag \( t_i \).</li>
  </ul>
</section>

<section>
  <h2>Staying Within Budgets</h2>
  <p>Participants must carefully allocate votes within their voting budget.</p>
  <p>\( \sum_{i=1}^n v_{j,i}^2 \leq B_j \)</p>
  <ul>
    <li>\( B_j \): The total voting budget for participant \( p_j \).</li>
    <li>\( \sum_{i=1}^n v_{j,i}^2 \): The total cost of all votes allocated by \( p_j \).</li>
  </ul>
</section>

<section>
  <h2>Aggregating Community Preferences</h2>
  <p>#VOICE aggregates votes to reveal collective priorities.</p>
  <ul>
    <li>Tags with more votes reflect stronger community consensus.</li>
    <li>The results guide onboarding decisions and focus areas.</li>
  </ul>
  <p>\( W_i = \sum_{j=1}^m v_{j,i} \)</p>
  <ul>
    <li>\( W_i \): The total preference weight of tag \( t_i \).</li>
    <li>\( v_{j,i} \): The votes participant \( p_j \) assigned to tag \( t_i \).</li>
  </ul>
</section>

<section>
  <h2>Building Relationships Between Tags</h2>
  <p>#VOICE builds a **preference-weighted graph** to reveal relationships between tags.</p>
  <ul>
    <li>Tags that are voted on together have stronger connections.</li>
    <li>Edge weights normalize for participant budgets to ensure fairness.</li>
  </ul>
  <p>\( w_{i,k} = \sum_{j=1}^m \frac{v_{j,i} \cdot v_{j,k}}{\max(B_j, 1)} \)</p>
  <ul>
    <li>\( w_{i,k} \): The edge weight between tags \( t_i \) and \( t_k \).</li>
    <li>\( v_{j,i}, v_{j,k} \): Votes participant \( p_j \) allocated to tags \( t_i \) and \( t_k \).</li>
  </ul>
</section>

<section>
  <h2>Integrating Feedback for Richer Insights</h2>
  <p>#VOICE combines votes with qualitative feedback to refine priorities.</p>
  <p>\( w_{\text{final},i,k} = \alpha \cdot w'_{i,k} + \beta \cdot q_{i,k} \)</p>
  <ul>
    <li>\( w_{\text{final},i,k} \): Final edge weight combining votes and feedback.</li>
    <li>\( w'_{i,k} \): Quantitative co-preference weight.</li>
    <li>\( q_{i,k} \): Qualitative similarity derived from participant comments.</li>
  </ul>
</section>

<section>
  <h2>Why Communities Choose #VOICE</h2>
  <p>#VOICE delivers structured, actionable insights for onboarding:</p>
  <ul>
    <li>Encourages thoughtful prioritization with quadratic voting.</li>
    <li>Reveals collective preferences and relationships through graphs.</li>
    <li>Combines quantitative votes with qualitative reasoning for deeper sensemaking.</li>
  </ul>
</section>

<section>
  <h2>Conclusion</h2>
  <p>#VOICE empowers communities to:</p>
  <ul>
    <li>Make clear, data-driven onboarding decisions.</li>
    <li>Align around shared priorities and goals.</li>
    <li>Build collective intelligence through Semantic Ballot Voting.</li>
  </ul>
  <p>Get started with #VOICE and onboard to Scroll today!</p>
</section>
