# Word-Pair-Scoring-Problem

The following is my solution to the word-pair-scoring-problem. 

The file can be run via: `python3 word_pairs.py`

There are a number of considerations that have been made in order to achieve greater efficiency. 
Some of these are:
1. Optimized built-in functions have been used whenever possible
2. Multiple assignment has been used when possible
3. Exiting early from conditions in the code loops have been used whenever possible
4. sets have been avoided
5. dot operations have been avoided (for example using sqrt instead of math.sqrt)
6. Rather than have expensive helper function calls, all has been incorporated into the single function highest_scoring_pair
7. Use in and not in operators as oppossed to == and != 
