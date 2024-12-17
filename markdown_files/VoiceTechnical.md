<section>
  <h1>Semantic Ballot Voting: A Technical Overview</h1>
  <p>A new deliberative sensemaking tool and system for collective intelligence formation.</p>
</section>

<section>
  <h2>Introducing Semantic Ballot Voting</h2>
  <p>Semantic Ballot Voting (SBV) extends traditional voting mechanisms to capture richer, more structured preferences.</p>
  <ul>
    <li>Votes are allocated across <strong>semantic tags</strong> representing decision axes.</li>
    <li>Participants’ preferences are expressed quantitatively and qualitatively, enabling deep deliberation.</li>
    <li>SBV builds a preference-weighted graph to visualize and analyze collective priorities.</li>
  </ul>
</section>

<section>
  <h2>Defining the Decision Space</h2>
  <p>We begin by defining the set of options that participants can vote on, represented as semantic tags.</p>
  <ul>
    <li>Each semantic tag represents a distinct decision axis or priority.</li>
    <li>This creates a structured decision space for participants to navigate.</li>
  </ul>
</section>

<section>
  <h2>Defining Semantic Tags</h2>
  <p>\( T = \{ t_1, t_2, \dots, t_n \} \)</p>
  <ul>
    <li>\( T \): The set of semantic tags.</li>
    <li>\( t_i \): Each individual decision axis or option within the set.</li>
  </ul>
</section>

<section>
  <h2>Assigning Voting Budgets</h2>
  <p>Participants are assigned a finite voting budget to express their preferences.</p>
  <ul>
    <li>The budget ensures participants prioritize their most important options.</li>
    <li>This budget creates trade-offs, encouraging deliberative decision-making.</li>
  </ul>
</section>

<section>
  <h2>Participants and Voting Budget</h2>
  <p>\( P = \{ p_1, p_2, \dots, p_m \} \)</p>
  <ul>
    <li>\( P \): The set of participants.</li>
    <li>\( p_j \): A participant who allocates votes across the semantic tags.</li>
  </ul>
</section>

<section>
  <h2>Quadratic Voting: Balancing Influence</h2>
  <p>To ensure fairness, SBV uses quadratic voting. The cost of votes grows quadratically with their quantity.</p>
  <ul>
    <li>Quadratic costs prevent participants from concentrating votes on a single tag.</li>
    <li>This mechanism promotes balanced, thoughtful preference distribution.</li>
  </ul>
</section>

<section>
  <h2>Quadratic Voting</h2>
  <p>\( \text{Cost}_{j,i} = v_{j,i}^2 \)</p>
  <ul>
    <li>\( \text{Cost}_{j,i} \): The cost for participant \( p_j \) to allocate \( v_{j,i} \) votes to tag \( t_i \).</li>
    <li>\( v_{j,i} \): The number of votes participant \( p_j \) assigns to tag \( t_i \).</li>
  </ul>
</section>

<section>
  <h2>Ensuring Budget Constraints</h2>
  <p>Participants must stay within their assigned budgets. This encourages careful allocation of votes.</p>
</section>

<section>
  <h2>Budget Constraint</h2>
  <p>\( \sum_{i=1}^n v_{j,i}^2 \leq B_j \)</p>
  <ul>
    <li>\( B_j \): The total voting budget for participant \( p_j \).</li>
    <li>\( \sum_{i=1}^n v_{j,i}^2 \): The total cost of all votes allocated by \( p_j \).</li>
  </ul>
</section>

<section>
  <h2>Aggregating Preferences</h2>
  <p>After votes are cast, we aggregate preferences to determine the importance of each semantic tag.</p>
  <ul>
    <li>Tags with more votes are deemed more important to the group.</li>
    <li>This step reveals the group’s collective priorities.</li>
  </ul>
</section>

<section>
  <h2>Aggregating Preferences</h2>
  <p>\( W_i = \sum_{j=1}^m v_{j,i} \)</p>
  <ul>
    <li>\( W_i \): The total preference weight of tag \( t_i \).</li>
    <li>\( v_{j,i} \): The number of votes participant \( p_j \) assigned to tag \( t_i \).</li>
    <li>\( m \): The total number of participants.</li>
  </ul>
</section>

<section>
  <h2>Building Connections Between Preferences</h2>
  <p>SBV constructs a preference-weighted graph to reveal relationships between tags.</p>
  <ul>
    <li>Tags that receive votes together are connected by weighted edges.</li>
    <li>Edge weights are normalized to ensure fairness across participants.</li>
  </ul>
</section>

<section>
  <h2>Building Weighted Relationships</h2>
  <p>\( w_{i,k} = \sum_{j=1}^m \frac{v_{j,i} \cdot v_{j,k}}{\max(B_j, 1)} \)</p>
  <ul>
    <li>\( w_{i,k} \): The edge weight between tags \( t_i \) and \( t_k \).</li>
    <li>\( v_{j,i}, v_{j,k} \): Votes participant \( p_j \) allocated to tags \( t_i \) and \( t_k \).</li>
    <li>\( B_j \): The total budget of participant \( p_j \).</li>
  </ul>
</section>

<section>
  <h2>Integrating Qualitative Insights</h2>
  <p>To enrich the graph, qualitative feedback is combined with quantitative preferences.</p>
  <ul>
    <li>Natural Language Processing (NLP) analyzes thematic similarities from participant comments.</li>
    <li>Final edge weights reflect both quantitative votes and qualitative themes.</li>
  </ul>
</section>

<section>
  <h2>Integrating Qualitative Feedback</h2>
  <p>\( w_{\text{final},i,k} = \alpha \cdot w'_{i,k} + \beta \cdot q_{i,k} \)</p>
  <ul>
    <li>\( w_{\text{final},i,k} \): Final edge weight between tags \( t_i \) and \( t_k \).</li>
    <li>\( w'_{i,k} \): Normalized quantitative co-preference weight.</li>
    <li>\( q_{i,k} \): Qualitative similarity score derived from feedback.</li>
    <li>\( \alpha, \beta \): Scaling coefficients to balance components.</li>
  </ul>
</section>

<section>
  <h2>Centrality and Collective Intelligence</h2>
  <p>The graph reveals influential tags based on their centrality, helping prioritize collective actions.</p>
</section>

<section>
  <h2>Analyzing Graph Centrality</h2>
  <p>\( C_{\text{degree}}(t_i) = \sum_{k \neq i} w_{i,k} \)</p>
  <ul>
    <li>\( C_{\text{degree}}(t_i) \): Degree centrality of tag \( t_i \), summing all its edge weights.</li>
    <li>\( w_{i,k} \): Edge weight between tag \( t_i \) and other tags \( t_k \).</li>
  </ul>
</section>

<section>
  <h2>Conclusion</h2>
  <p>Semantic Ballot Voting combines structured voting, graph analysis, and qualitative feedback to:</p>
  <ul>
    <li>Capture and prioritize nuanced preferences.</li>
    <li>Reveal relationships and emerging consensus.</li>
    <li>Empower collective intelligence formation through deliberative sensemaking.</li>
  </ul>
</section>
