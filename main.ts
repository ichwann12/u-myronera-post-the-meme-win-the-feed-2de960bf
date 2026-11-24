// Entry program for the "Post the Meme, Win the Feed" bounty.
// Node 22, standard library only. The graded program is deliberately tiny:
// it hands the house the address of the X post that carries the meme by
// copying POST.json into the output directory. The post itself is the entry,
// and nothing written here about it is scored.
//
// To run it the way the grader does, point MAKEFUN_BOT_DIR at this folder
// and MAKEFUN_OUTPUT_DIR at an empty folder, then run node main.ts.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const raw = readFileSync(join(botDir, "POST.json"), "utf8");
const post = JSON.parse(raw);
if (typeof post.url !== "string" || !post.url.startsWith("https://")) {
  throw new Error("POST.json must hold a post address under https://");
}
// A placeholder address is still a string under https://, so the copy
// succeeds and the house gate refuses it later as "no such post" — that is
// the correct behaviour until the real post address is written in.

mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "POST.json"), raw);
