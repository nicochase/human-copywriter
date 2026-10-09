# Human Copywriter

A focused skill for natural website copy and grounded SEO articles, adapted from Marketing Skills and Humanizer.

**Brief → draft → passage-specific edit → whole-article human voice review → factual/website check.**

Write commercial pages, headlines and CTAs; write or refresh informational articles; edit existing copy; humanize supplied text. Match authentic brand samples when available, with a clear conversational default. Preserve evidence, qualifications, useful headings, citations, links and real offer terms.

This is an editorial workflow, not a claim of improved rankings, conversion rates or AI-detector scores. It does not install marketing integrations or publish content.

## Use

In Codex:

```text
Use $human-copywriter to write a service page for [brand]. Here is the audience, offer and proof: ...
```

In Claude Code:

```text
/human-copywriter Write an SEO article from this brief in our brand voice: ...
```

Or ask naturally to write/edit website copy or SEO articles; the skill supports automatic selection. Supply actual facts, the reader, the action/answer and any voice samples. You can ask for an outline first; otherwise the default is finished copy with essential notes. The skill does not select a model. Live Claude Code checks used the configured Haiku model and Opus at high effort; see the validation notes for results and limits.

## Install locally

Requires Python 3; no additional dependencies. From this repository:

```sh
python3 scripts/manage.py install --client codex
python3 scripts/manage.py install --client claude
```

Codex installs into `$CODEX_HOME/skills/human-copywriter`, falling back to `~/.codex/skills/human-copywriter`. Claude Code installs into `~/.claude/skills/human-copywriter`. `--dest /path/to/skills` selects a different parent directory. Identical installs are a no-op; a different existing skill is not overwritten. Start a new session/turn to discover it; an existing client's reload behavior may vary by version.

## Claude web / Desktop

```sh
python3 scripts/manage.py package
```

Upload `dist/human-copywriter.zip` at **Customize → Skills → + → Create skill → Upload a skill**, then enable it. You can also download the prepared ZIP from [GitHub Releases](https://github.com/nicochase/human-copywriter/releases). Skills/code-execution availability may depend on account or organization settings. ZIP packaging is validated locally; a live upload must be tested in your account. See [Claude's official instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

The archive contains the `human-copywriter/` folder, its instructions, relative resources and license. It excludes this README, scripts, evaluation outputs, Git history and private brand profiles.

## Brand profiles

Use the included [template](skills/human-copywriter/assets/brand-profile.md) when you want a durable profile. Keep one private file per brand at the current project's `.agents/copywriting/brands/<brand>.md`, or attach/paste it in a hosted chat. Local Claude projects can also use `.claude/copywriting/brands/`. Do not create competing copies in both locations. Profiles are not required for a one-off request.

Facts, evidence and voice samples belong in private project inputs, not this reusable repository. With several profiles, name the brand in the request. The skill does not persist profiles automatically.

## Editorial evaluation

For a test or editorial audit, ask for evaluation mode. It retains an initial draft, a critique quoting specific passages, the revised final and a factual comparison. Normal writing still returns finished copy with only material notes. Version 0.2 adds a whole-article rhetorical review, explicit hypothetical-example rules, verbal-quantity checks and stronger use of authentic voice samples. It keeps useful headings and allows good prose to stay unchanged. Version 0.3 targets the cadence that still reads as machine written in careful prose: runs of sentences opening with a command verb, instructions that justify themselves, piles of if/when/where conditions, sections that all share one shape, and briefs turned into checklists. It allows clearly illustrative placeholder names and everyday scenes in examples (never presented as real experience), and it never uses em or en dashes as punctuation.

The skill is guidance, not an enforced multi-call workflow; evaluation artifacts make application inspectable. Separate reviewer execution must be available, authorized and actually performed before it is described as independent.

## Version and validation

Version 0.3.0. Local package validation checks paths, relative resource links and frontmatter shape. Independent forward tests use supplied fictional briefs and assess the resulting writing for fact/meaning preservation, appropriate page type and voice. See [validation notes](VALIDATION.md) for actual results and limits.

```sh
python3 scripts/manage.py check
python3 -m unittest discover -s tests
```

See the [rewritten handoff example](examples/project-handoff.md). It includes an additional editorial pass; it is not untouched model output. The small anonymous version comparison had mixed style results, while checked factual and formatting invariants were preserved.

The installed skill is content-only. Packaging/install scripts are maintenance tools, not required while writing.

## Provenance

See [ATTRIBUTION.md](ATTRIBUTION.md) and [LICENSE](LICENSE). Retains the MIT notices for both upstream repositories. Shared concepts have been selectively rewritten, reconciled and adapted; this is not the complete marketing library and is not endorsed by the upstream authors.

Hosted publicly at [nicochase/human-copywriter](https://github.com/nicochase/human-copywriter).
