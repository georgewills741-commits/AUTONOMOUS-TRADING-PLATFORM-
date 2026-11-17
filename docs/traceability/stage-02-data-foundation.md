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
| Files | Each checkpoint's verification record, "Scope" |
| Implementation status | Checkpoint A in progress: U1's readiness check, dependency review, and venue verification done (below) |
| Test status | On the new lockfile, every Stage 1 check passes: lint, formatting, both type checks, 1,108 tests, the documentation checker and its self-test (2026-11-17, 23:50 UTC) |
| Verification 1, 2, 3 | Per checkpoint, in its verification record |
| Security status | No credential is used or held; no venue endpoint has been contacted (venue verification below) |
| Performance status | No baseline exists; none is claimed |
| Documentation status | This record; the developer guide and the specifications as each unit changes them |
| Traceability status | The generated [verification matrix](verification-matrix.md) traces Stage 1's requirements; Stage 2's are added as their code and tests are written |
| Git commit | Each checkpoint's commit is in the [project state](../project-state.md)'s checkpoint log |
| Blockers | No venue is verified for public market data ("Checkpoint A: venue verification", below): the work that needs a venue's live data (U4's live checks and recorded responses, U10's runs) waits for the owner's answer |
| Next stage | CORE TRADING FOUNDATION, after this stage's exit and the owner's approval |

## Checkpoints

| Checkpoint | Units | Status |
|---|---|---|
| A | U1 readiness, dependencies, and venue verification; U2 contracts and configuration; U3 measurement | In progress |
| B | U4 adapters; U5 validation and clock drift | Not started |
| C | U6 storage; U7 the Quantitative Engine with the Fee and Slippage Engines | Not started |
| D | U8 the Market Regime Engine; U9 the Opportunity Detection Engine | Not started |
| E | U10 the process and its baselines; U11 closure | Not started |

## Entry gate, re-checked on 2026-11-17 (master execution constitution §12)

| Condition | Result |
|---|---|
| Prerequisite stage, architecture, contracts, decisions, documentation | As the plan's section 2 records; the owner approved the plan on 2026-11-17 (DEC-073), effective with commit `447290f` |
| Required environment | U1's readiness check, below: what Stage 2 needs is available here, with one difference in how the database image is fetched |
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
| PostgreSQL 16 with TimescaleDB | PostgreSQL 16.15 server programs installed, without TimescaleDB, which the system's package lists do not carry. The image runs PostgreSQL 16.15 with TimescaleDB 2.32.0: the extension was created and reported its version | Available in the container |
| Docker on the machine checks' runners | GitHub's `ubuntu-24.04` runner image, version 20261111.370.1, in the machine checks of `447290f`; its published software list includes Docker Server and Client 28.0.4, Docker Compose 2.38.2, and PostgreSQL 16.15, whose service is off by default | Docker is there. A pull on the runners is first made when U6's database tests run in the machine checks; if Docker Hub refuses it there, the same mirror and digest apply |
| Disk | 28 GB free | Enough for the image (2.6 GB unpacked) |

**The smallest compliant solution.** Nothing is bought and no account, credential, or new service is needed: in a session that runs database tests, the Docker daemon is started with `mirror.gcr.io` as its registry mirror, and the image is named by its digest wherever it is used. This is how the image is fetched, not a change to the approved stack; the developer guide gains the command with U6, the first unit that needs the daemon. No decision or expense needs the owner's approval for it.

## Checkpoint A: versions, dependency review, and licenses (D12)

Versions are fixed in `uv.lock` and `pyproject.toml` ([developer guide](../development.md)); this section is the evidence of the review, not a second list to maintain.

**Choice of versions.** Each package at the newest release published at least a week before the lock, unless a newer one carries a fix for a published advisory: CCXT 4.5.92 (published 13 days before), not 4.5.93 (published the same day), and psycopg 3.3.8 (13 days), not 3.3.9 (5 days). The advisory scan below finds no advisory against either, so neither newer release is needed for a fix. The image is the exception: `2.32.0-pg16` is five days old, and is chosen because it carries PostgreSQL 16.15, the current minor release, which the PostgreSQL project asks every installation to run. A precaution for this lock, not a rule: a later lock is reviewed on its own terms.

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

**The environment's location.** This environment's outbound address is in Council Bluffs, Iowa, in the United States (Google's network), read once from a public address-lookup service on 2026-11-17 at 23:40 UTC; the machine checks run in GitHub's Azure region `westus3`, also in the United States. A venue's terms and the law are therefore checked against access from the United States.

**Method.** For each venue, its published terms and its API documentation, read on 2026-11-17 after 23:41 UTC by a separate page-reading agent per venue, legal and documentation pages only: no API endpoint, no account, no credential. Where a page could not be read, it was not fetched again. A second reading by other routes (the remainder of KuCoin's terms, OKX's region list, and archived copies of the pages that refused automated reading) was refused by this session's permission controls and was not attempted another way.

| Venue | Terms checked | Endpoint, date, result | Status for public market data | Trading eligibility |
|---|---|---|---|---|
| Binance | Terms of Use (`binance.com/en/terms`): the page's text is drawn by the browser and did not come back; the API documentation (last modified 2026-11-17) says Binance's products are subject to those terms and gives `data-api.binance.vision` for public market data, with nothing on locations | None: no request made | **Disabled**: the terms are unread | Not established |
| OKX | From the United States, `okx.com` serves the terms of OKX's United States platform (last updated 2026-10-29). Its risk disclosure (last updated 2026-11-14) says OKX "may restrict or prohibit use of all or a portion of the Services from Restricted Locations", naming "certain jurisdictions within the United States of America including all U.S. territories such as Puerto Rico". Its API agreement (last updated 2026-07-28): "Public Market Data endpoints are accessible without an API Key but remain subject to this Agreement" (3.2(a)); "You may access and use Market Data solely for your own personal, non-commercial trading and account management purposes" (9.4); eligibility includes "applicable age, residency, and jurisdictional requirements" (2.1) | None: no request made | **Disabled**: which United States jurisdictions are restricted is unread, the global platform's terms were not served from here, and the use the agreement allows depends on the operator | Not established |
| Coinbase | Market Data Terms of Use (`coinbase.com/legal/market_data`): refused automated reading (HTTP 403). The documentation says "Market Data APIs provide market data and are public" and "By accessing the Exchange Market Data API, you agree to be bound by the Market Data Terms of Use"; it gives the public endpoints `GET /time` and `GET /market/products` under `api.coinbase.com/api/v3/brokerage`, for which "A JWT is not required" | None: no request made | **Disabled**: the terms that govern the data are unread | Not established |
| Bybit | Terms of Service: the page answered HTTP 503; the API introduction says nothing on locations or accounts | None: no request made | **Disabled**: the terms are unread | Not established |
| KuCoin | Terms of Use (last updated 2026-10-29): "Users must register with the Platform before they may access the Platform services" (Art. 11), real-time quotations being among those services (Art. 24(2)); a user declares that it "is not a resident of or registered in, any of the Restricted Locations", which include "the United States (including its territories such as Puerto Rico, Guam, the Northern Mariana Islands, American Samoa, etc)" (Art. 17(5)) | None: no request made | **Disabled**: the terms read require registration before access to its services and exclude residents of the United States | Not established |

**Result.** No venue is verified for public market data, and no venue endpoint has been contacted: every venue stays disabled, its status recorded, as the owner decided (DEC-073, decision 3). Adding a venue later needs no platform change (EXA-006). What would resolve each is owner-level information or a reading the builder could not do from here: the operator's jurisdiction (KuCoin's and OKX's terms turn on residence, and OKX's allowed use on the operator), a human reading of the terms that refused automated reading (Binance, Coinbase, Bybit), and, for the venues whose terms exclude access from the United States, an environment located where their terms and the law permit it, which this one is not.

## Checkpoint A: CCXT findings (D5)

From CCXT 4.5.92's own code, with network use refused during the inspection; nothing was requested from a venue.

- **Amounts.** CCXT's unified fields are floats: its `Exchange.number` is `float`, and `parse_number` converts with it. A response is decoded with `orjson` (`on_json_response = staticmethod(json_parser.loads)`), and CCXT's own comment says its option `quoteJsonNumbers` "is ignored in python". So in a response's raw `info`, an amount the venue sends as a JSON string keeps the venue's text, and one sent as a JSON number is already a float. Under D5, an adapter takes amounts only from the venue's text: where a venue sends JSON numbers, U4 decodes the raw body itself or uses TEC-005's native-client exception, recorded. Which venues send which is confirmed on recorded responses, once a venue is verified.
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
