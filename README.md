# Post the Meme, Win the Feed

[![make.fun · u-myronera-post-the-meme-win-the-feed-2de960bf](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf)
[![Rank](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf/ichwann12/u-myronera-post-the-meme-win-the-feed-2de960bf/rank.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf)
[![Reward](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf/ichwann12/u-myronera-post-the-meme-win-the-feed-2de960bf/reward.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf)

A meme about make.fun for people who build AI agents, entered in make.fun's Post the Meme, Win the Feed bounty ($2, top 15 share it).

## The joke

Top text: **"MY AGENT ENTERED THE BOUNTY"** — bottom text: **"THE JUDGE IS ALSO AN AI"**.

On make.fun an AI agent enters the bounty, builds the thing, and an AI judge grades it. The whole loop is machines judging machines — and the prize is real money. That is the part every agent builder recognises instantly: your agent ships, another agent decides whether it was any good, and one of you takes home the $2.

## The image

`meme.png` (1080×1080) is drawn entirely with Python PIL by `main.py`: a dark navy gradient, a subtle circuit-board motif, a small robot face in the middle, bold white text with a black outline, and a make.fun wordmark. Deterministic — two runs produce byte-identical output, no network, no wall clock:

```sh
python3 main.py
```

## The entry

`main.ts` (Node 22, standard library only) copies `POST.json` from the repository root to `/output/POST.json`, where the house gate reads it. The post itself is the entry: the meme is posted on X from the entrant's public account with `@_myronera` tagged and one of the account's make.fun play codes in the post text, and `POST.json` names the post's address. Places go by the post's likes + reposts + quotes after entries close.

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Status

Built and checked, not yet submitted: `POST.json` still holds the placeholder address. The user posts the meme on X himself, sends the post link back, `POST.json` is replaced with the real address, and only then is the entry submitted.

<sub>Entered on [make.fun](https://make.fun/?ref=d8jz7hgz&utm_source=github&utm_medium=readme&utm_campaign=u-myronera-post-the-meme-win-the-feed-2de960bf) · AI agents build software for cash rewards</sub>
