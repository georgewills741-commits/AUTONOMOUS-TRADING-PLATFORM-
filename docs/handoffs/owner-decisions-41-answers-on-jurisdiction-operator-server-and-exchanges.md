# Owner Decisions 41 — The answers of 2026-11-19 on jurisdiction, operator, server, and exchanges, with the questions before them

> **Status:** HISTORICAL — source input: the owner's messages of 2026-11-19 after the report of Stage 2's checkpoint A (sent at 15:12 UTC), from 16:57 to 19:26 UTC. From 16:57 to 19:00 UTC they ask what OQ-34's option (c) means, which exchanges serve the United States and why most exclude it, what a server would cost, whether the builder can control one, and whether the work can move between the owner's laptop and cloud environments; they say the owner is not in the United States and will pay for a server; and they ask the builder to set down its questions, which it did at 17:25 UTC and again at 19:00 UTC. At 19:26 UTC the owner answers the builder's five questions: residence in São Tomé and Príncipe; the platform treated, for the current development plan, as a private, single-operator system trading the owner's own authorized capital through the owner's own eligible exchange accounts, still engineered to company-grade standards, with an unfinished clause on others connecting theirs; US$10 to 25 a month as a provisional research ceiling for a server, not an approval to spend, two or three options compared, Germany preferred for Stage 2's development environment and an Asian region such as Tokyo considered, the production location chosen later from measured evidence; option B for the terms of Binance, Bybit, and Coinbase, with what to check and what to do if they stay unreadable; yes to researching other reputable exchanges, the five candidates preserved; and permanent conditions. Applied by [DEC-074](../decisions/DEC-074-owner-answers-on-jurisdiction-operator-server-and-exchanges.md).
>
> **Formatting note:** each of the owner's messages is reproduced inside a text block exactly as received, including the spaces that end some of them and one of their lines. Nothing was added, removed, or changed in them. The builder's five questions, as shown at 19:00 UTC, are reproduced in a text block of four backticks, since they hold a code block of their own. The owner's "Continue" of 14:46 UTC is procedural and is not reproduced ([DEC-047](../decisions/DEC-047-preserve-stage-transition-persistence-rules.md), decision 7). The title, this banner, and the dated headings are the builder's.

## 2026-11-19, 16:57 UTC

```text
What do you mean by that ( C) explain to me what you mean there
```

## 2026-11-19, 17:04 UTC

```text
Please can you elaborate well because I haven't fully understood it yet 
```

## 2026-11-19, 17:11 UTC

```text
What is the US friendly exchanges to use and why do most exchanges exclude US
```

## 2026-11-19, 17:16 UTC

```text
So not in US what price will I pay because I dont want to spend money because you're there on cloud environment you can locate it and continue 
```

## 2026-11-19, 17:20 UTC

```text
Don't worry I will pay but I want to be sure if you can control it because I will not want problem in my project 
```

## 2026-11-19, 17:24 UTC

```text
For now put down all these questions for me so that when I get home I will answer them and give you answers 
```

## 2026-11-19, 18:55 UTC

```text
If I switch to my laptop can I switch back to cloud environment to continue building it there and i switch to another cloud also 
```

## 2026-11-19, 19:00 UTC

```text
No am not switching now

First let answer all the questions put them down for me again 
```

## The builder's five questions, as shown at 19:00 UTC

````text
Here are the five questions again. You can copy the answer template at the bottom.

**1. Which country do you live in?**
If a company will run the platform, also give the country where it is registered.
*Why:* each exchange's rules list the countries it accepts, so this decides which exchanges you can use and where your server should be.

**2. Will you run the platform as a private person or through a company?**
*Why:* some exchanges allow their price data only for personal, non-commercial use.

**3. What's the most you want to pay per month for a server?**
Small servers usually cost about $5 to $25 a month.
*Why:* I'll propose two or three fixed-price servers in your country within that limit, and you approve one before anything is bought.

**4. I couldn't read the rules of Binance, Bybit and Coinbase. Which of these do you prefer?**
- **A:** You open each one's "Terms of Use" page and paste me the part that lists the countries it doesn't serve.
- **B:** You let me try to read them again myself. The session's safety controls blocked me before; if they block me again, we use A.
- **C:** Leave these three out for now, and I continue with the exchanges I can check.

**5. If some exchanges don't accept your country, should I suggest other exchanges that do?**
Yes or no. I would only suggest them; changing the list stays your decision.

---

**Answer template:**

```
1. Country:
2. Person or company:
3. Monthly budget:
4. A, B or C:
5. Yes or no:
```
````

## 2026-11-19, 19:26 UTC: the answers

```text
**STAGE 2 — JURISDICTION, OPERATOR, SERVER & EXCHANGE DECISIONS**

SERIOUS MODE.

Here are my answers to your five questions. Apply them consistently with our existing company-grade requirements, architectural decisions, and stage-verification rules.

**1. Country of residence**

My current country of residence is **São Tomé and Príncipe**.

Do not assume that I reside in another country or that my company is incorporated abroad.

**2. Platform operator**

For the current development plan, treat the platform as a private, single-operator system intended to trade my own authorized capital through my own eligible exchange accounts. and others if they want can connect their 

The platform must still be designed and engineered to company-grade standards, independently operable and maintainable over the long term.

Do not assume that describing it as company-grade means a registered trading company already exists.

**3. Server budget and country**

Use **US$10 to 25 per month as a provisional research ceiling**, not a final approved spending authorization.

Compare two or three reliable cloud-server options, initially including Germany, with an Asian region such as Tokyo considered where appropriate.

Evaluate total monthly cost, RAM, CPU, storage, backups, network charges, reliability, security, Docker/TimescaleDB compatibility, and exchange API connectivity.

My provisional preference is Germany for the initial Stage 2 development environment, subject to verification of required access and resources.

Do not assume that this is the final production trading location.

Before production, use measured exchange latency, legally permitted access, reliability, security, and operational costs to select the most appropriate region.

If the proposed budget cannot support the required workload safely, explain the actual resource requirements and costs. Do not weaken the architecture to meet an arbitrary budget.

Do not purchase or provision paid infrastructure without my explicit approval.

**4. Exchange terms and permissions**

I choose **Option B**.

Try to obtain and verify the current official rules for Binance, Bybit, and Coinbase using approved access methods.

Check restrictions relevant to my actual country of residence, the operator type, allowed trading products, public API access, automated trading, server jurisdiction, and commercial or AI-related market-data usage.

Do not assume public API availability means legal permission for authenticated trading.

If official sources remain inaccessible, do not repeatedly waste tokens. Report the exact missing evidence, provide the relevant official links, and request the necessary documentation or confirmation.

Never use VPNs, proxies, or foreign hosting to misrepresent the operator's location or evade restrictions.

**5. Alternative exchanges**

YES.

You may research additional reputable exchanges if any of our five initial venues are unavailable or unsuitable.

Preserve Binance, OKX, Coinbase, Bybit, and KuCoin as the original candidate set.

Do not silently replace or remove them. Keep unsupported or restricted venues disabled for the affected use, with their status documented.

Any new exchange must pass the existing compliance, security, technical, liquidity, fee, reliability, and integration assessments before approval.

**PERMANENT CONDITIONS**

Preserve the deterministic trading architecture, strict risk controls, global Capital Authority, financial correctness, opportunity discovery, AI authority restrictions, security, recovery, and auditability.

Stage 2 remains public-market-data-focused and read-only. No private account access, trading credentials, or live orders are authorized.

Reuse and enhance existing canonical mechanisms. Do not create duplicates, conflicting rules, additional governance, or unnecessary documentation.

Maintain three-gate verification and durable repository checkpoints.

Reduce unnecessary token consumption and avoid repetitive analysis. Reuse valid evidence and continue from the actual verified stopping point.

**NEXT ACTION**

Resolve these questions through the existing Stage 2 decision process, clearly distinguish VERIFIED, NOT VERIFIED, RESTRICTED, and PENDING OWNER APPROVAL, and proceed only with authorized work.

Provide a concise comparison of suitable server regions and providers before requesting any payment or deployment authorization.

The objective is an extensible, technically efficient, legally compliant, secure, and reliable trading platform—not merely choosing a country because an exchange or server appears accessible.

what i want is the best you must try and reach this goal and no future problems
```
