import chainlit as cl
import markdown
from mdx_math import MathExtension

notes = r"""
# Enhanced: Introduction to Probability

## Section 1: Brief Review of Key Concepts

Probability is a measure of the likelihood of an event occurring. It is a number between 0 and 1, where 0 represents an impossible event and 1 represents a certain event. The probability of an event is often denoted by the symbol P(A) and is calculated using the formula:

$$P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}$$

## Section 2: Detailed Walkthrough of Existing Examples

### Example 1: Coin Toss

Problem Statement: A fair coin is tossed. What is the probability that it lands heads up?

Solution Steps:

1. Define the sample space: The sample space is the set of all possible outcomes, which is {heads, tails}.
2. Determine the number of favorable outcomes: There is 1 favorable outcome, which is the coin landing heads up.
3. Calculate the probability: $$P(\text{heads}) = \frac{1}{2}$$

### Example 2: Drawing a Card

Problem Statement: A deck of 52 cards is shuffled and a card is drawn at random. What is the probability that the card is a king?

Solution Steps:

1. Define the sample space: The sample space is the set of all possible outcomes, which is the 52 cards in the deck.
2. Determine the number of favorable outcomes: There are 4 favorable outcomes, which are the 4 kings in the deck.
3. Calculate the probability: $$P(\text{king}) = \frac{4}{52} = \frac{1}{13}$$

## Section 3: New Worked Examples

### Example 3: Rolling a Die

Problem Statement: A fair six-sided die is rolled. What is the probability that the number on the top is greater than 3?

Solution Steps:

1. Define the sample space: The sample space is the set of all possible outcomes, which is {1, 2, 3, 4, 5, 6}.
2. Determine the number of favorable outcomes: There are 3 favorable outcomes, which are the numbers 4, 5, and 6.
3. Calculate the probability: $$P(\text{number > 3}) = \frac{3}{6} = \frac{1}{2}$$

### Example 4: Drawing a Ball

Problem Statement: A box contains 5 red balls, 3 blue balls, and 2 green balls. A ball is drawn at random. What is the probability that the ball is blue?

Solution Steps:

1. Define the sample space: The sample space is the set of all possible outcomes, which is the 10 balls in the box.
2. Determine the number of favorable outcomes: There are 3 favorable outcomes, which are the 3 blue balls.
3. Calculate the probability: $$P(\text{blue}) = \frac{3}{10}$$

### Example 5: Multiple Events

Problem Statement: A fair coin is tossed twice. What is the probability that both tosses result in heads?

Solution Steps:

1. Define the sample space: The sample space is the set of all possible outcomes, which is {(heads, heads), (heads, tails), (tails, heads), (tails, tails)}.
2. Determine the number of favorable outcomes: There is 1 favorable outcome, which is the outcome (heads, heads).
3. Calculate the probability: $$P(\text{both heads}) = \frac{1}{4}$$
"""


@cl.on_chat_start
async def start():
  # Send the Markdown + LaTeX message directly
  await cl.Message(content=notes).send()
