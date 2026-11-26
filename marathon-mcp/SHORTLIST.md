# awesome-mcp-servers, filtered for Marathon GC

Source: github.com/punkpeye/awesome-mcp-servers (pulled Nov 26, 2026, about 1,400 entries). Judged on one question: does it bring in a lead, raise the close rate, raise the ticket, bring a customer back, or get cash collected?

## Installed by the kit
| Server | Why |
| --- | --- |
| modelcontextprotocol/server-filesystem | Job photos, plans, bids folder |
| Thx93/mcp-weather-server | Free NWS forecasts and alerts (snow trigger) |
| Kentucky-ai/opentakeoff | Plan takeoff for bids. **Note:** the project moves to a new format Dec 1, 2026. Takeoff stays free, but expect an update. |
| LienDeadline/liendeadline-mcp | Free state lien guides. Deadline calculator needs a paid key and is built for suppliers. |
| microsoft/playwright-mcp | GBP, Nextdoor, Meta Business Suite, any site without a connector |
| cablate/mcp-google-map (optional) | Storm routes, prospect lists, geocoding |

## Worth adding later, when the business is ready
| Server | When | Cost / catch |
| --- | --- | --- |
| localseodata/mcp-server | Once you're tracking the 25-review goal and map rank across Fall River, Somerset and Swansea | Paid API key |
| HagaiHen/facebook-mcp-server | If you want Claude to read Page comments and draft replies outside Meta Business Suite | Python setup and Page token. Adspirer already covers ads. |
| vibecodebeast/swath-mcp | Hail and wind history by address. Useful if you add roofing or storm-damage repair. | Check pricing |
| malonestar/gov-data-mcp | FEMA flood and EPA site checks before demolition or additions | Free Apify token |
| XeroAPI/xero-mcp-server | Only if you move bookkeeping to Xero | Xero account |
| io.github.opsconduit/jobber-mcp | Only if you adopt Jobber for scheduling and invoicing | Jobber account |
| MarceauSolutions/hvac-quotes-mcp | Only if you take on HVAC subs | — |

## Skipped on purpose
- **Gmail, Sheets, Calendar, Drive, Workspace servers (~45):** your claude.ai connectors already do this, signed in to the right account.
- **Social schedulers (Postiz-style, ~10):** your rules say Facebook groups are manual and every post needs your OK. Meta Business Suite scheduling already covers it.
- **Procore, Korean/Russian construction codes, federal (SAM.gov) bidding:** wrong size or wrong market.
- **License verifiers (WA, CA only):** they don't cover MA.
- **"Pay-per-call x402" gateways:** crypto micropayments. No need.
- **Lead scrapers and skip-tracing tools:** risky for a local brand (spam laws, reputation). Use Leadfeeder plus the Google Maps prospect list instead.
- **Remaining ~1,300 entries:** developer, crypto, gaming and other servers with no tie to revenue.
