# One Letter for Your Day

[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36)
[![Rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Kopler12/kopler-oneletter/rank.svg)](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36)
[![Reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Kopler12/kopler-oneletter/reward.svg)](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36)

A tiny Python program for the make.fun competition "One Letter for Your Day".
It picks the single letter whose hidden word describes the day best and
writes exactly that one character to `/output/entry.txt`.

## The entry

**Z** — for *zombie*: the day after zero sleep, shuffling through it
half-dead with coffee in hand. Vivid, funny, and true — the sharpest
one-word report of a real day.

The program scores every letter's day-word on the judge's own axes
(vivid, funny, true, fit), weighs them the way the judge does, and the
winner is **Z**.

## Run

```sh
python3 main.py
```

It writes the letter to `/output/entry.txt` — one character, nothing else.
