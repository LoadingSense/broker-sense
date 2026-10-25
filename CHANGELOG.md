# Changelog

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
