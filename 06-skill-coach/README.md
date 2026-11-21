# CCAR-F Skill Coach, cohort edition

`ccarf-coach` is a Claude Code skill: a study coach that quizzes you, explains the Claude
stack in exam terms, recaps any cohort chapter, reads your practice exam result, and walks
you through the labs. It loads by itself when you ask Claude Code for any of those.

## Install

Recommended: in the root of this repository, so the coach can open the labs by path.

```bash
cd Claude-Code-Certified-Architect-Foundation-CCAR-F-Certification-Bootcamp
mkdir -p .claude/skills
cp -r 06-skill-coach/ccarf-coach .claude/skills/
claude
```

Or for every project on your machine:

```bash
cp -r 06-skill-coach/ccarf-coach ~/.claude/skills/
```

Check it loaded: ask Claude Code "quiz me on domain 2".

## What to ask it

| You say | It does |
|---|---|
| "Quiz me on domain 4" / "a question on task 1.3" / "quiz me on Chapter E" | One exam-style item, answer hidden until you reply, then the evidence, why it wins, why each distractor fails, the chapter that teaches it, and a running score |
| "Explain PreToolUse for the exam" / "tool use vs MCP" | The decision the exam tests, the mechanism, the classic distractor, where a lab shows it, the official docs |
| "Recap Chapter H" | The chapter's decisions as short rules, its slides and lab, then two quiz items |
| "Here is my practice exam result" (paste the summary from Copy result summary) | Your domains ordered by exam weight, the chapters and labs for each missed task, and a revision plan |
| "Walk me through Lab 3" / "run the quick win" | Step by step: what to watch before each command, what it showed after |

It never writes new items on the fly, and it never reveals items from the practice exam, the
clinic, the homework or the simulated exam: those stay unspoiled for your own attempt.

## What changed from the webinar edition

The webinar's starter kit shipped a three-mode coach built around one refund demo. Fitting it
to the cohort's two days needed these changes:

| Area | Webinar edition | Cohort edition | Why |
|---|---|---|---|
| Modes | Quiz, explain, demo guide | Quiz, explain, **labs guide**, **chapter recap**, **result reading** | The cohort has nine chapters, six labs and a 60-item practice exam to connect |
| Quiz bank | 30 items, one per task statement | The same 30, each tagged with the cohort chapter that teaches its task | A wrong answer now points to the chapter to revisit |
| Demo guide | The starter kit's refund demo | `labs-guide.md`: the quick win step by step plus all six labs, each mapped to its chapter | The cohort's code is the six course labs, not only the demo |
| Stack explainer | "In this kit" pointed to starter-kit files | "In the cohort labs" points to `03-labs/` and the chapter that teaches it | Paths must resolve in the cohort folder |
| Chapter map | none | `cohort-map.md`, generated from the running order and each chapter's "What you will learn" slide | Recaps follow what each chapter promised, not what the coach improvises |
| Spoiler rule | none needed | Never reproduces practice exam, clinic, homework or sim items | Those sets lose their value once seen |
| Result reading | none | Reads the apps' "Copy result summary" text | The practice exam is the final-week tool; the coach turns its result into a plan |

The 30 quiz-bank items and the cohort's 94 new items (60 practice exam, 6 clinic, 12
homework, 16 simulated exam) were written separately and checked against each other for
overlap, so practising with the coach does not spoil the practice exam.
