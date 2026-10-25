# Broker Sense

A free AI team for Australian mortgage brokers, from [LoadingSense](https://loadingsense.com): your broker expert and
specialist business partner. Eight skills: fact-finds, lender research, best-interests file notes, deal plans,
contracts, client care, compliance and marketing. Connect it to Broker Sense's live knowledge and every lender line and
cost comes with the lender's own document and its date.

## Install

**Claude:** download `broker-sense.zip` from the [latest release](https://github.com/loadingsense/broker-sense/releases/latest)
(don't unzip it), then in Claude open **Customize → Plugins** and upload it. On the plugin's **Connectors** tab, connect
**Broker Sense**: sign in to LoadingSense and verify your credit representative number once. Then ask "what can my AI
team do?"

**Claude Code:**
```
/plugin marketplace add loadingsense/broker-sense
/plugin install broker-sense@loadingsense
```

ChatGPT, Microsoft 365 Copilot, Grok and others: connect Broker Sense directly. Step-by-step for every assistant:
[loadingsense.com/install](https://loadingsense.com/install).

## What's inside

The plugin is in [`plugins/broker-sense`](plugins/broker-sense): its [README](plugins/broker-sense/README.md) lists the
skills, what Broker Sense costs, and how your clients' data is handled. Changes are in [CHANGELOG.md](CHANGELOG.md).

## Support

Email [hey@loadingsense.com](mailto:hey@loadingsense.com). Free to install and use, including in your business; not
for resale ([LICENSE](LICENSE)). This repository holds the built package; it's published from LoadingSense's own
source, so pull requests can't be merged here.
