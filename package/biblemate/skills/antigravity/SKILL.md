---
name: bible-study
description: Structured multi-step workflow with planning, execution, and quality control for comprehensive bible study. Use when users ask bible questions requiring in-depth study, theological analysis, or multi-faceted exploration.
---

# Bible Study Skill

## Overview
This skill provides a structured, agentic approach to bible study that mirrors professional biblical scholarship. When a user asks a bible question, you will create a preliminary action plan, define measurable outcomes, execute the plan using appropriate tools, and synthesize findings into a comprehensive report.

## When to Use This Skill
Trigger this skill when:
- User asks in-depth bible questions requiring theological analysis
- User requests study of specific verses, passages, or biblical themes
- User wants to understand context, meaning, or application of scripture
- User asks comparative questions (e.g., "What does the Bible say about...")
- User requests exegetical or hermeneutical analysis
- User wants cross-references, word studies, or thematic exploration

**DO NOT** use for simple verse retrieval requests (e.g., "What is John 3:16?"). For those, directly use the appropriate biblemate tool.

## Workflow Structure

### Phase 1: Analysis & Planning
When a user asks a bible study question:

1. **Analyze the Request**: Identify what the user is asking for
   - What scripture(s) are involved?
   - What type of study is needed? (exegetical, thematic, applicational, comparative, etc.)
   - What depth of analysis is appropriate?
   - What specific questions need answering?

2. **Refine and Engineer the Prompt**: Improve the user's original request to ensure optimal results.
   - **Identify and address ambiguities**: Clarify unclear assumptions, missing information, or vague terms.
   - **Rephrase for comprehension**: Apply knowledge of language structures, syntax, and semantics to rephrase the prompt for better comprehension.
   - **Contextualize**: Consider the context, goals, and potential constraints of the task or request.
   - **Optimize**: Ensure the revised prompt is concise, yet comprehensive, and accurately reflects the user's needs.
   - **Apply Best Practices**: Specify output formats, provide examples, or define key terms as needed.

3. **Create Preliminary Action Plan**: Document your plan in a structured format
   ```markdown
   # Preliminary Action Plan
   
   ## Study Objective
   [Clear statement of what you're studying and why]
   
   ## Study Steps
   1. **[Step Name]** - [Brief description]
      - Tool: `[appropriate biblemate tool]`
      - Purpose: [Why this step is needed]
   
   2. **[Step Name]** - [Brief description]
      - Tool: `[appropriate biblemate tool]`
      - Purpose: [Why this step is needed]
   
   [Continue for all steps...]
   
   # Measurable Outcomes
   
   ## Quality Control Criteria
   - [ ] [Specific criterion to verify]
   - [ ] [Specific criterion to verify]
   - [ ] [Specific criterion to verify]
   
   ## Expected Deliverables
   - [What the final report should contain]
   - [What insights should be provided]
   ```

4. **Use task_boundary tool**: Set mode to PLANNING with TaskName like "Bible Study: [Topic/Passage]"

### Phase 2: Execution
Execute each step in your action plan:

1. **Switch to EXECUTION mode** using task_boundary
2. **Call appropriate biblemate tools** for each step in sequence
3. **Document findings** as you go - keep notes on key insights from each step
4. **Adapt if needed** - if you discover new relevant areas during execution, add them to your plan

### Phase 3: Quality Control
Review your findings against measurable outcomes:

1. **Switch to VERIFICATION mode** using task_boundary
2. **Check each quality criterion**: Have you addressed all aspects?
3. **Identify gaps**: Are there questions left unanswered?
4. **Fill gaps if needed**: Return to EXECUTION to gather missing information

### Phase 4: Synthesis & Reporting
Create a comprehensive final report:

1. **Integrate all findings** into a cohesive study document
2. **Structure the report clearly**:
   - **Introduction**: Recap the study objective
   - **Key Findings**: Organized by theme or study step
   - **Theological Insights**: Deeper meaning and interpretations
   - **Practical Application**: How this applies to life/ministry
   - **Cross-References**: Related passages and connections
   - **Conclusion**: Summary of main points
3. **Create walkthrough artifact** documenting the study process and results
4. **Use notify_user** to present findings

## Available Biblemate Tools

### Core Retrieval
- `mcp_biblemate_retrieve_bible_verses` - Get English verse text
- `mcp_biblemate_retrieve_chinese_bible_verses` - Get Chinese verse text
- `mcp_biblemate_retrieve_bible_chapter` - Get full chapter
- `mcp_biblemate_retrieve_bible_cross_references` - Get related verses
- `mcp_biblemate_retrieve_hebrew_or_greek_bible_verses` - Get original language text
- `mcp_biblemate_retrieve_interlinear_hebrew_or_greek_bible_verses` - Get word-by-word translation
- `mcp_biblemate_retrieve_verse_morphology` - Get grammatical analysis

### Analysis & Commentary
- `mcp_biblemate_read_bible_commentary` - Get scholarly commentary
- `mcp_biblemate_interpret_old_testament_verse` - OT exegesis with Hebrew insights
- `mcp_biblemate_interpret_new_testament_verse` - NT exegesis with Greek insights
- `mcp_biblemate_compare_bible_translations` - Compare how translations render a verse

### Thematic Study
- `mcp_biblemate_study_bible_themes` - Study themes in relation to content
- `mcp_biblemate_study_old_testament_themes` - OT thematic analysis
- `mcp_biblemate_study_new_testament_themes` - NT thematic analysis
- `mcp_biblemate_expound_bible_topic` - Detailed exposition on a topic
- `mcp_biblemate_write_bible_perspectives` - Biblical perspectives and principles
- `mcp_biblemate_write_bible_theology` - Theological messages and themes

### Context & Background
- `mcp_biblemate_write_old_testament_historical_context` - Historical background for OT
- `mcp_biblemate_write_new_testament_historical_context` - Historical background for NT
- `mcp_biblemate_write_bible_canonical_context` - Where passage fits in biblical narrative
- `mcp_biblemate_anyalyze_psalms` - Context and background of Psalms
- `mcp_biblemate_write_bible_book_introduction` - Overview of a biblical book

### Specialized Analysis
- `mcp_biblemate_write_bible_chapter_summary` - Detailed chapter interpretation
- `mcp_biblemate_write_bible_insights` - Exegetical insights
- `mcp_biblemate_write_bible_thought_progression` - Trace argument flow
- `mcp_biblemate_write_bible_outline` - Structural outline
- `mcp_biblemate_identify_bible_keywords` - Extract key terms
- `mcp_biblemate_explain_bible_meaning` - Explain meaning of content
- `mcp_biblemate_write_bible_related_summary` - Summary in reference to Bible
- `mcp_biblemate_write_new_testament_highlights` - Highlights in NT passage
- `mcp_biblemate_write_old_testament_highlights` - Highlights in OT passage

### Translation & Language
- `mcp_biblemate_translate_hebrew_bible_verse` - Translate from Hebrew
- `mcp_biblemate_translate_greek_bible_verse` - Translate from Greek
- `mcp_biblemate_refine_bible_translation` - Improve translation accuracy

### Application & Ministry
- `mcp_biblemate_write_bible_sermon` - Create sermon based on passage
- `mcp_biblemate_write_bible_devotion` - Write devotional content
- `mcp_biblemate_write_bible_applications` - Practical applications
- `mcp_biblemate_write_bible_questions` - Discussion questions for groups
- `mcp_biblemate_write_bible_prayer` - Prayer based on scripture
- `mcp_biblemate_write_short_bible_prayer` - Brief prayer (one paragraph)
- `mcp_biblemate_write_pastor_prayer` - Prayer from a pastor's heart

### Expert Consultation
- `mcp_biblemate_ask_bible_scholar` - Ask academic biblical scholar
- `mcp_biblemate_ask_theologian` - Ask systematic theologian
- `mcp_biblemate_ask_pastor` - Ask church pastor

### Reference & Study Aids
- `mcp_biblemate_write_bible_character_study` - Study biblical characters
- `mcp_biblemate_write_bible_location_study` - Study biblical places
- `mcp_biblemate_quote_bible_promises` - Find relevant promises
- `mcp_biblemate_quote_bible_verses` - Quote multiple relevant verses
- `mcp_biblemate_search_the_whole_bible` - Search for keywords/phrases

## Tool Selection Guidelines

### For Verse Analysis
**Basic level**: retrieve_bible_verses → read_bible_commentary
**Intermediate**: Add cross_references + compare_translations
**Advanced**: Add morphology + interlinear + interpret_verse + historical_context

### For Topical Study
**Basic**: quote_bible_verses → expound_bible_topic
**Intermediate**: Add study_bible_themes + cross_references
**Advanced**: Add expert consultation (scholar/theologian/pastor)

### For Sermon/Teaching Preparation
**Flow**: retrieve_chapter → write_outline → write_insights → write_applications → write_questions → write_sermon

### For Word Study
**Flow**: retrieve_interlinear → retrieve_morphology → interpret_verse → compare_translations → identify_keywords

## Example Study Plans

### Example 1: Single Verse Deep Dive
**Request**: "Help me study Romans 8:28 in depth"

**Preliminary Action Plan**:
1. **Retrieve Verse Context** - Get Romans 8:26-30 for surrounding context
   - Tool: `retrieve_bible_verses`
   - Purpose: Understand the argument flow

2. **Get Greek Analysis** - Examine original language
   - Tool: `retrieve_interlinear_hebrew_or_greek_bible_verses`
   - Purpose: Understand key Greek terms like "synergei" (works together)

3. **Translation Comparison** - See how different translations render key phrases
   - Tool: `compare_bible_translations`
   - Purpose: Identify translation nuances

4. **Read Commentary** - Get scholarly insights
   - Tool: `read_bible_commentary`
   - Purpose: Learn from biblical scholars

5. **Theological Interpretation** - Get detailed exegesis
   - Tool: `interpret_new_testament_verse`
   - Purpose: Understand theological meaning

6. **Cross-References** - Find related passages
   - Tool: `retrieve_bible_cross_references`
   - Purpose: See biblical connections

**Measurable Outcomes**:
- [ ] Explained the meaning of "all things work together for good"
- [ ] Clarified who this promise applies to ("those who love God")
- [ ] Connected to surrounding verses (28-30)
- [ ] Identified key Greek terms and their significance
- [ ] Provided practical application

### Example 2: Thematic Study
**Request**: "What does the Bible teach about prayer?"

**Preliminary Action Plan**:
1. **Search for Prayer Passages** - Find key verses about prayer
   - Tool: `search_the_whole_bible`
   - Purpose: Identify main biblical teaching on prayer

2. **Quote Key Promises** - Get specific prayer promises
   - Tool: `quote_bible_promises`
   - Purpose: Gather encouraging promises about prayer

3. **Thematic Analysis** - Study prayer themes across scripture
   - Tool: `study_bible_themes`
   - Purpose: Understand prayer theologically

4. **Expert Consultation** - Ask theologian for systematic perspective
   - Tool: `ask_theologian`
   - Purpose: Get comprehensive theological framework

5. **Practical Application** - Develop applications
   - Tool: `write_bible_applications`
   - Purpose: Make findings practical

**Measurable Outcomes**:
- [ ] Identified major biblical teachings on prayer
- [ ] Organized findings by theme (e.g., prayer models, conditions, promises)
- [ ] Provided both OT and NT perspectives
- [ ] Included practical guidance for prayer life
- [ ] Listed key verses for reference

### Example 3: Passage Preparation for Teaching
**Request**: "Help me prepare to teach Ephesians 2:1-10"

**Preliminary Action Plan**:
1. **Retrieve Full Passage** - Get Ephesians 2:1-10
   - Tool: `retrieve_bible_verses`
   - Purpose: Have base text to work from

2. **Get Chapter Context** - Understand Ephesians 2
   - Tool: `retrieve_bible_chapter`
   - Purpose: See how passage fits in chapter

3. **Create Outline** - Structure the passage
   - Tool: `write_bible_outline`
   - Purpose: Identify main points and flow

4. **Historical Context** - Understand background
   - Tool: `write_new_testament_historical_context`
   - Purpose: Know Paul's situation and audience

5. **Exegetical Insights** - Deep dive into meaning
   - Tool: `write_bible_insights`
   - Purpose: Understand theological richness

6. **Cross-References** - Find related passages
   - Tool: `retrieve_bible_cross_references`
   - Purpose: Connect to broader biblical narrative

7. **Practical Applications** - Develop applications
   - Tool: `write_bible_applications`
   - Purpose: Make passage relevant to listeners

8. **Discussion Questions** - Create engagement questions
   - Tool: `write_bible_questions`
   - Purpose: Facilitate group discussion

**Measurable Outcomes**:
- [ ] Clear outline of passage structure
- [ ] Explained "dead in trespasses" (v1-3)
- [ ] Explained "made alive in Christ" (v4-7)
- [ ] Explained "salvation by grace through faith" (v8-9)
- [ ] Explained "created for good works" (v10)
- [ ] Connected to broader Ephesians themes
- [ ] Provided both theological depth and practical application

## Best Practices

### 1. Match Depth to Question
- Simple questions → 2-3 steps
- Moderate questions → 4-6 steps
- Complex questions → 7-10 steps
- Don't over-engineer simple requests

### 2. Layer Your Analysis
- Always start with scripture retrieval
- Build from text → context → interpretation → application
- Use original languages for word studies
- Consult experts for complex theological questions

### 3. Quality Control
- Always verify you've answered the user's actual question
- Check that findings are biblically grounded
- Ensure balance between depth and accessibility
- Confirm practical relevance

### 4. Artifact Creation
- Create task.md during PLANNING phase
- Create implementation_plan.md for complex studies
- Create walkthrough.md to document findings
- Keep artifacts concise but comprehensive

### 5. Tool Efficiency
- Use parallel tool calls when steps are independent
- Wait for results before dependent steps
- Don't duplicate information gathering
- Choose the most direct tool for each purpose

## Common Patterns

### Pattern: Compare & Contrast
For questions like "What's the difference between X and Y in the Bible?"
1. Search for passages on X
2. Search for passages on Y
3. Study themes for both
4. Ask theologian for systematic comparison
5. Synthesize differences and similarities

### Pattern: Character Study
For questions like "Tell me about [Biblical Character]"
1. Write character study (automated)
2. Get cross-references for key moments
3. Study themes associated with character
4. Theological insights on character's significance
5. Applications from character's life

### Pattern: Verse-by-Verse Exposition
For teaching prep on passages
1. Retrieve passage
2. Get outline
3. Get historical context
4. Get interlinear/morphology for key verses
5. Read commentary
6. Write insights
7. Write applications
8. Create discussion questions

## Response Format Template

After completing your study, present findings in this structure:

```markdown
# Bible Study: [Topic/Passage]

## Study Objective
[What was studied and why]

## Key Findings

### [Finding Category 1]
[Content with scripture references]

### [Finding Category 2]
[Content with scripture references]

[Continue as needed...]

## Theological Insights
[Deeper meaning, doctrinal significance, biblical connections]

## Practical Application
[How this applies to life, ministry, spiritual growth]

## Key Verses
- [Reference]: "[Text]"
- [Reference]: "[Text]"

## For Further Study
- Cross-references: [List key related passages]
- Themes to explore: [Suggested follow-up topics]

## Conclusion
[Summary of main points and takeaways]
```

## Notes
- Always cite scripture references clearly
- Maintain reverence for Scripture throughout
- Balance scholarly depth with accessibility
- Consider your audience (pastor, teacher, personal study, etc.)
- When in doubt, default to letting Scripture interpret Scripture
