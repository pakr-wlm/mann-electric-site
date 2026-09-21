# Mann Electric and Generator Services, LLC (Washington, GA): Website

The old presence is Facebook-only — no standalone website at all, despite 27+ years of electrical
experience and 21+ years specializing in Generac generators. That's the outreach angle: a real,
professional homepage to show what's possible, standing in for the site they've never had.

Edit `index.src.html` / `styles.css`, run `python build.py`.

## How this build differs from a normal run

This session had no browser/Chrome tooling (no `navigate`, `get_page_text`, `javascript_tool`, etc.)
and direct site fetches were blocked by this environment's network policy, so the usual intake steps
(load their site, harvest real photos, click through Google Maps reviews) could not run. Everything
below was gathered via text search only. No fact was invented to fill the gap — sections that needed
photos, review quotes, hours, an address, or an email that couldn't be sourced were reduced or dropped
instead (see "Not used" below).

## Real data used (each with its source)

- Business name, phone (706) 338-8509 — Facebook page and multiple post ads
- "Been in business 23 years with 27+ years of electrical experience and 21+ years of Generac
  generator experience" — verbatim from a Facebook post
- "CLASS II LICENSED ELECTRICIAN" — same Facebook post
- "Mann Electric Achieves 100% Score on Generac Dealer/Technician Recertification" — Facebook video title
- "residential electrical and Generac generator needs" — Facebook ad copy (source for the two service
  categories used; no more granular service list was published anywhere found)
- 5.0★ rating from 2 reviews — Facebook page listing (no review text was available to quote; see below)
- City/zip Washington, GA 30673 — Indeed job listing for the business
- First name "Steve" as the person to ask for — Facebook ad ("Call Steve today")
- Facebook page URL — used as `sameAs` in the JSON-LD

## Still placeholders / stock

- **Hero, about, and all 4 gallery photos** are the skill's credited stock set (`assets/*.jpg`), not
  Mann Electric's own work — no photos could be harvested this session (no browser access to their
  Facebook photos or their HubSpot page). Swap for real job/generator photos before this goes live.
- **Logo**: no logo file was found; using the base bolt-badge stand-in.
- **Reviews section**: dropped entirely rather than shown with invented quotes. Facebook shows 5.0★
  from 2 reviews, but no review text was retrievable without browser access — that aggregate number
  is used in the stats bar and footer only, with no fabricated testimonial quotes.
- **Contact form email**: `TO_EMAIL` is intentionally empty (see verify_site.py WARN). No published
  email address was found for this business anywhere searched.

## Conflicts to confirm

- **Street address**: not confirmed by any two sources — only city/zip (Washington, GA 30673) is
  published. The service-area map is centered on the city, not a specific address, per the skill's
  conflict rule.
- **Hours**: none published anywhere found. No hours are shown on the site; don't imply 24/7 or
  business hours without confirming with the owner.
- **A prospect URL was supplied mid-build**
  (`https://mann-electric--generator-service-llc-45133434.hubspotpagebuilder.com/en-us/`) but could not
  be loaded — direct fetch was blocked by this environment's network policy and it isn't search-indexed.
  If this is a real site the business is building, it may contain their own photos, real hours, a real
  address, and an email that should replace the stock/placeholder content above.

## Not used (and why)

- No street address was used because it isn't confirmed by two independent sources (the intake
  playbook's conflict rule).
- No "insured/bonded" claim — not stated anywhere found.
- No 24/7 or emergency-service claim — not stated anywhere found.
- No guarantee/warranty band — none on file, so the base template's Guarantee section was dropped
  rather than filled with an invented claim.
- The HubSpot page builder URL above was not used as a source for any fact, since it could not be loaded.

## Next steps for the owner (local SEO)

1. **Claim/verify a Google Business Profile.** No evidence of one was found — the only public presence
   is Facebook. GBP signals are the single largest factor in local pack ranking; right now this business
   has none of that weight working for it.
2. **Build review count and velocity on Google.** Only 2 reviews exist (on Facebook). Ten or more
   recent Google reviews is the commonly-cited threshold that starts meaningfully helping local ranking
   — ask recent customers directly, and keep a steady cadence rather than one push.
3. **Publish consistent NAP (name/address/phone) on a few more citations** — Bing Places (feeds
   ChatGPT/Copilot/Alexa answers), Apple Maps/Business Connect, BBB, Yelp. Right now Facebook is the
   only place this is published.
4. **Confirm and publish a real street address**, so it can go on the site, in the schema, and in every
   citation consistently — right now only city/zip is confirmed.
5. **Once this site is live on a real domain**, add it as the website link on the Google Business
   Profile and keep the NAP identical everywhere it appears.

## After launch (not run this session)

`seo-page`, `seo-technical`, `seo-audit`, `seo-google` all judge live-domain/rendered-page signals and
refuse to run against localhost — run them once this is hosted on `wiredlocalmarketing.com/mann-electric`
or a real domain.

## Verification

`python <skill>/tools/verify_site.py sites/mann-electric` → **0 FAIL, 2 WARN** (both expected and
explained above: empty `TO_EMAIL`, and 15 inert nav links instead of 18 because the Reviews nav item
was deliberately dropped along with the Reviews section). SlopMonster copy score: **5/5 CLEAN**. Claude
SEO content quality: **93/100, no flags**. `seo-schema` and `seo-images` were run manually (no findings
requiring fixes beyond what's already applied: `fetchpriority="high"` on the hero, `decoding="async"`
on the rest).

**Not done this session**: the browser test protocol (§E in checklists.md) needs a real browser/Chrome
tool that wasn't available here, so desktop/375px visual QA and click-through testing were not
performed. The automated verifier and static analysis passed clean, but a manual look-over is worth
doing before sending this to the prospect.
