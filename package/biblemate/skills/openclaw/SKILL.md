---
name: biblemate
description: Bible study tools via MCP — search, retrieve verses, commentaries, cross-references, Hebrew/Greek interlinear, devotions, sermons, and theological analysis.
metadata: {"openclaw":{"emoji":"📖","requires":{"bins":["mcporter"]}}}
---

# Biblemate (MCP)

Bible study MCP server with 48 tools. Use `mcporter call biblemate.<tool>` for all Bible-related queries.

## Workflow: Structured Bible Study

When a user asks a Bible-related question, **DO NOT** answer directly. Follow this structured approach:

### Step 1: Analyze the Request

Identify:
- The core question or topic
- Type of study needed (exegesis, devotional, theological, historical, practical)
- Relevant Bible passages, characters, or themes
- User's apparent level (casual reader, student, scholar)

### Step 2: Create Preliminary Action Plan

Output a plan in this format:

```
# Preliminary Action Plan

**Request:** [Restate the user's question]
**Study Type:** [exegetical | devotional | theological | historical | topical | character | comparative]

## Steps

1. **[Step Name]**
   - Tool: `biblemate.<tool_name>`
   - Purpose: [What this step accomplishes]
   - Input: [The request parameter]

2. **[Step Name]**
   - Tool: `biblemate.<tool_name>`
   - Purpose: [What this step accomplishes]
   - Input: [The request parameter]

[...continue for 3-7 steps as needed...]

# Measurable Outcomes

- [ ] [Specific deliverable 1]
- [ ] [Specific deliverable 2]
- [ ] [Specific deliverable 3]
```

### Step 3: Execute the Plan

Run each step sequentially using `mcporter call biblemate.<tool> request="..."`.

For each step:
- Execute the tool call
- Capture key findings
- Note any cross-references or follow-up insights

### Step 4: Quality Control

Before finalizing, verify:
- All measurable outcomes have been addressed
- Findings are consistent across sources
- Original languages support the conclusions (if applicable)
- Practical application is grounded in the text

### Step 5: Final Report

Provide an integrated response:

```
# Final Report: [Topic/Question]

## Summary
[2-3 sentence overview of findings]

## Key Findings

### [Finding 1 Title]
[Details with verse references]

### [Finding 2 Title]
[Details with verse references]

[...continue as needed...]

## Original Language Insights
[Hebrew/Greek insights if relevant]

## Cross-References
[Related passages discovered]

## Theological Significance
[Broader meaning and doctrinal connections]

## Practical Application
[How this applies to life/faith]

## Sources Consulted
- [List of tools used and their contributions]
```

---

## Tool Reference

### Retrieve & Search
- `mcporter call biblemate.retrieve_bible_verses request="John 3:16-17"`
- `mcporter call biblemate.retrieve_bible_chapter request="Psalm 23"`
- `mcporter call biblemate.search_the_whole_bible request="love your neighbor"`
- `mcporter call biblemate.retrieve_bible_cross_references request="Romans 8:28"`

### Original Languages
- `mcporter call biblemate.retrieve_hebrew_or_greek_bible_verses request="Gen 1:1"`
- `mcporter call biblemate.retrieve_interlinear_hebrew_or_greek_bible_verses request="John 1:1"`
- `mcporter call biblemate.retrieve_verse_morphology request="Eph 2:8"`
- `mcporter call biblemate.translate_hebrew_bible_verse request="<Hebrew text>"`
- `mcporter call biblemate.translate_greek_bible_verse request="<Greek text>"`

### Compare & Commentary
- `mcporter call biblemate.compare_bible_translations request="Psalm 23:1"`
- `mcporter call biblemate.read_bible_commentary request="Rom 8:28"`
- `mcporter call biblemate.refine_bible_translation request="Gen 1:2"`

### Study & Analysis
- `mcporter call biblemate.write_bible_chapter_summary request="Genesis 1"`
- `mcporter call biblemate.write_bible_book_introduction request="Romans"`
- `mcporter call biblemate.write_bible_outline request="Ephesians"`
- `mcporter call biblemate.write_bible_insights request="Matt 5:1-12"`
- `mcporter call biblemate.interpret_old_testament_verse request="Isaiah 53:5"`
- `mcporter call biblemate.interpret_new_testament_verse request="Heb 11:1"`

### Themes & Context
- `mcporter call biblemate.study_bible_themes request="grace"`
- `mcporter call biblemate.study_old_testament_themes request="Exodus 20"`
- `mcporter call biblemate.study_new_testament_themes request="Galatians 5"`
- `mcporter call biblemate.write_old_testament_historical_context request="1 Kings 18"`
- `mcporter call biblemate.write_new_testament_historical_context request="Acts 2"`
- `mcporter call biblemate.write_bible_canonical_context request="Daniel"`
- `mcporter call biblemate.write_bible_thought_progression request="Romans 8"`

### Characters & Locations
- `mcporter call biblemate.write_bible_character_study request="David"`
- `mcporter call biblemate.write_bible_location_study request="Jerusalem"`

### Devotional & Practical
- `mcporter call biblemate.write_bible_devotion request="Phil 4:6-7"`
- `mcporter call biblemate.write_bible_applications request="James 1:2-4"`
- `mcporter call biblemate.write_bible_questions request="Mark 4:1-20"`
- `mcporter call biblemate.quote_bible_verses request="comfort in grief"`
- `mcporter call biblemate.quote_bible_promises request="anxiety"`

### Psalms
- `mcporter call biblemate.anyalyze_psalms request="Psalm 51:1-5"`

### Theology & Teaching
- `mcporter call biblemate.expound_bible_topic request="justification by faith"`
- `mcporter call biblemate.write_bible_theology request="Trinity"`
- `mcporter call biblemate.write_bible_perspectives request="suffering"`
- `mcporter call biblemate.explain_bible_meaning request="born again"`
- `mcporter call biblemate.identify_bible_keywords request="faith hope love"`
- `mcporter call biblemate.write_bible_sermon request="John 14:1-6"`

### Highlights & Summaries
- `mcporter call biblemate.write_old_testament_highlights request="Isaiah 40"`
- `mcporter call biblemate.write_new_testament_highlights request="Hebrews 11"`
- `mcporter call biblemate.write_bible_related_summary request="parables of Jesus"`

### Prayer
- `mcporter call biblemate.write_bible_prayer request="healing"`
- `mcporter call biblemate.write_short_bible_prayer request="peace"`
- `mcporter call biblemate.write_pastor_prayer request="Sunday service"`

### Ask Experts
- `mcporter call biblemate.ask_theologian request="predestination vs free will"`
- `mcporter call biblemate.ask_pastor request="how to forgive someone"`
- `mcporter call biblemate.ask_bible_scholar request="authorship of Hebrews"`

---

## Example Workflow

**User asks:** "What does it mean to be 'born again' in John 3?"

### Preliminary Action Plan

**Request:** Explain the meaning of being "born again" in John 3
**Study Type:** exegetical + theological

## Steps

1. **Retrieve the Text**
   - Tool: `biblemate.retrieve_bible_verses`
   - Purpose: Get the primary passage
   - Input: "John 3:1-8"

2. **Greek Interlinear Analysis**
   - Tool: `biblemate.retrieve_interlinear_hebrew_or_greek_bible_verses`
   - Purpose: Examine the Greek "γεννηθῇ ἄνωθεν" (born again/from above)
   - Input: "John 3:3-7"

3. **Cross-References**
   - Tool: `biblemate.retrieve_bible_cross_references`
   - Purpose: Find related passages on spiritual rebirth
   - Input: "John 3:3"

4. **Commentary**
   - Tool: `biblemate.read_bible_commentary`
   - Purpose: Scholarly interpretation
   - Input: "John 3:3-5"

5. **Theological Exposition**
   - Tool: `biblemate.expound_bible_topic`
   - Purpose: Doctrinal significance of regeneration
   - Input: "born again regeneration"

6. **Practical Application**
   - Tool: `biblemate.write_bible_applications`
   - Purpose: How this applies to believers today
   - Input: "John 3:1-8"

## Measurable Outcomes

- [ ] Greek meaning of "ἄνωθεν" (anōthen) clarified
- [ ] Relationship between water/Spirit birth explained
- [ ] OT background Nicodemus should have known identified
- [ ] Theological doctrine of regeneration summarized
- [ ] Practical application for modern readers provided

[Then execute each step, verify outcomes, and compile the Final Report]

---

## Notes

- All tools take a `request` parameter (string).
- For verse references, use standard format: `Book Chapter:Verse` (e.g., `John 3:16`, `Gen 1:1-3`).
- Adjust the number of steps based on question complexity (simple = 3-4 steps, complex = 5-7 steps).
- Always include at least one original language tool for exegetical questions.
- The final report should integrate findings, not just concatenate tool outputs.
