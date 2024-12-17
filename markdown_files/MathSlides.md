<section>
  <h2>Defining Semantic Tags</h2>
  <p>We begin by defining the set of decision options, represented as semantic tags.</p>
  <ul>
    <li>Each tag corresponds to a decision axis.</li>
    <li>Participants allocate votes across these tags to express preferences.</li>
  </ul>
  <p>\( T = \{ t_1, t_2, \dots, t_n \} \)</p>
  <ul>
    <li>\( T \): The set of semantic tags.</li>
    <li>\( t_i \): Each individual decision axis or option within the set.</li>
  </ul>
</section>

<section>
  <h2>Participants and Voting Budget</h2>
  <p>Each participant is assigned a finite voting budget.</p>
  <ul>
    <li>The budget limits total votes a participant can allocate.</li>
    <li>This enforces prioritization and trade-offs.</li>
  </ul>
  <p>\( P = \{ p_1, p_2, \dots, p_m \} \)</p>
  <ul>
    <li>\( P \): The set of participants.</li>
    <li>\( p_j \): A participant who allocates votes across the semantic tags.</li>
  </ul>
</section>

<section>
  <h2>Quadratic Voting</h2>
  <p>Quadratic voting ensures that the cost of casting votes grows quadratically.</p>
  <ul>
    <li>Vote cost increases non-linearly to discourage concentration on a single tag.</li>
    <li>Participants must allocate votes carefully to stay within their budgets.</li>
  </ul>
  <p>\( \text{Cost}_{j,i} = v_{j,i}^2 \)</p>
  <ul>
    <li>\( \text{Cost}_{j,i} \): The cost for participant \( p_j \) to allocate \( v_{j,i} \) votes to tag \( t_i \).</li>
    <li>\( v_{j,i} \): The number of votes participant \( p_j \) assigns to tag \( t_i \).</li>
  </ul>
</section>

<section>
  <h2>Budget Constraint</h2>
  <p>Participants’ total spending must remain within their assigned budgets.</p>
  <p>\( \sum_{i=1}^n v_{j,i}^2 \leq B_j \)</p>
  <ul>
    <li>\( B_j \): The total voting budget for participant \( p_j \).</li>
    <li>\( \sum_{i=1}^n v_{j,i}^2 \): The total cost of all votes allocated by \( p_j \).</li>
  </ul>
</section>

<section>
  <h2>Aggregating Preferences</h2>
  <p>We calculate the total preference weight for each tag by summing votes across all participants.</p>
  <ul>
    <li>This determines the relative importance of each tag.</li>
    <li>Higher votes indicate stronger preference.</li>
  </ul>
  <p>\( W_i = \sum_{j=1}^m v_{j,i} \)</p>
  <ul>
    <li>\( W_i \): The total preference weight of tag \( t_i \).</li>
    <li>\( v_{j,i} \): The number of votes participant \( p_j \) assigned to tag \( t_i \).</li>
    <li>\( m \): The total number of participants.</li>
  </ul>
</section>

<section>
  <h2>Building Weighted Relationships</h2>
  <p>Tags are connected by weighted edges based on shared votes.</p>
  <ul>
    <li>Edge weights measure co-preference between tags.</li>
    <li>We normalize the weights using participant budgets for fairness.</li>
  </ul>
  <p>\( w_{i,k} = \sum_{j=1}^m \frac{v_{j,i} \cdot v_{j,k}}{\max(B_j, 1)} \)</p>
  <ul>
    <li>\( w_{i,k} \): The edge weight between tags \( t_i \) and \( t_k \).</li>
    <li>\( v_{j,i}, v_{j,k} \): Votes participant \( p_j \) allocated to tags \( t_i \) and \( t_k \).</li>
    <li>\( B_j \): The total budget of participant \( p_j \) (ensures normalization).</li>
  </ul>
</section>

<section>
  <h2>Integrating Qualitative Feedback</h2>
  <p>We refine edge weights by combining quantitative co-preferences with qualitative reasoning.</p>
  <ul>
    <li>Natural Language Processing (NLP) extracts thematic similarity from participant feedback.</li>
    <li>Final edge weights combine quantitative and qualitative components.</li>
  </ul>
  <p>\( w_{\text{final},i,k} = \alpha \cdot w'_{i,k} + \beta \cdot q_{i,k} \)</p>
  <ul>
    <li>\( w_{\text{final},i,k} \): Final edge weight between tags \( t_i \) and \( t_k \).</li>
    <li>\( w'_{i,k} \): Normalized quantitative co-preference weight.</li>
    <li>\( q_{i,k} \): Qualitative similarity score derived from feedback.</li>
    <li>\( \alpha, \beta \): Scaling coefficients to balance components.</li>
  </ul>
</section>

<section>
  <h2>Analyzing Graph Centrality</h2>
  <p>Tags are analyzed to determine their importance in the graph.</p>
  <ul>
    <li>Central tags are highly connected and influential in the decision space.</li>
    <li>Degree centrality measures the total connectivity of each tag.</li>
  </ul>
  <p>\( C_{\text{degree}}(t_i) = \sum_{k \neq i} w_{i,k} \)</p>
  <ul>
    <li>\( C_{\text{degree}}(t_i) \): Degree centrality of tag \( t_i \), summing all its edge weights.</li>
    <li>\( w_{i,k} \): Edge weight between tag \( t_i \) and other tags \( t_k \).</li>
  </ul>
</section>

<section>
  <h2>Summary</h2>
  <p>Semantic Ballot Voting combines multiple components to capture nuanced preferences:</p>
  <ul>
    <li><strong>Quadratic Voting</strong>: Ensures fair allocation of votes through exponential costs.</li>
    <li><strong>Preference Aggregation</strong>: Aggregates votes to reveal collective priorities.</li>
    <li><strong>Graph Analysis</strong>: Builds a preference-weighted graph to identify relationships and key tags.</li>
    <li><strong>Qualitative Integration</strong>: Combines quantitative data with NLP insights for richer results.</li>
  </ul>
</section>
