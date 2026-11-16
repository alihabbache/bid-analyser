---
name: ecosystem-integration-fit
description: Invoke when requirements name integrations, toolchains or adjacent products (e.g. issue trackers, ITSM, source control, MCP/AI agents, SIEM, identity providers, observability or FinOps tools) to verify how the product connects, at what effort, and with what licensing dependency.
---

## Purpose
Separate integrations that are real, supported and in the box from ones that need plugins, custom work or extra licences, so the response doesn't promise an integration the delivery team then has to build.

## Uses
- Agent capabilities: file/document storage search, web search (vendor-official sources only)
- Knowledge: the `<PRODUCT>` `<VERSION>` reference files, the Claims Register, the Capability Map

## Instructions
1. Collect every integration requirement and every named product from the requirements register, plus the customer's existing toolchain if the RFP describes it.
2. For each integration, find the mechanism in a `<VERSION>` or vendor-official source and classify it as one of: **Native** (built in), **Plugin** (supported and shipped by the vendor), **API/Webhook** (possible, but needs configuration or code), **MCP** (exposed through the product's MCP server, if it has one), **Partner/Custom**, or **Not supported / Unknown**.
3. Record the direction (inbound, outbound or bidirectional), the data that flows, which product capability is involved, which product and version, and whether a **separate licence** is needed (adjacent products from the same vendor are often separately licensed).
4. For multi-product stories (e.g. "vulnerability remediation flow across two products" or "cost analytics fed by delivery data"), break the story into individual hops. Mark each hop Verified or Unverified. The whole story is only as strong as its weakest hop.
5. Add the effort and risk to deliver it: Low (native), Medium (plugin or configuration), or High (custom work, or any hop that is Unverified).

## Output
Save `<Client> - Integration Fit - YYYY-MM-DD.xlsx` to `03 - Analysis` with these columns:
`Req ID | Integration | Mechanism | Direction & data | Product capability | Product/version | Extra licence? | Evidence | Status | Effort/risk`
In chat, report: integrations that will work as described, integrations that need extra licences, and integrations at risk.

## Rules
- Being sold by the same vendor does not make a product integrated. Each hop needs a source.
- Do not describe a multi-product flow as a single capability in response wording unless every hop is Verified.
- Add any new verified integration to the "Suggested Claims Register updates" list for the register owner to review. Do not edit the register yourself.

## Hand-off
Pass every integration classified as Partner/Custom or Not supported/Unknown, and every multi-product story with an Unverified hop, to `capability-gap-capture` with gap type Integration. Include the Req ID, the mechanism you checked, and the hop that failed.
