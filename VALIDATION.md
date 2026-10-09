# Version 0.3.0 validation

October 9, 2026.

## Why this version

An anonymous AI writing checker scored the v0.2 handoff sample at 65 percent "AI-like signals." The checker is kept anonymous on purpose so the skill is not tuned to one tool. Its findings were editorial rather than vocabulary based: every paragraph followed instruction, reason, qualification; sentence openings repeated (Include, Link, Record, Keep); sections shared one shape; coverage was even, like a checklist; conditionals piled up; and examples felt generated rather than observed.

## Changes

- Humanizer: a new instructional rhythm review covering opening streaks, instructions that justify themselves, conditional pileup, explaining the obvious, sections that share one shape, and even coverage, with a before and after example.
- Examples: clearly illustrative placeholder names, weekdays and recognizable everyday scenes are now allowed. Illustrations still may not be presented as real events, and first person anecdotes, case studies, testimonials, customer stories and results remain banned. v0.2 had stripped exactly this kind of placeholder from the sample.
- SEO articles: a brief's topic list is coverage, not the outline or the weighting.
- Default voice: plain observations and stated opinions alongside instructions.
- No em or en dashes as punctuation in any voice, with exceptions only for exact quotes, proper names, URLs and code. A new unit test fails if the skill files themselves contain either character.
- Test brief 09 (inbox cover during leave) targets instructional rhythm.

Package check passes (ten skill files). All five unit tests pass.

## Blind comparison

Two subagents with the same model and settings each read one frozen skill copy (v0.2 from the previous commit, v0.3 candidate) and wrote final copy only. v0.2 wrote briefs 01, 05, 06, 07 and 09; v0.3 wrote all nine. A third agent read only anonymous pairs and the briefs, with X/Y assignment alternating by brief, and judged natural voice, usefulness and integrity.

| Brief | Winner | Judge confidence | Deciding observation |
| --- | --- | --- | --- |
| 01 Handoff | v0.3 | Medium | v0.2 ran eight imperative sections with the same shape; v0.3 grouped topics, varied shape and used placeholder sample lines. |
| 05 Bike repair shop | v0.3 | Low | Better voice; v0.2 was somewhat more useful on parts choices. Near tie. |
| 06 Client feedback | v0.3 | Medium | v0.2 opened four sections with "Ask"; v0.3 started from the problem. |
| 07 Author voice | v0.3 | High on voice fit | v0.3 kept the supplied first person voice; v0.2 turned it into a command sequence. |
| 09 Inbox cover | v0.3 | Low | v0.2 repeated instruction, "For example," sample line in three sections. |

The judge found no invented statistics, research, case studies, testimonials or first person events in any of the ten pieces, and no missing brief topic. On usefulness the two versions were close; where v0.2 won on usefulness it was the more thorough version, not the better voiced one.

Factual fixtures, v0.3 only, checked by hand: brief 02 kept the six studio pilot scope, median 50 to 35 minutes, August 2026, 14 day trial, card required and $19/month renewal unless canceled (it ran under length because the brief gives no product capabilities, and it still spends two sentences on the pilot caveat). Brief 03 kept the id, href, "over 3,000," the capacity condition and the exact customer quote; it reworded "Same-day repairs" and "Customer comment:" around them. Brief 04 was returned unchanged. Brief 08 kept every condition and the exact URL.

## Limits

One judge, one sample per brief, all agents from the same model family, each writer producing its briefs within one session. The writers ran with the maintainer's personal settings loaded, which include a no hyphen and no dash rule, so this comparison cannot show the effect of the skill's own dash rule; neither version used dashes. Five wins out of five is directional evidence, not a benchmark. No detector was rerun by the maintainer within this record.

## New sample article

`examples/project-handoff.md` is the v0.3 output for brief 01, unedited. Unlike the v0.2 sample, it received no additional editorial pass.

## Prior version record

# Version 0.2.0 validation

October 9, 2026.

## Changes and package checks

Added a whole-piece rhetorical review, explicit hypothetical-example rules, verbal-quantity and causal-strength checks, more specific voice analysis, and optional inspectable evaluation artifacts. Ordinary writing still delivers final copy without a mandatory audit. A follow-up correction distinguishes removing a slogan from merely paraphrasing it, and prevents repeating caution to fill commercial copy.

The Skill Creator validator, local resource/link check and all four package/installer tests pass. The package contains ten skill files, including the new evaluation reference. The installer implementation and its overwrite protections are unchanged.

## Eight-brief comparison

Two separate Codex subagents, with the same inherited model/effort settings, received identical frozen briefs and equivalent artifact instructions. One read a frozen v0.1.0 skill, the other the initial v0.2.0 candidate. Each produced all eight cases within a single session; briefs were not run as sixteen isolated calls. This can introduce within-session carryover. Neither author received the intended answer or the other version's outputs.

A third agent read only anonymous final-copy pairs, with A/B assignments alternating, and judged usefulness, factual integrity, natural prose and scope. On decoding the labels, it preferred v0.1 in four cases, the candidate in one, and tied three identical outputs. This is one subjective review with one sample per case, not evidence that v0.2 generally improves style. Both versions retained all checked offer terms, HTML, exact quote, URLs, advice conditions and clean copy; the reviewer found no invented evidence. The baseline also labeled its fictional example appropriately when explicitly asked.

| Case | Initial comparison observation |
| --- | --- |
| Handoff article | Both covered the brief and labeled the hypothetical example; baseline responsibility wording was preferred. |
| Commercial section | Both preserved pilot scope, median, date, card requirement, renewal and cancellation condition. Both repeated trial deliberation and underexplained the offer, which was sparse in the brief. |
| HTML/service excerpt | Both left the clear input, exact quote, lower bound, conditional availability, anchor and link unchanged. |
| Clean paragraph | Both correctly retained it unchanged. |
| Bike repair article | Both covered the five topics without invented shops, tests or terms; baseline phrasing was preferred. |
| Client feedback article | Candidate examples were preferred for illustrating errors versus preferences. |
| Author-voice exercise | Both preserved the supplied information; baseline was preferred for rhythm and phrasing. |
| Advice versus company promise | Both preserved the conditional questions and exact terms URL. |

The frozen fictional briefs are in `tests/writing-briefs.json`. These are manual behavioral fixtures, not automated quality assertions. The anonymous review and full generation artifacts are retained locally outside the installable skill. No detector, search ranking or conversion tests were performed.

## Follow-up findings

A live Claude Code Opus/high-effort rewrite used the candidate files through read-only tools, with hooks and MCP disabled. It retained draft, passage-specific critique, revised final and comparison. The first final removed named fictional colleagues and the unsupported “half” claim, but paraphrased a slogan rather than resolving it and retained unsupported certainty. This demonstrated that even an explicit self-check is insufficient evidence of success. Two short contextual examples were added to the Humanizer reference. The commercial reference was also clarified to avoid repeating caution to fill a target length. Only the affected probes were rerun; the eight-brief anonymous comparison above describes the initial candidate, not the final corrected package.

The focused commercial rerun reduced repeated caution to one pilot qualification and preserved every supplied term. It deliberately returned a shorter section because the brief did not supply a product category or capabilities; useful full-length offer copy still requires those facts. The targeted slogan probe returned direct advice about a short main note, linked background and named ownership without predicting guaranteed failure or success. Both are informed follow-ups within the same candidate session, not blind comparisons.

Both installed copies were checked against the frozen v0.1 inventory before replacement, backed up in the local test workspace, and then compared byte-for-byte against all ten source files. No locally modified skill was overwritten.

## Rewritten sample article

The second Claude pass repaired the opening, paraphrased slogan, fictional names/dates and several claims of certainty, but its self-comparison still incorrectly asserted that no numbers or quotes existed. The final sample therefore received an additional root-assistant editorial pass and a separate agent review, rather than being represented as untouched skill output. The final reviewer found no material issue. Its final text has 548 whitespace-separated words including title and headings. It uses one explicitly hypothetical vague/better pair, role descriptions in the example, and instructions to supply actual reviewer/request/deadline details. No detector has been run. The sample is in `examples/project-handoff.md`, outside the installable package.

Both live Claude calls completed without tool permission denials. Model: Opus alias, high effort. These calls read candidate files directly, not through installed slash discovery; installed discovery was previously checked for v0.1. User setting context remained enabled, so they were not fully context-isolated. The final sample demonstrates an assisted editorial workflow, not guaranteed one-pass skill compliance.

## Prior version record

# Version 0.1.0 validation

October 9, 2026.

## Package and installer

- Skill Creator's frontmatter validator passed. Its PyYAML dependency was provided in an isolated tool environment; the writing skill and local installer require no Python packages.
- Local package check passed: nine skill files, with all bundled relative resource links resolving inside the package.
- Four automated checks passed: deterministic ZIP bytes and exact extracted resources; install/file verification and identical reinstall; refusal to replace a differing local skill or symlink; rejection of a missing reference.
- Installed copies in Codex and Claude Code were compared byte-for-byte with the source. No pre-existing skills were overwritten.

## Independent writing tests

Two independent agents read the skill and relevant resources with no review history or intended answers. They used fictional supplied briefs, without browsing or publishing. The resulting texts were manually reviewed against the inputs.

| Case | Observed behavior |
|---|---|
| Commercial hero and benefits | Kept six-studio pilot scope, median 50→35 minutes and August 2026 date. Stated 14-day trial, required card, $19/month renewal unless canceled. No invented guarantee or universal performance promise. |
| Humanize a service excerpt | Kept “over 3,000,” conditional same-day availability, all three services, exact testimonial, heading anchor and link target. Replaced empty hype with supplied concrete services. |
| SEO article from a supplied brief | Covered the five provided decision checks with relevant headings and title/meta description. No invented tests, provider rankings, metrics or sources. |
| Polish clean copy | Left the supplied paragraph unchanged instead of forcing a rewrite. |

One usability issue surfaced: a routine “no research conducted” note appeared even though the user explicitly requested brief-only writing. The SEO reference now distinguishes a material unmet research request from a deliberately brief-only task. Re-running that case produced a 351-word article with no routine disclaimer.

## Live Claude Code check

Claude Code 2.1.224 recognized `/human-copywriter` from its personal skill installation. An initial overly isolated run had disabled the user setting source and therefore did not discover personal skills; enabling the user source resolved that test configuration issue.

The configured default model, Haiku 4.5, initially suggested converting reader advice into an unsupported company promise. The entrypoint and Humanizer reference now explicitly protect the speaker and advice-versus-promise distinction, including suggested alternatives. Re-running with the default model and with Opus 5 at high effort retained the original clean paragraph and did not add a business promise. Both completed without tool permission denials.

These client tests used only read/skill tools, with hooks and MCP connections disabled for those runs. They did not change the user's default model or settings. Opus still returned more explanatory commentary than the skill requests, influenced by the existing personal context; output brevity remains model/context-dependent. The probes establish discovery and this small behavioral check, not comprehensive Claude quality.

These are small behavioral checks, not a statistical writing-quality benchmark. They do not establish SEO improvement, conversion lift, personal-voice fidelity across brands, or superiority to the upstream skills. Real brand profiles and user feedback are the next source of improvement.

## Client limitations

Claude web/Desktop ZIP structure is checked against current official upload guidance, but no live upload has been performed. Codex's next-turn discovery and automatic selection have not been observed from a fresh client session. Local file installation alone is not proof of automatic invocation.
