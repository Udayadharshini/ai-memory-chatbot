# Prompt Engineering Experiments – Task 2

## 1. Zero-shot vs Few-shot Prompting

**Task:** Classify the review: “The product arrived late, but the quality is excellent.”

### Zero-shot prompt
```text
Classify the sentiment of the following customer review as Positive, Negative, or Neutral.

Review: "The product arrived late, but the quality is excellent."

Return only the sentiment label.
```
**Observed output:** `Neutral`

### Few-shot prompt
```text
Classify each customer review as Positive, Negative, or Neutral.

Examples:
Review: "I love this product. It works perfectly."
Sentiment: Positive

Review: "The item broke after one day. Very disappointed."
Sentiment: Negative

Review: "The package arrived yesterday."
Sentiment: Neutral

Review: "The service was terrible and the staff were rude."
Sentiment: Negative

Review: "Excellent quality and fast delivery!"
Sentiment: Positive

Now classify this review:
Review: "The product arrived late, but the quality is excellent."

Return only the sentiment label.
```
**Observed output:** `Positive`

**Analysis:** The prompts produced different labels for a mixed-sentiment review. The examples may have influenced the model toward the positive aspect. One example is not enough to prove few-shot prompting is always more accurate.

## 2. Direct Answer vs Step-by-step Prompt

**Direct prompt**
```text
A shop sells a bag for ₹800 after giving a 20% discount. What was the original price of the bag?

Give only the final answer.
```
**Observed output:** `₹1,000`

**Step-by-step prompt**
```text
A shop sells a bag for ₹800 after giving a 20% discount. What was the original price of the bag?

Explain your solution step by step, showing the calculation and the final answer.
```
**Observed output**
```text
The bag's selling price after a 20% discount is ₹800.

Step 1: Find the percentage you actually paid.
100% − 20% = 80%
So, ₹800 represents 80% of the original price.

Step 2: Find the original price.
Original Price = (800 × 100) / 80 = ₹1,000

Check: 20% of ₹1,000 = ₹200. ₹1,000 − ₹200 = ₹800. Correct!
```
**Analysis:** Both prompts gave the correct answer. The step-by-step version made the calculation easier to inspect and verify. In this test, it improved transparency rather than the final answer's correctness.

## 3. Structured JSON Output

### Prompt template
```text
Extract the person's name, date, and amount from the text below.

Return valid JSON only, using exactly these three keys:
"name", "date", "amount".

Use a string for each value. If a value is missing, use an empty string. Do not add explanations or Markdown.

Text: [input text]
```

### Test inputs and observed outputs

**Test 1 input:** Udaya paid ₹1500 on 12 October 2026 for the course fee.

```json
{
  "name": "Udaya",
  "date": "12 October 2026",
  "amount": "₹1500"
}
```

**Test 2 input:** Rahul purchased a laptop for ₹45,999 on 25 September 2026.

```json
{
  "name": "Rahul",
  "date": "25 September 2026",
  "amount": "₹45,999"
}
```

**Test 3 input:** Priya paid ₹750 for books on 18 October 2026.

```json
{
  "name": "Priya",
  "date": "18 October 2026",
  "amount": "₹750"
}
```

**Test 4 input:** On 5 October 2026, Arun received a payment of ₹2,300 for freelance work.

```json
{
  "name": "Arun",
  "date": "5 October 2026",
  "amount": "₹2,300"
}
```

**Test 5 input:** On 22 October 2026, Meena registered for the workshop, but the payment amount was not mentioned.

```json
{
  "name": "Meena",
  "date": "22 October 2026",
  "amount": ""
}
```

**Analysis:** All five observed outputs followed the requested keys and missing-value rule. Observed success rate: **5/5 (100%)** on these five test cases. This small test set does not guarantee the same result for every input.

## 4. What I learned

I learned that examples in a prompt can influence classification, step-by-step instructions can make calculations easier to verify, and a clearly defined JSON format can make extracted information more consistent. I also learned that prompts should clearly state the expected labels, keys, and how missing values should be handled.

## 5. Conclusion

These experiments show that prompt wording affects the format, explanation, and sometimes the result of an AI response. More test cases would be needed to make stronger claims about reliability.
