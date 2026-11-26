# Marathon GC: Claude Desktop tool kit

I went through all ~1,400 servers in [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) and kept the few that help Marathon's one goal: **booked, collected revenue at a healthy margin.** The rest are skipped on purpose (see `SHORTLIST.md`).

## What you already have (don't install again)

Your claude.ai account already connects these, and they also work in Claude Desktop:
Gmail, Google Calendar, Google Sheets (Marathon Leads), Google Drive, AccuWeather, Leadfeeder, Canva, Adobe, Meta and Google Ads (Adspirer), Gusto, Zapier, Notion. Your **Marathon GC Agent** and **Bid Estimator** skills are there too.

Many servers on the list just repeat these (about 30 Gmail servers, 10 Google Sheets servers). They're skipped.

## What this kit adds to your desktop

| Server | What it does for Marathon | Revenue lever | Key needed? |
| --- | --- | --- | --- |
| **marathon-files** | Claude can read and write `Documents/Marathon` (Bids, Plans, Job Photos, Contracts, Marketing). Drop site photos or a plan PDF in, then ask for a quote or a post. Nothing outside that folder. | Quotes within 24 hrs, content multiplier | No |
| **nws-weather** | National Weather Service forecasts and active MA alerts. Free, official, no account. Feeds the 7 a.m. snow alert and the storm-day checklist. | Snow & Ice storm prep | No |
| **plan-takeoff** | Reads plan PDFs and measures square footage and linear feet for bids. Runs on your computer; nothing is uploaded. | Faster, accurate good/better/best quotes | No |
| **lien-guides** | Massachusetts lien rules and statute citations (free guides). Use it when a customer won't pay. | Collected cash | No for guides |
| **browser** | Claude drives a browser window for sites with no connector: Google Business Profile posts and review replies, Nextdoor, Meta Business Suite, MA license lookups. It asks before posting. | Reviews, GBP, Nextdoor cadence | No |
| **google-maps** *(optional)* | Plans storm routes street by street, finds property managers, HOAs and churches in the service area, and geocodes the lead list. | Street density, high-value accounts | Google Maps API key |

## Install (about 5 minutes)

You need **Claude Desktop** (claude.ai/download) and **Node.js 20+** (the installer gets it for you).

1. Download this folder: GitHub > branch `claude/dreamy-heisenberg-l0gvdw` > **Code > Download ZIP**, then unzip it.
2. Open `marathon-mcp/install` and run the installer for your computer:
   - **Windows:** right-click `install-windows.ps1` > **Run with PowerShell**.
   - **Mac:** open Terminal, type `bash ` (with a space), drag `install-mac.sh` into the window, then press Enter.
3. **Fully quit** Claude Desktop (Windows: system tray icon > Quit. Mac: Cmd+Q) and open it again.
4. In a new chat, click the tools/connectors icon. You should see the five servers. The first start of each takes a minute while it downloads.

The installer backs up your existing config, never removes anything, and you can run it again safely.

**Optional, Google Maps:** create a key at console.cloud.google.com (enable Places, Geocoding, Routes; set a budget alert). Then run the installer again with the key:
- Windows (PowerShell, from the install folder): `$env:GOOGLE_MAPS_API_KEY="YOUR_KEY"; .\install-windows.ps1`
- Mac: `GOOGLE_MAPS_API_KEY=YOUR_KEY bash install-mac.sh`

## Try these first

- "Morning list." (Leads sheet + NWS forecast for Fall River)
- "Is 2 inches or more forecast for Fall River in the next 48 hours? If yes, give me the storm-day checklist and customer text."
- "I put kitchen photos and notes in Marathon/Bids/Smith. Build a good/better/best quote with the margin check."
- "Take off the deck plan in Marathon/Plans/deck.pdf: square footage, railing linear feet, stair count."
- "Open my Google Business Profile and draft replies to any unanswered reviews. Show me before posting."
- "What are the Massachusetts mechanic's lien deadlines for a residential GC?"
- *(Maps)* "List 15 property management companies within 10 miles of Fall River with phone numbers, and draft a snow + repairs intro."

## Ground rules this kit keeps

- Claude only sees the Marathon folder, not the rest of your computer.
- The browser tool posts or sends only after you say OK, as your GC Agent rules require.
- Keep Howard Home Solutions out of it. If the browser opens signed in to a Howard account, sign out and use the Marathon Gmail.
- Lien guides are reference only, not legal advice. Before you file anything, check with a MA attorney.
