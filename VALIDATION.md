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
