# Product plan

## ICP and JTBD
Primary ICP: remote adult-child executor with a 7–14 day property deadline. JTBD: “Help us agree on what must not disappear, assign the remaining routes, and empty the house without regret.”

## MVP
Guided room queue; explicit keep/unsure/release signal; deterministic routing to family hold, expert review, resale batch, or donation/recycling; checklist and owner trail. Image recognition, payments, hauling dispatch, and automated appraisal are excluded.

## Data model
`EstateCase` has rooms and deadlines. `Item` has room, description, condition, market-clue count, hypothesis range, story, and evidence photos. `Decision` records family signal, route, confidence, reasons, next actions, owner, and timestamp. `ConsentEvent` records reversals and release approval.

## AI/model strategy
Start deterministic and human-reviewed. Later use vision only to propose categories and visible marks, never authoritative value. Retrieval can match specialist playbooks; route confidence must expose evidence and abstain when uncertain. Evaluate false-negative “discard” recommendations as the primary safety metric.

## Economics
Hypothesis: $149 remote triage, with a $399 specialist-review bundle. At 55% gross margin after human review, 100 monthly sessions yield roughly $8.2k gross profit before acquisition and overhead. Affiliate hauling is optional upside, not core unit economics.

## Validation
Landing CTA: “Book a $149 do-not-discard walkthrough.” Success in 30 days: 20 qualified conversations, 5 paid sessions, 60% completion, median packet delivery under 24 hours, and at least 3 referrals. Kill or reframe if fewer than 2 pay after 20 qualified conversations.

## Moat
Not generic vision. Potential moat is consented decision history, specialist outcomes, local routing performance, and trusted distribution through estate professionals. None exists yet.

## Risks
False confidence causes loss; family disputes stall decisions; valuation can trigger regulatory or reputational exposure; low household frequency hurts consumer CAC; local-provider quality varies. Mitigate with abstention, reversible holds, shared consent, non-appraisal language, partner distribution, and auditable routing.

## Roadmap
- 0–30 days: five observed walkthroughs, three paid concierge sessions, route taxonomy.
- 31–60 days: shared decision links, owner/consent trail, specialist packet, partner pilot.
- 61–90 days: limited visual mark capture, provider quality feedback, repeatable partner acquisition.
