# AI Feature Brief: Meeting Action Item Extractor

A one-page brief an AI engineer writes *before* building. Copy this template for your own features.

## 1. Problem
After meetings, people forget who agreed to do what. Users want a list of action items (owner + task) they can save to their task tracker.

## 2. Is AI the right tool?
- **Yes, because:** transcripts are messy, free-form language. Rules or keyword matching would miss most real phrasings ("I can take that").
- **Risks:** the model may miss tasks, assign the wrong owner, or invent people who weren't in the meeting.

## 3. What does "good" look like?
- Captures tasks someone explicitly agreed to do.
- Owner is always a real attendee.
- Returns an empty list when there are no action items.
- These rules are encoded as test cases in [`eval_cases.json`](eval_cases.json).

## 4. System design
| Part | Decision |
|---|---|
| Input | Transcript + attendee list (context) |
| Model | A general chat model through an API, `temperature=0` |
| Output | JSON: `{"items": [{"owner", "task"}]}`, validated before saving |
| Integration | Saved to the task tracker only after the user confirms |

## 5. Handling wrong answers (UX)
- Show each item next to the transcript line it came from.
- Let users edit or delete items before saving.
- If the output is invalid, show "Couldn't extract action items" instead of guessing.

## 6. Cost & latency
- Cost grows with transcript length (tokens), so long meetings cost more. Measure the cost per meeting during testing.
- Target: results within a few seconds of the meeting ending. Process the transcript in the background if needed.

## 7. After launch
- Track how often users edit or delete items. That's a direct quality signal.
- Re-run the eval set before switching to a new model version.
- Review a small sample of real outputs every week.

## 8. Who's involved
Product manager (success metric) · Designer (review-before-save UI) · Backend engineer (task tracker integration) · Security/legal (which meeting data can be sent to the model provider)
