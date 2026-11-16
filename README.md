# GenLayer Explained: A Blockchain That Can Agree on Meaning

Learning notes on GenLayer: intelligent contracts, deployment notes, and an explanatory article.

## Contents

- `article.md` — "GenLayer Explained: A Blockchain That Can Agree on Meaning". Covers Intelligent Contracts, the GenVM, the Equivalence Principle and Optimistic Democracy, with sources to the GenLayer docs and blog.
- `first_intelligent_contract.py` — a minimal first Intelligent Contract: it checks whether the word "iana" appears in the rendered HTML of example.org, using `gl.nondet.web.render` inside a non-deterministic block and `gl.eq_principle.strict_eq` to validate the result.
- `football_prediction_market.py` — a full worked example: a football prediction market that resolves a match from BBC Sport via an LLM and the Equivalence Principle. (Same contract as in the [genlayer-prediction-market](https://github.com/rjrajput-web3/genlayer-prediction-market) repo.)

## Read it

Start with `article.md`, then run the two contracts in GenLayer Studio.
