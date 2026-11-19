# Stage 2 — DATA FOUNDATION: Stage Record

> **Status:** ACTIVE stage record (master execution constitution §142; format: [traceability README](README.md)). Created at the start of checkpoint A on 2026-11-17, as U11 of the [Stage 2 plan](../roadmap/stage-02-data-foundation-plan.md) (APPROVED, [DEC-073](../decisions/DEC-073-stage-2-plan-approved-with-changes.md)) provides, and updated at each checkpoint. Each checkpoint's three gates are in its own verification record; this record holds the stage's status and the evidence its units produce.

## Stage

| Field (§142) | Now |
|---|---|
| Stage ID | 2 — DATA FOUNDATION |
| Purpose | The plan's section 1 |
| Dependencies | Stage 1, complete ([DEC-067](../decisions/DEC-067-stage-1-exit-and-owner-answers-of-2026-11-10.md)); the entry gate re-checked below |
| Requirements | The plan's section 3: delivered (3.1), started (3.2), applied as design rules (3.3), applied in later stages (3.4), not built (3.5) |
| Systems affected | SYS-01, SYS-02, SYS-03 with the Fee and Slippage Engines, SYS-04, SYS-05, SYS-29's drift detection, and the cross-cutting modules of the plan's D4 |
| Files | Each checkpoint's verification record, "Scope": [checkpoint A verification](stage-02-checkpoint-a-verification.md) |
| Implementation status | Checkpoint A built: U1, the readiness check, the dependencies and their review, and the venue verification; U2, SYS-02's contracts and Stage 2's settings; U3, the measurement framework (below) |
| Test status | 1,432 tests, all passing, with every other check of the developer guide, on checkpoint A's tree ([checkpoint A verification](stage-02-checkpoint-a-verification.md), "Checks"); before U2 and U3, every Stage 1 check passed on the new lockfile, 1,108 tests among them (2026-11-17, 23:50 UTC) |
| Verification 1, 2, 3 | Per checkpoint, in its verification record |
| Security status | No credential is used or held; the database's password appears only as the name of a declared secret (SEC-005); no venue endpoint has been contacted (venue verification below) |
| Performance status | No baseline exists; none is claimed. U3's framework measures and sets no target (V-45, V-46) |
| Documentation status | This record; the developer guide's records of the new settings (MIG-034); the contract conventions, the numerical policy, the technology stack, the architecture-to-repository map, and the values register (V-41's note, V-45, V-46); the roadmap and the project state |
| Traceability status | The generated [verification matrix](verification-matrix.md) lists Stage 2's markers as their code and tests are written: `atp.marketdata`, `atp.measurement`, and their tests and the settings' at checkpoint A. Its check of delivered requirements reads the Stage 1 plan only, until U11 extends it to Stage 2's |
| Git commit | Each checkpoint's commit is in the [project state](../project-state.md)'s checkpoint log |
| Blockers | No venue is verified for public market data ("Venue verification for the operator's country", below; OQ-34 of the [open-question register](../open-questions/register.md)): the work that needs a venue's data (U4's adapter, recorded responses, and live checks for each venue; U10's runs) waits for the rest of OQ-34: the owner's approval of a server, and each venue's verification |
| Next stage | CORE TRADING FOUNDATION, after this stage's exit and the owner's approval |

## Checkpoints

| Checkpoint | Units | Status |
|---|---|---|
| A | U1 readiness, dependencies, and venue verification; U2 contracts and configuration; U3 measurement | Built; its three gates are in its verification record, [checkpoint A verification](stage-02-checkpoint-a-verification.md) |
| B | U4 adapters; U5 validation and clock drift | Not started |
| C | U6 storage; U7 the Quantitative Engine with the Fee and Slippage Engines | Not started |
| D | U8 the Market Regime Engine; U9 the Opportunity Detection Engine | Not started |
| E | U10 the process and its baselines; U11 closure | Not started |

## Entry gate, re-checked on 2026-11-17 (master execution constitution §12)

| Condition | Result |
|---|---|
| Prerequisite stage, architecture, contracts, decisions, documentation | As the plan's section 2 records; the owner approved the plan on 2026-11-17 (DEC-073), effective with commit `447290f` |
| Required environment | U1's readiness check, below: the tools and services Stage 2 needs are available here, with one difference in how the database image is fetched; access to the venues' public market data is the venue verification's question, below |
| Python | 3.12.3, the system interpreter, as in Stage 1 |
| Package index and advisory database | Both reachable: pypi.org, and the OSV service (api.osv.dev), which Stage 1 could not reach |

## Checkpoint A: environment readiness (D2)

Checked on 2026-11-17 between 23:30 and 23:41 UTC, before any work that depends on infrastructure, as the owner required (DEC-073, decision 4). Each configuration was tried once; the one that failed was not tried again.

| Need | Found | Result |
|---|---|---|
| uv 0.12.23 | 0.11.32 on the path; 0.12.23 installed from the Python package index into a separate tool environment, as the [developer guide](../development.md) describes | Available |
| A Docker daemon (testcontainers, D11) | Docker Engine 29.9.2 installed, not running when the session starts; started by hand, it was ready within 4 seconds (overlay storage, cgroup v1), and a container's port published on 127.0.0.1 answered | Available, started in each session |
| Docker Compose (D7's development services) | Compose v5.6.1 | Available |
| The TimescaleDB image, by digest | Docker Hub refused the pull with `429 Too Many Requests`, its limit on pulls without an account, counted per network address, which this environment shares; the network proxy reported no failure of its own. Docker Hub's catalogue gives `timescale/timescaledb:2.32.0-pg16`, published on 2026-11-12, as the index digest `sha256:2f87efeaec6fbdd3ba4a6993b921c05d069cd8e980792cb23c7c5f32a6fe68a7`. Google's public mirror of Docker Hub, `mirror.gcr.io`, serves the same index under the same digest; the daemon, started with that mirror, pulled the image by digest in 25 seconds | Available through the mirror. The digest is a hash of the content, so the image is the one Docker Hub publishes whichever registry serves it |
| PostgreSQL 16 with TimescaleDB | PostgreSQL 16.15 server programs installed, without TimescaleDB, which the system's package lists do not carry. The image runs PostgreSQL 16.15 with TimescaleDB 2.32.0: the extension, which the image creates in its default database, reported its version | Available in the container |
| Docker on the machine checks' runners | In the machine checks of `447290f` the two jobs ran on different hosts: the job `secrets` on GitHub's `ubuntu-24.04` image 20261111.370.1 in Azure's `westus3`, whose published software list includes Docker Server and Client 28.0.4, Docker Compose 2.38.2, and PostgreSQL 16.15, whose service is off by default; the job `checks` on the image 20261111.127.1 in AWS's `us-west-2`, for which no software list was published when read on 2026-11-18 | Docker is on the job `secrets`' image; on the job `checks`' image, which runs the tests, it is confirmed when U6's database tests first run there; if Docker Hub refuses the pull, the same mirror and digest apply |
| Disk | 28 GB free | Enough for the image (2.6 GB unpacked) |

**The smallest compliant solution.** Nothing is bought and no account, credential, or new service is needed: in a session that runs database tests, the Docker daemon is started with `mirror.gcr.io` as its registry mirror, and the image is named by its digest wherever it is used. This is how the image is fetched, not a change to the approved stack; the developer guide gains the command with U6, the first unit that needs the daemon. No decision or expense needs the owner's approval for it.

## Checkpoint A: versions, dependency review, and licenses (D12)

Versions are fixed in `uv.lock` and `pyproject.toml` ([developer guide](../development.md)); this section is the evidence of the review, not a second list to maintain.

**Choice of versions.** Each of the six packages this change adds directly (CCXT, DuckDB, OpenTelemetry's API and SDK, psycopg, testcontainers) is at the newest release published at least a week before the lock, unless a newer one carries a fix for a published advisory: CCXT 4.5.92 (published 13 days before), not 4.5.93 (published the same day), and psycopg 3.3.8 (13 days), not 3.3.9 (5 days). The advisory scan below finds no advisory against either, so neither newer release is needed for a fix. Of the 35 packages the lock adds, 25, those six among them, are at that release; the other ten are at releases their dependents require exactly: CCXT 4.5.92 pins nine, each older than the newest release published a week before the lock (cffi 2.0.0, charset-normalizer 3.4.7, idna 3.18, multidict 6.9.1, propcache 0.5.2, pycparser 3.0, uvloop 0.22.1, winloop 0.6.3, zlib-ng 1.0.0), and OpenTelemetry's SDK 1.45.2 pins its semantic conventions at the pre-release 0.66b2. The advisory scan covers each as locked. The 19 packages of Stage 1's lock are unchanged, newer releases or not, since an upgrade is not mixed with unrelated work (constitution Rule 101). The image is the exception: `2.32.0-pg16` is five days old, and is chosen because it carries PostgreSQL 16.15, the current minor release, which the PostgreSQL project asks every installation to run. A precaution for this lock, not a rule: a later lock is reviewed on its own terms.

**Review method (U1; constitution Rules 99 to 102; master execution constitution §40).** For each of the 54 locked packages, PyPI's JSON record of that exact release, read on 2026-11-17: its declared license. Then one scanner run, not added to the project: pip-audit 2.10.1, run with `uvx`, against the OSV database, on the hashed requirements that `uv export` gives for the lockfile, at 23:46 UTC.

| Package | Version | Use | License |
|---|---|---|---|
| ccxt | 4.5.92 | Runtime (TEC-005) | MIT |
| aiohttp, aiohappyeyeballs, aiohttp-fast-zlib, aiosignal, attrs, frozenlist, multidict, propcache, yarl | 3.14.5, 2.7.1, 0.3.0, 1.4.0, 26.1.0, 1.8.0, 6.9.1, 0.5.2, 1.25.1 | Runtime, through CCXT | Apache-2.0 AND MIT, PSF-2.0, Apache-2.0, Apache-2.0, MIT, Apache-2.0, Apache-2.0, Apache-2.0, Apache-2.0 |
| requests, urllib3, idna, charset-normalizer, certifi | 2.34.2, 2.8.0, 3.18, 3.4.7, 2026.10.23 | Runtime, through CCXT (requests and urllib3 also through testcontainers) | Apache-2.0, MIT, BSD-3-Clause, MIT, MPL-2.0 |
| cryptography, cffi, pycparser, coincurve | 50.0.2, 2.0.0, 3.0, 21.0.0 | Runtime, through CCXT (coincurve on 64-bit CPython before 3.14) | Apache-2.0 OR BSD-3-Clause, MIT, BSD-3-Clause, MIT OR Apache-2.0 |
| orjson, zlib-ng, uvloop, winloop | 3.13.0, 1.0.0, 0.22.1, 0.6.3 | Runtime, through CCXT (uvloop not on Windows; winloop on Windows only) | MPL-2.0 AND (Apache-2.0 OR MIT), PSF-2.0, MIT, MIT |
| duckdb | 2.0.0 | Runtime (TEC-006) | MIT |
| psycopg, psycopg-binary | 3.3.8 | Runtime, the PostgreSQL driver (D12) | LGPL-3.0-only |
| tzdata | 2026.6 | Runtime, through psycopg, on Windows only | Apache-2.0 |
| opentelemetry-api, opentelemetry-sdk, opentelemetry-semantic-conventions | 1.45.2, 1.45.2, 0.66b2 | Runtime (TEC-010) | Apache-2.0 |
| testcontainers | 4.15.0 | Development (TEC-009) | Apache-2.0 |
| docker, python-dotenv, wrapt, pywin32 | 7.2.0, 1.2.4, 2.5.2, 312 | Development, through testcontainers (pywin32 on Windows only) | Apache-2.0, BSD-3-Clause, BSD-2-Clause, PSF |

The packages locked at Stage 1 are unchanged, at the versions and licenses in the [Stage 1 record](stage-01-foundation.md)'s dependency review.

**Result:** no published advisory affects a locked version: pip-audit audited 50 packages and skipped none (the other four are Windows-only, and the scan runs where they are not installed), with no vulnerability found. Every license is permissive, except:

- **LGPL-3.0-only** for psycopg and psycopg-binary. The platform imports the library unchanged; the licence's obligations apply when the library is distributed with another work (its notice, and a way for the recipient to replace it), which running the platform does not do. If the platform is ever distributed, they are met then. psycopg-binary carries its own build of libpq (18.0.6, which works with a PostgreSQL 16 server), so the libpq in use is the one the lockfile fixes on every machine; psycopg's documentation advises a build linked to the system's libpq for a production site, a choice that belongs to OPERATIONALIZATION's deployment, as a dependency change under the developer guide's rules.
- **MPL-2.0**, a file-level copyleft that applies to changes to those packages' own files, for certifi and part of orjson; neither is changed.

**The image's license.** TimescaleDB is under the Apache License 2.0 outside its `tsl` directory, and under the Timescale License inside it ([the repository's license file at 2.32.0](https://github.com/timescale/timescaledb/blob/2.32.0/LICENSE)). The Timescale License grants use "solely for Your own internal business purposes in a manner that does not expose or give access to, directly or indirectly (e.g., via a wrapper), the Timescale Data Definition Interfaces or the Timescale Data Manipulation Interfaces to any person or entity other than You or Your employees and Contractors working on Your behalf" (section 2.1(a)), and prohibits offering it as a database service (section 2.2). The image starts with the Timescale License's features on (the setting `timescaledb.license` is `timescale`). Stage 2 needs only features under the Apache License: hypertables, and `drop_chunks` for V-18's retention, the archive being compressed as Parquet (TEC-012). So U6 starts the server with `timescaledb.license=apache`, and a later stage that needs a Timescale License feature records that decision first.

## Checkpoint A: strict typing and warnings (D12)

Checked on 2026-11-17 in a scratch copy of the project with the new lockfile, under the project's settings: strict mypy, and pytest with warnings as errors.

| Package | Strict mypy | Imports with warnings as errors |
|---|---|---|
| CCXT 4.5.92 (`ccxt`, `ccxt.async_support`, `ccxt.pro`) | Refused: the package ships no type information (`import-untyped`) | Pass |
| psycopg 3.3.8 | Pass, the asynchronous connection included: D12's "typed and asynchronous" holds on the locked version | Pass |
| DuckDB 2.0.0; OpenTelemetry 1.45.2 | Pass | Pass |
| testcontainers 4.15.0 | Pass | Pass for `testcontainers.core` and `testcontainers.community.postgres`; the old module `testcontainers.postgres` raises a `DeprecationWarning` and is not used |

**CCXT's exception, as D12 provides.** CCXT fails strict mypy, so the exception is confined to `atp.exchange`: when U4 writes the first adapter, mypy is told to treat CCXT as untyped for the module `ccxt` only, CCXT's values are typed at the adapter's boundary before anything else sees them, and the structure test keeps CCXT inside `atp.exchange` (TEC-005). No exception is needed for warnings.

## Checkpoint A: venue verification (D1)

**The environment's location.** This environment's outbound address is in Council Bluffs, Iowa, in the United States (Google's network), read once from a public address-lookup service on 2026-11-17 at 23:40 UTC; the machine checks of `447290f` ran in the United States too, the job `secrets` in Azure's `westus3` and the job `checks` in AWS's `us-west-2`. A venue's terms and the law are therefore checked against access from the United States.

**Method.** For each venue, its published terms and its API documentation, read on 2026-11-17 after 23:41 UTC by a separate page-reading agent per venue, legal and documentation pages only: no API endpoint, no account, no credential. Where a page could not be read, it was not fetched again. A second reading by other routes (the remainder of KuCoin's terms, OKX's region list, and archived copies of the pages that refused automated reading) was refused by this session's permission controls and was not attempted another way.

| Venue | Terms checked | Endpoint, date, result | Status for public market data | Trading eligibility |
|---|---|---|---|---|
| Binance | Terms of Use (`binance.com/en/terms`): the page's text is drawn by the browser and did not come back; the API documentation (last modified 2026-11-17) says Binance's products are subject to those terms and gives `data-api.binance.vision` for public market data, with nothing on locations | None: no request made | **Disabled**: the terms are unread | Not established |
| OKX | From the United States, `okx.com` serves the terms of OKX's United States platform (last updated 2026-10-29). Its risk disclosure (last updated 2026-11-14) says OKX "may restrict or prohibit use of all or a portion of the Services from Restricted Locations", naming "certain jurisdictions within the United States of America including all U.S. territories such as Puerto Rico". Its API agreement (last updated 2026-07-28): "Public Market Data endpoints are accessible without an API Key but remain subject to this Agreement" (3.2(a)); "You may access and use Market Data solely for your own personal, non-commercial trading and account management purposes" (9.4); eligibility includes "applicable age, residency, and jurisdictional requirements" (2.1) | None: no request made | **Disabled**: which United States jurisdictions are restricted is unread, the global platform's terms were not served from here, and the use the agreement allows depends on the operator | Not established |
| Coinbase | Market Data Terms of Use (`coinbase.com/legal/market_data`): refused automated reading (HTTP 403). The documentation says "Market Data APIs provide market data and are public" and "By accessing the Exchange Market Data API, you agree to be bound by the Market Data Terms of Use"; it gives the public endpoints `GET /time` and `GET /market/products` under `api.coinbase.com/api/v3/brokerage`, for which "A JWT is not required" | None: no request made | **Disabled**: the terms that govern the data are unread | Not established |
| Bybit | Terms of Service: the page answered HTTP 503; the API introduction says nothing on locations or accounts | None: no request made | **Disabled**: the terms are unread | Not established |
| KuCoin | Terms of Use (last updated 2026-10-29): "Users must register with the Platform before they may access the Platform services" (Art. 11), real-time quotations being among those services (Art. 24(2)); Art. 17(5) requires that the user "is not a resident of or registered in, any of the Restricted Locations", which include "the United States (including its territories such as Puerto Rico, Guam, the Northern Mariana Islands, American Samoa, etc)" | None: no request made | **Disabled**: the terms read require registration before access to its services and exclude residents of the United States | Not established |

**Result.** No venue is verified for public market data, and no venue endpoint has been contacted: every venue stays disabled, its status recorded, as the owner decided (DEC-073, decision 3). Adding a venue later needs no platform change (EXA-006). What would resolve each is owner-level information or a reading the builder could not do from here, put to the owner as OQ-34: the operator's jurisdiction (KuCoin's and OKX's terms turn on residence, and OKX's allowed use on the operator), a human reading of the terms that refused automated reading (Binance, Coinbase, Bybit), and, for any venue whose terms exclude access from the United States but permit the operator's own, an environment located where its terms and the law permit that access; never as a way around a restriction of residence or location (no proxy, no other region: the plan's U1; DEC-073, decision 3). The owner answered on 2026-11-19 ([DEC-074](../decisions/DEC-074-owner-answers-on-jurisdiction-operator-server-and-exchanges.md)); the verification for the operator's country follows.

## Venue verification for the operator's country (D1)

**The operator.** An individual resident in São Tomé and Príncipe, trading the owner's own capital through the owner's own accounts, as PLT-010 states ([owner decisions 41](../handoffs/owner-decisions-41-answers-on-jurisdiction-operator-server-and-exchanges.md); [DEC-074](../decisions/DEC-074-owner-answers-on-jurisdiction-operator-server-and-exchanges.md)). Each venue's terms and the law are checked against that operator, and against access from Germany, the owner's provisional preference for where Stage 2's live work runs (below).

**Method.** Option B, the owner's choice: each venue's official legal and documentation pages read again on 2026-11-19 from 19:30 UTC, by a separate page-reading agent per venue; each URL fetched once, and a page that failed not fetched again, as the owner asked; no API endpoint, account, credential, archived copy, or third-party site. The pages were served to this environment, in the United States. The law of São Tomé and Príncipe: one web search.

| Venue | Pages read | The operator's country | Germany; Japan | Public market data and its use | Status for public market data | Trading eligibility |
|---|---|---|---|---|---|---|
| OKX | Terms of Service (last updated 2026-10-29; read in part, the rest summarized by the reader), API agreement (last updated 2026-07-28), Risk and Compliance Disclosure (last updated 2026-11-14); served with OKX's United States platform in their metadata, the terms naming Aux Cayes FinTech Co. Ltd. (Seychelles) as the contracting party for the other eligible users | Not among the Restricted Locations, which the disclosure lists as current (its section 3): Afghanistan, Canada, Cuba, Hong Kong, Iran, India, Japan, Malaysia, Nepal, North Korea, Syria, the Crimea, Donetsk, and Luhansk regions of Ukraine, Uzbekistan, and certain jurisdictions of the United States; OKX may restrict others | Japan restricted; Germany not named | Public endpoints need no API key but stay subject to the agreement (3.2(a)); market data only for the user's own personal, non-commercial trading and account management, not redistributed, and not used to train an AI system meant to be commercialized; no automated scripts, bots, or web scrapers extracting data at a rate beyond what the user's personal trading reasonably needs (9.4) | **Terms: VERIFIED from the pages read, served with OKX's United States metadata**, for the operator's own trading. **Endpoint: not checked**, waiting for the server the owner approves (Germany, the owner's provisional preference; PENDING OWNER APPROVAL). The law of the operator's country: NOT VERIFIED. Stays disabled | Not established. API trading for the user's own account is permitted (3.3, 3.4(b), 9.3), after OKX's identity verification (2.2); orders for third parties need OKX's written approval (9.3(c)) |
| KuCoin | Terms of Use (last updated 2026-10-29; read to 39,950 of its 88,923 characters, Article 17 in the part read, the rest summarized by the reader); its API introduction answered HTTP 404 | Not among the Restricted Locations of Article 17(5), in the reader's paraphrase: the United States and its territories, Singapore, mainland China and Hong Kong, Malaysia, Kazakhstan, Uzbekistan, Russia, Belarus, Ontario and British Columbia, France, the Netherlands, and the Crimea, Donetsk, Luhansk, Zaporizhzhia, and Kherson regions | Neither named | Registration required before access to its services (Article 11); real-time quotations only for registered users (Article 24) | **RESTRICTED for Stage 2**: its data needs an account, which Stage 2 does not authorize (DEC-073, decision 5) | Not established |
| Binance | Terms of Use and Prohibited Use Policy: only the pages' navigation came back, their text drawn by the browser; its legal index: links only; its API changelog: no terms | Unknown | Unknown | Unknown | **NOT VERIFIED**: disabled | Not established |
| Bybit | Terms of Service: HTTP 503; its API introduction: no terms | Unknown | Unknown | Unknown | **NOT VERIFIED**: disabled | Not established |
| Coinbase | Market Data Terms, User Agreement, and a help page on availability: HTTP 403; its developer documentation's landing page: no terms | Unknown | Unknown | Unknown | **NOT VERIFIED**: disabled | Not established |

**Other venues, researched at the owner's request and not added.** Kraken: its global terms (last updated 2026-11-18, read in part) apply to residents outside Brazil, Canada, and the European Economic Area, name sanctioned jurisdictions but not São Tomé and Príncipe, and leave eligibility to Kraken's discretion; its API terms were not read: NOT VERIFIED. Bitget: both pages tried answered HTTP 404: NOT VERIFIED. A venue is added only after the compliance, security, technical, liquidity, fee, reliability, and integration assessments the owner named, D1's verification, and the owner's approval (DEC-074, decision 3); EXA-006 keeps its addition to a new adapter and its configuration.

**The law of São Tomé and Príncipe.** One web search on 2026-11-19 found no notice of its central bank (Banco Central de São Tomé e Príncipe) on crypto-assets; one regulation-comparison site says the country has no specific regulation, though its pages conflict. NOT VERIFIED: the owner is asked to confirm (OQ-34).

**Result.** No venue is verified for public market data yet, and no venue endpoint has been contacted. OKX's terms permit its data for the operator: its endpoint is checked from the server the owner approves (Germany, the owner's provisional preference), once it is provisioned, and the venue is enabled only once the law of the operator's country is confirmed too. KuCoin stays restricted for Stage 2. Binance, Bybit, and Coinbase wait for their terms, which the owner is asked to provide: Binance's Terms of Use and Prohibited Use Policy (`binance.com/en/terms`, `binance.com/en/about-legal/prohibited-use-policy`), Bybit's Terms of Service (`bybit.com/en/help-center/article/Terms-of-Service`), and Coinbase's Market Data Terms and User Agreement (`coinbase.com/legal/market_data`, `coinbase.com/legal/user_agreement`), with the list of countries each serves.

## Hosting options for Stage 2's live work (D2)

**What the work needs.** One host running Docker Compose (TEC-011), with PostgreSQL 16 and TimescaleDB, market data kept 30 days there and then in compressed Parquet archives (TEC-012), the collectors of the verified venues, and the measurement framework; an x86 Linux server, the builder's choice. The builder's ESTIMATE, not a measurement: 2 vCPUs, 4 GB of memory, and 80 GB of disk carry the first venue and a limited set of markets; the server's processor, memory, and storage use is to be measured before more venues or deeper books are enabled (MIG-005), which may need 4 vCPUs and 8 GB. The location must be in none of the verified venues' Restricted Locations: Germany is in none read, Japan is in OKX's, and France and the Netherlands are in KuCoin's. Latency from Germany to each venue is not measured: U10 measures it on the server, and production's location is chosen later from measurements (D2).

**Offers read on 2026-11-19** from the providers' official price pages, by one reading agent; Vultr's page answered HTTP 403, and Akamai's plan table was not read:

| Provider and location | Server | Monthly price | Backups | Traffic |
|---|---|---|---|---|
| Hetzner, Nuremberg or Falkenstein (Germany) | CPX22: 2 shared AMD vCPUs, 4 GB, 80 GB NVMe | €19.99 before VAT (Nuremberg) | Priced with the server, from €1.098 a month for its smallest; CPX22's amount not on the pages read | 20 TB included |
| Hetzner, Helsinki (Finland) | CPX22, the same | €16.99 before VAT | The same | 20 TB included |
| DigitalOcean, Frankfurt | Basic: 2 vCPUs, 4 GiB, 80 GiB SSD | US$24.00 | 20% of the price for weekly, 30% for daily (US$4.80 or US$7.20) | 4,000 GiB; inbound free |
| AWS Lightsail, Frankfurt | 2 vCPUs, 4 GB, 80 GB SSD | US$24 (US$20 without a public IPv4 address) | Snapshots at US$0.05 per GB a month | 4 TB; inbound not charged |
| Tokyo | Not compared | — | — | Not suitable for Stage 2: OKX restricts Japan |

Not compared: the providers' reliability and security, which the owner asked to have evaluated (owner decisions 41, answer 3); no page on either was read. Traffic beyond the allowance: Hetzner €1.00 per TB before VAT; Lightsail's page gives US$0.09 per GB as an example; DigitalOcean's page does not state it.

The next sizes up: Hetzner's CPX32 (4 vCPUs, 8 GB, 160 GB NVMe), €35.99 in Nuremberg; DigitalOcean's 4 vCPUs and 8 GiB, US$48; Lightsail's 2 vCPUs and 8 GB, US$44. Neither DigitalOcean's nor Lightsail's page states a price by region.

**Recommendation: PROPOSED, PENDING OWNER APPROVAL.** Hetzner's CPX22 in Nuremberg, Germany (Falkenstein's price not on the pages read), with its automatic backups: €19.99 a month before VAT, plus the backups, about the owner's ceiling of US$25 depending on the exchange rate and the backups' price; or the same server in Helsinki for €16.99, if a location outside Germany is acceptable. Reasons: the most traffic included, an NVMe disk, and €19.99 against US$24 before backups for the others. The owner orders the server on the owner's own account; the builder buys nothing and holds no billing access (DEC-073, decision 6; DEC-074, decision 4). Once it is approved, the server's setup is written in the repository and verified through the three gates: login by key only, a firewall admitting only the operator's own access, automatic security updates, and no secret in the repository.

## Checkpoint A: CCXT findings (D5)

From CCXT 4.5.92's own code, with network use refused during the inspection; nothing was requested from a venue.

- **Amounts.** CCXT's unified fields are floats: its `Exchange.number` is `float`, and `parse_number` converts with it. A response is decoded with `orjson` (`on_json_response = staticmethod(json_parser.loads)`), and CCXT's own comment says its option `quoteJsonNumbers` "is ignored in python". So in a response's raw `info`, an amount the venue sends as a JSON string keeps the venue's text, and one sent as a JSON number is already a Python number, a float where it has a fraction or an exponent and an int otherwise, never the venue's text. Under D5, an adapter takes amounts only from the venue's text: where a venue sends JSON numbers, U4 decodes the raw body itself or uses TEC-005's native-client exception, recorded. Which venues send which is confirmed on recorded responses, once a venue is verified.
- **Streams and data CCXT declares** (its `has` table, not verified against any venue):

| CCXT class | REST: time, markets, ticker, trades, book, OHLCV | REST: funding rate | WebSocket: ticker, trades, book | WebSocket: OHLCV | WebSocket: funding rate | Market types |
|---|---|---|---|---|---|---|
| `binance` | Yes | Yes | Yes | Yes | Not declared | Spot, swap, margin |
| `okx` | Yes | Yes | Yes | Yes | Yes | Spot, swap, margin |
| `coinbase` | Yes | No | Yes | No | Not declared | Spot, swap |
| `coinbaseexchange` | Yes | No | Yes | No | Not declared | Spot |
| `bybit` | Yes | Emulated | Yes | Yes | Not declared | Spot, swap, margin |
| `kucoin` | Yes | Yes | Yes | Yes | Yes | Spot, swap, margin |
| `kucoinfutures` | Yes | Yes | Yes | Yes | Yes | Swap |

## Checkpoint A: U2, the contracts and the settings

**SYS-02's contracts** (`atp.marketdata`; ARCH-025, EXA-013, MKD-005, MKD-010, HLT-014). Fourteen contracts at version 1.0, each with its committed schema under `contracts/`: the market and an item's lineage; market metadata (the venue's symbol, status, increments, and minimums); ticker; trade; book level, book snapshot, and book update (with the venue's sequence numbers that place it); OHLCV bar; funding rate; venue state; and this system's quality assessment, quarantine record, and record of untranslatable input. Each item names its market, or its venue, the venue's event time where it gives one with that time's resolution, the local receipt time, its evidence identifier, and its lineage (D5). Times are integer nanoseconds since the Unix epoch, UTC, refused below zero or beyond a signed 64-bit integer; amounts are `Amount`, a float or JSON number refused; identifiers are checked against patterns. Evidence identifiers (MKD-005) are sha256 digests of the form `atp.evidence/1` over the venue, the stream, the market, and the venue's own key of the item, or, where the venue gives none, the item's event time and a digest of its content, so the same item received twice has the same identifier. Their inputs are checked first (a venue's name, the market's venue, a market for every stream but the venue's status and none for it, a whole-number event time in range, text for the key and the content), so that malformed inputs cannot give one item another identifier; where an item is identified by its content, the adapters (U4) give its event time wherever the venue gives one, since the same content given with and without it gets two identifiers. An item of a margin market's book, trades, ticker, or bars names its spot market: the same item named under both gets two identifiers.

**Stage 2's settings** (`atp.config`; MIG-010, MIG-034, SEC-005). Version 1.1 of both parts of the configuration, adding settings whose defaults keep a 1.0 document's meaning: in the portable part, `market_data`, with the venues and instrument types monitored (D1), each venue's published fee schedules with their source and date (D8), and the regime timeframes (D9); in the environment-specific part, `database` (its address, database, user, and the name of the declared `server` secret that holds the password) and `archive_directory`. Each setting's record (MIG-034) is in the [developer guide](../development.md)'s "Configuration", and each rule has a test that refuses a document breaking it. The examples name no venue (GOV-017), and each environment's gives a database at a host of the reserved `.invalid` domain.

**Tests:** 231 for the contracts and 18 for evidence identifiers (`tests/marketdata/`), 40 for the settings (`tests/config/test_stage_2_settings.py`); the schema snapshots of every contract (`tests/contracts/test_schemas.py`); `atp config check` passes on every example (`tests/cli/test_cli.py`).

## Checkpoint A: U3, the measurement framework

`atp.measurement` (PERF-008, PERF-009, PERF-010, PERF-018, PERF-020, TEC-010), built first so that the later units are measured as they are built:

- **Points:** a name, one of PERF-009's paths that Stage 2's code runs on (market data; the detection part of the arbitrage and directional paths; monitoring), and a component.
- **The recorder:** durations on the monotonic clock; delays from a venue's event time to local receipt on the wall clock, marked unreliable while the local clock's drift is beyond its limit, which the caller reports (`atp.health` from checkpoint B); queue depth and the time items waited; counts of errors and of shed work. Samples go into a buffer of fixed capacity: when it is full, a sample is dropped and counted, and the call returns at once.
- **Exact statistics:** p50, p95, p99, p99.9, and the maximum, as nearest-rank percentiles on integers, so each figure is one of the samples; a percentile is reported only with enough samples (V-45); jitter is the same figures over the absolute differences between consecutive samples.
- **OpenTelemetry metrics**, on the cold path: histograms with fixed bucket edges (V-46), a gauge of queue depth, and counters of errors, shed work, dropped samples, and delays below zero, which the clocks' disagreement can give and a histogram cannot hold, so that none is lost.

No target is set. **Tests:** 34 (`tests/measurement/`), and the agreement of V-45 and V-46 with the values register (`tests/repository/test_values.py`).

## Checkpoint A: builder details and plan wording

Choices the plan left to implementation, and one plan item moved to a later unit. None changes a requirement or a decision.

| Item | What was done | Why |
|---|---|---|
| D10's budgets | Not added at checkpoint A: the per-venue budget of depth subscriptions and the scan frequency are added with U9, as a further minor version of the portable configuration. U2's other settings are added | The plan's U2 names "universe bounds and budgets, D10", but their meaning is designed with the Opportunity Detection Engine and their values come from measurement (D10). The universe's bounds are the enabled venues and instrument types (OPP-009), which U2 adds; exclusions are the Policy System's (CORE). A budget defined before its consumer could need a major version once U9 is designed, while a minor version can add it later with a default |
| What the contracts check | Structure only: types, forms, and fields that belong together (an event time and its resolution, a perpetual and its settlement asset, a book update's first and last sequence numbers, an unavailable venue and its cause) | A well-formed but implausible item reaches SYS-02's validation and is quarantined with its evidence (MKD-009, MKD-013), never refused unseen at the adapter |
| The fields the plan gives each contract | Each item a venue gives (market metadata, ticker, trade, book snapshot and update, OHLCV bar, funding rate) carries its event and receive times, its market, which names the venue, its evidence identifier, and its lineage; a venue's state carries the venue in place of a market. This system's records about an item refer to it instead of repeating it: the quality assessment by its evidence identifier, the quarantine record by its evidence identifier with its venue, market, and stream. An untranslatable input, which has no translated item, carries its venue, stream, lineage, and receive time, and its content's digest and length in place of an evidence identifier | The plan's U2 gives each contract these fields (D5); an item's times and lineage are kept once, on the item (constitution Rule 42), and input that could not be translated has no event time or market to give |
| Margin markets | A margin market is described by its metadata; its book, trades, ticker, and bars are its spot market's | A venue publishes one book per spot pair, which margin trading uses (PLT-011) |
| Lineage | The venue's endpoint or channel, and the adapter and its version; the validation version is carried by the validated item (U5) | MKD-010's other parts (dataset, feature, strategy, and policy versions) belong to the calculations and decisions of later units |
| Jitter | The distribution of the absolute differences between consecutive samples, with the same figures as the samples (the delay variation of RFC 3393) | PERF-010 names jitter without defining it; this definition is exact on integers and needs no float or mean |
| Percentiles | Nearest-rank, with at least one sample beyond a reported percentile (V-45) | Exact; the plan's "p99.9: at least 1,000" extends to each percentile by the same rule |
| Integer division | `atp.measurement._statistics` is listed in the structure test's `INTEGER_DIVISION_ALLOWED`; it refuses any value that is not a whole number | It divides only integers, to find a rank, as N4 of the [numerical policy](../architecture/numerical-policy.md) provides for such a module |
| The recorder | Used from the process's event loop, not shared between threads; a full buffer drops the new sample | One process (TEC-008); keeping the oldest samples means a burst cannot erase what came before it, and each drop is counted |
| Fee rates | Maker above -1 and below 1, below zero a rebate; taker from 0 to below 1; written as text | Maker rebates exist; a rate of 100% or more is no fee schedule; amounts are text in configuration (N6) |
| Dates in configuration | Text, YYYY-MM-DD, checked to be a date that exists | The loader refuses TOML dates, and Pydantic's date type would also read a Unix timestamp written as text ([contract conventions](../architecture/contracts.md)) |
| The database's password | The name of a secret declared with the kind `server`, checked against the environment's declarations | SEC-005: a secret's value comes only from the process environment |
| The examples' layout | Each environment file's database table comes before its secret declarations | The repository test for secrets plants a value at the end of each environment example, beside the declaration it expects there; this layout keeps that test's assumption, so the test was not changed |

## Carried to later units

- **Checkpoint B (U4):** the mypy exception for CCXT, confined to `atp.exchange` ("Checkpoint A: strict typing and warnings"); per venue, from recorded responses, whether CCXT gives amounts as the venue's text ("Checkpoint A: CCXT findings"); the adapter, recorded responses, and live checks of each venue only after its verification: OKX's endpoint checked from the server the owner approves (Germany, the owner's provisional preference), the other venues once their terms and the law are verified ("Venue verification for the operator's country"; [open-question register](../open-questions/register.md), OQ-34); the rule that an item of a margin market's book, trades, ticker, or bars names its spot market, enforced where the adapters, or `evidence_id`, take the market ([checkpoint A verification](stage-02-checkpoint-a-verification.md), J-27).
- **Checkpoint B (U5):** a quarantine record's market checked against its stream, as `evidence_id` checks it: a market for every stream but the venue's status, and none for it (J-28); the exporter's tests of a delay measured on a reliable clock, exported as reliable, and of a delay well below zero, beside the boundary of -1, with a mutation entry that makes the reliability label constant (J-32).
- **Checkpoint C (U6):** the developer guide's command to start the Docker daemon with Google's mirror ("Checkpoint A: environment readiness"); Docker on the job `checks`' runner, which runs the tests, and the first pull of the image there; the server started with `timescaledb.license=apache`, or instead Docker Hub's `2.32.0-pg16-oss` tag (`sha256:3aa1fb6faff8928f220e343b83536752d6649aaa0352f0daba43504e2a96762d`, pushed 2026-11-12), once what that build contains is confirmed ("Checkpoint A: versions, dependency review, and licenses"); testcontainers' module `testcontainers.community.postgres` or `testcontainers.core`, not the deprecated `testcontainers.postgres`; and, if `atp.marketdata`'s tables and migrations need `atp.storage`, which reads `atp.config`, the names of venues and instrument types moved first to a module both may import, since `atp.config` imports them from `atp.marketdata`.
- **Checkpoint D (U9):** D10's budgets (above).
