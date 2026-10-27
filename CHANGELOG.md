# Changelog

## 2.0.6 (27 Oct 2026)
- The file-note skill is called the BID file note, the term brokers use.
- A lender rule from its broker-portal guide is cited by the guide's name and its own date, in Broker Sense's words,
  and stays out of anything sent to a client.
- Every skill: never firm a fact up ("PAYG" isn't "full-time PAYG"); in anything drafted for someone else, what you
  weren't told stays in [brackets].
- The README gives prices incl. GST (A$53.90 a month after the beta, half for founding members) and the beta's end
  date.

## 2.0.5 (25 Oct 2026)
- When Broker Sense had too little on part of a question and a skill sends that part to Broker Sense for research, it
  now tells you so in one line. Tools that record something are reached by name through `use_write_tool`.

## 2.0.4 (25 Oct 2026)
- The listing links to the install guide, help, privacy policy and terms (no change to the skills).

## 2.0.3 (25 Oct 2026)
- When Broker Sense isn't connected, the skills say so at the start, with the steps to connect it, then still help
  (marking what they couldn't check). They used to mention it once, at the end.
- Setting up: after connecting Broker Sense, set its tool permissions to Allow all, for read and write tools, so it
  doesn't stop to ask before each lookup or record.

## 2.0.2 (25 Oct 2026)
- The connector shows as "Broker Sense" on the plugin's Connectors tab (it was "broker-sense"). If you installed 2.0.1,
  connect it again after updating: Claude treats the renamed connector as a new one.
- The plugin has its icon: the LoadingSense mark.

## 2.0.1 (25 Oct 2026)
- First public release: eight skills for Australian mortgage brokers (fact-find, lender strategy, best-interests
  file notes, deal plans, contracts, client care, compliance and marketing), plus "what can my AI team do?".
- They work on their own and say when they couldn't check something; connected to Broker Sense, they check lender
  policy, products, rates, schemes and costs against current published sources, with dates.
